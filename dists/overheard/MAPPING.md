# Overheard as Hermes profile `grok-overheard`

Source: https://x.ai/bot/marketplace/bots/overheard  Creator: Lenny Rachitsky (@lennysan)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `overheard--overheard-setup`
- `overheard--overheard`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily mention monitor | `0 9 * * 1-5` (weekdays at 09:00) | Paused weekday-morning mention sweep. Created after the watch-list interview. Enable only when the user says so. Digest… |

Enable with `hermes -p grok-overheard cron list` then `hermes -p grok-overheard cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **X** (Grok plugin `49086599`): Search posts and read accounts on X. Optional, improves X coverage over web search.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Optional. Deliver the weekday digest to a Slack channel you approve.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
