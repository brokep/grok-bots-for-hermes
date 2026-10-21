# GTM Connections as Hermes profile `grok-warm-intro-finder`

Source: https://x.ai/bot/marketplace/bots/warm-intro-finder  Creator: Brian Joseph

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `warm-intro-finder--connections-and-intros`
- `warm-intro-finder--agent-orchestration`
- `warm-intro-finder--humanizer`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Warm-path follow-through queue | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Disabled by default. Surface identified paths and intro requests whose next action is due or stalled. |

Enable with `hermes -p grok-warm-intro-finder cron list` then `hermes -p grok-warm-intro-finder cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Gmail** (Grok plugin `45893410`): 
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): 
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Salesforce** (Grok plugin `47725205`): 
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **Notion** (Grok plugin `404`): 
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Google Sheets** (Grok plugin `47662908`): 
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): 
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
