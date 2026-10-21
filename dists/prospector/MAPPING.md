# GTM Prospecting as Hermes profile `grok-prospector`

Source: https://x.ai/bot/marketplace/bots/prospector  Creator: Caro Scalercio

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `prospector--prospecting-loop`
- `prospector--agent-orchestration`
- `prospector--humanizer`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly prospecting hygiene | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Disabled by default. Audit selected lists for duplicates, stale ownership, recent touches, and suppression conflicts. |

Enable with `hermes -p grok-prospector cron list` then `hermes -p grok-prospector cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Gmail** (Grok plugin `45893410`): 
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `47662908`): 
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Notion** (Grok plugin `404`): 
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Salesforce** (Grok plugin `47725205`): 
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
