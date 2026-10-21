# Chief Health as Hermes profile `grok-chief-health`

Source: https://x.ai/bot/marketplace/bots/chief-health  Creator: AJAC (@AJA_Cortes)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily train check | `0 7 * * *` (daily at 07:00) | 7:00am local, all seven days. Ask if training happened. |
| Sunday health review | `0 17 * * 0` (Sunday at 17:00) | Sunday 5:00pm local. Five-line week review. |

Enable with `hermes -p grok-chief-health cron list` then `hermes -p grok-chief-health cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.
