# Customer Proof Desk as Hermes profile `grok-customer-stories`

Source: https://x.ai/bot/marketplace/bots/customer-stories  Creator: Anoop Baliga (@akbaliga96)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `customer-stories--getting-started`
- `customer-stories--add-sources-to-the-proof-bank`
- `customer-stories--mine-a-batch-of-calls`
- `customer-stories--write-a-case-study`
- `customer-stories--pull-proof-for-a-claim`
- `customer-stories--testimonials-and-pull-quotes`
- `customer-stories--build-a-deal-proof-one-pager`
- `customer-stories--get-the-customer-s-approval`
- `customer-stories--check-a-draft-against-the-bank`
- `customer-stories--lay-out-the-case-study`
- `customer-stories--run-the-case-study-pipeline`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly proof roundup | `0 9 * * 1` (Monday at 09:00) | Every Monday morning, what new proof came in, which customers are ready for a case study, which approvals are still sit… |
| Monthly proof refresh | `0 9 1 * *` (1st of the month at 09:00) | Once a month, the quotes and numbers that have aged out, the customers worth a fresh call, and the claims with the thin… |

Enable with `hermes -p grok-customer-stories cron list` then `hermes -p grok-customer-stories cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **notion-workspace** (Grok plugin `404`): Keep the proof bank, the case studies, and the drafts where your team already looks.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **slack** (Grok plugin `674`): Watch the channel where customer wins get posted, and drop the Monday roundup there.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **linear** (Grok plugin `512`): Track ready-to-write customers and pending approvals as tasks your team can see.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **figma** (Grok plugin `657`): Lay a finished case study into a page design instead of handing over raw text.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
- **hex** (Grok plugin `651`): Check a customer's numbers against your own data before you publish them.
  No known MCP server; search `hermes skills search hex` or wire one up under `mcp_servers:`.
- **Gmail** (Grok plugin `45893410`): Search, read, draft, and manage email.
  ```yaml
  mcp_servers:
    gmail:
      command: "npx"
      args: ["-y", "@gongrzhe/server-gmail-autoauth-mcp"]
  ```
- **Granola** (Grok plugin `5609`): Pull customer call notes straight from your meetings.
  No known MCP server; search `hermes skills search granola` or wire one up under `mcp_servers:`.
