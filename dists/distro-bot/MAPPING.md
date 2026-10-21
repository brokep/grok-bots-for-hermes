# Distro Bot as Hermes profile `grok-distro-bot`

Source: https://x.ai/bot/marketplace/bots/distro-bot  Creator: Shub Gaur (@shubgaur)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `distro-bot--distro-setup`
- `distro-bot--ad-accounts`
- `distro-bot--campaign-loop`
- `distro-bot--ad-creative`
- `distro-bot--market-scan`
- `distro-bot--outbound-desk`
- `distro-bot--distro-scripts`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Campaign check | `25 8 * * *` (daily at 08:25) | Disabled by default. Daily 8:25am: numbers, pacing, flags, and one loop step per campaign. |
| Trend scan | `35 9 * * 1-5` (weekdays at 09:35) | Disabled by default. Weekdays 9:35am: topics worth jumping on, each with a draft post. |
| Outbound replies | `15 11 * * 1-5` (weekdays at 11:15) | Disabled by default. Weekdays 11:15am and 4:15pm: replies handed to sales, follow-ups drafted. |
| Weekly distro review | `45 8 * * 1` (Monday at 08:45) | Disabled by default. Mondays 8:45am: every channel's numbers, competitor moves, and this week's tests. |

Paused jobs are hidden by default: `hermes -p grok-distro-bot cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-distro-bot cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **X** (Grok plugin `49086599`): Recommended. Trends, news, and posts for topic scans, plus your own posts' numbers to learn from. Read only, and reads bill your X API credits.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Optional. Outbound drafts in your inbox, replies from leads, and past emails to learn from. Sends only a batch you approve.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
