# Deal Inspector as Hermes profile `grok-deal-qualification`

Source: https://x.ai/bot/marketplace/bots/deal-qualification  Creator: Jon Grigull

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `deal-qualification--getting-started`
- `deal-qualification--crm-writeback`
- `deal-qualification--qualification-frameworks`
- `deal-qualification--stage-gate-audit`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Friday stage audit | `0 12 * * 5` (Friday at 12:00) | Every Friday afternoon, audit each of the owner's opportunities that was created or moved stage this week against the q… |

Paused jobs are hidden by default: `hermes -p grok-deal-qualification cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-deal-qualification cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Gong** (Grok plugin `47725204`): Call transcripts, the evidence behind every criterion. Granola works too.
  No known MCP server; search `hermes skills search gong` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): Transcript source for meetings your recorder did not capture.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
- **Salesforce** (Grok plugin `47725205`): Opportunities, stage history, and the qualification fields the audit fills. Connect the one CRM you use.
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **HubSpot** (Grok plugin `49339689`): CRM alternative to Salesforce.
  ```yaml
  mcp_servers:
    hubspot:
      url: "https://mcp.hubspot.com"
  ```
- **Attio** (Grok plugin `62459236`): CRM alternative to Salesforce.
  No known MCP server; search `hermes skills search attio` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Deliver the weekly audit as a DM.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Gmail** (Grok plugin `45893410`): Checks whether we did what we promised on the last call.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Notion** (Grok plugin `404`): Keep audits and the framework definitions where your team already looks.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Google Sheets** (Grok plugin `47662908`): Export the scorecards when your team tracks them in a sheet.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
