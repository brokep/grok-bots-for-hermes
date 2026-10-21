---
name: follow-through-agent--routine-commitment-strand-audit
description: "Routine: Disabled by default. Reconcile approved sources and privately surface evidence-backed commitments or facts stranded without a completed destination."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["follow-through-agent", "grok-bot", "routine"]
    related_skills: ["follow-through-agent--open-loop-audit", "follow-through-agent--agent-orchestration", "follow-through-agent--humanizer", "follow-through-agent--conversation-to-action", "follow-through-agent--follow-through-drafts"]
---
# Routine: Commitment-strand audit

Original schedule: Disabled by default. Reconcile approved sources and privately surface evidence-backed commitments or facts stranded without a completed destination.

# Commitment-strand audit

This routine ships disabled. Confirm timezone, cadence, source scope, private destination, empty-result behavior, and approval boundary before enabling.

When enabled, reconcile only new or changed artifacts across approved systems. Surface commitments or customer facts only when evidence shows the required destination or action is still missing. Deduplicate repeats, preserve source evidence, and produce closure drafts only. Stay silent when empty unless the installer chose an empty notice. Never create a general day agenda, pipeline digest, external send, or silent write.
