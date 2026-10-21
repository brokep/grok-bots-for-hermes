# Video Editor as Hermes profile `grok-video-editor`

Source: https://x.ai/bot/marketplace/bots/video-editor  Creator: Ethan Ng (@Ethan_Ng_13)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `video-editor--video-editor-getting-started`
- `video-editor--edit-plan`
- `video-editor--cut-and-render`
- `video-editor--delivery-check`
- `video-editor--video-tools`

## Integrations

Grok plugins have no direct Hermes equivalent. Add an MCP server to `config.yaml` under `mcp_servers:` (same shape as a Claude Code `mcpServers` entry), then restart the profile.

- **Remotion** (Grok plugin `49339676`): Optional. Remotion's own skills for animations, captions, and rendering, used for the graphics in each edit.
  No known MCP server; search `hermes skills search remotion` or wire one up under `mcp_servers:`.
- **Google Drive** (Grok plugin `45893413`): Optional. Pull raw footage from Drive and share preview links of finished cuts.
  No known MCP server; search `hermes skills search google-drive` or wire one up under `mcp_servers:`.
