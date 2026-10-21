# Pfp Bot as Hermes profile `grok-pfp-bot`

Source: https://x.ai/bot/marketplace/bots/pfp-bot  Creator: Shub Gaur (@shubgaur)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `pfp-bot--icon-setup`
- `pfp-bot--make-icon`
- `pfp-bot--icon-prompt`
- `pfp-bot--icon-finish`
- `pfp-bot--icon-guide`
- `pfp-bot--take-selfie`
- `pfp-bot--icon-credit`
- `pfp-bot--pfp-scripts`

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **X** (Grok plugin `49086599`): Optional. Reads your X profile photo and handle directly, so nothing needs typing. Without it, I fetch your public profile photo from the handle you type.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
