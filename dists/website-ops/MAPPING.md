# Website Ops as Hermes profile `grok-website-ops`

Source: https://x.ai/bot/marketplace/bots/website-ops  Creator: Josh Kim (@joshkim)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `website-ops--website-ops-setup`
- `website-ops--connect-accounts`
- `website-ops--site-audit`
- `website-ops--ship-a-change`
- `website-ops--landing-page-from-brief`
- `website-ops--content-update`
- `website-ops--evidence-media`
- `website-ops--html-report`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Weekly site audit | `0 8 * * 1` (Monday at 08:00) | Disabled by default. Monday at 8am in the user's timezone. Re-audits the saved page list for SEO, links, speed, accessi… |

Paused jobs are hidden by default: `hermes -p grok-website-ops cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-website-ops cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **GitHub** (Grok plugin `48677658`): Required. Clones the website repo, opens the branch and the pull request for every change, and reads the pull request checks for a preview URL. Never merges.
  ```yaml
  mcp_servers:
    github:
      url: "https://api.githubcopilot.com/mcp/"
  ```
- **Google Drive** (Grok plugin `45893413`): Optional. Reads landing page briefs and picks up images or exports that belong on a page. A paste or an upload works instead.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
- **Slack** (Grok plugin `674`): Optional. A destination for the weekly audit instead of this chat, when you name a channel. Read only otherwise.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **Figma** (Grok plugin `657`): Optional. Reads the design reference a brief points at so a page matches the intended layout. Read only, and the repo's existing components still win.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
