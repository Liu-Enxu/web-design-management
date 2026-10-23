# Menu: system shape

Decides: how the system is split into deployable units.
Cost to reverse: one-way (splitting later is possible; merging back is painful).

## Questions to answer first
- How many teams will work on it in the next year?
- Do parts have very different scale, release cadence or reliability needs (NFRs)?
- Is there a hard requirement to deploy parts independently?

## Options
| Option | What it is | Good for | Costs |
|---|---|---|---|
| **Modular monolith (default)** | One deployable app, split into modules with clear boundaries | Most products, 1–3 teams | Boundaries need discipline to stay clean |
| Simple monolith | One app, little internal structure | Prototypes, short-lived tools | Becomes tangled as it grows |
| Monolith + few services | Main app plus 1–3 separate services for special needs | One part needs different scale, language or runtime (e.g. ML inference, batch jobs) | Network calls, separate deploys |
| Microservices | Many independently deployed services | Many teams needing independent releases | High operational cost, distributed failures, data consistency work |

## Default
**Modular monolith**: you get structure without the cost of networks, multiple deploys and distributed data.

## Choose another option when
- **Simple monolith** if the project is a prototype expected to be thrown away.
- **Monolith + few services** if a part has an NFR the main app cannot meet (very different scale, GPU, long-running jobs) or needs a different language.
- **Microservices** only if several teams are already blocked by shared releases. Team coordination pain is the trigger, not code untidiness.

## Common mistakes
- Splitting into services before the domain boundaries are understood.
- Shared database between "independent" services.
