# Critiquito: Design Critique as Hermes profile `grok-critiquito`

Source: https://x.ai/bot/marketplace/bots/critiquito  Creator: Manuel Muñoz Solera (@mamuso)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `critiquito--getting-started`
- `critiquito--screen-critique`
- `critiquito--compare-versions`
- `critiquito--flow-critique`
- `critiquito--accessibility-pass`
- `critiquito--ui-copy-pass`
- `critiquito--hand-off-the-fixes`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly open fixes | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Every week, lists the critique findings still open on each screen and offers to re-check the ones with a new version. |

Paused jobs are hidden by default: `hermes -p grok-critiquito cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-critiquito cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **figma** (Grok plugin `657`): Read a frame straight from a file link instead of waiting on a screenshot.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **slack** (Grok plugin `674`): Post a critique you approved into the channel your team reviews in.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the critiques and open fix lists on a page your team can read.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): File the blockers as tickets on the right team, drafted for your yes.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
