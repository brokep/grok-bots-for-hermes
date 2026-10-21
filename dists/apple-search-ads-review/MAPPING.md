# Apple Search Ads Review as Hermes profile `grok-apple-search-ads-review`

Source: https://x.ai/bot/marketplace/bots/apple-search-ads-review  Creator: Chris Everett

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `apple-search-ads-review--getting-started`
- `apple-search-ads-review--set-spend-targets`
- `apple-search-ads-review--spend-review`
- `apple-search-ads-review--search-terms-and-negatives`
- `apple-search-ads-review--bids-and-budgets`
- `apple-search-ads-review--weekly-ad-review`
- `apple-search-ads-review--change-sheet`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly ad review | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Every week on the user's chosen morning, a read on last week's Apple Search Ads spend against target, with the changes… |
| Daily spend check | `0 9 * * 1-5` (weekdays at 09:00) | Each weekday morning, checks for a new export and speaks up only about groups over target or spending with nothing to s… |

Paused jobs are hidden by default: `hermes -p grok-apple-search-ads-review cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-apple-search-ads-review cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post a review you approved to the channel your growth team already reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the targets sheet and every review where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **hex** (Grok plugin `651`): Pull spend and install numbers straight from your warehouse when they are modeled there.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Databricks SQL** (Grok plugin `32738678`): Query your Apple Search Ads reports straight from the warehouse instead of an export.
  No known MCP server; search `hermes skills search databricks-sql` or wire one up under `mcp_servers:`.
- **linear** (Grok plugin `512`): Turn an approved change list into tasks for whoever holds ad account access.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
