# EBR & Value Deck Builder as Hermes profile `grok-ebr-value-deck-builder`

Source: https://x.ai/bot/marketplace/bots/ebr-value-deck-builder  Creator: Krista Letz (@kristaletz)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `ebr-value-deck-builder--getting-started`
- `ebr-value-deck-builder--brand-kit`
- `ebr-value-deck-builder--ebr-deck`
- `ebr-value-deck-builder--pptx-compat`
- `ebr-value-deck-builder--three-whys`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Renewal deck reminder | `0 9 1 1,4,7,10 *` (first day of each quarter at 09:00) | On the 1st of each month, list the owner's accounts with a renewal inside 120 days that have no review deck this quarte… |

Enable with `hermes -p grok-ebr-value-deck-builder cron list` then `hermes -p grok-ebr-value-deck-builder cron resume <id>`; fix the time first with `cron edit` if the guess is wrong.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Salesforce** (Grok plugin `47725205`): Account, contract, contacts, and history the deck is built from. Connect the one CRM you use.
  No known MCP server; search `hermes skills search salesforce` or wire one up under `mcp_servers:`.
- **HubSpot** (Grok plugin `49339689`): CRM alternative to Salesforce.
  ```yaml
  mcp_servers:
    hubspot:
      url: "https://mcp.hubspot.com"
  ```
- **Attio** (Grok plugin `62459236`): CRM alternative to Salesforce.
  No known MCP server; search `hermes skills search attio` or wire one up under `mcp_servers:`.
- **Gong** (Grok plugin `47725204`): What the customer said they wanted, in their words, for the goals and outcomes slides.
  No known MCP server; search `hermes skills search gong` or wire one up under `mcp_servers:`.
- **Mixpanel** (Grok plugin `11976`): Adoption and usage trends for the account's domain.
  No known MCP server; search `hermes skills search mixpanel` or wire one up under `mcp_servers:`.
- **Google Drive** (Grok plugin `45893413`): Upload the finished deck next to the account's other files.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **OneDrive** (Grok plugin `57302028`): Upload destination for Microsoft 365 users.
  No known MCP server; search `hermes skills search onedrive` or wire one up under `mcp_servers:`.
