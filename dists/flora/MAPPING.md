# Flora as Hermes profile `grok-flora`

Source: https://x.ai/bot/marketplace/bots/flora  Creator: Rich Silver (@RichSilver)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `flora--houseplant-care-first-run`
- `flora--private-houseplant-journal`
- `flora--houseplant-care-card`
- `flora--houseplant-weekly-collection-news`
