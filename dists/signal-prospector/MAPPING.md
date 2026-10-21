# Signal Prospector as Hermes profile `grok-signal-prospector`

Source: https://x.ai/bot/marketplace/bots/signal-prospector  Creator: Krista Letz (@kristaletz)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `signal-prospector--getting-started`
- `signal-prospector--account-tiering`
- `signal-prospector--contact-ranking`
- `signal-prospector--first-touch-drafts`
- `signal-prospector--signal-scan`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Monday signal digest | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, scan the week's signals across the owner's book, rank the accounts and contacts, and stage first-… |

Paused jobs are hidden by default: `hermes -p grok-signal-prospector cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-signal-prospector cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Salesforce** (Grok plugin `47725205`): Leads, contacts, campaign responses, activities, and ownership. Connect the one CRM you use.
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **HubSpot** (Grok plugin `49339689`): CRM alternative to Salesforce; form fills and email engagement count as signals.
  ```yaml
  mcp_servers:
    hubspot:
      url: "https://mcp.hubspot.com"
  ```
- **Attio** (Grok plugin `62459236`): CRM alternative to Salesforce; lists and notes carry the signals.
  No known MCP server; search `hermes skills search attio` or wire one up under `mcp_servers:`.
- **Mixpanel** (Grok plugin `11976`): Product signups, activation, and usage spikes by company domain.
  No known MCP server; search `hermes skills search mixpanel` or wire one up under `mcp_servers:`.
- **X** (Grok plugin `49086599`): Public posts from the account and its leaders, for a dated hook the signal scan can cite.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
- **Hunter** (Grok plugin `62459238`): Finds and verifies business emails for ranked contacts who are not in the CRM yet.
  No known MCP server; search `hermes skills search hunter` or wire one up under `mcp_servers:`.
- **Clay** (Grok plugin `49110469`): Enrichment for titles, seniority, and company facts when you already run Clay.
  No known MCP server; search `hermes skills search clay` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Saves first-touch drafts and learns the owner's voice. Use Outlook instead on Microsoft 365.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Slack** (Grok plugin `674`): Deliver the signal digest as a DM.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
