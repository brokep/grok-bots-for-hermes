# Proto Bot as Hermes profile `grok-proto-bot`

Source: https://x.ai/bot/marketplace/bots/proto-bot  Creator: Shub Gaur (@shubgaur)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `proto-bot--proto-setup`
- `proto-bot--proto-connect`
- `proto-bot--proto-codebase`
- `proto-bot--proto-build`
- `proto-bot--proto-figma`
- `proto-bot--proto-media`
- `proto-bot--proto-research`
- `proto-bot--proto-share`
- `proto-bot--proto-scripts`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Prototype rundown | `0 9 * * 1-5` (weekdays at 09:00) | Disabled by default. Weekday mornings at 9: packets for builds that finished, results of media jobs, and briefs for que… |
| Craft scan | `0 9 * * 1` (Monday at 09:00) | Disabled by default. Mondays at 10: new models, techniques, and guides for the crafts you name, with links. |

Enable with `hermes -p grok-proto-bot cron list` then `hermes -p grok-proto-bot cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Figma** (Grok plugin `657`): Optional. Reads your files for references and design reviews, and draws mocks, screens, and decks when a cloud agent can't.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **Slack** (Grok plugin `674`): Optional. Reads a thread you point at so a prototype starts from the real discussion. Posts only a draft you approve.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **X** (Grok plugin `49086599`): Optional. Searches posts and threads for craft research. Web search works without it.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
