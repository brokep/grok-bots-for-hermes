# Site Audit as Hermes profile `grok-site-audit`

Source: https://x.ai/bot/marketplace/bots/site-audit  Creator: Shimecki (@scheemunai)

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
| Monthly site re-audit | `0 9 1 * *` (1st of the month at 09:00) | Monthly re-audit of the one primary site |
| Weekly audit self-improve | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Weekly audit self-improve |

Enable with `hermes -p grok-site-audit cron list` then `hermes -p grok-site-audit cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.
