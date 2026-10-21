# Love ❤️ as Hermes profile `grok-love`

Source: https://x.ai/bot/marketplace/bots/love  Creator: Danny Buck (@dannybuck)

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
| Monday date check | `0 9 * * 1` (Monday at 09:00) | Monday date check |
| Wednesday question | `0 9 * * 3` (Wednesday at 09:00) | Wednesday question |
| Monthly small gift | `0 9 1 * *` (1st of the month at 09:00) | Monthly small gift |

Paused jobs are hidden by default: `hermes -p grok-love cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-love cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
