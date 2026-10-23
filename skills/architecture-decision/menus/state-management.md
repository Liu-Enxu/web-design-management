# Menu: state management (client applications)

Decides: where each kind of client-side state lives. N/A for projects without a client app.
Cost to reverse: two-way (can change per feature).

## First: state is not one thing
| Kind | Example | Default home |
|---|---|---|
| Server state | Search results, user profile | A query/cache layer that fetches, caches and refetches |
| Local UI state | Is this menu open | The component itself |
| Form state | Draft input, validation errors | A form helper or the component |
| URL state | Filters, page number, selected tab | The URL (shareable, survives refresh) |
| Global app state | Current user, theme, feature flags | A small global store or context |

## Options for global state
| Option | Good for | Costs |
|---|---|---|
| **Minimal global state (default)** | Most apps once server state is handled by a cache | Requires discipline about what is "global" |
| Central store (Flux/Redux-style) | Complex client-only logic, many writers, need for time-travel debugging | Boilerplate, everything tends to end up global |
| Reactive signals / observables | Fine-grained updates, high-frequency UI | Different mental model for the team |
| Client-side database / sync engine | Offline-first, collaborative editing | Sync and conflict handling |

## Default
**Server state in a query/cache layer, everything else as local as possible, a small global store only for truly global values.**

## Choose another option when
- **Central store** if the client has substantial logic that is not server data (editors, games, simulators).
- **Signals** if profiling shows re-render performance problems.
- **Client database/sync** if a requirement needs offline use or real-time collaboration.

## Common mistakes
- Copying server data into a global store and keeping it in sync by hand.
- Mixing several state libraries without rules for which one handles what.
