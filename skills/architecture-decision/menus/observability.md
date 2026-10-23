# Menu: observability

Decides: how we know what the system is doing in production.
Cost to reverse: two-way.

## Questions to answer first
- What would we need to know during an incident?
- Availability and performance NFRs: what must be measured to prove them?
- Sensitive data that must not appear in logs?

## Building blocks
| Block | Answers | Default |
|---|---|---|
| Structured logs | What happened, for one request | JSON logs with a request ID |
| Metrics | How much, how fast, how often | Request rate, error rate, latency per endpoint |
| Traces | Where time went across components | Add when there are several services or slow multi-step requests |
| Error tracking | Which errors, how often, with context | Yes, from day one |
| Alerts | When a person must act | Only on user-visible symptoms tied to NFRs |
| Domain/AI traces | Inputs, outputs, cost of model calls | Yes for any LLM/ML feature |

## Options
| Option | Good for | Costs |
|---|---|---|
| **Managed observability service (default)** | Small teams | Cost grows with volume |
| Self-hosted open-source stack | Data must stay in-house, large volume | Operating it |
| Logs only | Prototypes | Blind to trends and slowdowns |

## Default
**Managed service with structured logs, basic metrics, error tracking and a few NFR-based alerts.**

## Choose another option when
- **Self-hosted** if data residency or cost at volume requires it.
- **Add tracing** when a request crosses more than two components.

## Common mistakes
- Alerts on every error, so people ignore them.
- Personal or secret data in logs.
