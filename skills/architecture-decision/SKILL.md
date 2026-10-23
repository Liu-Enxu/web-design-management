---
name: architecture-decision
description: Stage 3 of the team workflow. Use to design the architecture from approved requirements: the agent proposes an architecture, the team picks a tech stack from default options, decides each category from option menus, designs the data model (database choice, data types for time, images, money, IDs), the API contract and security (threats, admins, credential owners), with backend, frontend, security and operations reviews. Use for any "how should we build it", "which stack/database" or "which approach" question. Writes docs/decisions/ and docs/design/.
---

# Architecture (stage 3)

Goal: from the requirements, a proposed and agreed architecture, a chosen stack, data and API designs both sides can build against, and known security risks, each decision recorded with its reason.

## Entry criteria
- `docs/product/requirements.md` approved (NFRs, constraints, data requirements).
- `docs/design/ux.md` drafted (screens tell us what data the API must provide).

## Steps

### A. Propose (the agent suggests, people decide)
1. **Read** requirements, constraints and screens. List the forces that shape the design: scale, latency, data sensitivity, integrations, team skills, budget.
2. **Propose 1–2 candidate architectures.** For each: a container diagram (`diagrams` skill), one paragraph on how it meets the Must requirements and NFRs, main risks, rough cost and effort. Recommend one and say why. Mark everything `proposed`.

### B. Choose the stack
3. **Start from `stacks.md`** (the team's list of common stacks with defaults). Pick the profile that fits the requirements; list any part you change and why. If `stacks.md` has no fitting profile, propose one from the menus and mark it as a proposal for the team list.
4. Record the stack as a decision record.

### C. Decide by menu
5. **List decisions needed.** Go through `menus/` and mark each category: needed now, later, or N/A. Add project-specific decisions.
6. **Sort by reversibility.** One-way door (expensive to undo): decide now with perspective reviews. Two-way door: take the default; it can change later with a short note.
7. **For each decision:** read the menu, start from the default, check each "choose another option when" trigger against requirement IDs, take the default unless a trigger fires, name the concrete tool, write the record from `templates/decision.md` as `proposed`.

### D. Data, API and security design (rules in `rules/`)
8. **Data** per `rules/data.md`: entities, ownership, database choice with the differences explained, data types (time, images and files, money, IDs, text, enums), migrations. Writes `docs/design/data-model.md`.
9. **API** per `rules/api.md`: operations per Must story, contract written first, conventions, authorization per operation, sign-off by frontend and backend owners. Writes `docs/design/api.md` and `docs/design/api/`.
10. **Security** per `rules/security.md`: trust boundaries, STRIDE threats, roles and admins, credential register. Writes `docs/design/security.md`; mitigations become NFRs or tasks; accepted threats go to `docs/project/risks.md`.

### E. Review and describe
11. **Perspective reviews.** For each one-way decision record, collect reviews from the perspectives in `perspectives/README.md`. Answer every objection in the record before marking it `accepted`.
12. **Describe the system.** Write `docs/design/architecture.md` with context and container diagrams and one paragraph per container. Link decision records; don't repeat their reasoning.
13. **Check coverage.** Every NFR is addressed by a decision record, by the data, API or security design, or explicitly by implementation.

## Menus (in `menus/`)

| File | Decides | Usually |
|---|---|---|
| system-shape.md | Monolith, modular monolith, services | One-way |
| rendering.md | How UI is produced | One-way |
| data-storage.md | Kind of store per data type | One-way |
| api-style.md | How parts and clients talk | One-way |
| auth.md | Identity and access control model | One-way |
| background-work.md | Jobs, queues, schedules | Two-way → one-way at scale |
| caching.md | Whether and where to cache | Two-way |
| state-management.md | Client and server state | Two-way |
| deployment.md | Where and how it runs | Mixed |
| code-organization.md | Repositories and folder structure | One-way for repos |
| testing.md | Test mix and gates | Two-way |
| observability.md | Logs, metrics, traces, alerts | Two-way |

Mark N/A categories with one line (a CLI tool has no rendering decision).

## Rules
- A decision without a decision record did not happen.
- Accepted records are never edited except their status; a change is a new record that supersedes the old one.
- Prefer boring, well-known options; novelty needs a requirement behind it.
- No pattern without its problem (services or micro-frontends for a small team, caches without measurements).
- The agent proposes; a named person decides. Reviewers comment on their concerns, not on taste.
- Never write secret values anywhere in `docs/`.

## Output
- `docs/decisions/0001-<title>.md` per decision, and the index `docs/decisions/README.md`:

```markdown
| Record | Title | Category | Status | Reversibility | Reviews |
|---|---|---|---|---|---|
| 0001 | Modular monolith | system-shape | accepted | one-way | BE ✓ FE ✓ SEC ✓ OPS ✓ |
```
- `docs/design/architecture.md`, `data-model.md`, `api.md` + `api/`, `security.md`.

## Gate checklist
- [ ] Proposal reviewed; one architecture chosen.
- [ ] Stack recorded (from `stacks.md` or proposed for it).
- [ ] Every menu category marked needed / later / N/A; one-way records accepted with reviews.
- [ ] Data model: database choice explained, every entity has owner, types, sensitivity and retention.
- [ ] API contract approved by frontend and backend owners.
- [ ] Threats rated; high ones mitigated or accepted by a named person; every admin role has two named holders; every credential has an owner and storage location.
- [ ] Every NFR traced; architecture.md has context and container diagrams.
- [ ] A person approved in docs/STATE.md.

## Handoff
→ `task-breakdown`.
→ Back to `requirements` if a decision exposes a missing or contradictory requirement.
