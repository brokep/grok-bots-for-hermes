# Outbound Prospecting as Hermes profile `grok-pg`

Source: https://x.ai/bot/marketplace/bots/pg  Creator: Krista Letz (@kristaletz)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `pg--getting-started`
- `pg--build-the-target-list`
- `pg--research-a-prospect`
- `pg--draft-a-first-touch`
- `pg--draft-a-follow-up`
- `pg--handle-a-reply`
- `pg--weekly-prospecting-recap`
- `pg--sharpen-what-is-working`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekday draft batch | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, researches the next few names on the target list and leaves a first-touch draft for each one, wa… |
| Friday prospecting recap | `0 9 * * 5` (Friday at 09:00) | Every Friday, what went out this week, what came back, which rows are waiting on you, and where the list is running thi… |
| Monday list top-up | `0 9 * * 1` (Monday at 09:00) | Every Monday, adds new companies and named people that match your ideal customer so the list never runs dry. |

Paused jobs are hidden by default: `hermes -p grok-pg cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-pg cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Post the day's drafts or the Friday recap to a channel your team reads.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep the target list and every draft where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Turn a reply or a booked meeting into a task somebody owns.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **Gmail** (Grok plugin `45893410`): Every draft sits unsent in your own account until you send it.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Google Sheets** (Grok plugin `47662908`): Keep the target list somewhere you can edit directly.
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **X** (Grok plugin `49086599`): Read a prospect's recent posts for a real, dated hook when X is your channel.
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
- **Salesforce** (Grok plugin `47725205`): Read who you already know so the list drops open deals and customers.
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
