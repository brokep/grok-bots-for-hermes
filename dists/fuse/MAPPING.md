# Ad Spend Watch as Hermes profile `grok-fuse`

Source: https://x.ai/bot/marketplace/bots/fuse  Creator: Miguel Cruz (@cruzmiguel000)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `fuse--getting-started`
- `fuse--set-accounts-and-thresholds`
- `fuse--read-an-ad-platform-export`
- `fuse--pull-numbers-from-a-connected-source`
- `fuse--run-the-spend-and-performance-check`
- `fuse--diagnose-what-broke`
- `fuse--check-budget-pace`
- `fuse--write-the-fix-list`
- `fuse--answer-a-spend-question`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily spend and performance check | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, checks the newest ad numbers against your thresholds and flags what broke, with the one change t… |
| Midday burn check | `0 12 * * 1-5` (weekdays at 12:00) | Every weekday around midday, catches a spend spike the same day it happens, but only when a live source is connected. |
| Weekly budget pace check | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, where month-to-date ad spend lands against your plan and which accounts are going to overshoot. |

Paused jobs are hidden by default: `hermes -p grok-fuse cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-fuse cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post an alert or a fix list in the channel your team actually watches.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the threshold set, the checks, and the alert log where your team can find them.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): File the fix when a breach belongs to engineering, like a dead pixel or a broken checkout.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **hex** (Grok plugin `651`): Read spend straight from your warehouse when the numbers already live in a query.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **datadog** (Grok plugin `1411`): Check whether the site or checkout was down or slow when conversions dropped.
  No known MCP server; search `hermes skills search datadog` or wire one up under `mcp_servers:`.
- **sentry** (Grok plugin `579`): Check whether checkout errors spiked at the hour your conversions stopped.
  ```yaml
  mcp_servers:
    sentry:
      url: "https://mcp.sentry.dev/mcp"
  ```
- **figma** (Grok plugin `657`): Pull up the creative behind a campaign whose click-through rate is sliding.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Read the daily report the ad platform emails you.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `47662908`): Read a spend sheet you already keep.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
