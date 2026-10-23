# Operations perspective

## Running it
- Where does it run, and who operates it?
- How is it deployed, rolled back and configured per environment?
- What does it cost per month at expected load, and at 10× load?

## Knowing it works
- What metrics, logs and alerts prove the related NFRs?
- What is the first thing to check when it breaks? Is there a runbook entry?

## Recovery
- Backup and restore: what, how often, tested how?
- What is the impact if it is down for an hour? Does that meet the availability NFR?

## Red flags
- Manual steps in deploy or recovery.
- A component nobody on the team can operate.
- No way to tell from monitoring that it has failed.
