# Menu: data storage

Decides: what kind of store holds each type of data.
Cost to reverse: one-way (data migrations are expensive).

## Questions to answer first
- What are the main entities and how do they relate?
- Do we need transactions across several records?
- What queries matter: exact lookups, filters, full-text, similarity, analytics?
- Data size and growth (NFR), retention and sensitivity (data requirements).

## Options
| Option | What it is | Good for | Costs |
|---|---|---|---|
| **Relational database (default)** | Tables, SQL, transactions | Most business data, related records, reporting | Schema changes need migrations |
| Document store | Flexible JSON-like documents | Data with highly varied shape, read-mostly by key | Weak joins, consistency is your job |
| Key-value / cache | Fast lookup by key | Sessions, caching, rate limits | Not a primary store for important data |
| Search engine | Inverted index for text search and ranking | Full-text search at scale, faceting | Second copy of data to keep in sync |
| Vector index | Similarity search over embeddings | Semantic search, recommendations, RAG | Approximate results, needs an embedding pipeline |
| Object / file storage | Blobs and files | Documents, images, backups, large files | No querying inside files |
| Analytics store / warehouse | Columnar, for large aggregations | Reporting over large history | Not for transactional workloads |

## Default
**One relational database** for core data, plus **object storage** for files. Many relational databases also offer full-text search, JSON columns and vector extensions; use those before adding a separate store.

## Choose another option when
- **Search engine** if full-text ranking quality or scale exceeds what the relational database handles (measure first).
- **Vector index (separate)** if similarity search volume or size exceeds what the database extension handles.
- **Document store** if records truly have no common shape and are always read whole by key.
- **Key-value/cache** if an NFR on response time cannot be met otherwise; never as the only copy.
- **Warehouse** if analytics queries slow down the main database.

## Common mistakes
- Adding a new store for every query type before trying the existing one.
- No plan for keeping copies in sync (which store is the source of truth?).
