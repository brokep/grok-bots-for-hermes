# Import Bot as Hermes profile `grok-import-bot`

Source: https://x.ai/bot/marketplace/bots/import-bot  Creator: Shub Gaur (@shubgaur)

| Grok Bot | Hermes | Where |
|---|---|---|
| profile + memories + notes | SOUL.md (loaded every message) | `SOUL.md` |
| skills | agentskills.io SKILL.md folders, auto-indexed | `skills/<name>/SKILL.md` |
| routines | cron jobs that load a routine skill; installed paused | `cron/jobs.json` |
| plugins | MCP servers in config.yaml `mcp_servers` (hints below) | add by hand |
| per-user memory | Hermes memory tool (MEMORY.md / USER.md) | automatic |

## Skills

- `import-bot--import-bot-setup`
- `import-bot--collect-local`
- `import-bot--collect-accounts`
- `import-bot--parse-import`
- `import-bot--transcript-toolkit`
- `import-bot--cleanup-fix`
- `import-bot--write-user-memory`
- `import-bot--plan-experts`
- `import-bot--project-folders`
- `import-bot--bot-design-standard`
- `import-bot--expert-packet`
- `import-bot--spawn-experts`
- `import-bot--routines-roster`
- `import-bot--connectors-encourage`
- `import-bot--import-receipt`
- `import-bot--resync`
- `import-bot--adjust-experts`
- `import-bot--interview-fallback`
- `import-bot--fallback-collect-script`
- `import-bot--import-scripts`
