# Call Follow-Ups as Hermes profile `grok-call-follow-ups`

Source: https://x.ai/bot/marketplace/bots/call-follow-ups  Creator: Daniel Brill (@danielbrill_)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `call-follow-ups--getting-started`
- `call-follow-ups--crm-update-proposal`
- `call-follow-ups--next-steps-note`
- `call-follow-ups--promise-tracker`
- `call-follow-ups--recap-email`
- `call-follow-ups--voice-profile`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| New call watch | `0 9 * * 1-5` (weekdays at 09:00) | Every 30 minutes on weekdays, find calls the owner hosted that finished since the last run and stage the post-call pack… |

Enable with `hermes -p grok-call-follow-ups cron list` then `hermes -p grok-call-follow-ups cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Gong** (Grok plugin `47725204`): Finished calls, summaries, and transcripts. Granola covers the meetings it did not record.
  No known MCP server; search `hermes skills search gong` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): Transcript source for meetings your recorder did not capture. Works alongside Gong or on its own.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
- **Salesforce** (Grok plugin `47725205`): Where next steps, stage, close date, and new contacts are proposed. Connect the one CRM you use.
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **HubSpot** (Grok plugin `49339689`): CRM alternative to Salesforce.
  ```yaml
  mcp_servers:
    hubspot:
      url: "https://mcp.hubspot.com"
  ```
- **Attio** (Grok plugin `62459236`): CRM alternative to Salesforce.
  No known MCP server; search `hermes skills search attio` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Learns your voice from sent mail and saves follow-ups as drafts. Use Outlook instead on Microsoft 365.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Outlook** (Grok plugin `57302029`): Email alternative for Microsoft 365 users.
  No known MCP server; search `hermes skills search outlook` or wire one up under `mcp_servers:`.
- **Google Calendar** (Grok plugin `45893411`): Matches a call to its meeting and attendees when the recorder's participant list is thin.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Deliver the post-call pack as a DM.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Notion** (Grok plugin `404`): Keep post-call notes and the open promises where your team already looks.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Linear** (Grok plugin `512`): Turn a commitment from a call into a ticket, drafted for you to approve.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **Hex** (Grok plugin `651`): Pull account numbers before a call when your team keeps them in a warehouse.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
