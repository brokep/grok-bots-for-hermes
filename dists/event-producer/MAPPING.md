# Event Producer as Hermes profile `grok-event-producer`

Source: https://x.ai/bot/marketplace/bots/event-producer  Creator: Jenna Nanpei (@jennananpei)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `event-producer--getting-started`
- `event-producer--build-the-event-brief`
- `event-producer--run-of-show`
- `event-producer--vendor-and-venue-tracker`
- `event-producer--guest-list-and-invites`
- `event-producer--guest-travel-and-hotels`
- `event-producer--day-of-checklist`
- `event-producer--post-event-recap`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Event countdown check | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, what is due, what is late, and what is still unconfirmed, with the days-out count, registrations… |
| Day-of brief | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | On the morning of the event, the run of show with owners, vendor arrival times with phone numbers, the guest and dietar… |
| Post-event recap draft | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Two days after the event, drafts the recap from the trackers and asks for the three numbers it cannot know. |

Enable with `hermes -p grok-event-producer cron list` then `hermes -p grok-event-producer cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post the day-of brief and countdown checks in the channel your crew already reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the event brief, run of show, and trackers where the team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Give every prep task an owner and a due date in the tracker your team already uses.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **figma** (Grok plugin `657`): Pull signage, name badges, and slide files from your real design files.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Vendor and invite mail waits in your drafts, unsent.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): Load-in, the event, and vendor deadlines sit on a real calendar.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Keep the vendor tracker and guest list editable by the whole team.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
