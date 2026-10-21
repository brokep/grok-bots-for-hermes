# Credit Card Max as Hermes profile `grok-credit-card-max`

Source: https://x.ai/bot/marketplace/bots/credit-card-max  Creator: Trevin Chow (@trevin)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `credit-card-max--getting-started`
- `credit-card-max--credit-card-max`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Monthly card rollup | `0 9 1 * *` (1st of the month at 09:00) | Fires on the 1st of each month to deliver a perk-maximization rollup (not a budget review). |
| Perk expiry watch | `0 9 * * *` (daily at 09:00) | Runs daily to nag only on T-5 and period-end for unmuted unused watched perks; silent otherwise. |
| Wrong-card recurring watch | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Runs weekly to flag recurring charges on a suboptimal card; silent when the queue is clean. |

Enable with `hermes -p grok-credit-card-max cron list` then `hermes -p grok-credit-card-max cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.
