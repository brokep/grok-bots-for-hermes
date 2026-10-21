# Event Request Desk as Hermes profile `grok-event-request-desk`

Source: https://x.ai/bot/marketplace/bots/event-request-desk  Creator: Emma Weyrauch

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `event-request-desk--getting-started`
- `event-request-desk--log-a-new-event-request`
- `event-request-desk--score-an-event-request`
- `event-request-desk--tune-the-decision-rubric`
- `event-request-desk--draft-the-reply`
- `event-request-desk--track-what-you-owe-after-a-yes`
- `event-request-desk--event-spend-and-yes-rate`
- `event-request-desk--queue-review`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekday intake sweep | `0 21 * * 1-5` (weekdays at 21:00) | Every weekday morning, logs and scores every event ask that came in overnight and names the ones that need a decision t… |
| Weekly queue review | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, the whole event request queue grouped by what needs a decision, what is stale, and what is alread… |
| Weekly commitment check | `0 9 * * 4` (Thursday at 09:00) | Every Thursday morning, what the team still owes organizers for events already said yes to, with anything overdue first. |

Paused jobs are hidden by default: `hermes -p grok-event-request-desk cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-event-request-desk cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Read new event and sponsorship asks out of the channel where people already ask.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the event queue and the weekly review where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Track what you owe an organizer after a yes as issues with owners and due dates.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **figma** (Grok plugin `657`): Pull the logo pack, booth artwork, or slides an organizer is waiting on.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **hex** (Grok plugin `651`): Chart event spend against your cap and your yes rate over a quarter.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Google Drive** (Grok plugin `45893413`): Read the tracker sheet and organizer files your team already keeps in Drive.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
