# dr eggbot as Hermes profile `grok-dr-eggbot-v2`

Source: https://x.ai/bot/marketplace/bots/dr-eggbot-v2  Creator: Lauren Tan (@poteto)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `dr-eggbot-v2--design-a-grok-bot`
- `dr-eggbot-v2--make-bot-ui`
- `dr-eggbot-v2--routine-healthcheck`
- `dr-eggbot-v2--transcript-healthcheck`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| transcript-healthcheck | `0 9 * * 1-5` (weekdays at 09:00) | Cron 44 8 * * 1-5 (weekdays 8:44 local). Scans recent bot transcripts for user friction; proposes skills/bots/routines;… |
| routine-healthcheck | `0 9 * * 1` (Monday at 09:00) | Cron 49 8 * * 1 (Mondays 8:49 local). Audits fleet routines for token waste; reports fixes; stays quiet when nothing is… |

Paused jobs are hidden by default: `hermes -p grok-dr-eggbot-v2 cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-dr-eggbot-v2 cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **pstack** (Grok plugin `9717366`): if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence.
  No known MCP server; search `hermes skills search pstack` or wire one up under `mcp_servers:`.
