---
name: review
description: Stage 6 of the team workflow. Use to review a pull request or completed task against its acceptance criteria, requirements, decision records, API contract and Figma design, plus code quality, security testing and performance testing, and to run measured optimization when a performance or cost budget is missed. Use for any "review this PR/change/code", "security test", "performance test", "make it faster/cheaper" request. Produces review notes and writes docs/design/performance.md.
---

# Review, security and performance (stage 6)

Goal: confirm the change does what was agreed, the way it was agreed, is safe, and is fast and cheap enough to merge.

## Entry criteria
- A pull request using the implementation PR template, linked to a task.

## Review order
Review in this order; stop and send back early if a top item fails.

1. **Right thing.** Does the change meet the task's acceptance criteria? Is anything included that no task or requirement asked for?
2. **Within decisions and designs.** Follows the linked decision records, the API contract, the data model (including data types), and for UI the `ready` Figma frame with all its states? Any silent deviation?
3. **Correctness.** Logic, edge cases, error handling, empty and failure states.
4. **Security.** Run the per-PR checklist in `rules/security-test.md`.
5. **Tests.** Each acceptance criterion covered; tests would fail if the behavior broke.
6. **Performance.** If the change touches a budgeted path, test per `rules/performance.md`; no regression against `docs/design/performance.md`.
7. **Maintainability.** Naming, structure, duplication, code in the folder the code-organization decision says.
8. **Operability.** Logs, metrics and config per the observability decision record.
9. **Docs.** Files updated per the `design-doc` update triggers, in the folder the structure rule says.

## When a budget is missed
Run the optimization loop in `rules/performance.md` (measure, profile, one change at a time, keep or revert, guard, stop). Each optimization is its own PR, reviewed with this skill.

## Comment labels
- `blocking:` must change before merge.
- `suggestion:` worth doing, author decides.
- `question:` reviewer needs to understand something.
- `nit:` minor style; never blocks.

## Outcomes
- **Approve:** no blocking comments.
- **Request changes:** at least one blocking comment.
- **Send back a stage:** the problem is a missing requirement or a wrong decision. Raise a change request in `docs/project/changes.md` and route to `requirements` or `architecture-decision`.

## Rules
- Review the change, not the person.
- Agents may review and comment; a person approves merges for anything touching a one-way decision, auth, data deletion or payments.
- Two rounds without agreement: talk synchronously, then record the outcome on the PR.

## Review notes template

```markdown
Review of PR <link> (T-xxx)
- Acceptance criteria: met / not met (<which>)
- Decision / contract / design conformance: ok / deviation (<which, what>)
- Security checklist: ok / issues
- Performance: n/a / within budget / regression (<metric>)
- Tests: adequate / gaps
- Docs updated: yes / missing (<file>)
- Outcome: approve | request changes | send back to <stage>
```

## Handoff
→ Merge, then `release-retro` when the milestone is complete.
→ Back to `implementation` on request changes.
