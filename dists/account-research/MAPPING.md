# GTM Account Research as Hermes profile `grok-account-research`

Source: https://x.ai/bot/marketplace/bots/account-research  Creator: Stefan Markarian

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `account-research--account-research`
- `account-research--agent-orchestration`
- `account-research--humanizer`
- `account-research--account-sot-sync`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly account monitor | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Disabled by default. Check selected strategic accounts for sourced changes and update their private research brief. |

Paused jobs are hidden by default: `hermes -p grok-account-research cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-account-research cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Salesforce** (Grok plugin `47725205`): 
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): 
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): 
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): 
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Notion** (Grok plugin `404`): 
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Google Sheets** (Grok plugin `47662908`): 
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): 
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
