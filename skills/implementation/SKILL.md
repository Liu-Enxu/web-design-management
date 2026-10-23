---
name: implementation
description: Stage 5 of the team workflow. Use when writing code for a planned task: branch and pull request flow, coding conventions, commit messages, definition of done, and what to do when a task conflicts with requirements or decision records. Use for any "implement", "build" or "fix" request in a workflow-managed project.
---

# Implementation (stage 5)

Goal: code that does what the task says, follows the recorded decisions, and is ready for review.

## Entry criteria
- The task exists in `docs/project/plan.md` (or is a recorded small change, see project-flow) with acceptance criteria and an owner.

## Steps

1. **Read before coding.** The task, its requirements, the decision records it links, and the relevant design files:
   - UI work: the screen's Figma frame (status must be `ready`) and `design/ux.md`. Generate the code from the frame (through a Figma connection if available), use library components and tokens, build every designed state, then run it end to end against the API or its mock. Set the frame to `built` once merged.
   - Backend work: `design/api.md` and `design/data-model.md`, including the data-type rules (UTC times, images in object storage, no floats for money); the contract is the agreement, so change it only through a PR both owners review.
   - Anything touching auth, data or credentials: `design/security.md`.
   If something is unclear, ask before writing code.
2. **Put code where the code-organization decision record says.** New feature → its feature/module folder; shared code only under the rule for shared code. If nothing fits, raise it instead of inventing a new top-level folder.
3. **Branch.** One branch per task: `<type>/<task-id>-<short-name>`, for example `feat/T-012-jurisdiction-filter`. Types: feat, fix, refactor, docs, test, chore.
4. **Small steps.** Commit in small, working steps. Commit messages: `<type>(<scope>): <what> [T-012]`.
5. **Tests with the code.** Write or update tests per the testing decision record. Each acceptance criterion should map to at least one test.
6. **Stay inside the decisions.** If the task cannot be done within the decision records or requirements:
   - stop, do not quietly work around it;
   - write a short note in the PR and in `docs/project/changes.md`;
   - route back to `architecture-decision` or `requirements`.
7. **Open a pull request** using the template below. Keep PRs reviewable (as a guide, under about 400 changed lines; split larger work).
8. **Update the plan.** Set the task status in `docs/project/plan.md` (or the linked tracker).

## Definition of done
- [ ] Acceptance criteria met, each with a test or a written manual check.
- [ ] Tests, linters and type checks pass in CI.
- [ ] No unrelated changes in the PR.
- [ ] Design docs updated per the `design-doc` update triggers, in the same PR.
- [ ] UI matches the `ready` design, including loading, empty, error and permission states.
- [ ] Follows linked decision records and the API contract; any deviation raised, not hidden.
- [ ] Secrets are not in code or logs; new credentials added to the security register (no values).
- [ ] Reviewed and approved (stage 6).

## Rules for AI agents
- Work only on the assigned task; list anything else you notice as a follow-up instead of fixing it in the same PR.
- Never change a decision record, requirement or gate status; propose the change instead.
- State what you tested and what you could not test.

## PR template

```markdown
## What
<one paragraph>

## Why
Task: T-xxx · Requirements: FR-xxx, NFR-xxx · decision records: 000x · Design: S-xx / API op / TH-xx
Docs updated: <design/ files changed, or "none needed">
Screenshots: <for UI changes, compared with the design frame>

## How to verify
1. 

## Acceptance criteria
- [ ] <criterion> — <test name or manual check>

## Deviations or open questions
- none / <description and change request ID>
```

## Handoff
→ `review`.
