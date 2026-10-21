# Startup QA Bot as Hermes profile `grok-startup-qa-bot`

Source: https://x.ai/bot/marketplace/bots/startup-qa-bot  Creator: Shub Gaur (@shubgaur)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `startup-qa-bot--qa-setup`
- `startup-qa-bot--test-account`
- `startup-qa-bot--product-walk`
- `startup-qa-bot--product-rundown`
- `startup-qa-bot--qa-scripts`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Morning product walk | `0 9 * * 1-5` (weekdays at 09:00) | Disabled by default. Weekday mornings, ready by 9: walks your product in its test account and sends what shipped, what… |

Paused jobs are hidden by default: `hermes -p grok-startup-qa-bot cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-startup-qa-bot cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **AgentMail** (Grok plugin `48668144`): Recommended. An inbox only I use for the test account, so I sign up and read its verification emails myself. I only create that inbox and read it, never send.…
  No known MCP server; search `hermes skills search agentmail` or wire one up under `mcp_servers:`.
- **GitHub** (Grok plugin `48677658`): Optional. Merged pull requests tell me what should be live before I walk. Read-only. Without it, I use your changelog page or just walk.
  ```yaml
  mcp_servers:
    github:
      url: "https://api.githubcopilot.com/mcp/"
  ```
- **Linear** (Grok plugin `512`): Optional. Issues moved to done tell me what should have shipped. Read-only, and I never file or change issues.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
