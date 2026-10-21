# Hiring Signals as Hermes profile `grok-hiring-activity-monitor`

Source: https://x.ai/bot/marketplace/bots/hiring-activity-monitor  Creator: Simon Lackowski

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `hiring-activity-monitor--hiring-signals`
- `hiring-activity-monitor--agent-orchestration`
- `hiring-activity-monitor--humanizer`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekday hiring signal digest | `0 9 * * 1-5` (weekdays at 09:00) | Disabled by default. Ingest selected sources, write normalized rows to the confirmed system of record, and deliver new… |

Paused jobs are hidden by default: `hermes -p grok-hiring-activity-monitor cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-hiring-activity-monitor cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Google Sheets** (Grok plugin `47662908`): 
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Notion** (Grok plugin `404`): 
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Slack** (Grok plugin `674`): 
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Salesforce** (Grok plugin `47725205`): 
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
