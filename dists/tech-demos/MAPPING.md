# Tech Demos as Hermes profile `grok-tech-demos`

Source: https://x.ai/bot/marketplace/bots/tech-demos  Creator: Matt Palmer (@mattyp)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `tech-demos--project-planning`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily X tech scout | `0 9 * * 1-5` (weekdays at 09:00) | Weekdays at 9:00 AM. Lands paused on import. |

Paused jobs are hidden by default: `hermes -p grok-tech-demos cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-tech-demos cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **X** (Grok plugin `49086599`): Search posts, read timelines, pull trends, and manage bookmarks.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
