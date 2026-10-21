# Tradbot as Hermes profile `grok-tradbot-2`

Source: https://x.ai/bot/marketplace/bots/tradbot-2  Creator: Claire Vo (@clairevo)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `tradbot-2--family-calendar-briefs`
- `tradbot-2--kitchen-table-newspaper`
- `tradbot-2--monthly-parent-note`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekday family digest | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, one short brief of the household things that need you today, and quiet when nothing does. |
| Afternoon pickup check | `0 12 * * 1-5` (weekdays at 12:00) | Every weekday afternoon, a one line check that today's pickup is covered, and the fix when it is not. |
| Kitchen table newspaper | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, the printable one-page kitchen newspaper kids can read at the table. |
| Weekend preview | `0 17 * * 0,6` (weekends at 17:00) | Every Friday evening, the weekend and the week after it with the collisions, what to prepare, and everything still owed. |
| Monthly parent note | `0 9 1 * *` (1st of the month at 09:00) | On the first of each month, local events worth considering plus age-adjusted development and parenting notes. |

Enable with `hermes -p grok-tradbot-2 cron list` then `hermes -p grok-tradbot-2 cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
