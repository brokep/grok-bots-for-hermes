# Game Art Director as Hermes profile `grok-sable-game-art`

Source: https://x.ai/bot/marketplace/bots/sable-game-art  Creator: Danny Limanseta (@DannyLimanseta)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `sable-game-art--getting-started`
- `sable-game-art--style-guide`
- `sable-game-art--prompt-sheets`
- `sable-game-art--sprite-and-tile-specs`
- `sable-game-art--asset-consistency-check`
- `sable-game-art--sprite-sheet-toolkit`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly art review | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Once a week, checks new art against the style guide and the spec, reports what drifted with the numbers behind it, and… |
| Weekly reference sweep | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Once a week, sends four to six fresh art references in the user's genre and style, each with a source link and what is… |

Paused jobs are hidden by default: `hermes -p grok-sable-game-art cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-sable-game-art cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **figma** (Grok plugin `657`): Read your mood board and mockups, and keep the style guide where your artists already work.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **notion-workspace** (Grok plugin `404`): Keep the style guide, the spec, and the shot list where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **slack** (Grok plugin `674`): Post the weekly art review to the channel your team already reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **linear** (Grok plugin `512`): Turn the shot list into issues so the art backlog sits with the rest of the work.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
