# Menu: API style

Decides: how parts of the system and outside clients talk to each other.
Cost to reverse: one-way for public APIs, two-way for internal ones.

## Questions to answer first
- Who calls the API: our own frontend, other teams, third parties?
- Do different clients need very different shapes of the same data?
- Is anything real-time (pushed updates) or long-running?
- Are client and server written in the same language?

## Options
| Option | What it is | Good for | Costs |
|---|---|---|---|
| **Resource-based HTTP (REST-style) (default)** | URLs for resources, standard methods, JSON | Most APIs, public APIs, caching | Over/under-fetching for complex screens |
| Typed RPC | Call server functions with shared types | One team, same language end to end | Tight coupling of client and server |
| Query language (GraphQL-style) | Client asks for exactly the fields it needs | Many clients with different data needs | Server complexity, caching and authorization are harder |
| Binary RPC (gRPC-style) | Schema-defined, fast, streaming | Service-to-service, high throughput | Harder from browsers, tooling needed |
| Events / messaging | Publish messages; consumers react | Async work, decoupling, long jobs | Debugging and ordering are harder |
| Real-time channels (WebSocket/SSE) | Server pushes updates | Live dashboards, chat, progress | Connection handling, scaling |

## Default
**Resource-based HTTP with a written contract (an OpenAPI-style spec)**, agreed before frontend and backend start, so both can build in parallel.

## Choose another option when
- **Typed RPC** if one team owns both sides in the same language and the API is internal.
- **Query language** if three or more clients need substantially different data shapes.
- **Binary RPC** for internal service-to-service calls with throughput NFRs.
- **Events** for work that can finish later (emails, reports, ingestion) or must not block the user.
- **Real-time** add-on when a requirement needs pushed updates; keep it beside the main API, not instead of it.

## Common mistakes
- No contract; frontend and backend discover the API by trial and error.
- No versioning plan for an API others depend on.
