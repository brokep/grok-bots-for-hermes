# figma bro as Hermes profile `grok-figma-bro`

Source: https://x.ai/bot/marketplace/bots/figma-bro  Creator: John Bai (@johnbai)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `figma-bro--getting-started`
- `figma-bro--frame-to-build-spec`
- `figma-bro--build-a-screen-from-a-brief`
- `figma-bro--component-library-audit`
- `figma-bro--design-token-audit`
- `figma-bro--motion-and-prototype-notes`
- `figma-bro--design-to-code-handoff-notes`
- `figma-bro--file-structure-cleanup-plan`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly library check | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, checks the component library and token set for new duplicates, detached instances, and hardcoded… |
| Ready for dev sweep | `0 12 * * 5` (Friday at 12:00) | Every Friday afternoon, lists the frames marked ready for dev that still have no spec, and offers to write the next one. |

Enable with `hermes -p grok-figma-bro cron list` then `hermes -p grok-figma-bro cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **figma** (Grok plugin `657`): Read your file directly: the layer tree, the components, the variables, the prototype, and the exact values.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **notion-workspace** (Grok plugin `404`): Park specs and audits where your team already looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Turn handoff open questions and audit fixes into issues you approve first.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **slack** (Grok plugin `674`): Drop a spec or a handoff note into the channel your engineers already read.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
