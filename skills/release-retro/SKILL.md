---
name: release-retro
description: Stage 7 of the team workflow. Use when a milestone or release is ready to ship, and afterwards to run a retrospective and feed lessons back into stories, requirements, decision records and the workflow itself. Use for "ship", "release", "retro" or "what did we learn". Writes docs/project/releases/<version>.md.
---

# Release and retrospective (stage 7)

Goal: ship safely, check that the release did what it was meant to, and make the next cycle better.

## Entry criteria
- All tasks in the milestone done and reviewed.

One file per release: `docs/project/releases/<version>.md`. After the retro, move the milestone's plan to `docs/project/archive/` and start the next milestone in `project/plan.md`.

## Part A: release

### Release checklist
- [ ] All Must requirements of the milestone verified against acceptance criteria.
- [ ] CI green on the release commit; version or tag created.
- [ ] Data migrations tested on a copy of real data; backup taken.
- [ ] Rollback plan written and tested (how to undo, who decides, how long it takes).
- [ ] Monitoring and alerts in place for the new behavior.
- [ ] Security re-check (`architecture-decision/rules/security.md` and the before-release list in `review/rules/security-test.md`): new boundaries, roles and credentials registered; high threats mitigated or accepted; access list current (leavers removed).
- [ ] Performance budgets met, or misses accepted by the product owner (`design/performance.md`).
- [ ] Design docs audited per the `design-doc` skill (no stale or duplicated sections).
- [ ] Release sign-off pack built with `doc-assemble` (profile: release sign-off) if an approver needs one.
- [ ] Release notes written for users and for the team.
- [ ] People who must know (support, users, stakeholders) informed.

### Release strategy (pick one, record it)
| Option | Use when |
|---|---|
| All at once (default) | Small user base, easy rollback |
| Staged rollout (percentage or group) | Many users, risky change |
| Feature flag | Code ships before the feature is turned on |
| Blue-green / parallel run | Downtime or a bad release is costly |

### After release
- Watch the agreed metrics for the agreed period.
- Check results against the outcomes in the stories ("so that…"). Did users get the outcome?

## Part B: retrospective

Hold within a week of release. Format (default): **Keep / Problem / Try**.

1. **Facts first.** Planned vs shipped, dates, incidents, metrics.
2. **Keep:** what worked.
3. **Problem:** what hurt. Focus on process and decisions, not people.
4. **Try:** at most three concrete changes, each with an owner.
5. **Feed back:**
   - new or changed needs → `user-stories`;
   - wrong or missing requirements → `requirements`;
   - decisions that proved wrong → new superseding decision record;
   - design gaps: screens → `requirements`; data, contract, threats → `architecture-decision`;
   - performance or cost problems → optimization loop in `review/rules/performance.md`;
   - workflow problems → a pull request to this skills repo.

## Output: docs/project/releases/<version>.md

```markdown
# Release and retro: <milestone>
Release date: · Strategy: · Version:

## Shipped vs planned
| Planned | Shipped | Note |
|---|---|---|

## Outcomes check
| Story | Intended outcome | Observed | Met? |
|---|---|---|---|

## Incidents
- 

## Keep
- 
## Problem
- 
## Try
| Action | Owner | Due |
|---|---|---|

## Feedback into the workflow
- Stories: 
- Requirements: 
- Decisions: 
- Workflow skills: 
```

## Gate checklist
- [ ] Release checklist complete.
- [ ] Outcomes checked against stories.
- [ ] Retro held; actions have owners.
- [ ] Feedback items routed to their stages.
- [ ] A person approved in docs/STATE.md.

## Handoff
→ `project-flow` to start the next milestone (usually back at `user-stories` or `task-breakdown`).
