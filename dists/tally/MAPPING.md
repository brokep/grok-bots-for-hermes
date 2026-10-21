# Paid Media Report Desk as Hermes profile `grok-tally`

Source: https://x.ai/bot/marketplace/bots/tally  Creator: Miguel Cruz (@cruzmiguel000)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `tally--getting-started`
- `tally--map-an-export`
- `tally--answer-a-reporting-ask`
- `tally--weekly-paid-media-report`
- `tally--monthly-paid-media-report`
- `tally--what-moved-and-why`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Reporting ask watch | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Through the working day, checks the channels you named for paid media reporting asks and brings you a drafted reply to… |
| Weekly paid media report | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Once a week, builds last week's paid media report from the exports on hand, or names exactly which export it still need… |
| Monthly paid media report | `0 9 1 * *` (1st of the month at 09:00) | On the first business day of the month, builds the closed month's report with the three-month trend, campaign rollup, a… |

Enable with `hermes -p grok-tally cron list` then `hermes -p grok-tally cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Watch your channels for reporting asks and post the reports you approve.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep every weekly and monthly report where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Turn something a report says to fix into an issue in your backlog.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **hex** (Grok plugin `651`): Read spend and conversion data that already lands in your warehouse.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Databricks SQL** (Grok plugin `32738678`): Query spend and conversion tables straight from your warehouse.
  No known MCP server; search `hermes skills search databricks-sql` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Pick up the scheduled export emails the ad platforms send.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `47662908`): Read exports you keep in a sheet.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
