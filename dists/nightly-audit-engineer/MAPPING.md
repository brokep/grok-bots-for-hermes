# Nightly Audit Engineer as Hermes profile `grok-nightly-audit-engineer`

Source: https://x.ai/bot/marketplace/bots/nightly-audit-engineer  Creator: Lingxi Li (@lingxi)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Nightly code-quality audit (4am) | `0 4 * * 1` (Mondays at 04:00 (weekly default)) | Research the whole tree, then one cleanup per area. Defaults to 4am; ask when to run. |

Enable with `hermes -p grok-nightly-audit-engineer cron list` then `hermes -p grok-nightly-audit-engineer cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.
