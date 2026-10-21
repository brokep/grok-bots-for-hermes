# SEO & AEO Desk as Hermes profile `grok-seo-aeo-desk`

Source: https://x.ai/bot/marketplace/bots/seo-aeo-desk  Creator: Adam Tanguay (@adamta)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `seo-aeo-desk--getting-started`
- `seo-aeo-desk--keyword-and-question-research`
- `seo-aeo-desk--writer-content-brief`
- `seo-aeo-desk--weekly-search-report`
- `seo-aeo-desk--answer-engine-question-map`
- `seo-aeo-desk--page-audit-and-refresh-plan`
- `seo-aeo-desk--extra-recurring-checks`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Content ideas digest | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Once a week, 3 to 5 new page ideas pulled from the keyword source and Search Console, ranked, with the top pick ready t… |
| Weekly search report | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, what moved in Search Console last week, why, and the two to four things worth doing about it. |
| Topic watch | `0 9 * * 1-5` (weekdays at 09:00) | Each weekday morning, speaks up only when a new question or topic worth a page shows up in the user's space. |

Paused jobs are hidden by default: `hermes -p grok-seo-aeo-desk cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-seo-aeo-desk cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **notion-workspace** (Grok plugin `404`): Keep the ideas board, briefs, and question map where your team already writes.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **slack** (Grok plugin `674`): Post the weekly search report and topic watch to a channel you choose.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **linear** (Grok plugin `512`): File each brief as a ticket on your content backlog so writers pick it up in the queue.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **hex** (Grok plugin `651`): Query your warehouse to tie organic pages back to signups and closed deals.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Profound** (Grok plugin `51168001`): Read prompt volumes and AI answer visibility for the topics on your board.
  No known MCP server; search `hermes skills search profound` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
