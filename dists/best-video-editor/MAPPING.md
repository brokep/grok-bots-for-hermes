# Video Edit Desk as Hermes profile `grok-best-video-editor`

Source: https://x.ai/bot/marketplace/bots/best-video-editor  Creator: X Freeze (@xfreeze)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `best-video-editor--getting-started`
- `best-video-editor--footage-intake`
- `best-video-editor--cut-from-your-notes`
- `best-video-editor--captions-and-transcript`
- `best-video-editor--short-clips-from-a-long-video`
- `best-video-editor--platform-versions-and-delivery-check`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly cut queue | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Once a week, finishes the cuts the user parked, attaches them here, and asks the one question each stuck job needs. |

Enable with `hermes -p grok-best-video-editor cron list` then `hermes -p grok-best-video-editor cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Drop a cut you approved in the channel that reviews it.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the shot notes and the cut log where your team looks.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Pick up edit requests filed as issues and put the finished cut back on the issue.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **figma** (Grok plugin `657`): Pull a title card, lower third, or thumbnail frame out of your brand file.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
