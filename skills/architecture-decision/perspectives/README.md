# Perspective reviews

Every one-way-door decision record is reviewed from each relevant perspective before it is accepted. Two-way-door decision records need only the perspective of the team that implements them.

Each perspective is represented by a named person (or an agent working from the checklist, with a person confirming). The reviewer answers the questions in their file and records the result in the decision record's "Perspective review" table:

- **agree** — no concerns;
- **agree with conditions** — conditions become requirements, tasks or follow-up decision records;
- **object** — reason given; the decider must answer it in the decision record before accepting.

| Perspective | File | Required for |
|---|---|---|
| Backend | backend.md | system shape, data storage, API, auth, background work, caching, deployment, code organization |
| Frontend | frontend.md | rendering, API, state management, auth (login flows), code organization |
| Security | security.md | auth, data storage, API, deployment, any external integration |
| Operations | operations.md | system shape, deployment, observability, data storage |
| Design/UX | (use the handoff checklist in `requirements/rules/ux-art.md`) | rendering, state management, anything that changes what users see |

Disagreement is expected and useful. The decider (named in the decision record) makes the call after objections are answered; the objection stays in the decision record.
