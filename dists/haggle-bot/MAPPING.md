# Haggle Bot as Hermes profile `grok-haggle-bot`

Source: https://x.ai/bot/marketplace/bots/haggle-bot  Creator: Daniel Gartshein

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `haggle-bot--haggle-setup`
- `haggle-bot--build-spend-inventory`
- `haggle-bot--score-savings-opportunity`
- `haggle-bot--research-alternatives`
- `haggle-bot--draft-vendor-counter`
- `haggle-bot--google-sheets-final-check`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Renewal window watch | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Disabled by default. Weekly scan of the vendor database for contracts renewing inside the priority window (default 120… |
| Monthly inventory refresh | `0 9 1 * *` (1st of the month at 09:00) | Disabled by default. Monthly re-pull of Ramp cards and bills, diffed against the vendor database, with new vendors, spe… |

Paused jobs are hidden by default: `hermes -p grok-haggle-bot cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-haggle-bot cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Ramp** (Grok plugin `32766883`): Live card and bill spend. Primary source for the vendor inventory.
  No known MCP server; search `hermes skills search ramp` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): The vendor database and savings tabs live here.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Draft vendor RFQs and counters. Never sends without your go.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Slack** (Grok plugin `674`): Optional. Source for vendor owners and usage, and colleague DMs for data. Never posts without your go.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Notion** (Grok plugin `404`): Optional. Source for vendor owners, purpose, and usage notes.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Google Drive** (Grok plugin `45893413`): Optional. Contracts, order forms, and quotes for commitment evidence.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): Optional. Vendor call notes for sentiment and commitments.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
