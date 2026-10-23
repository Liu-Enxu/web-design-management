# Backend perspective

Answer each question for the proposed decision. "Not affected" is a valid answer.

## Data
- Which module or service is the single writer of each affected entity?
- Does this need transactions across entities? Can the chosen store provide them?
- How do schema changes and data migrations work under this decision?
- What happens to existing data (backfill, migration cost, downtime)?

## Contracts
- Does this change or constrain the API contract? Is it backward compatible?
- How are errors, retries and idempotency handled?
- What does the frontend need that this makes easier or harder?

## Behavior under load and failure
- Expected load and growth (NFR): does the option handle it with margin?
- What happens when a dependency (database, external API, model provider) is slow or down?
- Is any work long-running or retryable that should move to background work?

## Operability
- Can we test it locally and in CI without heroic setup?
- How is it deployed, configured and observed?
- Who on the team can maintain it? Is the skill gap acceptable?

## Red flags
- A shared database between parts that are meant to be independent.
- Business logic that will end up duplicated in frontend and backend.
- A new store or service with no requirement behind it.
- No owner for a piece of data.
