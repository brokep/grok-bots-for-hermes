# Product Marketer as Hermes profile `grok-product-marketer`

Source: https://x.ai/bot/marketplace/bots/product-marketer  Creator: Josh Kim (@joshkim)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `product-marketer--product-marketer-setup`
- `product-marketer--learn-the-product`
- `product-marketer--principles`
- `product-marketer--sharpen-positioning`
- `product-marketer--draft-copy`
- `product-marketer--copy-review`
- `product-marketer--anti-slop`
- `product-marketer--learn-from-shipped`
- `product-marketer--brief-out`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Principles review | `0 9 * * 1` (Monday at 09:00) | Disabled by default. Mondays at 9am in the user's timezone. Re-reads the positioning principles doc and the voice profi… |

Paused jobs are hidden by default: `hermes -p grok-product-marketer cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-product-marketer cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Google Drive** (Grok plugin `45893413`): Optional. Reads the brand, positioning, and messaging docs you already have, and holds the principles doc, the voice profile, every draft, and every brief as M…
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Google Sheets** (Grok plugin `47662908`): Optional. Where the ads copy set lives as a live sheet with the Overview, RSA long format, Keywords, and Callouts tabs. Without it the same tables ship as CSV…
  No known MCP server; search `hermes skills search google-sheets` or wire one up under `mcp_servers:`.
- **Notion** (Grok plugin `404`): Optional. Reads the brand, product, and positioning pages you point me at, and can hold the principles doc and drafts instead of Drive.
  ```yaml
  mcp_servers:
    notion:
      url: "https://mcp.notion.com/mcp"
  ```
- **X** (Grok plugin `49086599`): Optional and read only. Reads how you and your competitors position the category in public, for the claim map in sharpen-positioning. Never follows, likes, rep…
  No known MCP server; search `hermes skills search x` or wire one up under `mcp_servers:`.
