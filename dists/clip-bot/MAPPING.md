# Clip Bot as Hermes profile `grok-clip-bot`

Source: https://x.ai/bot/marketplace/bots/clip-bot  Creator: This Week in AI (@ThisWeeknAI)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `clip-bot--getting-started`
- `clip-bot--transcribe-a-recording`
- `clip-bot--find-the-clippable-moments`
- `clip-bot--cut-a-clip`
- `clip-bot--clip-pack-from-one-recording`
- `clip-bot--clip-captions-and-post-copy`

## Routines (cron, paused on install)

| Job | Guessed schedule | Original wording |
|---|---|---|
| Clip queue pass | `0 9 * * 1-5` (weekdays at 09:00) | Every weekday morning, transcribes any new recording waiting in the clip queue and comes back with the moments worth cu… |
| Friday clip recap | `0 9 * * 5` (Friday at 09:00) | Every Friday, a short recap of what got clipped this week, which strong moments are still uncut, and the three worth cu… |

Paused jobs are hidden by default: `hermes -p grok-clip-bot cron list --all` shows them. Fix the time with `cron edit <id>` if the guess is wrong, then `hermes -p grok-clip-bot cron resume <id>`.

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **slack** (Grok plugin `674`): Drop the moment list and finished clips in the channel your team picks from.
  ```yaml
  mcp_servers:
    slack:
      command: "npx"
      args: ["-y", "@modelcontextprotocol/server-slack"]
      env: {"SLACK_BOT_TOKEN": "", "SLACK_TEAM_ID": ""}
  ```
- **notion-workspace** (Grok plugin `404`): Keep transcripts, moment lists, and the clip log where your team looks things up.
  ```yaml
  mcp_servers:
    notion-workspace:
      url: "https://mcp.notion.com/mcp"
  ```
- **linear** (Grok plugin `512`): Turn approved moments into clip tasks your team can track to done.
  ```yaml
  mcp_servers:
    linear:
      url: "https://mcp.linear.app/mcp"
  ```
- **figma** (Grok plugin `657`): Pull title cards, end cards, and caption styling so clips match your brand.
  ```yaml
  mcp_servers:
    figma:
      url: "http://127.0.0.1:3845/mcp"
  ```
