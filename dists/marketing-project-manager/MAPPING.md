# Project Manager as Hermes profile `grok-marketing-project-manager`

Source: https://x.ai/bot/marketplace/bots/marketing-project-manager  Creator: Josh Kim (@joshkim)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `marketing-project-manager--project-manager-setup`
- `marketing-project-manager--plan`
- `marketing-project-manager--delegate`
- `marketing-project-manager--check-in`
- `marketing-project-manager--gates`
- `marketing-project-manager--retro`
- `marketing-project-manager--html-report`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekday status check-in | `0 9 * * 1-5` (weekdays at 09:00) | Disabled by default. Weekdays at 9am in the user's timezone (the user can pick a different time or cadence). Runs one s… |
| Friday week ahead | `0 16 * * 5` (Friday at 16:00) | Disabled by default. Fridays at 4pm in the user's timezone. Lists what is due in the next 7 days, what the user has to… |

Enable with `hermes -p grok-marketing-project-manager cron list` then `hermes -p grok-marketing-project-manager cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Linear** (Grok plugin `512`): Optional. Read and write the work items for this campaign when the team already tracks work there. A plain list in this chat works instead.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **Notion** (Grok plugin `404`): Optional. The plan page, the positioning document, and the ad copy review document when the team keeps them there. A file under /workspace/pm/ works instead.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **Slack** (Grok plugin `674`): Optional. Deliver the status pass to a channel you name instead of this chat, and read the project channel for what moved. Never a destination for a gate, whic…
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Google Drive** (Grok plugin `45893413`): Optional. Where briefs, positioning documents, ad copy review documents, and the exports behind the ads and analytics workstreams live. Read and write, no secr…
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Google Calendar** (Grok plugin `45893411`): Optional. Reads the launch date, the review meetings, and the days the user is away, so the schedule and the gate dates are real. Read only.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
