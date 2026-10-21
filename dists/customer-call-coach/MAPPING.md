# Customer Call Coach & Assistant as Hermes profile `grok-customer-call-coach`

Source: https://x.ai/bot/marketplace/bots/customer-call-coach  Creator: Anoop Baliga (@akbaliga96)

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
| Friday Coach Refresh | `0 12 * * 5` (Friday at 12:00) | Quiet Friday afternoon refresh of coaching signals from meetings and Slack; stays silent unless a connector fails. Ship… |

Paused jobs are hidden by default: `hermes -p grok-customer-call-coach cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-customer-call-coach cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Granola** (Grok plugin `5609`): Your meetings in your workflow. Granola gives Cursor access to what your team discussed, decided, and committed to.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
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
