---
name: account-book--open-threads-and-next-steps
description: "Use when the user pastes notes from a call or an email thread, or asks what is still open on an account."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["account-book", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["account-book--getting-started", "account-book--build-the-account-list", "account-book--account-brief-before-a-call", "account-book--week-ahead-call-prep", "account-book--stakeholder-map", "account-book--incumbent-and-competitor-check"]
---
# Open threads and next steps

Inputs: pasted call notes, an email thread, a transcript, or a typed-up voice memo, plus the account file.

1. Read what they gave you and say back what you found before you change anything: who was there, the date, and how many items you pulled.
2. Pull four kinds of item and nothing else: what they asked for, what the user promised, what was decided, and what was left unresolved.
3. Turn each into an open thread with what it is, who owns it (them or us), the date it was raised, a due date when one was said, and a status of open, waiting on them, waiting on us, or closed.
4. Close anything these notes resolve, and say which threads closed.
5. Flag every thread with no owner or no date. Those are the ones that die quietly.
6. Write the next steps. At most five, each an action with an owner and a date. Nothing vague.

Output: the open threads table, what closed, and the next steps. Then offer once to draft the follow-up note through Outreach and follow-up drafts. Never send it. When Linear is connected and a thread is a product request or a bug, offer to open or link an issue so their team can see it, only on a yes.

Fallbacks: messy or partial notes still get processed, with a short "needs a look" list for the lines you could not place. Never invent an attendee, a commitment, a date, or a quote. When a line is ambiguous, quote it and ask rather than deciding for them.

Save the threads and the next steps into the account file.
