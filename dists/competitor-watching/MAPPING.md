# Competitor Watch as Hermes profile `grok-competitor-watching`

Source: https://x.ai/bot/marketplace/bots/competitor-watching  Creator: Shimecki (@scheemunai)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `competitor-watching--getting-started`
- `competitor-watching--build-the-watch-list`
- `competitor-watching--competitor-page-diff`
- `competitor-watching--weekly-competitor-brief`
- `competitor-watching--pricing-and-packaging-comparison`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly competitor brief | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, diffs the pages on the watch list against the last snapshot and delivers a brief of what changed… |
| Daily launch check | `0 9 * * 1-5` (weekdays at 09:00) | Each weekday morning, checks changelog, release note, and blog pages across the watch list and speaks up only when a co… |

Enable with `hermes -p grok-competitor-watching cron list` then `hermes -p grok-competitor-watching cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post the weekly brief to a channel you choose.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the watch list and every brief where your team reads.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Turn a competitor move into an issue in your product backlog.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
