# Copy Humanizer as Hermes profile `grok-human-copywriter`

Source: https://x.ai/bot/marketplace/bots/human-copywriter  Creator: Massimo De Luisa (@massimodeluisa)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `human-copywriter--getting-started`
- `human-copywriter--build-the-voice-profile`
- `human-copywriter--edit-a-draft`
- `human-copywriter--rewrite-a-draft`
- `human-copywriter--anti-slop-pass`
- `human-copywriter--draft-for-a-channel`
- `human-copywriter--learn-from-what-shipped`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly shipped check | `0 12 * * 5` (Friday at 12:00) | Every Friday afternoon, asks what copy actually went out this week and folds the edits the user made into their voice p… |

Enable with `hermes -p grok-human-copywriter cron list` then `hermes -p grok-human-copywriter cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **notion-workspace** (Grok plugin `404`): Keep the voice profile and every draft where your team already writes.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **slack** (Grok plugin `674`): Drop a draft in the channel where people give you feedback.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **figma** (Grok plugin `657`): Read the copy sitting in a design frame and hand back rewritten lines.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **linear** (Grok plugin `512`): Turn shipped issues into release notes a customer can read.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
