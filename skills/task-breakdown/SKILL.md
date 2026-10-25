---
name: task-breakdown
description: Stage 4 of the team workflow. Use to break approved requirements and architecture decisions into milestones and tasks with assignees, estimates, dependencies and acceptance criteria. Use when planning a release, sprint or "who does what". Writes docs/project/plan.md.
---

# Task breakdown and plan (stage 4)

Goal: a plan where every task traces to a requirement and has a clear "done".

## Entry criteria
- Requirements gate (stage 2) and architecture gate (stage 3) passed.

## Sources of tasks
- Requirements (FR/NFR) in the milestone.
- Screens marked `ready` in `design/ux.md` (at least one task per screen, linked as `S-xx`).
- API operations and data model changes in `design/api.md` and `design/data-model.md` (backend tasks; frontend tasks may start against the contract with a mock).
- Threat mitigations in `design/security.md` (`TH-xx`), and decision record follow-ups and perspective-review conditions.

## Steps

1. **Milestones.** Use the release slices from `product/requirements.md`. Each milestone has a goal a user could notice, and a target date.
2. **Walking skeleton first.** The first milestone should be a thin end-to-end path through every major part of the system (for example: one screen → API → storage → deploy), even if it does almost nothing. It proves the architecture early. Its first task is **scaffolding the repository** per the code-organization decision record: folders, workspace tooling, import-rule lint, CI, and run/test/deploy steps in the root `README.md`.
3. **Tasks.** For each requirement in the milestone, write tasks:
   - assignee: a person, or `none` until someone picks it up;
   - links to FR/NFR and decision records;
   - acceptance criteria (copied or refined from the requirement);
   - estimate (pick one scale per project: T-shirt sizes, points or days);
   - dependencies on other tasks.
   Tasks bigger than about 3 days are split.
4. **Risk tasks.** For each high risk in `docs/project/risks.md`, add a spike (time-boxed investigation) early in the plan, with a question it must answer.
5. **Critical path.** Mark the chain of dependent tasks that sets the earliest finish date.
6. **Capacity check.** Compare the estimate total with the people available. If over, move Should/Could items, not quality work.

## Decision points
- **Estimate scale:** T-shirt (S/M/L, default for early planning), points, or days. Record the choice.
- **Tracking tool:** this file is the source of truth for the plan's structure; an issue tracker may hold the live status. If both are used, link task IDs both ways.

## Output: docs/project/plan.md

```markdown
# Plan: <project>
Estimate scale: <T-shirt | points | days>

## Milestones
| ID | Goal | Includes | Target date | Status |
|---|---|---|---|---|
| M1 | Walking skeleton | FR-001 (thin) | | |

## Tasks
| ID | Task | Milestone | Assignee | Requirement | Design (S-/API/TH-) | decision record | Estimate | Depends on | Status | Done by |
|---|---|---|---|---|---|---|---|---|---|---|
| T-001 | | M1 | none | FR-001 | S-01 | DR-0001 | S | | todo | |

### T-001 acceptance criteria
- 

## Spikes
| ID | Question to answer | Time box | Assignee | Result | Done by |
|---|---|---|---|---|---|

## Critical path
T-001 → T-004 → T-009

## Capacity
| Person | Available (days) | Assigned (days) |
|---|---|---|
```

## Gate checklist
- [ ] Every Must requirement in the milestone has tasks.
- [ ] Every `ready` screen and every mitigated threat in the milestone has tasks.
- [ ] Every task has acceptance criteria and an estimate (assignee may be `none`).
- [ ] First milestone is a walking skeleton.
- [ ] Capacity fits, or the cut is agreed.
- [ ] A person approved in docs/STATE.md.

## Handoff
→ `implementation`.
