# AI Search Visibility as Hermes profile `grok-ai-search-visibility`

Source: https://x.ai/bot/marketplace/bots/ai-search-visibility  Creator: Adam Tanguay (@adamta)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `ai-search-visibility--getting-started`
- `ai-search-visibility--build-the-prompt-list`
- `ai-search-visibility--run-a-visibility-check`
- `ai-search-visibility--capture-a-pasted-answer`
- `ai-search-visibility--weekly-visibility-brief`
- `ai-search-visibility--citation-source-audit`
- `ai-search-visibility--share-of-answer-comparison`
- `ai-search-visibility--draft-the-fix`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly visibility brief | `0 9 * * 1` (Mondays at 09:00 (weekly default)) | Every week, runs the whole prompt list, then reports which answers moved, who is winning, and the one thing to do about… |
| Top prompt spot check | `0 9 * * 1,4` (Mondays and Thursdays at 09:00) | Twice a week, re-runs the top five prompts and speaks up only when the user drops out of an answer or a new name shows… |

Paused jobs are hidden by default: `hermes -p grok-ai-search-visibility cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-ai-search-visibility cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post the weekly brief in a channel your team already reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the prompt list, the briefs, and the fix list where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Turn the fix list into tracked issues for whoever owns those pages.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **hex** (Grok plugin `651`): Chart the share of answer scoreboard over time if your team already uses Hex.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Profound** (Grok plugin `51168001`): Read AI answer visibility and citations across engines to widen the capture.
  No known MCP server; search `hermes skills search profound` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
