# Dan Lanning as Hermes profile `grok-dan-lanning`

Source: https://x.ai/bot/marketplace/bots/dan-lanning  Creator: Jenna Nanpei (@jennananpei)

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
| Post-pitch call review | `0 17 * * 1-5` (weekdays at 17:00) | Weekday evening review of recent pitch-call transcripts with structured coaching |

Enable with `hermes -p grok-dan-lanning cron list` then `hermes -p grok-dan-lanning cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Notion** (Grok plugin `404`): Notion Skills + Notion MCP server packaged as a Cursor plugin.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
