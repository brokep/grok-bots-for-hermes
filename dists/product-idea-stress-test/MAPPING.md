# Product Idea Stress Test as Hermes profile `grok-product-idea-stress-test`

Source: https://x.ai/bot/marketplace/bots/product-idea-stress-test  Creator: Hiten Shah (@hnshah)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `product-idea-stress-test--pist-evidence-investigator`
- `product-idea-stress-test--pist-experiment-designer`
- `product-idea-stress-test--pist-method-codifier`
