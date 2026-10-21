# Marketing Analyst as Hermes profile `grok-marketing-analyst`

Source: https://x.ai/bot/marketplace/bots/marketing-analyst  Creator: Josh Kim (@joshkim)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `marketing-analyst--marketing-analyst-setup`
- `marketing-analyst--connect-accounts`
- `marketing-analyst--ingest-exports`
- `marketing-analyst--weekly-report`
- `marketing-analyst--monthly-report`
- `marketing-analyst--answer-a-reporting-ask`
- `marketing-analyst--spend-watch`
- `marketing-analyst--html-report`
- `marketing-analyst--evidence-media`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Reporting ask watch | `0 9 * * 1-5` (weekdays at 09:00) | Disabled by default. Hourly during weekday working hours in the user's timezone. Reads the mailbox or label the user na… |
| Weekly paid media report | `0 9 * * 1` (Monday at 09:00) | Disabled by default. Monday mornings in the user's timezone. Builds last week's paid media report from the exports on h… |
| Monthly paid media report | `0 9 1 * *` (1st of the month at 09:00) | Disabled by default. The 1st of the month in the user's timezone. Builds the closed month's report with the three month… |

Paused jobs are hidden by default: `hermes -p grok-marketing-analyst cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-marketing-analyst cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Google Sheets** (Grok plugin `47662908`): Recommended. Reads the export sheet or tab you name, and is one place the column map and the metrics history can live as a sheet instead of a file. Read only u…
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Google Drive** (Grok plugin `45893413`): Recommended. Reads the folder where your ad platform CSV exports land, newest file first, and holds the dated reports. A pasted file works instead.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Optional. Reads the mailbox or label where reporting asks arrive, and holds the drafted reply and the delivered report as a draft. Sends only when you say send.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Slack** (Grok plugin `674`): Optional. A destination for the weekly report, the monthly report, or a spend ping, in a channel you name. Nothing is posted without your explicit yes.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
