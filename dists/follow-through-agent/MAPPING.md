# GTM Loop Closer as Hermes profile `grok-follow-through-agent`

Source: https://x.ai/bot/marketplace/bots/follow-through-agent  Creator: Jon Grigull

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `follow-through-agent--open-loop-audit`
- `follow-through-agent--agent-orchestration`
- `follow-through-agent--humanizer`
- `follow-through-agent--conversation-to-action`
- `follow-through-agent--follow-through-drafts`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Commitment-strand audit | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Disabled by default. Reconcile approved sources and privately surface evidence-backed commitments or facts stranded wit… |

Enable with `hermes -p grok-follow-through-agent cron list` then `hermes -p grok-follow-through-agent cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

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
- **Granola** (Grok plugin `5609`): 
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
- **Notion** (Grok plugin `404`): 
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Google Sheets** (Grok plugin `47662908`): 
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
