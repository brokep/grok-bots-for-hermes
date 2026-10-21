# Talent Discovery as Hermes profile `grok-sherlock`

Source: https://x.ai/bot/marketplace/bots/sherlock  Creator: Tommy Hansen (@TommyHansenTA)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `sherlock--getting-started`
- `sherlock--read-the-role`
- `sherlock--source-a-batch`
- `sherlock--lookalike-search`
- `sherlock--dedupe-against-your-pipeline`
- `sherlock--draft-outreach`
- `sherlock--shortlist-review`
- `sherlock--role-market-read`
- `sherlock--share-the-shortlist`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Daily candidate batch | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, sources a small batch of new candidates for the open role, deduped against your pipeline, with e… |
| Weekly sourcing recap | `0 9 * * 5` (Friday at 09:00) | Every Friday, a recap of who was added, what you kept and passed on, who has not replied yet, and whether the bar needs… |

Paused jobs are hidden by default: `hermes -p grok-sherlock cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-sherlock cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post new candidates to the hiring channel your team already reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the role scorecard and the shortlist where your hiring team already looks.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Track the search, or each candidate, as issues if your team runs hiring in Linear.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **figma** (Grok plugin `657`): Read a designer's shared case study or portfolio file when you are hiring design.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `47662908`): Read and write Google Sheets.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Ashby** (Grok plugin `49104326`): Search candidates, prep interviews, and manage pipeline tasks.
  No known MCP server; search `hermes skills search ashby` or wire one up under `mcp_servers:`.
