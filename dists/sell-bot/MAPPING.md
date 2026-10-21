# Sell Bot as Hermes profile `grok-sell-bot`

Source: https://x.ai/bot/marketplace/bots/sell-bot  Creator: Shub Gaur (@shubgaur)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `sell-bot--sell-setup`
- `sell-bot--accounts`
- `sell-bot--draft-email`
- `sell-bot--schedule`
- `sell-bot--watch-on-x`
- `sell-bot--prep-page`
- `sell-bot--call-wrap`
- `sell-bot--follow-through`
- `sell-bot--account-watch`
- `sell-bot--support-desk`
- `sell-bot--proposal-desk`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Morning prep | `0 7 * * 1-5` (weekdays at 07:00) | Disabled by default. Weekdays 7am: prep pages for today's watched calls. |
| Confirm notes | `0 9 * * 1-5` (weekdays at 09:00) | Disabled by default. Hourly on weekdays: confirm-note drafts for calls about an hour out. |
| Evening wrap-up | `45 17 * * 1-5` (weekdays at 17:45) | Disabled by default. Weekdays 5:45pm: wrap-ups and the digest for today's calls. |
| Daily follow-through | `50 7 * * 1-5` (weekdays at 07:50) | Disabled by default. Weekdays 7:50am: check-ins, wow moments, and due series emails. |
| Daily account watch | `56 8 * * 1-5` (weekdays at 08:56) | Disabled by default. Weekdays 8:56am: credit runway, expansion, watched accounts, and X. |
| Daily prospect follow-up | `40 9 * * 1-5` (weekdays at 09:40) | Disabled by default. Weekdays 9:40am: prospect replies, follow-ups, leads, and invites. |
| Weekly pipeline review | `0 9 * * 1` (Monday at 09:00) | Disabled by default. Mondays 9am: stalled deals, overdue touches, and nudges. |
| Monday impact read | `20 9 * * 1` (Monday at 09:20) | Disabled by default. Mondays 9:20am: how accounts with calls moved against everyone else. |
| Launch heads-ups | `10 10 * * 1-5` (weekdays at 10:10) | Disabled by default. Weekdays 10:10am and 3:10pm: launches matched to customers who asked. |
| Friday writing review | `30 15 * * 5` (Friday at 15:30) | Disabled by default. Fridays 3:30pm: drafts against what you sent, and voice rules. |

Paused jobs are hidden by default: `hermes -p grok-sell-bot cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-sell-bot cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Gmail** (Grok plugin `45893410`): Recommended. Drafts every email, reads replies and support email, and compares sent mail with drafts. Sends only when you say send.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Calendar** (Grok plugin `45893411`): Required for the call routines. Finds watched calls, and books calls after your yes.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
- **Granola** (Grok plugin `5609`): Optional. Call notes for learnings and follow-ups. Pasted notes work too.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `45893414`): Optional. Lead lists, usage or credit exports, and your roster sheet.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Optional. Reads launch channels for heads-ups. Read only.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **X** (Grok plugin `49086599`): Optional. Finds handles and reads posts. Never follows, posts, or sends DMs. Reads bill your X API credits.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
