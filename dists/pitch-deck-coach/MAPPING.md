# Pitch Deck Coach as Hermes profile `grok-pitch-deck-coach`

Source: https://x.ai/bot/marketplace/bots/pitch-deck-coach  Creator: Hiten Shah (@hnshah)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `pitch-deck-coach--pitch-deck-coach`
- `pitch-deck-coach--pdc-methodology`
- `pitch-deck-coach--pdc-modes`
- `pitch-deck-coach--pdc-workspace`
