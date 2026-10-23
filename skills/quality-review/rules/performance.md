# Rules: performance testing and optimization

Used in stage 6 when a change touches a budgeted path, and whenever a budget is missed. Output: `docs/design/performance.md`.
Team TODO: frontend lead to extend with the team's own test approach.

## 1. Budgets
Write targets in `performance.md`, each tied to an NFR. Examples: p95 response time per key operation, page load on a mid-range device, largest bundle size, query time, memory, cost per month, model/API cost per request.

## 2. How to test
| Test | Measures | When |
|---|---|---|
| Benchmark of key operations | Time per operation | In CI for budgeted paths |
| Load test | Throughput, p95/p99 under expected and 2–3× load | Before release |
| Page performance audit | Load time, layout shift, interactivity | Before release, for Must screens |
| Bundle size check | Size of frontend code shipped | In CI |
| Query review | Slow queries, missing indexes, N+1 queries | When data access changes |
| Cost check | Infrastructure and model/API spend | Monthly and before release |

Measure on production-like data and load. Record method, data set and environment so results can be repeated.

## 3. Optimization loop (only when a budget is missed)
1. **Baseline**: measure and record.
2. **Find the bottleneck by profiling**, not guessing. Usual suspects, most common first: database (indexes, N+1, large scans) → network round trips and payload size → external and model calls (batch, cache, smaller model) → client rendering and bundle size → algorithms.
3. **Hypothesis**: "Changing X will reduce Y by about Z, because …".
4. **One change at a time**, behind tests; measure again with the same method.
5. **Keep or revert**: keep only changes that move the metric without costing more readability than they gain. Log both.
6. **Guard it**: add a CI check or alert that catches the regression.
7. **Stop** when the budget is met.

Changes that alter architecture (new store, new service, cache layer) need a decision record in stage 3.

## Output: docs/design/performance.md

```markdown
# Performance
Owner: · Audience: engineers · Last reviewed:
Sources: NFR-xxx

## Budgets
| Metric | Budget | Source | Current | Status |
|---|---|---|---|---|

## Measurement method
<tools, data set, load, environment>

## Optimization log
| Date | Hypothesis | Change | Before | After | Kept? | PR |
|---|---|---|---|---|---|---|
```

## Team additions
- 
