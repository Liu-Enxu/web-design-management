# Rules: API contract

Used in stage 3, step 9. Output: `docs/design/api.md` (one-page summary) and `docs/design/api/` (machine-readable spec).

## Steps
1. **Operations per story.** For each Must story, the operations it needs, named from the user's point of view. Check every Must screen in `docs/design/ux.md` can get its data.
2. **Write the spec first**, in the format chosen in the api-style decision record (for example an OpenAPI file). Frontend can then build against a mock while backend builds the real thing.
3. **Conventions** (decide once, record in `api.md`):
   - error format: one shape for all errors, with a stable error code and a human message;
   - pagination, filtering and sorting style;
   - idempotency for creates and retried operations;
   - versioning and deprecation;
   - dates and times per `rules/data.md` (UTC, ISO 8601);
   - file uploads: direct-to-storage with signed URLs, size and type limits;
   - limits: page size, payload size, rate limits.
4. **Authorization per operation**: which role or rule allows it (from the role matrix in `security.md`).
5. **Background work**: long or retryable operations (ingestion, reports, emails, image processing) go to jobs per the `background-work` menu; define retries, timeouts, idempotency and what the user sees meanwhile.
6. **Integrations**: for each external system: purpose, direction, protocol, failure mode and fallback, credential (entered in the credential register).
7. **Consistency**: where transactions are needed, and where eventual consistency is acceptable (and what the user sees).

## Sign-off
Frontend and backend owners both approve the spec. Later changes go through a pull request that both review.
