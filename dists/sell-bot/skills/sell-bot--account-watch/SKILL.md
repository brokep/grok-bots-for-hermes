---
name: sell-bot--account-watch
description: "Use for credit runway, expansion signals, watched accounts, and the roster sheet."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["sell-bot", "grok-bot", "from-grok-bot-team", "sales"]
    related_skills: ["sell-bot--sell-setup", "sell-bot--accounts", "sell-bot--draft-email", "sell-bot--schedule", "sell-bot--watch-on-x", "sell-bot--prep-page"]
---
# account-watch

# account-watch

## Credit runway (credit programs only)

Balance and 7 days of spend for every program account per accounts, ranked by runway days. Urgent: under the runway threshold, or out with spend in the last 7 days. Urgent with no burn draft in drafts.csv this week: a draft per draft-email with where they stand, what runs out when, and the choices under Credit options.

## Expansion signals

Customers at the expansion threshold in setup.md, with seats or usage up 50% in 4 weeks, or asking about a bigger plan: an expansion deal per proposal-desk with the numbers and dates, and the date saved as expansion flagged. Once a month per account at most.

## Watched accounts

Each one under Watched accounts: one line on usage and burn, silent while it has no account or no usage. Then posts from customers and watched X accounts per watch-on-x.

## Report

Top 10 by runway (account, balance, daily spend, runway, source and date), expansion deals opened, drafts, and flags. Nothing new: quiet.

## Roster sheet

The user's own customer list (for example credit recipients). First use: ask for the link and key column, and save them under Roster sheet with the columns I may edit. On request: match rows by the key column, compare with the sources, show the adds and changes, and write them after a yes (append rows, update saved columns). Never touch columns a number source owns, delete rows, or reorder columns. No Sheets connector: send the updated list as a CSV attachment.
