# Alfred as Hermes profile `grok-alfred`

Source: https://x.ai/bot/marketplace/bots/alfred  Creator: Robin Delta (@heyrobinai)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `alfred--grok-bot-organization-discovery-architecture`
- `alfred--workflow-automation-decision`
- `alfred--grok-bot-system-design`
- `alfred--pilot-test-activate`
- `alfred--audit-repair-govern`
- `alfred--public-share-security-audit`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly Company & Grok Bot Improvement Review | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Weekly Company & Grok Bot Improvement Review |
| Monthly Bot Portfolio Strategy Review | `0 9 1 * *` (1st of the month at 09:00) | Monthly Bot Portfolio Strategy Review |
| Quarterly Company & AI Operating Model Review | `0 9 1 1,4,7,10 *` (first day of each quarter at 09:00) | Quarterly Company & AI Operating Model Review |

Paused jobs are hidden by default: `hermes -p grok-alfred cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-alfred cron resume <id>`.
