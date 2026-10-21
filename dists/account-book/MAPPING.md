# Account Research Desk as Hermes profile `grok-account-book`

Source: https://x.ai/bot/marketplace/bots/account-book  Creator: Anoop Baliga (@akbaliga96)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `account-book--getting-started`
- `account-book--build-the-account-list`
- `account-book--account-brief-before-a-call`
- `account-book--week-ahead-call-prep`
- `account-book--stakeholder-map`
- `account-book--incumbent-and-competitor-check`
- `account-book--account-signals-refresh`
- `account-book--open-threads-and-next-steps`
- `account-book--account-usage-and-health`
- `account-book--outreach-and-follow-up-drafts`
- `account-book--account-plan`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly account signals | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, checks your accounts for public news, funding, leadership, and hiring signals, and reports only w… |
| Weekday call prep | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, a short prep on the external calls that day with what changed, who is on them, and what is still… |
| Friday open threads review | `0 9 * * 5` (Friday at 09:00) | Every Friday morning, the open threads and next steps across your accounts, with what has gone stale and what closed th… |

Paused jobs are hidden by default: `hermes -p grok-account-book cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-account-book cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post a brief or plan you approved to the channel your deal team reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep account files and plans where your team already looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): See what an account asked for as issues, and check status before a call.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **hex** (Grok plugin `651`): Read account usage or pipeline numbers your team keeps in a warehouse.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Databricks SQL** (Grok plugin `32738678`): Query account usage and health numbers straight from your warehouse.
  No known MCP server; search `hermes skills search databricks-sql` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): Pull notes from your customer calls.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
- **Google Drive** (Grok plugin `45893413`): Read account docs and decks your team already keeps in Drive.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Salesforce** (Grok plugin `47725205`): Read and update Salesforce records.
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
