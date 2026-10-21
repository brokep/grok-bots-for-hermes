# Office Ops Desk as Hermes profile `grok-office-ops-desk`

Source: https://x.ai/bot/marketplace/bots/office-ops-desk  Creator: Erika Cabrera (@ericacabera)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `office-ops-desk--getting-started`
- `office-ops-desk--build-the-office-ops-ledger`
- `office-ops-desk--weekly-facilities-digest`
- `office-ops-desk--late-shipment-follow-up`
- `office-ops-desk--team-celebrations-list`
- `office-ops-desk--new-hire-setup`
- `office-ops-desk--sync-to-notion-linear-and-slack`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily shipment status | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, a short status on what was delivered, what is late, and what has stopped moving. |
| Weekly facilities digest | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, the open facilities issues grouped by severity with owners and days open. |
| Team celebrations reminder | `0 9 * * 5` (Friday at 09:00) | Every Friday morning, the birthdays and work anniversaries landing in the next 14 days. |

Enable with `hermes -p grok-office-ops-desk cron list` then `hermes -p grok-office-ops-desk cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post a facilities digest or shipment status you approved to a team channel.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Mirror the shipments, facilities, and celebrations ledgers into your office wiki.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): File facilities issues as tickets and keep their status in step with the log.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
