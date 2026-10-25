# Rules: data design

Used in stage 3, step 8. Output: `docs/design/data-model.md`.

## 1. Entities and ownership
- Derive entities from stories and requirements: each noun users care about, with key fields. Link each entity to the FRs that need it.
- One module or service is the **only writer** of each entity. Others read through its interface.
- States each record can be in (state diagram), and who can change them.
- Per entity: sensitivity, retention, deletion (soft or hard), audit needs, from the data requirements.

## 2. Choosing the database: what the differences mean

Start from the `data-storage` menu (default: one relational database plus object storage). Use this table to explain the choice in the decision record.

| Store type (examples) | Data looks like | Strong at | Weak at | Pick it when |
|---|---|---|---|---|
| **Relational** (PostgreSQL, MySQL) | Tables with fixed columns and relations | Transactions, joins, constraints, reporting; often also JSON, full-text, vector via extensions | Very uneven data shapes; extreme write scale | Default for core business data |
| **Document** (MongoDB) | JSON-like documents, shape varies | Reading/writing whole records by key; flexible shape | Joins, cross-document transactions, consistency | Records truly have no common shape and are read whole |
| **Key-value / in-memory** (Redis) | Key → value, in memory | Very fast lookups, counters, sessions, rate limits, simple queues | Durability, complex queries; memory is costly | Cache or short-lived data; never the only copy of important data |
| **Search engine** (Elasticsearch, OpenSearch) | Inverted text index | Full-text ranking, facets, fuzzy match | Being the source of truth; must be kept in sync | Full-text needs exceed the database's built-in search (measured) |
| **Vector index** (pgvector, Qdrant) | Embeddings | Similarity / semantic search | Exact filters alone; approximate results | Semantic search or RAG beyond what a DB extension handles |
| **Object storage** (S3-compatible) | Files and blobs | Images, documents, backups, large files, cheap | Querying inside files | Any binary file |
| **Analytics / warehouse** | Columnar | Aggregations over large history | Transactional updates | Reports slow down the main database |

Commonly confused: **Redis** is a server-side in-memory data store. **Redux** is a client-side state library for React apps (see the `state-management` menu). **React** is a frontend UI library (see `rendering` and `stacks.md`).

For every extra store, write down which store is the **source of truth** and how copies are kept in sync.

## 3. Data types

| Kind of data | Store as | API format | Rules |
|---|---|---|---|
| **Moment in time** (created, sent, paid) | Timestamp with time zone, in UTC | ISO 8601 with offset: `2026-10-22T21:10:00Z` | Never store local-time strings. Set `created_at` / `updated_at` in the database. |
| **Calendar date** (birthday, due date) | Date only | `2026-10-22` | Not a timestamp; no time zone shift. |
| **Local time that must stay local** (opening hours, recurring 9:00 meeting) | Local time + IANA time zone name (`America/Detroit`) | Time + zone fields | Convert to UTC only when computing a specific occurrence. |
| **User's time zone** | IANA name string | Same | Never a fixed offset like `-04:00` (it changes with daylight saving). |
| **Duration** | Integer seconds (or ms) | Integer or ISO 8601 duration `PT90M` | State the unit in the field name: `timeout_seconds`. |
| **Images and files** | Binary in object storage; row in DB with key, content type, size, width/height, checksum, owner, created_at | URL (CDN or signed, expiring) + metadata | Never store blobs in DB rows. Validate type and size on upload. Make thumbnails and variants in a background job. Strip location metadata (EXIF) when privacy matters. |
| **Money** | Decimal, or integer minor units (cents) + ISO 4217 currency code | String or integer + `currency` | Never floating point. |
| **IDs** | UUID (v7 or ULID if they must sort by time) for anything exposed; integer allowed internally | String | Don't expose sequential IDs where enumeration is a risk. |
| **Status / category** | Text enum or lookup table | String values | Prefer a status enum over several booleans when more than two states are likely. |
| **Free text** | UTF-8 text with a length limit | String | Normalize what you compare (lowercase emails, trimmed). |
| **Flexible attributes** | JSON column | Object | Only for data you don't filter or join on often; core fields get real columns. |
| **Measurements** | Number with the unit in the name | Number | `weight_kg`, `distance_m`; one unit per field. |

Every column: explicit nullability and default.

## 4. Migrations
- Every schema change is a versioned migration in the repo.
- Backward compatible for one release: **expand → migrate data → contract** (add new column, backfill, switch reads, remove old column later).
- Test migrations on a copy of real-sized data before release.

## Output: docs/design/data-model.md

```markdown
# Data model
Audience: engineers · Last updated: <date> by <name>
Sources: DR-xxxx (data-storage), FR-xxx

## Stores
| Store | Holds | Source of truth? | Decision record |
|---|---|---|---|

## Entities
| Entity | Key fields and types | Owner module | Sensitivity | Retention | FRs |
|---|---|---|---|---|---|

## Diagram
<ER diagram, Mermaid>

## Lifecycles
<state diagrams for entities with states>
```
