# Home robots as Hermes profile `grok-home-robots`

Source: https://x.ai/bot/marketplace/bots/home-robots  Creator: Sawyer Merritt (@SawyerMerritt)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `home-robots--connect-navimow`
- `home-robots--control-navimow`
- `home-robots--connect-matic`
- `home-robots--control-matic`
- `home-robots--connect-home-robot`
- `home-robots--control-home-robot`
- `home-robots--share-this-bot`
