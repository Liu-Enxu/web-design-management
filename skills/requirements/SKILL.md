---
name: requirements
description: Stage 2 of the team workflow. Use to translate user stories into engineering requirements (functional and non-functional), set scope boundaries and constraints, rank priorities, and set the UX and art direction (screens, look and feel, Figma designs; the agent proposes directions if the team has none). Use when the team asks "what exactly do we build", "what's in or out", "what comes first" or "what should it look like". Writes docs/product/requirements.md and docs/design/ux.md.
---

# Requirements, boundaries, priorities and UX (stage 2)

Goal: turn user language into testable engineering requirements, draw the boundary of what we build, agree what comes first, and agree what it looks like.

## Entry criteria
- `docs/product/stories.md` exists with agreed stories.

## Steps

### A. Translate stories into requirements
1. **Functional requirements (FR).** For each agreed story, write one or more requirements the system must meet. Use "The system shall…". Each FR is testable and links back to its story.
   - Story: "As an analyst, I want to filter cases by jurisdiction, so that I only read relevant law."
   - FR-012: "The system shall filter search results by one or more jurisdictions." (from US-004)
2. **Non-functional requirements (NFR).** Walk this checklist for every project. Write a requirement with a number where it matters, or write "no requirement" explicitly:
   - Performance (response time, throughput)
   - Scale (users, data size, growth)
   - Availability and recovery (uptime, backup, restore time)
   - Security and privacy (auth, data sensitivity, audit)
   - Compliance and legal
   - Accessibility
   - Compatibility (platforms, browsers, devices, integrations)
   - Maintainability and operability (logging, monitoring, deploys)
   - Cost (budget limits for infrastructure or services)
3. **Data requirements.** What data exists, where it comes from, who owns it, how long it is kept.
4. **Traceability check.** Every agreed story maps to at least one FR. Every FR maps to a story or to an explicit reason (for example, a legal obligation).

### B. Boundaries
5. **In scope / out of scope.** Two lists. Out of scope is as important as in scope; write the things people might assume are included.
6. **Constraints.** Fixed facts the design must live with: deadlines, budget, team skills, mandated tools, existing systems, regulations.
7. **Assumptions and dependencies.** What we believe but have not verified, and what other teams or systems we depend on. Risky assumptions are also entered in `docs/project/risks.md`.
8. **Interfaces and ownership.** Where this system ends and others begin, and who owns each side.

### C. Priorities
9. **Rank with MoSCoW (default).**
   - Must: the release fails without it.
   - Should: important, painful to leave out, not fatal.
   - Could: nice to have if time allows.
   - Won't (this time): agreed out, recorded so it is not reopened by accident.
   Rule of thumb: Must items should fit in about 60% of the available effort.
10. **Optional second method** when Must is too crowded or there is disagreement (pick one, record which):
    - **RICE** (Reach × Impact × Confidence ÷ Effort) for comparing many items with data.
    - **Value vs effort 2×2** for a quick workshop.
    - **Kano** (basic / performance / delighter) when deciding what makes the product feel complete.
11. **Release slices.** Group Must items into the first release (MVP). Should and Could items go into later slices.

### D. UX and art direction (rules in `rules/ux-art.md`)
12. **Screens.** From the Must stories, list the screens and flows (screen IDs `S-01`…).
13. **Art direction.** Use what the team supplies (brand, references, existing Figma). If there is none, the agent proposes 2–3 directions (mood, palette, typography, component library, reference products) and a person picks one.
14. **Figma first.** Design the Must screens in Figma (or the team's design tool) with all states; mark each `ready` when it passes the handoff checklist. Implementation then generates the code from `ready` frames and runs it end to end.

## Decision points
- Priority method: MoSCoW unless the team records a reason to use another.
- Every NFR number needs a source (a user need, a contract, a measurement), not a guess. Mark guesses as `assumption`.
- Disagreements on priority: the product owner decides and the reason is recorded.

## Output: docs/product/requirements.md

```markdown
# Requirements: <project>

## Functional requirements
| ID | Requirement (The system shall…) | From story | Priority | Acceptance test |
|---|---|---|---|---|
| FR-001 | | US-001 | Must | |

## Non-functional requirements
| ID | Category | Requirement (with number) | Source | Priority |
|---|---|---|---|---|
| NFR-001 | Performance | | | |

## Data requirements
| Data | Source | Owner | Sensitivity | Retention |
|---|---|---|---|---|

## Scope
### In scope
- 
### Out of scope
- 

## Constraints
- 

## Assumptions and dependencies
| ID | Assumption / dependency | Risk if wrong | Owner |
|---|---|---|---|

## Interfaces and ownership
| Boundary | Our side | Other side | Owner |
|---|---|---|---|

## Prioritization
Method: MoSCoW (+ <secondary method, if used, and why>)

### Release slices
- R1 (MVP): FR-…, NFR-…
- R2: …

## Traceability
| Story | Requirements |
|---|---|
| US-001 | FR-001, FR-002 |
```

Also writes `docs/design/ux.md` (format in `rules/ux-art.md`).

## Gate checklist
- [ ] Every agreed story maps to at least one FR.
- [ ] NFR checklist walked; every category has a requirement or "no requirement".
- [ ] In/out of scope written and reviewed by the product owner.
- [ ] Must items fit the effort budget.
- [ ] Art direction chosen; every Must screen designed with all states and marked `ready`.
- [ ] A person approved in docs/STATE.md.

## Handoff
→ `architecture-decision` (NFRs, constraints and screens are the main inputs). UX design can continue in parallel with stage 3 for Should/Could screens.
→ Back to `user-stories` if translation exposes a missing or unclear need.
