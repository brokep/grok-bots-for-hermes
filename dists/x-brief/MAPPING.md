# X Brief as Hermes profile `grok-x-brief`

Source: https://x.ai/bot/marketplace/bots/x-brief  Creator: Dan McAteer (@daniel_mac8)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `x-brief--getting-started`
- `x-brief--build-the-x-watch-list`
- `x-brief--daily-x-brief`
- `x-brief--weekly-x-recap`
- `x-brief--read-a-thread-or-post`
- `x-brief--draft-a-post-or-reply`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily X brief | `0 9 * * *` (daily at 09:00) | Once a day at the hour you pick, reads your watch list and sends the day's items grouped by theme with a link on every… |
| Weekly X recap | `0 9 * * 0,6` (weekends at 09:00) | Every Friday, pulls the week's briefs into the themes that held, the voices worth adding, the accounts that went quiet,… |

Enable with `hermes -p grok-x-brief cron list` then `hermes -p grok-x-brief cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **X** (Grok plugin `49086599`): Read your timeline, lists, and the accounts you follow, and open posts reliably.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
- **slack** (Grok plugin `674`): Post the daily brief to a channel you and your team already read.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the watch list and every brief where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Turn anything in the brief you want to act on into a task with the link on it.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
