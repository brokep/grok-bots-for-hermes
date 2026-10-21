---
name: account-book--incumbent-and-competitor-check
description: "Use when the user asks what an account already uses, who else is in the deal, or how to position against whoever is in there today."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["account-book", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["account-book--getting-started", "account-book--build-the-account-list", "account-book--account-brief-before-a-call", "account-book--week-ahead-call-prep", "account-book--stakeholder-map", "account-book--account-signals-refresh"]
---
# Incumbent and competitor check

Inputs: the company name and site, the account file, and anything the user heard on a call.

1. Look for public evidence of what they run: job posts, engineering blog, docs, status page, public integration or partner pages, conference talks, open source repos, and security or trust pages.
2. Mark every tool confirmed, likely, or unknown. Confirmed means a public source names it and you have the link and the date. Likely means you inferred it and you say from what. Never let a likely read as confirmed.
3. Add what the user heard on calls, labeled as theirs, and say when it disagrees with the public evidence.
4. Look for timing signals that are actually public, such as a migration mentioned in a job post or a rebuild described on their blog. Contract dates are almost never public, so do not guess one.
5. For each incumbent that matters, write one positioning line: where what the user sells is genuinely different, in plain words, and one question that would test whether the difference matters here. No bashing and no claims about the incumbent you cannot source.

Output: a table of tool, category, confirmed or likely, source and date, and what it means for this deal. Then the positioning lines, then what you could not find.

Fallbacks: an account with no public technical footprint gets one honest line saying so and three questions to ask on the next call instead.

Save the findings into the account file.
