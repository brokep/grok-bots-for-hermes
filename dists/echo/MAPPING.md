# Meeting Recap Deck as Hermes profile `grok-echo`

Source: https://x.ai/bot/marketplace/bots/echo  Creator: Krista Letz (@kristaletz)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `echo--getting-started`
- `echo--read-the-slide-template`
- `echo--build-the-recap-deck`
- `echo--update-one-slide`
- `echo--recap-note-without-slides`
- `echo--share-the-approved-recap`
- `echo--next-steps-to-tickets`
- `echo--themes-across-meetings`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Post-meeting recap draft | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | After a meeting ends, drafts the recap from your notes and leaves it here for you to check. |
| Friday recap roundup | `0 9 * * 5` (Friday at 09:00) | Every Friday, the recaps that went out this week, the drafts still sitting unsent, and the next steps that are past the… |

Enable with `hermes -p grok-echo cron list` then `hermes -p grok-echo cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **figma** (Grok plugin `657`): Read the template slide you point at and build the recap deck in it.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **Google Slides** (Grok plugin `47662907`): Build the recap deck in your Google Slides template.
  No known MCP server; search `hermes skills search google-slides` or wire one up under `mcp_servers:`.
- **notion-workspace** (Grok plugin `404`): Pull meeting notes from your pages and keep finished recaps where your team reads them.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **slack** (Grok plugin `674`): Post a recap you approved to the channel your team already reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **linear** (Grok plugin `512`): Turn the next steps you agreed to into tickets with owners and dates.
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
- **Google Calendar** (Grok plugin `45893411`): Search events and schedule meetings.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): Your meetings in your workflow. Meeting notes, decisions, and commitments.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
- **Gong** (Grok plugin `47725204`): Pull call summaries and transcripts when your notes live in Gong.
  No known MCP server; search `hermes skills search gong` or wire one up under `mcp_servers:`.
