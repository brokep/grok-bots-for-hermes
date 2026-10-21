---
name: account-book--week-ahead-call-prep
description: "Use when the user asks what is coming up, wants to get ready for the week, or pastes a calendar, a schedule, or a set of invites."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["account-book", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["account-book--getting-started", "account-book--build-the-account-list", "account-book--account-brief-before-a-call", "account-book--stakeholder-map", "account-book--incumbent-and-competitor-check", "account-book--account-signals-refresh"]
---
# Week ahead call prep

Inputs: a connected calendar, a pasted schedule, forwarded invites, or the next dates on the account list.

1. Collect the external calls in the window they asked for, the rest of this week by default. Ignore internal meetings unless they say otherwise.
2. Match each call to an account. A call you cannot match gets listed at the end by name so they can tell you who it is.
3. Read each account file before you write anything about it.
4. Write one block per call, at most six lines: the company and the time, who is on it and their role in the deal, one line on what changed since the last touch with a source and a date, the open threads each side owes, and one question worth asking.
5. Calls with no account file get three lines of quick public research and a note that a full brief is one ask away.
6. End with the one call that needs the most work before it happens, and offer to build that full brief now.

Output: day by day, calls in time order, then the unmatched list, then the one call to prepare properly.

Fallbacks: no calendar connected means asking them to paste the week or forward the invites, and either works. A call with only a company name still gets a block. Never contact anyone on the calendar and never add a meeting to their schedule.

Save any new account you learned about into the account list, and save each block into that account's file.
