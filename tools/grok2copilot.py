#!/usr/bin/env python3
"""Convert Grok Bot marketplace templates (bots.json) into Microsoft Copilot assets.

Per bot it writes:
  declarativeAgent.json   Declarative agent manifest v1.8 (Microsoft 365 Copilot / Agents Toolkit)
  instructions.md         Full instructions for the Copilot Studio Build tab (no truncation)
  skills/<name>/SKILL.md  One Agent Skills package per Grok skill (upload in Copilot Studio > Skills)
  MAPPING.md              Routines, integrations and anything that needs a manual step
Usage: python3 grok2copilot.py bots_full.json out_dir   (bots_full.json from fetch_full_templates.py; bots.json from the website also works but lacks skill/routine bodies)
"""
import json, os, re, sys, csv

LIMITS = {"name": 100, "description": 1000, "instructions": 8000, "starters": 12}

# Grok integration name -> declarative agent capability objects (built in to M365 Copilot)
CAPABILITY_MAP = {
    "gmail": [{"name": "Email"}, {"name": "EmailActions"}],
    "outlook": [{"name": "Email"}, {"name": "EmailActions"}],
    "agentmail": [{"name": "Email"}, {"name": "EmailActions"}],
    "google calendar": [{"name": "Meetings"}, {"name": "MeetingActions"}],
    "slack": [{"name": "TeamsMessages"}],
    "google drive": [{"name": "OneDriveAndSharePoint"}],
    "onedrive": [{"name": "OneDriveAndSharePoint"}],
    "notion": [{"name": "OneDriveAndSharePoint"}],
    "notion-workspace": [{"name": "OneDriveAndSharePoint"}],
    "google sheets": [{"name": "OneDriveAndSharePoint"}, {"name": "CodeInterpreter"}],
    "google slides": [{"name": "OneDriveAndSharePoint"}],
    "x": [{"name": "WebSearch"}],
    "granola": [{"name": "Meetings"}],
}
# Grok integration name -> suggested Copilot Studio tool (connector / MCP) to add by hand
TOOL_MAP = {
    "salesforce": "Salesforce connector (Power Platform)",
    "hubspot": "HubSpot connector (Power Platform)",
    "linear": "Linear MCP server or custom connector (no first-party connector)",
    "figma": "Figma MCP server (no first-party connector)",
    "github": "GitHub connector (Power Platform)",
    "gong": "Gong connector (Power Platform, premium)",
    "hex": "Hex has no connector; expose via custom connector or MCP",
    "databricks sql": "Databricks connector or SQL Server connector",
    "attio": "Attio REST API via custom connector",
    "mixpanel": "Mixpanel REST API via custom connector",
    "ashby": "Ashby REST API via custom connector",
    "profound": "custom connector",
    "pstack": "custom connector",
    "datadog": "Datadog connector (Power Platform)",
    "sentry": "Sentry REST API via custom connector",
    "ramp": "Ramp REST API via custom connector",
    "vercel": "Vercel REST API via custom connector",
    "hunter": "Hunter.io REST API via custom connector",
    "clay": "Clay REST API via custom connector",
    "remotion": "no equivalent; drop or replace with a flow",
    "granola": "Granola has no connector; Teams meeting transcripts cover the same need",
    "x": "X (Twitter) has no first-party connector; WebSearch capability added instead",
}

def slug(s, n=64):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:n].rstrip("-") or "skill"

def clip(s, n):
    return s if len(s) <= n else s[: n - 1].rstrip() + "…"

def build_instructions(t):
    """Join memories into one instruction block. Returns (full, fitted, overflow)."""
    parts = []
    for i, m in enumerate(t["memories"], 1):
        parts.append(m["description"].strip())
    full = "\n\n".join(parts)
    if t.get("logs"):
        seeded = full + "\n\nKnown facts:\n" + "\n".join(f"- {m}" for m in t["logs"])
        if len(seeded) <= LIMITS["instructions"]:
            full = seeded; t["_logs_in_instructions"] = True
    if t.get("gettingStarted"):
        full += f"\n\nOn the first conversation, or whenever no user preferences are stored, run the \"{t['gettingStarted']}\" skill before anything else."
    if t.get("instructions"):
        full = t["instructions"].strip() + "\n\n" + full
    if len(full) <= LIMITS["instructions"]:
        return full, full, ""
    fitted, overflow, used = [], [], 0
    footer = "\n\nAdditional operating detail is in the attached knowledge file extended-instructions.md. Read it before acting."
    budget = LIMITS["instructions"] - len(footer)
    for p in parts:
        if used + len(p) + 2 <= budget and not overflow:
            fitted.append(p); used += len(p) + 2
        else:
            overflow.append(p)
    return full, "\n\n".join(fitted) + footer, "\n\n".join(overflow)

def starters(t):
    out = []
    for s in t["skills"][: LIMITS["starters"]]:
        out.append({"title": clip(s["name"], 60), "text": clip(s.get("description") or s["name"], 400)})
    return out

def capabilities(t, instr):
    caps, seen = [], set()
    names = [i["name"].lower() for i in t["integrations"]]
    if re.search(r"\b(web|news|search the internet|google it|competitor|market)\b", instr, re.I):
        names.append("x")
    for n in names:
        for c in CAPABILITY_MAP.get(n, []):
            if c["name"] not in seen:
                seen.add(c["name"]); caps.append(c)
    return caps

def skill_md(s, bot):
    name = slug(s["name"])
    desc = clip((s.get("description") or s["name"]).replace("\n", " "), 1024)
    body = s.get("content") or s.get("description") or ""
    return name, f"""---
name: {name}
description: {desc}
---

# {s['name']}

Part of the "{bot['name']}" agent (converted from Grok Bot marketplace template `{bot['id']}`).

## When to use

{s.get('description') or s['name']}

## Procedure

{body}
"""

def mapping_md(t, caps, overflow):
    L = [f"# Manual steps for {t['name']} (`{t['id']}`)\n",
         f"Source: https://x.ai/bot/marketplace/bots/{t['id']}  Creator: {t['creatorName']} (@{t['handle']})\n"]
    L.append("\n## Capabilities set in declarativeAgent.json\n")
    L += [f"- {c['name']}\n" for c in caps] or ["- none\n"]
    L.append("\n## Integrations that need a tool added in Copilot Studio\n")
    any_tool = False
    for i in t["integrations"]:
        n = i["name"].lower()
        if n in CAPABILITY_MAP and n not in TOOL_MAP:
            continue
        any_tool = True
        pid = f" (Grok plugin id {i['pluginId']})" if i.get("pluginId") else ""
        L.append(f"- **{i['name']}**{pid}: {i.get('description','')}\n  - Suggested: {TOOL_MAP.get(n, 'no mapping, add a connector or MCP server by hand')}\n")
    if not any_tool: L.append("- none\n")
    L.append("\n## Harness\n- Create this agent on the **GitHub Copilot harness**. It is the only harness with skills, memory, file handling and MCP, which this template relies on. The choice is permanent per agent.\n- The declarativeAgent.json next to this file is for the Copilot chat harness (extending Microsoft 365 Copilot). It keeps instructions, capabilities and starters only.\n")
    L.append("\n## Routines (build each as a Workflow with a Recurrence trigger and a Call-an-agent action; spec in routines/<slug>.md)\n")
    L += [f"- **{r['name']}** (`{r.get('id')}`): {r.get('summary','')}\n" for r in t["routines"]] or ["- none\n"]
    if t.get("logs"):
        where = "already appended to instructions as Known facts" if t.get("_logs_in_instructions") else "did NOT fit the 8,000-character instruction cap; upload seed-memories.md as a knowledge file"
        L.append(f"\n## Seed memories ({where})\n- Makers cannot write into Copilot Studio Memory. Memory is per user, private, cleared after 28 idle days, and off in Teams channels and group chats. Turn it on for the user-preference slots (timezone, brand, audience); keep fixed facts in instructions or knowledge.\n")
        L += [f"- {m}\n" for m in t["logs"]]
    if overflow:
        L.append("\n## Instruction overflow\n- Instructions exceeded 8,000 characters. The remainder is in knowledge/extended-instructions.md. Upload it as a knowledge file or paste it into Copilot Studio instructions, which has the same cap.\n")
    L.append("\n## Not converted\n- Grok memory slots that hold per-user preferences (timezone, brand, audience) rely on the Memory feature. Turn Memory on in the Build tab; it is private per user and makers cannot seed it.\n- Billing: the GitHub Copilot harness charges Copilot Credits from the moment you start building, including Preview and Evaluate. Estimate before importing all 90.\n- Install counts, color and shape are cosmetic and dropped.\n")
    return "".join(L)

def normalise(b):
    """Return a web-shaped template dict from either bots.json (web) or bots_full.json (RPC blob) records."""
    t = b["template"]
    if "profile" not in t:
        t.setdefault("logs", []); t.setdefault("plugins", []); return t
    L = b["listing"]; P = t["profile"]
    prof = [m["content"] for m in t.get("memory", []) if m.get("kind") == "profile"]
    logs = [m["content"] for m in t.get("memory", []) if m.get("kind") != "profile"]
    gs = (t.get("gettingStarted") or {}).get("skill")
    skills = [{"id": f"skill-{i}", "name": s["name"], "description": s.get("description", ""), "content": s.get("content", "")} for i, s in enumerate(t.get("skills", []))]
    if gs:
        skills.sort(key=lambda s: 0 if s["name"] == gs else 1)
    return {
        "id": L["slug"], "name": P.get("name") or L["name"], "description": P.get("description") or L["description"],
        "creatorName": L.get("creator", {}).get("name", ""), "handle": L.get("creator", {}).get("handles", {}).get("x", ""),
        "categories": L.get("categories") or ([L["category"]] if L.get("category") else []),
        "shareId": L.get("shareId"), "updatedAt": L.get("updatedAtMs"),
        "instructions": "", "gettingStarted": gs,
        "memories": [{"id": f"memory-{i}", "name": f"memory {i+1}", "description": c} for i, c in enumerate(prof)],
        "logs": logs, "skills": skills,
        "routines": [{"id": r.get("slug"), "name": r["name"], "summary": r.get("description", ""), "content": r.get("content", "")} for r in t.get("routines", [])],
        "integrations": [{"id": p.get("pluginId"), "name": p["name"], "description": p.get("description", ""), "pluginId": p.get("pluginId")} for p in t.get("plugins", [])],
        "plugins": t.get("plugins", []),
    }


README_TEXT = """# Grok Bot -> Microsoft Copilot Studio conversion

Generated by `../grok2copilot.py` from `../bots_full.json`. Re-run with `python3 grok2copilot.py bots_full.json copilot`.

## Harness choice

Create each agent on the **GitHub Copilot harness**. It is the only one of the three Copilot Studio harnesses with skills, memory, file handling, MCP tools and workflows, which these templates rely on, and the choice is permanent per agent. The standard harness is topic-based and drops skills and memory. The Copilot chat harness (extending Microsoft 365 Copilot) is what `declarativeAgent.json` targets. Reference: https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview

## What is in each bot folder

| File | Use it in | Notes |
|---|---|---|
| `instructions.md` | Build > Instructions | profile memories joined, fixed facts appended as Known facts when they fit the 8,000-character cap |
| `skills/*/SKILL.md` | Build > Skills > Upload a skill | full procedure per Grok skill |
| `routines/*.md` | Workflows > New workflow | spec: Recurrence trigger + Call-an-agent action with the routine prompt |
| `seed-memories.md` | Build > Knowledge | only when the fixed facts did not fit the instruction cap |
| `MAPPING.md` | you | tools to add, harness notes, what was dropped |
| `declarativeAgent.json` | Agents Toolkit, Copilot chat harness path | schema v1.8; instructions, capabilities, starters only |

## Field mapping

| Grok Bot field | Copilot target |
|---|---|
| `profile` + memory `kind: profile` | instructions |
| memory `kind: log` | Known facts in instructions, else `seed-memories.md` as knowledge (makers cannot write into Memory) |
| user-preference slots in memory | Memory toggle on; per user, private, cleared after 28 idle days, off in Teams channels |
| `skills[]` | SKILL.md packages plus the first 12 as conversation starters |
| `routines[]` | Workflows: Recurrence trigger, Call-an-agent action; each run uses workflow capacity plus Copilot Credits |
| `plugins[]` with an M365 equivalent | capabilities in the manifest (Email, EmailActions, Meetings, MeetingActions, TeamsMessages, OneDriveAndSharePoint, WebSearch) |
| other `plugins[]` | Build > Tools: connector or MCP server, listed in MAPPING.md with the Grok plugin id |
| `gettingStarted` | first conversation starter plus a line in instructions |

## Cost

The GitHub Copilot harness bills Copilot Credits from the moment you start building, including Preview and Evaluate. Import a few bots before all 90, and use the Copilot Credits estimator.

## Known gaps

- Instructions still use Grok runtime terms (memory slots, files, "my skill"). No deeper rewrite was done.
- The `$schema` URL in each manifest follows the documented pattern but was not fetched; validate with `wiqd agent validate`.
- Capability assignment is heuristic. `EmailActions` grants mail write access; review per bot.
- Nothing has been imported or tested in a tenant.
"""

def convert(bots_path, out_dir):
    d = json.load(open(bots_path))
    os.makedirs(out_dir, exist_ok=True)
    report = []
    for b in d["bots"]:
        t = normalise(b)
        bd = os.path.join(out_dir, t["id"]); os.makedirs(os.path.join(bd, "skills"), exist_ok=True)
        full, fitted, overflow = build_instructions(t)
        caps = capabilities(t, full)
        manifest = {
            "$schema": "https://developer.microsoft.com/json-schemas/copilot/declarative-agent/v1.8/schema.json",
            "version": "v1.8",
            "id": t["id"],
            "name": clip(t["name"], LIMITS["name"]),
            "description": clip(t["description"], LIMITS["description"]),
            "instructions": fitted,
        }
        if caps: manifest["capabilities"] = caps
        cs = starters(t)
        if cs: manifest["conversation_starters"] = cs
        manifest["behavior_overrides"] = {"default_response_mode": "Auto"}
        json.dump(manifest, open(os.path.join(bd, "declarativeAgent.json"), "w"), indent=2, ensure_ascii=False)
        open(os.path.join(bd, "instructions.md"), "w").write(f"# {t['name']}\n\n{t['description']}\n\n## Instructions\n\n{full}\n")
        if overflow:
            os.makedirs(os.path.join(bd, "knowledge"), exist_ok=True)
            open(os.path.join(bd, "knowledge", "extended-instructions.md"), "w").write(overflow)
        used = set()
        for s in t["skills"]:
            name, md = skill_md(s, t)
            base = name; k = 2
            while name in used: name = f"{base}-{k}"; k += 1
            used.add(name)
            sd = os.path.join(bd, "skills", name); os.makedirs(sd, exist_ok=True)
            open(os.path.join(sd, "SKILL.md"), "w").write(md)
        if t["routines"]:
            rd = os.path.join(bd, "routines"); os.makedirs(rd, exist_ok=True)
            for r in t["routines"]:
                open(os.path.join(rd, f"{slug(r.get('id') or r['name'])}.md"), "w").write(
                    f"# {r['name']}\n\n## Build as a Copilot Studio workflow (GitHub Copilot harness)\n\n"
                    f"1. Workflows > New workflow. Trigger: **Recurrence**, set from this schedule: {r.get('summary','')}\n"
                    f"2. Action: **Call an agent** > {t['name']}. Message: the prompt below, verbatim.\n"
                    f"3. Optional second action for delivery (Teams message, Outlook send) if the prompt asks to send something; the prompt itself forbids sending without a yes, so keep delivery to a draft or DM to the owner.\n"
                    f"4. Each run consumes workflow capacity per action and Copilot Credits for the agent call.\n\n"
                    f"## Prompt to pass to the agent\n\n{r.get('content','')}\n")
        if t.get("logs") and not t.get("_logs_in_instructions"):
            open(os.path.join(bd, "seed-memories.md"), "w").write("# Seed memories\n\n" + "\n\n".join(f"- {m}" for m in t["logs"]) + "\n")
        open(os.path.join(bd, "MAPPING.md"), "w").write(mapping_md(t, caps, overflow))
        report.append({"slug": t["id"], "name": t["name"], "instr_chars": len(full), "overflow": bool(overflow),
                       "capabilities": ";".join(c["name"] for c in caps), "skills": len(t["skills"]),
                       "routines_manual": len(t["routines"]), "skill_chars": sum(len(s.get("content","")) for s in t["skills"]), "seed_memories": len(t.get("logs", [])),
                       "tools_manual": sum(1 for i in t["integrations"] if i["name"].lower() not in CAPABILITY_MAP or i["name"].lower() in TOOL_MAP)})
    open(os.path.join(out_dir, "README.md"), "w").write(README_TEXT)
    with open(os.path.join(out_dir, "conversion-report.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(report[0].keys())); w.writeheader(); w.writerows(report)
    print(f"converted {len(report)} bots -> {out_dir}; overflow: {sum(r['overflow'] for r in report)}")

if __name__ == "__main__":
    convert(sys.argv[1], sys.argv[2])
