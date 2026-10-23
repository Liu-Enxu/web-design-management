# Menu: testing strategy

Decides: the mix of tests and what blocks a merge or release.
Cost to reverse: two-way.

## Questions to answer first
- Which user flows would hurt most if broken (Must requirements)?
- What is hard to test (external services, hardware, AI outputs)?
- How fast must feedback be for developers?

## Test types
| Type | Checks | Speed | Use for |
|---|---|---|---|
| Static checks (types, lint) | Obvious mistakes | Instant | Everything |
| Unit | One function or module | Fast | Logic, calculations, edge cases |
| Integration | Modules together, real database/API | Medium | Data access, API contracts |
| End-to-end | Whole system through the UI or API | Slow | A few critical user flows |
| Contract | Client and server agree on the API | Fast | Separate frontend/backend teams |
| Evaluation sets | Quality of non-deterministic output (ML/LLM) | Slow | Anything model-driven; track scores over time |
| Manual / exploratory | What automation misses | Slow | Before releases, new features |

## Options
| Option | Shape | Good for |
|---|---|---|
| **Balanced (default)** | Static checks everywhere, many unit, fewer integration, a handful of end-to-end | Most projects |
| Integration-heavy | Mostly integration tests, fewer mocks | Apps that are mostly glue around a database and APIs |
| Evaluation-driven | Labeled datasets + score thresholds as gates | ML and LLM features |

## Default
**Balanced**, with these merge gates: static checks + unit + integration pass. End-to-end runs before release.

## Choose another option when
- **Integration-heavy** if most bugs come from how parts connect, not from logic.
- **Evaluation-driven** (in addition) for any model-based feature; a model or prompt change must not lower the score below the agreed threshold.

## Common mistakes
- Many end-to-end tests that are slow and flaky.
- Tests that pass even when the behavior is broken (too much mocking).
