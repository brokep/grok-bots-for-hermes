# Stalk Bot as Hermes profile `grok-stalk-bot`

Source: https://x.ai/bot/marketplace/bots/stalk-bot  Creator: Shub Gaur (@shubgaur)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `stalk-bot--stalk-setup`
- `stalk-bot--modules`
- `stalk-bot--identity-ladder`
- `stalk-bot--profile-us`
- `stalk-bot--subscribe`
- `stalk-bot--walk-the-product`
- `stalk-bot--snapshot-site`
- `stalk-bot--read-the-mail`
- `stalk-bot--watch-x`
- `stalk-bot--pulse`
- `stalk-bot--evidence-media`
- `stalk-bot--html-report`
- `stalk-bot--teardown`
- `stalk-bot--battlecard`
- `stalk-bot--competitor-churn`
- `stalk-bot--feature-matrix`
- `stalk-bot--add-competitor`
- `stalk-bot--drop-competitor`
- `stalk-bot--demo-pulse`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Competitor pulse | `0 9 * * 1,3,5` (Monday, Wednesday, Friday at 09:00) | Disabled by default. Monday, Wednesday, Friday at 9am in the user's timezone (user can pick daily, weekly, or a custom… |
| Weekly deep dive | `0 10 * * 5` (Friday at 10:00) | Disabled by default. Friday 10am, one competitor in rotation. Re-walks the product on video, re-runs the feature test p… |
| Competitor churn watch | `0 10 * * 1-5` (weekdays at 10:00) | Disabled by default and only useful once a churn source is named. Weekdays at 10am in the user's timezone. Scans the ch… |

Paused jobs are hidden by default: `hermes -p grok-stalk-bot cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-stalk-bot cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **AgentMail** (Grok plugin `48668144`): Preferred. Research inboxes for newsletters, trials, and sales sequences. Create inboxes and read mail via the plugin MCP.
  No known MCP server; search `hermes skills search agentmail` or wire one up under `mcp_servers:`.
- **X** (Grok plugin `49086599`): Needed for the X radar and complaint mining modules. Read-only: posts, mentions, replies for competitor and founder handles.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Fallback only. Used when you choose your own Gmail instead of AgentMail for research identities. Puts newsletters and trials on your address.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Slack** (Grok plugin `674`): Optional. Deliver the pulse to a channel you name instead of this chat.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Salesforce** (Grok plugin `47725205`): Optional, churn module only. Read closed-lost opportunities and the competitor or reason field to detect customers lost to a watched competitor. Read only. A s…
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Optional, churn module only. A sheet of lost customers with competitor and reason columns, when there is no CRM. Read only.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
