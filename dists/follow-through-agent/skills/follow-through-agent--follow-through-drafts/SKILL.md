---
name: follow-through-agent--follow-through-drafts
description: "Draft the reply, task, CRM update, or workspace note required to close an evidenced loop."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["follow-through-agent", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["follow-through-agent--open-loop-audit", "follow-through-agent--agent-orchestration", "follow-through-agent--humanizer", "follow-through-agent--conversation-to-action"]
---
# follow-through-drafts

# Follow-Through Drafts

From an approved loop, draft the required customer/internal reply, CRM next step or note, owned task, calendar follow-up hold, or workspace status. Preserve names, dates, numbers, commitments, and uncertainty. Never send or write automatically. Mark a loop Closed only after evidence confirms the action occurred.

## Delegation contract

Any delegated portion of this skill follows `agent-orchestration`. Workers inherit only the selected connector visibility and scoped read access. They may return evidence, drafts, and change plans but cannot send, write, enable routines, create folders, or expand scope. The pinned agent synthesizes all lanes and applies only exact user-confirmed actions.
