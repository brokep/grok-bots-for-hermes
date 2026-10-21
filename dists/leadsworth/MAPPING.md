# Lead Pipeline Desk as Hermes profile `grok-leadsworth`

Source: https://x.ai/bot/marketplace/bots/leadsworth  Creator: Miguel Cruz (@cruzmiguel000)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `leadsworth--getting-started`
- `leadsworth--build-the-lead-ledger`
- `leadsworth--score-and-qualify-leads`
- `leadsworth--merge-duplicate-leads`
- `leadsworth--route-leads-and-draft-the-first-reply`
- `leadsworth--pipeline-health-report`
- `leadsworth--connect-a-tool-or-change-the-source`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily lead triage | `0 21 * * 1-5` (weekdays at 21:00) | Every weekday morning, scores the leads that came in overnight, merges duplicates, and lists what has no owner or is pa… |
| Weekly pipeline report | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, the week's lead counts by source, the tier mix, what moved, what is stuck, and pacing against the… |

Paused jobs are hidden by default: `hermes -p grok-leadsworth cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-leadsworth cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post the morning triage and the weekly report to a channel your team already reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the lead ledger and every weekly report where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Open a follow-up issue when a lead is stuck or needs someone outside sales.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **hex** (Grok plugin `651`): Pull leads and pipeline history from your warehouse when that is where they land.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Databricks SQL** (Grok plugin `32738678`): Query lead and pipeline tables straight from your warehouse.
  No known MCP server; search `hermes skills search databricks-sql` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Save first replies as unsent drafts in your own account.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `47662908`): Read and write the lead list where it already lives.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Salesforce** (Grok plugin `47725205`): Read leads and write owners and next steps back to your CRM.
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
