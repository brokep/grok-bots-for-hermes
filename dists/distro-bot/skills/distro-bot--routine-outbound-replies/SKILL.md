---
name: distro-bot--routine-outbound-replies
description: "Routine: Disabled by default. Weekdays 11:15am and 4:15pm: replies handed to sales, follow-ups drafted."
version: 1.0.0
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: ["distro-bot", "grok-bot", "routine"]
    related_skills: ["distro-bot--distro-setup", "distro-bot--ad-accounts", "distro-bot--campaign-loop", "distro-bot--ad-creative", "distro-bot--market-scan", "distro-bot--outbound-desk"]
---
# Routine: Outbound replies

Original schedule: Disabled by default. Weekdays 11:15am and 4:15pm: replies handed to sales, follow-ups drafted.

# Outbound replies

This routine ships disabled. Before enabling, confirm the timezone, the inbox, and who gets replied leads.

When enabled:
1. distro.py status. Setup not done, or Outbound replies not in routines_on: stop silently.
2. Run Replies in @outbound-desk: every reply is logged, then handed to the sales teammate or listed for the user.
3. Draft the follow-ups distro.py lead due lists, per @outbound-desk. Never send from this run.
4. One message: replies and where each went, drafts waiting. Nothing new: quiet.

Fires on:
- cron `15 11,16 * * 1-5`

Ask the importing user for:
- Timezone
