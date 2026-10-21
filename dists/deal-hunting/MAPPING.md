# Deal Hunting as Hermes profile `grok-deal-hunting`

Source: https://x.ai/bot/marketplace/bots/deal-hunting  Creator: Shimecki (@scheemunai)

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
| Watchlist check | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Watchlist check |
| Weekly process note | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Weekly process note |

Enable with `hermes -p grok-deal-hunting cron list` then `hermes -p grok-deal-hunting cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.
