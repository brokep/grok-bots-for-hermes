# Cooper as Hermes profile `grok-cooper`

Source: https://x.ai/bot/marketplace/bots/cooper  Creator: Tommy Hansen (@TommyHansenTA)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily AI/tech/VC briefing | `0 8 * * *` (daily at 08:00) | Every day at 8:00 AM — tight Slack DM briefing of top AI/tech/VC stories. |
| Midday competitor alert | `0 13 * * 1-5` (weekdays at 13:00) | Weekdays at 1:00 PM — Slack DM only if a top competitor/hire/priority-company story clears the bar; otherwise stay sile… |
| Afternoon competitor alert | `0 16 * * 1-5` (weekdays at 16:00) | Weekdays at 4:00 PM — Slack DM only if a top competitor/hire/priority-company story clears the bar; otherwise stay sile… |

Paused jobs are hidden by default: `hermes -p grok-cooper cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-cooper cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Slack** (Grok plugin `674`): Slack MCP server. Search channels, send messages, and perform other Slack actions through MCP-compatible clients.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
