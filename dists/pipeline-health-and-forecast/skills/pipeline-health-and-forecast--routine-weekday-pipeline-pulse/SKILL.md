---
name: pipeline-health-and-forecast--routine-weekday-pipeline-pulse
description: "Routine: Disabled by default. Scan an approved opportunity view for new signals, stale next steps, and forecast risk."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["pipeline-health-and-forecast", "grok-bot", "routine"]
    related_skills: ["pipeline-health-and-forecast--pipeline-pulse", "pipeline-health-and-forecast--agent-orchestration", "pipeline-health-and-forecast--humanizer"]
---
# Routine: Weekday pipeline pulse

Original schedule: Disabled by default. Scan an approved opportunity view for new signals, stale next steps, and forecast risk.

# Weekday pipeline pulse

This routine ships disabled. Confirm timezone, cadence, source scope, private destination, empty-result behavior, and approval boundary before enabling.

When enabled: Scan an approved opportunity view for new signals, stale next steps, and forecast risk. Deduplicate prior results, preserve source evidence, label partial coverage, and produce drafts only. Never send externally or silently write.
