# Recruiting Coordinator as Hermes profile `grok-mr-toms`

Source: https://x.ai/bot/marketplace/bots/mr-toms  Creator: Tommy Hansen (@TommyHansenTA)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `mr-toms--getting-started`
- `mr-toms--build-the-hiring-tracker`
- `mr-toms--schedule-an-interview-loop`
- `mr-toms--interviewer-prep-packet`
- `mr-toms--stalled-loop-follow-ups`
- `mr-toms--candidate-message-drafts`
- `mr-toms--run-the-debrief`
- `mr-toms--interviewer-coaching`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily hiring brief | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, today's interviews, who still needs scheduling, and what is waiting on someone. |
| Evening interview prep | `0 17 * * 1` (Mondays at 17:00 (weekly default)) | The evening before, a prep packet for each of tomorrow's interviews with the competency, questions, and open items per… |
| Afternoon loop check | `0 12 * * 1-5` (weekdays at 12:00) | Every weekday afternoon, what went stale since the morning brief, each item with a drafted nudge. |
| Urgent thread check | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Through the workday, flags a candidate or interviewer message that threatens a booked loop and drafts the reply. |
| Candidate reply drafts | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Through the workday, leaves an unsent draft reply for each new candidate email so the user only edits and sends. |
| Interview coaching review | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Once a week, coaches the scorecards and messages the user queued and flags ratings written without evidence. |
| Weekly pipeline review | `0 12 * * 5` (Friday at 12:00) | Every Friday afternoon, what moved per role, who is stuck and with whom, next week's interview load, and the calls that… |

Paused jobs are hidden by default: `hermes -p grok-mr-toms cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-mr-toms cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post a hiring brief or an interviewer nudge you approved to a channel you choose.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the hiring tracker, prep packets, and debrief summaries where the hiring team already looks.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Open a task for an approved req, a take-home review, or a new hire's first week.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **figma** (Grok plugin `657`): Open a design candidate's portfolio or take-home file so the panel reviews the real work.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): Pull interview notes and action items straight from your meetings.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Ashby** (Grok plugin `49104326`): Search candidates, prep interviews, and manage pipeline tasks.
  No known MCP server; search `hermes skills search ashby` or wire one up under `mcp_servers:`.
