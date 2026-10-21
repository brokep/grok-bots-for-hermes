# Market Researcher as Hermes profile `grok-market-researcher`

Source: https://x.ai/bot/marketplace/bots/market-researcher  Creator: Josh Kim (@joshkim)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `market-researcher--market-researcher-setup`
- `market-researcher--connect-accounts`
- `market-researcher--ad-and-creative-analysis`
- `market-researcher--landing-page-and-offer-watch`
- `market-researcher--search-overlap`
- `market-researcher--messaging-matrix`
- `market-researcher--content-and-social-cadence`
- `market-researcher--weekly-brief`
- `market-researcher--strategy-read`
- `market-researcher--capture-and-report`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly marketing brief | `0 8 * * 1` (Monday at 08:00) | Disabled by default. Monday at 8am in the user's timezone, or any day and time the user picks. Checks every competitor'… |
| Monthly strategy read | `0 10 1 * *` (1st of the month at 10:00) | Disabled by default. The 1st of the month at 10am in the user's timezone. Rolls the month of weekly briefs and the user… |

Enable with `hermes -p grok-market-researcher cron list` then `hermes -p grok-market-researcher cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **X** (Grok plugin `49086599`): Recommended. Reads competitor company and product handles for post volume, engagement, themes, and promoted copy being tested in public. Read only, it never fo…
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Optional. Holds the swipe file index, the promotion calendar, the search overlap table, and the messaging matrix when the user wants them outside chat, and is…
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Google Drive** (Grok plugin `45893413`): Optional. The folder where ad platform, analytics, or search console CSV exports are dropped for the runs when a platform is not signed in. Read only. A paste…
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Optional. Delivers the weekly brief and the strategy read to a channel the user names instead of this chat.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
