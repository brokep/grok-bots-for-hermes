# Sales Call Coach as Hermes profile `grok-sales-call-coach`

Source: https://x.ai/bot/marketplace/bots/sales-call-coach  Creator: Daniel Brill (@danielbrill_)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `sales-call-coach--getting-started`
- `sales-call-coach--call-scorecard`
- `sales-call-coach--objection-replay`
- `sales-call-coach--next-step-repair`
- `sales-call-coach--coaching-trends`
- `sales-call-coach--pre-call-plan`
- `sales-call-coach--discovery-question-bank`
- `sales-call-coach--filler-and-pacing-check`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly coaching recap | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Once a week, reads the calls you logged and sends the counts that moved, the two weakest dimensions with quotes, and th… |
| Objection drill | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | On the mornings you pick, runs one short live drill on the objection that keeps costing you, using wording from your ow… |

Paused jobs are hidden by default: `hermes -p grok-sales-call-coach cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-sales-call-coach cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **notion-workspace** (Grok plugin `404`): Keep your coaching log, scorecards, and pre-call plans where you already work.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **slack** (Grok plugin `674`): Send a scorecard or a follow-up draft to yourself or your manager, only when you say so.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **linear** (Grok plugin `512`): File the product gaps buyers name on your calls as issues, only when you say so.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **Gong** (Grok plugin `47725204`): Pull your call recordings and transcripts straight from Gong instead of pasting them.
  No known MCP server; search `hermes skills search gong` or wire one up under `mcp_servers:`.
- **Google Calendar** (Grok plugin `45893411`): See the calls coming up so a pre-call plan is ready before you dial in.
  No known MCP server; search `hermes skills search google-calendar` or wire one up under `mcp_servers:`.
