# tinkabot as Hermes profile `grok-tinkabot`

Source: https://x.ai/bot/marketplace/bots/tinkabot  Creator: Lauren Tan (@poteto)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `tinkabot--wrap-api-as-plugin`
- `tinkabot--prove-plugin-local`
- `tinkabot--publish-cursor-plugin`

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **pstack** (Grok plugin `9717366`): if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence.
  No known MCP server; search `hermes skills search pstack` or wire one up under `mcp_servers:`.
