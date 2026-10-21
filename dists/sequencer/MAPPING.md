# Sequencer as Hermes profile `grok-sequencer`

Source: https://x.ai/bot/marketplace/bots/sequencer  Creator: Simon Lackowski

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `sequencer--getting-started`
- `sequencer--auto-discovery`
- `sequencer--outbound-voice`
- `sequencer--humanizer`
- `sequencer--sequencer-core`
- `sequencer--sheet-brain`
- `sequencer--prospect-queue`
- `sequencer--crm-adapter`
- `sequencer--connect-accounts`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Sequencer daily | `0 8 * * 1-5` (weekdays at 08:00) | Disabled by default. Weekday mornings at 8am in the user's timezone. Advances every due sequence step, stages the next… |
| Daily prospects | `0 7 * * 1-5` (weekdays at 07:00) | Disabled by default. Weekday mornings at 7am in the user's timezone. Queues new prospects that match the confirmed ICP… |
| Inbox triage | `0 9 * * 1-5` (weekdays at 09:00) | Disabled by default. Hourly from 9am to 5pm on weekdays in the user's timezone. Flags inbound mail and messages from pe… |
| CRM sequence guard | `0 18 * * 1-5` (weekdays at 18:00) | Disabled by default. Weekday evenings at 6pm in the user's timezone. Pauses tracker rows where the CRM shows the saved… |

Paused jobs are hidden by default: `hermes -p grok-sequencer cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-sequencer cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Gmail** (Grok plugin `45893410`): Recommended, and the usual voice source when the user's mail runs here. Reads sent outbound and booked-meeting threads to build the voice card, and stages each…
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `66339841`): Recommended. The sequence tracker lives here when the user works in sheets, one row per contact per sequence. A CSV upload carries the same columns when it doe…
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Salesforce** (Grok plugin `47725205`): Optional, and one CRM option among peers. Supplies ownership, open-opportunity stages for the pause guard, and title winners during discovery. A CRM with no co…
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **Google Calendar** (Grok plugin `45893411`): Optional. Confirms which threads really ended in a booked meeting, so the voice card weights the touches that worked, and blocks review time for sending.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Optional. Adds team chat to inbox triage when a sequenced contact reaches the user there. Read only, never used to train cold voice.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
