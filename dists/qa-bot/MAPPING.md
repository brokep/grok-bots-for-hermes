# QA bot as Hermes profile `grok-qa-bot`

Source: https://x.ai/bot/marketplace/bots/qa-bot  Creator: Ulysses Ng

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `qa-bot--getting-started-ac-fail-gate-qa`
- `qa-bot--enterprise-ac-fail-gate`
- `qa-bot--adhd-friendly-agent-responses`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Post-merge AC fail-gate | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | When a PR merges in the watched product repo, verify Production SHA and re-run the BLOCK AC pack; stay quiet on unchang… |

Enable with `hermes -p grok-qa-bot cron list` then `hermes -p grok-qa-bot cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Vercel** (Grok plugin `649`): Build and deploy web apps and agents
  No known MCP server; search `hermes skills search vercel` or wire one up under `mcp_servers:`.
