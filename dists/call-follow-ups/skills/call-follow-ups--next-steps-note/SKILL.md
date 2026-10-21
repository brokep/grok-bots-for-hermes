---
name: call-follow-ups--next-steps-note
description: "Writes the 50-word next-steps note for the CRM in the team's format: current state, next step with owner and date, risk, solution."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["call-follow-ups", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["call-follow-ups--getting-started", "call-follow-ups--crm-update-proposal", "call-follow-ups--promise-tracker", "call-follow-ups--recap-email", "call-follow-ups--voice-profile"]
---
# next-steps-note

# next-steps-note

## When to use

After any call, as part of the post-call pack, or when the owner pastes a voice note or rough summary and asks for "next steps in our format".

## Format

Use the format stored in memory. The default is one running paragraph, no bullets, 50 words maximum:

`[YYYY-MM-DD]: CS: <current state in one clause>. NS: <next step, owner, date>. Risk: <the one thing most likely to stall this>. Solution: <what we are doing about it>.`

If the owner's team uses a different shape (MEDDPICC fields, a "Why now" line, a champion check), that shape wins. Ask before going longer than 50 words, and only if the extra context would materially change what leadership does with the note.

## Steps

1. Take the call read from `recap-email` (or produce it if running alone).
2. Current state in plain language: where the deal stands after this call, not what happened on the call.
3. Next step: one concrete action, one owner, one date. "Schedule technical review with platform team, Dana to send invite by Sep 15" is right. "Follow up" is not.
4. Risk: name the specific blocker (budget cycle, missing economic buyer, competitor in evaluation). Not "timing".
5. Solution: the move that addresses that risk.

## Output

The note as plain text, ready to paste or to hand to `crm-update-proposal`. Show the previous note from the CRM beside it so the owner sees what changed.

## Rules

- Never write to the CRM from this skill. `crm-update-proposal` handles writes, after approval.
- Dates absolute, never "next week".
- No em dashes.
