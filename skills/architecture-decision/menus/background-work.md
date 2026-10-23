# Menu: background work

Decides: how work that should not happen inside a user request is run (long tasks, retries, schedules, ingestion pipelines).
Cost to reverse: two-way at small scale, one-way once many jobs depend on it.

## Questions to answer first
- Which operations take longer than a user should wait (more than a few seconds)?
- Must work survive restarts and be retried on failure?
- Are there schedules (nightly, hourly)?
- What must the user see while work runs (progress, notification)?

## Options
| Option | What it is | Good for | Costs |
|---|---|---|---|
| **Job queue backed by the existing database (default)** | Jobs stored as rows; workers poll | Low to moderate volume, small teams | Limited throughput |
| Dedicated message queue / broker | Separate queueing system | High volume, many consumers, fan-out | Another system to run |
| Scheduled tasks (cron-style) | Run at fixed times | Periodic batch work | Not for user-triggered work |
| Workflow engine | Durable multi-step workflows with state | Long multi-step processes with human steps or compensation | Learning curve, operations |
| Serverless functions triggered by events | Platform runs code per event | Spiky, short tasks | Time limits, vendor coupling |

## Default
**Database-backed job queue**, with idempotent jobs, retries with backoff, a dead-letter list and visible job status.

## Choose another option when
- **Broker** if job volume or number of consumers exceeds what the database queue handles (measure).
- **Workflow engine** if a process has many steps over hours or days, with waits and rollbacks.
- **Scheduled tasks** for fixed-time batch work only.
- **Serverless** if the deployment decision record is already serverless.

## Common mistakes
- Jobs that are not idempotent, so retries duplicate effects.
- Failed jobs that disappear silently.
- Doing long work inside the request and hoping it finishes.
