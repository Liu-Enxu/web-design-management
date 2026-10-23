# Menu: caching

Decides: whether and where to keep copies of data to save time or cost.
Cost to reverse: two-way (but stale-data bugs are expensive).

## Questions to answer first
- Which measured budget is missed without a cache? (No measurement → no cache yet.)
- How stale may each piece of data be for users?
- Is the data the same for every user, or per user/permission?

## Options
| Option | Good for | Costs |
|---|---|---|
| **No cache, fix the query first (default)** | Most cases; indexes and smaller payloads solve it | None |
| HTTP caching / CDN | Static files and public, identical responses | Must set headers correctly; never for private data without care |
| Client query cache | Repeated reads in the UI | Already part of the state-management default |
| In-process memory cache | Small, hot, rarely changing data in one instance | Inconsistent across instances |
| Shared cache store (key-value) | Many instances, expensive computations, external API results | Another system; invalidation logic |
| Precomputed / materialized results | Heavy aggregations, reports | Refresh scheduling, storage |

## Default
**No new cache.** Measure, then fix queries and payloads. Use HTTP caching for static assets always.

## Choose another option when
- **Shared cache** if an expensive external or model call repeats with the same inputs (cache by input hash) or a measured budget is still missed after query fixes.
- **Precomputed results** for reports and aggregations over large data.
- **In-process** for small configuration-like data.

## Common mistakes
- Caching per-user or permissioned data under a shared key.
- No invalidation rule written down.
- Adding a cache to hide a missing index.
