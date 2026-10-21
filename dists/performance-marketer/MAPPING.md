# Performance Marketer as Hermes profile `grok-performance-marketer`

Source: https://x.ai/bot/marketplace/bots/performance-marketer  Creator: Josh Kim (@joshkim)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `performance-marketer--performance-marketer-setup`
- `performance-marketer--connect-accounts`
- `performance-marketer--review-sheet`
- `performance-marketer--build-shells`
- `performance-marketer--messaging-test-design`
- `performance-marketer--launch-gate`
- `performance-marketer--traffic-watch`
- `performance-marketer--evidence-media`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Traffic watch | `0 9 * * *` (daily at 09:00) | Disabled by default. Daily at 9am in the user's timezone. Reads every enabled campaign in the signed-in platform agains… |

Paused jobs are hidden by default: `hermes -p grok-performance-marketer cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-performance-marketer cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Google Sheets** (Grok plugin `47662908`): Recommended. The review sheet lives here so you can edit it, set Keep, Edit, or Cut per row, and approve it. Without it the same sheet is written as Markdown i…
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Google Drive** (Grok plugin `45893413`): Optional. Reads the ad copy and positioning documents a teammate or you put in Drive. A paste in chat works just as well.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Optional. Deliver the traffic read to a channel you name instead of this chat. Read and post only to what you name, and nothing is enabled from there.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
