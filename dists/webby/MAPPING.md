# Webby as Hermes profile `grok-webby`

Source: https://x.ai/bot/marketplace/bots/webby  Creator: Farzad (@farzyness)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `webby--strip-ai-isms`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily Exclusive long-form check | `0 9 * * *` (daily at 09:00) | Daily scan for new public long-form videos, write an Exclusive, fact-check, ship the site, and email the same day. |
| Daily Digest social pulse | `0 9 * * *` (daily at 09:00) | Email yesterday's digest first, then write today's social-pulse digest. Never email today's digest on the same run. |
| Site PR follow-up | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | On personal-site PR open, push, or merge: fix owned content issues; production-deploy after merge to main. |
| Weekday hourly dashboard book | `0 9 * * 1-5` (weekdays at 09:00) | Weekday intra-day public dashboard refresh at :35 (catch at :40). Backup only; fill ships are primary. |
| Weekday close dashboard book | `0 9 * * 1-5` (weekdays at 09:00) | Official cash-close public dashboard ship at 3:15 local, with a 3:20 catch. |
| Post-fill dashboard ship | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Ship the public dashboard immediately after a desk fill or close. Morning sweep is a safety net only. |

Paused jobs are hidden by default: `hermes -p grok-webby cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-webby cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **X** (Grok plugin `49086599`): Search posts, read timelines, pull trends, and manage bookmarks.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
