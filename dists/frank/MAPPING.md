# frank as Hermes profile `grok-frank`

Source: https://x.ai/bot/marketplace/bots/frank  Creator: Natasha Kuo (@tashatweetss)

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
| Exec interview-prep reminder | `0 9 * * 1-5` (weekdays at 09:00) | Weekdays: check today's interviews vs a Notion prep doc. |
| Exec conference-room rundown (2 business days ahead) | `0 12 * * 1-5` (weekdays at 12:00) | Weekday afternoon: room chart for two business days out. |
| Exec same-day conference-room check | `0 21 * * 1-5` (weekdays at 21:00) | Weekday morning: same-day room chart for overnight changes. |
| Weekly leadership-outreach check | `0 9 * * 5` (Friday at 09:00) | Friday: Slack outreach channel vs tracker for one exec. |

Enable with `hermes -p grok-frank cron list` then `hermes -p grok-frank cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Slack** (Grok plugin `674`): Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Notion** (Grok plugin `404`): Notion Skills + Notion MCP server packaged as a Cursor plugin.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Google Sheets** (Grok plugin `47662908`): 
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
