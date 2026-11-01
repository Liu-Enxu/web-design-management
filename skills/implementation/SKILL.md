---
name: implementation
description: Stage 5 of the team workflow. Use when writing code for a planned task. Covers branch and pull request flow, coding conventions, commit messages, definition of done, and what to do when a task conflicts with requirements or decision records. Use for any "implement", "build" or "fix" request in a workflow-managed project.
---

# Implementation (stage 5)

Goal: code that does what the task says, follows the recorded decisions, and is ready for review.

## Entry criteria
- The task exists in `docs/project/plan.md` (or is a recorded small change, see project-flow) with acceptance criteria.

## Steps

1. **Read before coding.** The task, its requirements, the decision records it links, and the relevant design files:
   - UI work: the screen's Figma frame (status must be `ready`) and `design/ux.md`. Generate the code from the frame (through a Figma connection if available), use library components and tokens, build every designed state, then run it end to end against the API or its mock. Set the frame to `built` once merged.
   - Backend work: `design/api.md` and `design/data-model.md`, including the data-type rules (UTC times, images in object storage, no floats for money); the contract is the agreement, so change it only through a PR both owners review.
   - Anything touching auth, data or credentials: `design/security.md`.
   If something is unclear, ask before writing code.
2. **Put code where the code-organization decision record says.** New feature → its feature/module folder; shared code only under the rule for shared code. If nothing fits, raise it instead of inventing a new top-level folder.
3. **Branch.** One branch per task: `<type>/<task-id>-<short-name>`, for example `feat/T-012-jurisdiction-filter`. Types: feat, fix, refactor, docs, test, chore.
4. **Small steps.** Commit in small, working steps. Commit messages: `<type>(<scope>): <what> [T-012]`.
5. **Tests first, one acceptance criterion at a time.** Where to test (unit, integration, end to end) comes from the testing decision record.
   - Take one criterion: write a test that fails, write just enough code to pass it, then take the next. Never write all the tests before the code.
   - Test through the public interface (the API operation, the screen as the user uses it, the module's exported functions), never internals. A test should still pass after a refactor that keeps the behavior.
   - Avoid tests that mock internal parts or check the database directly instead of the interface, and tests whose expected value is computed the same way the code computes it; take it from the requirement or a worked example.
   - Each acceptance criterion maps to at least one test. For a bug, follow "Fixing a bug" below.
6. **Stay inside the decisions.** If the task cannot be done within the decision records or requirements:
   - stop, do not quietly work around it;
   - write a short note in the PR and in `docs/project/changes.md`;
   - route back to `architecture-decision` or `requirements`.
7. **Open a pull request** using the template below. Keep PRs reviewable (as a guide, under about 400 changed lines; split larger work).
8. **Get it reviewed; don't ask how.** Start a fresh review subagent on Opus 5.5 (`claude-opus-5-5`); your own session never counts as the review. Give it the PR number and task ID, and tell it to follow `quality-review/SKILL.md`, post the review notes as a PR comment, and never edit, approve or merge.
   - Blocking comments: fix them, push, and start a new review subagent. Still blocking after two rounds: stop and ask a person.
   - No blocking comments and `Door: two-way`: merge the PR.
   - No blocking comments and `Door: one-way`: ask a person to approve; merge only after they do.
   - If you cannot start a subagent, ask a person to review instead.
9. **Update the plan.** Set the task status in `docs/project/plan.md` (or the linked tracker), and its `Done by` to the git user name (`git config user.name`), or `contributor` if none is set.

## Fixing a bug
For a `BUG-` item in `docs/product/stories.md`. Branch as `fix/BUG-001-<short-name>`.
1. **Make it fail first.** Build one command (a test, a curl call, a script) that runs the broken path and fails with the exact symptom in the bug report. Run it and keep the output, with secrets replaced by `<REDACTED>`. It must give the same result every run; for a bug that only sometimes happens, repeat the trigger until it fails often enough to work with.
2. **Shrink it.** Remove inputs, data and steps one at a time, rerunning after each, until it is the smallest case that still fails.
3. **Find the cause.** Test one guess at a time against the command. Do not change code on a guess the command has not confirmed.
4. **Fix it.** The command now passes; keep it as a regression test in the PR.

If you cannot make it fail, stop: list what you tried and ask the reporter for access, logs (without secrets) or exact steps.

## Definition of done
- [ ] Acceptance criteria met, each with a test or a written manual check.
- [ ] Tests, linters and type checks pass in CI.
- [ ] No unrelated changes in the PR.
- [ ] Design docs updated per the `design-doc` update triggers, in the same PR.
- [ ] UI matches the `ready` design, including loading, empty, error and permission states.
- [ ] Follows linked decision records and the API contract; any deviation raised, not hidden.
- [ ] Secrets are not in code or logs; new credentials added to the security register (no values).
- [ ] Reviewed per step 8 with no blocking comments; one-way PRs also approved by a person.

## Rules for AI agents
- Work only on the assigned task; list anything else you notice as a follow-up instead of fixing it in the same PR.
- Never change a decision record, requirement or gate status; propose the change instead.
- State what you tested and what you could not test.

## PR template

```markdown
## What
<one paragraph>

## Why
Task: T-xxx or BUG-xxx · Requirements: FR-xxx, NFR-xxx · decision records: DR-xxxx · Design: S-xx / API op / TH-xx
Docs updated: <design/ files changed, or "none needed">

## Evidence
- Before: <screenshot, output or failing test run>
- After: <screenshot, output or passing test run; for UI, compared with the design frame>

## Merge danger
Door: one-way | two-way (one-way: hard to undo once merged, such as a data migration or a published API change)
Blast radius: <what breaks, and for whom, if this is wrong>

## How to verify
1. 

## Acceptance criteria
- [ ] <criterion> — <test name or manual check>

## Deviations or open questions
- none / <description and change request ID>
```

## Handoff
→ `quality-review`.

Step 5, "Fixing a bug" and the Evidence and Merge danger sections are adapted from the `tdd`, `diagnosing-bugs` and `pr` skills in [mattpocock/skills](https://github.com/mattpocock/skills) (MIT).
