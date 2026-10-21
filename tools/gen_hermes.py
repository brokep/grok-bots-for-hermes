#!/usr/bin/env python3
"""Convert Grok Bot marketplace templates (bots_full.json) into Hermes Agent profile distributions.

Usage:
  python3 gen_hermes.py bots_full.json hermes [--provider anthropic --model claude-opus-4-6]

Output (one Hermes profile distribution per bot, installable with `hermes profile install <dir>`):
  hermes/dists/<slug>/
    distribution.yaml   manifest (name grok-<slug>, env_requires for the chosen provider)
    SOUL.md             persona: identity, profile memories, known facts, operating rules
    config.yaml         model block (provider/default) + sensible agent defaults
    skills/<slug>--<skill>/SKILL.md          one agentskills.io skill per Grok skill
    skills/<slug>--routine-<name>/SKILL.md   one skill per routine (the cron job loads it)
    cron/jobs.json      one scheduled job per routine (installer lands them paused)
    MAPPING.md          what mapped where, MCP hints for the bot's plugins
    README.md, .gitignore
  hermes/install.sh     install / remove selected bots (or --all) as profiles
  hermes/README.md
"""
import json, os, re, sys, argparse, hashlib, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grok2copilot import normalise  # noqa: E402

PROVIDER_ENV = {
    "anthropic": ("ANTHROPIC_API_KEY", "Anthropic API key (or run `hermes model` for Claude Max OAuth)"),
    "xai": ("XAI_API_KEY", "xAI API key (or `hermes auth add xai-oauth` for SuperGrok / X Premium+)"),
    "kimi-coding": ("KIMI_API_KEY", "Moonshot / Kimi API key (api.moonshot.ai)"),
    "openrouter": ("OPENROUTER_API_KEY", "OpenRouter API key"),
    "bedrock": (None, "AWS credentials via the boto3 chain"),
    "nous": (None, "Nous Portal OAuth (`hermes setup --portal`)"),
}
DEFAULT_MODELS = {"anthropic": "claude-opus-4-6", "xai": "grok-4.3", "kimi-coding": "kimi-for-coding",
                  "openrouter": "anthropic/claude-opus-4.6", "bedrock": "us.anthropic.claude-opus-4-6-v1"}

MCP_HINTS = {
    "gmail": {"command": "npx", "args": ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]},
    "slack": {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-slack"], "env": {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}},
    "notion": {"url": "https://mcp.notion.com/mcp"},
    "notion-workspace": {"url": "https://mcp.notion.com/mcp"},
    "linear": {"url": "https://mcp.linear.app/mcp"},
    "github": {"url": "https://api.githubcopilot.com/mcp/"},
    "hubspot": {"url": "https://mcp.hubspot.com"},
    "sentry": {"url": "https://mcp.sentry.dev/mcp"},
    "figma": {"url": "http://127.0.0.1:3845/mcp"},
}

def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", (s or "").lower()).strip("-")
    return s[:48] or "item"

def yq(s):
    return json.dumps(s, ensure_ascii=False)

def clip(s, n):
    s = " ".join((s or "").split())
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"

# ---------------------------------------------------------------- schedule prose -> cron
DAYS = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5, "saturday": 6, "sunday": 0}

def hour_from(text, default):
    m = re.search(r"\b(\d{1,2})(?::(\d{2}))?\s*(am|pm)\b", text)
    if m:
        h = int(m.group(1)) % 12 + (12 if m.group(3) == "pm" else 0)
        return h, int(m.group(2) or 0)
    if "evening" in text or "end of day" in text or "end of the day" in text: return 17, 0
    if "afternoon" in text or "midday" in text or "noon" in text: return 12, 0
    if "night" in text: return 21, 0
    return default, 0

def schedule_for(prose, name):
    """Best-effort cron expression + a plain-English display from routine prose. Jobs install paused; edit before enabling."""
    t = f"{name} {prose}".lower()
    h, mnt = hour_from(t, 9)
    days = sorted({DAYS[d] for d in DAYS if d in t})
    if "every weekday" in t or "weekday" in t or "each weekday" in t:
        return f"{mnt} {h} * * 1-5", f"weekdays at {h:02d}:{mnt:02d}"
    if "weekend" in t:
        return f"{mnt} {h} * * 0,6", f"weekends at {h:02d}:{mnt:02d}"
    if "twice a week" in t or "two times a week" in t:
        return f"{mnt} {h} * * 1,4", f"Mondays and Thursdays at {h:02d}:{mnt:02d}"
    if days:
        return f"{mnt} {h} * * {','.join(map(str, days))}", f"{', '.join(d.title() for d in DAYS if DAYS[d] in days)} at {h:02d}:{mnt:02d}"
    if "daily" in t or "every day" in t or "each day" in t or "every morning" in t or "each morning" in t:
        return f"{mnt} {h} * * *", f"daily at {h:02d}:{mnt:02d}"
    if "quarter" in t:
        return f"{mnt} {h} 1 1,4,7,10 *", f"first day of each quarter at {h:02d}:{mnt:02d}"
    if "monthly" in t or "every month" in t or "each month" in t or "month-end" in t or "end of month" in t:
        return f"{mnt} {h} 1 * *", f"1st of the month at {h:02d}:{mnt:02d}"
    if "hour" in t:
        return f"0 */4 * * *", "every 4 hours"
    return f"{mnt} {h} * * 1", f"Mondays at {h:02d}:{mnt:02d} (weekly default)"

# ---------------------------------------------------------------- pieces
def soul_md(t, skill_names, routine_names):
    L = [f"# {t['name']}", "", f"You are {t['name']}. {t['description']}", ""]
    if t["memories"]:
        L += ["## Who you are and how you work", ""]
        L += [m["description"].strip() for m in t["memories"]] + [""]
    if t.get("logs"):
        L += ["## Known facts (from the original bot's notes)", ""]
        L += [f"- {clip(x, 600)}" for x in t["logs"]] + [""]
    L += ["## Operating rules in Hermes", "",
          "- Your skills are listed in your skill index; use the skill tool to load one by name before doing that kind of work. "
          + ("Skills: " + ", ".join(f"`{s}`" for s in skill_names) + "." if skill_names else ""),
          "- Where the original bot kept per-user notes or memory slots, use the memory tool (MEMORY.md for working facts, USER.md for the user's preferences) and keep entries short.",
          "- Where the original bot wrote files, write them in the current working directory and tell the user the path.",
          ]
    if routine_names:
        L.append("- Your routines are scheduled jobs that load these skills: " + ", ".join(f"`{s}`" for s in routine_names)
                 + ". They are installed paused; the user enables them with `hermes cron resume`. If asked to run one now, load the skill and follow it.")
    if t.get("gettingStarted"):
        L.append(f"- On a brand-new session with no prior memory, offer to run the `{t['gettingStarted_skill']}` skill to get set up.")
    if t["integrations"]:
        L.append("- Integrations the original bot relied on: " + ", ".join(i["name"] for i in t["integrations"])
                 + ". If the matching MCP tools are not available, say so and offer a manual alternative instead of pretending.")
    L += ["", f"Source: Grok Bot marketplace, https://x.ai/bot/marketplace/bots/{t['id']} by {t['creatorName']}" + (f" (@{t['handle']})" if t.get("handle") else "") + "."]
    return "\n".join(L) + "\n"

def skill_md(name, desc, body, tags, related):
    fm = ["---", f"name: {name}", f"description: {yq(clip(desc, 240))}", "version: 1.0.0", "platforms: [linux, macos, windows]",
          "metadata:", "  hermes:", f"    tags: {json.dumps(tags)}", f"    related_skills: {json.dumps(related)}", "---", ""]
    return "\n".join(fm) + body.strip() + "\n"

def config_yaml(provider, model):
    return "\n".join([
        "# Written by gen_hermes.py. Change the model with `<profile> model` or `hermes -p <profile> config set model.default <id>`.",
        "model:", f"  provider: {provider}", f"  default: {yq(model)}", "  base_url: ''",
        "agent:", "  reasoning_effort: medium", "  max_turns: 90",
        "memory:", "  memory_enabled: true", "  user_profile_enabled: true", ""])

def distribution_yaml(t, provider, pname):
    env_key, env_desc = PROVIDER_ENV.get(provider, (f"{provider.upper().replace('-', '_')}_API_KEY", f"{provider} API key"))
    L = [f"name: {pname}", "version: 1.0.0", f"description: {yq(clip(t['description'], 300))}", 'hermes_requires: ">=0.14.0"',
         f"author: {yq('converted from the Grok Bot marketplace template by ' + (t['creatorName'] or 'unknown'))}",
         'license: "see source template on x.ai"']
    if env_key:
        L += ["env_requires:", f"  - name: {env_key}", f"    description: {yq(env_desc)}", "    required: true"]
    return "\n".join(L) + "\n"

def jobs_json(t, slug, routine_skill_by_id):
    jobs = []
    now = datetime.datetime.now().astimezone().isoformat()
    for r in t["routines"]:
        rid = r.get("id") or slugify(r["name"])
        sk = routine_skill_by_id[rid]
        expr, display = schedule_for(r.get("summary", ""), r["name"])
        jid = hashlib.sha1(f"{slug}:{rid}".encode()).hexdigest()[:12]
        jobs.append({
            "id": jid, "name": clip(r["name"], 80),
            "prompt": f"Load the `{sk}` skill and run it now. Original schedule: {clip(r.get('summary',''), 200) or 'not stated'}. Report the result as your final response.",
            "skills": [sk], "skill": sk, "model": None, "provider": None, "base_url": None, "script": None, "no_agent": False, "context_from": None,
            "schedule": {"kind": "cron", "expr": expr, "display": display}, "schedule_display": display,
            "repeat": {"times": None, "completed": 0},
            "enabled": False, "state": "paused", "paused_at": now, "paused_reason": "shipped paused by gen_hermes.py; check the schedule, then `hermes cron resume`",
            "created_at": now, "next_run_at": None, "last_run_at": None, "last_status": None, "last_error": None, "last_delivery_error": None,
            "deliver": "local", "origin": None, "enabled_toolsets": None, "workdir": None, "profile": None,
        })
    return {"jobs": jobs, "updated_at": now}

def mapping_md(t, pname, skill_names, routine_rows):
    L = [f"# {t['name']} as Hermes profile `{pname}`", "",
         f"Source: https://x.ai/bot/marketplace/bots/{t['id']}  Creator: {t['creatorName']}" + (f" (@{t['handle']})" if t.get("handle") else ""), "",
         "| Grok Bot | Hermes | Where |", "|---|---|---|",
         "| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |",
         "| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |",
         "| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |",
         "| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |",
         "| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |", ""]
    if skill_names:
        L += ["## Skills", ""] + [f"- `{s}`" for s in skill_names] + [""]
    if routine_rows:
        L += ["## Routines (cron, paused on install)", "", "| Job | Guessed schedule | Original wording |", "|---|---|---|"]
        L += [f"| {n} | `{e}` ({d}) | {clip(p, 120)} |" for n, e, d, p in routine_rows]
        L += ["", f"Enable with `hermes -p {pname} cron list` then `hermes -p {pname} cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.", ""]
    if t["integrations"]:
        L += ["## Integrations", "", "Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.", ""]
        for i in t["integrations"]:
            key = i["name"].lower()
            hint = MCP_HINTS.get(key)
            L.append(f"- **{i['name']}** (Grok plugin `{i.get('pluginId')}`): {clip(i.get('description',''), 160)}")
            if hint:
                L.append("  ```yaml\n  mcp_servers:\n    " + slugify(i["name"]) + ":\n" + "\n".join(f"      {k}: {json.dumps(v)}" for k, v in hint.items()) + "\n  ```")
            else:
                L.append("  No known MCP server; search `hermes skills search " + slugify(i["name"]) + "` or wire one up under `mcp_servers:`.")
        L.append("")
    return "\n".join(L)

GITIGNORE = """auth.json
.env
.env.EXAMPLE
state.db
state.db-shm
state.db-wal
hermes_state.db
response_store.db*
gateway.pid
gateway_state.json
processes.json
auth.lock
active_profile
.update_check
memories/
sessions/
logs/
plans/
workspace/
home/
*_cache/
cache/
checkpoints/
sandboxes/
backups/
errors.log
.hermes_history
cron/*
!cron/jobs.json
skills/.*
"""

# ---------------------------------------------------------------- main
def build(t, out, provider, model):
    slug = t["id"]; pname = f"grok-{slug}"
    d = os.path.join(out, "dists", slug)
    os.makedirs(os.path.join(d, "skills"), exist_ok=True); os.makedirs(os.path.join(d, "cron"), exist_ok=True)
    skill_names = []; related = []
    gs = t.get("gettingStarted")
    for s in t["skills"]:
        name = f"{slug}--{slugify(s['name'])}"
        if gs and s["name"] == gs: t["gettingStarted_skill"] = name
        skill_names.append(name)
    for s, name in zip(t["skills"], skill_names):
        body = s.get("content") or s.get("description") or ""
        os.makedirs(os.path.join(d, "skills", name), exist_ok=True)
        open(os.path.join(d, "skills", name, "SKILL.md"), "w").write(
            skill_md(name, s.get("description") or s["name"], f"# {s['name']}\n\n{body}", [slug, "grok-bot"] + [slugify(c) for c in t["categories"]][:3], [x for x in skill_names if x != name][:6]))
    routine_skill_by_id = {}; routine_rows = []; routine_names = []
    for r in t["routines"]:
        rid = r.get("id") or slugify(r["name"]); name = f"{slug}--routine-{slugify(r['name'])}"
        routine_skill_by_id[rid] = name; routine_names.append(name)
        body = f"# Routine: {r['name']}\n\nOriginal schedule: {r.get('summary','') or 'not stated'}\n\n{r.get('content') or r.get('summary') or ''}"
        os.makedirs(os.path.join(d, "skills", name), exist_ok=True)
        open(os.path.join(d, "skills", name, "SKILL.md"), "w").write(skill_md(name, "Routine: " + (r.get("summary") or r["name"]), body, [slug, "grok-bot", "routine"], skill_names[:6]))
        expr, disp = schedule_for(r.get("summary", ""), r["name"]); routine_rows.append((r["name"], expr, disp, r.get("summary", "")))
    if t["routines"]:
        json.dump(jobs_json(t, slug, routine_skill_by_id), open(os.path.join(d, "cron", "jobs.json"), "w"), indent=2, ensure_ascii=False)
    open(os.path.join(d, "SOUL.md"), "w").write(soul_md(t, skill_names, routine_names))
    open(os.path.join(d, "config.yaml"), "w").write(config_yaml(provider, model))
    open(os.path.join(d, "distribution.yaml"), "w").write(distribution_yaml(t, provider, pname))
    open(os.path.join(d, "MAPPING.md"), "w").write(mapping_md(t, pname, skill_names, routine_rows))
    open(os.path.join(d, ".gitignore"), "w").write(GITIGNORE)
    open(os.path.join(d, "README.md"), "w").write(
        f"# {t['name']} (Hermes profile distribution)\n\n{t['description']}\n\n"
        f"Install: `hermes profile install ./dists/{slug} --alias -y` (from the repo root) then `{pname} chat`.\n\n"
        f"Skills: {len(skill_names)}  Routines: {len(routine_names)}  Integrations: {', '.join(i['name'] for i in t['integrations']) or 'none'}\n\nSee MAPPING.md.\n")
    return {"slug": slug, "profile": pname, "name": t["name"], "skills": len(skill_names), "routines": len(routine_names),
            "integrations": [i["name"] for i in t["integrations"]], "categories": t["categories"], "description": clip(t["description"], 160)}

INSTALL_SH = r'''#!/usr/bin/env bash
# Install Grok marketplace bots as Hermes profiles.
#   ./install.sh human-copywriter prospector     # selected bots
#   ./install.sh --all                           # all of them (one profile each)
#   ./install.sh --remove human-copywriter       # delete the profile
#   ./install.sh --list                          # what is available
# Env: HERMES=hermes (binary), ALIAS=1 to also create `grok-<slug>` shell commands.
set -euo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"; HERMES="${HERMES:-hermes}"; ALIAS="${ALIAS:-1}"
flag=(); [ "$ALIAS" = "1" ] && flag=(--alias)
case "${1:-}" in
  --list) python3 -c "import json;[print(f\"{b['slug']:32} {b['name']:40} skills={b['skills']} routines={b['routines']}\") for b in json.load(open('$HERE/catalog.json'))]"; exit 0;;
  --all) set -- $(python3 -c "import json;print(' '.join(b['slug'] for b in json.load(open('$HERE/catalog.json'))))");;
  --remove) shift; for s in "$@"; do "$HERMES" profile delete "grok-$s" -y 2>/dev/null || "$HERMES" profile delete "grok-$s"; done; exit 0;;
  ""|-h|--help) sed -n '2,7p' "$0"; exit 0;;
esac
for s in "$@"; do
  [ -d "$HERE/dists/$s" ] || { echo "no such bot: $s"; continue; }
  "$HERMES" profile install "$HERE/dists/$s" -y "${flag[@]}" --force
done
echo; echo "Done. Try:  hermes -p grok-$1 chat     (or just: grok-$1 chat)"
'''

README = """# Grok Bot marketplace -> Hermes Agent profile distributions

Generated by `../gen_hermes.py` from `../bots_full.json`. One Hermes *profile distribution* per bot: SOUL.md persona, the bot's skills as agentskills.io `SKILL.md` folders, routines as paused cron jobs, and a `config.yaml` that pins the model you chose at generation time.

## Install

```
./install.sh --list                      # browse
./install.sh human-copywriter prospector # a few
./install.sh --all                       # all 90 (90 profiles; the profile list gets long)
grok-human-copywriter chat               # alias created by --alias; or: hermes -p grok-human-copywriter chat
```

Each profile is its own Hermes home under `~/.hermes/profiles/grok-<slug>/` with its own memory, sessions and cron jobs. API keys are **not** shipped. Put them in the profile's `.env` (the installer writes `.env.EXAMPLE` next to it) or export them in your shell; a profile does not read the root `~/.hermes/.env`.

## Models: Claude, Grok, Kimi

Keys go in `~/.hermes/profiles/<profile>/.env` (or export them):

```
ANTHROPIC_API_KEY=...     # provider: anthropic   models: claude-opus-4-6, claude-sonnet-4-6
XAI_API_KEY=...           # provider: xai         models: grok-4.3, grok-4-fast-reasoning (or `hermes auth add xai-oauth` with SuperGrok)
KIMI_API_KEY=...          # provider: kimi-coding models: kimi-for-coding, kimi-k2.5
```

Pick per profile:

```
hermes -p grok-prospector model                                   # interactive picker
hermes -p grok-prospector config set model.provider xai
hermes -p grok-prospector config set model.default grok-4.3
hermes -p grok-prospector chat -m kimi-for-coding --provider kimi-coding   # one session only
/model grok-4.3                                                   # inside a session
```

`hermes -p <profile> fallback` adds the other two providers as automatic fallbacks when the primary fails.

Regenerate with a different default: `python3 gen_hermes.py bots_full.json hermes --provider xai --model grok-4.3`.

## Routines

`cron/jobs.json` ships one job per routine with a cron expression guessed from the routine's prose (see each bot's `MAPPING.md`). Hermes installs shipped jobs **paused**. Check the time, then enable:

```
hermes -p grok-x-brief cron list
hermes -p grok-x-brief cron edit <id> --schedule "every friday at 4pm"
hermes -p grok-x-brief cron resume <id>
hermes cron status        # the scheduler must be running (gateway or `hermes cron tick` from your own cron)
```

Delivery is `local` (output under the profile's `cron/output/`); change `--deliver telegram` etc. once a gateway is configured.

## Integrations

Grok plugins (Gmail, Slack, Notion, Linear, GitHub, ...) map to MCP servers. Each `MAPPING.md` has a `mcp_servers:` snippet for the known ones; add it to the profile's `config.yaml` and restart.

## Caveats

- Templates belong to their creators on x.ai. SOUL.md keeps the attribution line.
- Schedules are guesses from prose. Review before resuming a job.
- Bot text still refers to Grok runtime ideas (memory slots, files, "my skill"); the SOUL.md operating-rules section maps them to Hermes memory, the working directory and the skill tool, nothing deeper.
- Built with Hermes Agent v0.15.0 on 2026-10-21. `hermes profile install` from a local directory and `profile list` were verified; no session was run against a model.
"""

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out")
    ap.add_argument("--provider", default="anthropic"); ap.add_argument("--model", default=None)
    a = ap.parse_args(); model = a.model or DEFAULT_MODELS.get(a.provider, "")
    if not model: sys.exit("pass --model for provider " + a.provider)
    d = json.load(open(a.src)); os.makedirs(a.out, exist_ok=True)
    cat = []
    for b in d["bots"]:
        t = normalise(b); cat.append(build(t, a.out, a.provider, model))
    json.dump(cat, open(os.path.join(a.out, "catalog.json"), "w"), indent=1, ensure_ascii=False)
    p = os.path.join(a.out, "install.sh"); open(p, "w").write(INSTALL_SH); os.chmod(p, 0o755)
    open(os.path.join(a.out, "README.md"), "w").write(README)
    print(f"{len(cat)} distributions in {a.out}/dists  skills={sum(c['skills'] for c in cat)} routines={sum(c['routines'] for c in cat)}  model={a.provider}/{model}")

if __name__ == "__main__":
    main()
