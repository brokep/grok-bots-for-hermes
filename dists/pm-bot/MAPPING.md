# PM bot as Hermes profile `grok-pm-bot`

Source: https://x.ai/bot/marketplace/bots/pm-bot  Creator: Ulysses Ng

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `pm-bot--getting-started-binding-prd-pm`
- `pm-bot--enterprise-binding-prd-cut`
- `pm-bot--adhd-friendly-agent-responses`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekday attention list | `0 9 * * 1-5` (weekdays at 09:00) | Weekday morning quiet digest of open cuts, Eng/QA blockers, and decisions waiting on the owner; stays silent when nothi… |

Enable with `hermes -p grok-pm-bot cron list` then `hermes -p grok-pm-bot cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.
