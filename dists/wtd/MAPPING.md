# WTD as Hermes profile `grok-wtd`

Source: https://x.ai/bot/marketplace/bots/wtd  Creator: Jenna Nanpei (@jennananpei)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `wtd--vip-ae-nomination-sheet`
- `wtd--deck-qa-standards`
- `wtd--gtm-branded-deck`
- `wtd--email-reply-standards`
- `wtd--comms-source-of-truth`
- `wtd--outstanding-asks-review`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| VIP Plan status refresh | `0 9 * * 1-5` (weekdays at 09:00) | Weekday morning refresh of the marketing-visible VIP project plan / status hub (status only). |

Paused jobs are hidden by default: `hermes -p grok-wtd cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-wtd cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Notion** (Grok plugin `404`): Notion Skills + Notion MCP server packaged as a Cursor plugin.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Slack** (Grok plugin `674`): Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Drive** (Grok plugin `45893413`): Search, read, create, and share files.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
