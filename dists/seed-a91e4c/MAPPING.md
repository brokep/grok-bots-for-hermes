# SWE as Hermes profile `grok-seed-a91e4c`

Source: https://x.ai/bot/marketplace/bots/seed-a91e4c  Creator: Cursor (@cursor_ai)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `seed-a91e4c--swe-bot-onboard`
- `seed-a91e4c--swe-bot`
- `seed-a91e4c--swe-bot-triage`
- `seed-a91e4c--swe-bot-code`
- `seed-a91e4c--swe-bot-babysit`
- `seed-a91e4c--swe-bot-test`
- `seed-a91e4c--swe-bot-monitor`
