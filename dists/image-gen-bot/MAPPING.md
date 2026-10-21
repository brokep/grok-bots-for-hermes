# Stills & Clips Desk as Hermes profile `grok-image-gen-bot`

Source: https://x.ai/bot/marketplace/bots/image-gen-bot  Creator: Matt Palmer (@mattyp)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `image-gen-bot--getting-started`
- `image-gen-bot--look-and-size-sheet`
- `image-gen-bot--pull-a-still-from-footage`
- `image-gen-bot--pull-a-short-clip`
- `image-gen-bot--screenshot-cleanup-for-docs`
- `image-gen-bot--export-sizes-captions-and-alt-text`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly pull queue | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Every week, works through the stills and clips waiting in the pull queue and posts each finished file here for review. |

Enable with `hermes -p grok-image-gen-bot cron list` then `hermes -p grok-image-gen-bot cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Drop a pulled still or clip in the channel where your team gives feedback.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the size sheet and the cleaned-up docs screenshots where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **figma** (Grok plugin `657`): Read the real logo file, hex codes, and font for anything that gets an overlay.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **linear** (Grok plugin `512`): Pick up asset requests filed as issues and feed them into the weekly pull queue.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
