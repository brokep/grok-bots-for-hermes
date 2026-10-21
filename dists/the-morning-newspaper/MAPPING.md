# The Morning Newspaper as Hermes profile `grok-the-morning-newspaper`

Source: https://x.ai/bot/marketplace/bots/the-morning-newspaper  Creator: Karen X. Cheng (@karenxcheng)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `the-morning-newspaper--morning-newspaper-bootstrap`
