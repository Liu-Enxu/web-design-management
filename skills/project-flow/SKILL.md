---
name: project-flow
description: Entry point for the team project workflow. Use at the start of any project session, when asked "where are we", "what's next", or to start, resume or change stage. On the first run it creates the full project structure from structure.yml (every docs file and folder, AGENTS.md, CLAUDE.md); afterwards it checks the structure, reads docs/STATE.md, reports the current stage and gaps, and routes to the right stage skill.
---

# Project flow (router)

You coordinate the workflow. You do not do the stage work yourself; you find out where the project is and hand off to the right skill.

## Stages

| # | Skill | Artifact | Gate question |
|---|---|---|---|
| 1 | user-stories | docs/product/stories.md | Do we have the stories that matter, with acceptance criteria? |
| 2 | requirements | docs/product/requirements.md, docs/design/ux.md | Requirements traceable, bounded, ranked; art direction chosen; Must screens `ready` in Figma? |
| 3 | architecture-decision | docs/decisions/, docs/design/ | Architecture and stack chosen; data, API and security designed; one-way decisions reviewed? |
| 4 | task-breakdown | docs/project/plan.md | Every Must requirement, screen and mitigation maps to owned tasks? |
| 5 | implementation | code + PRs | Planned tasks done to the definition of done? |
| 6 | review | PR reviews, docs/design/performance.md | Changes meet requirements and designs, pass security checks, stay within performance budgets? |
| 7 | release-retro | docs/project/releases/<version>.md | Shipped, security re-checked, lessons fed back? |

Cross-cutting skills: **design-doc** (what goes where in `docs/`), **diagrams** (Mermaid from docs), **doc-assemble** (combined doc per audience).

UX design for Should/Could screens may continue in parallel with stage 3.

## Steps

1. **Read state.** Open `docs/STATE.md`. If it does not exist, this is the **first run**:
   1. Ask for the project name, and find where these skills are installed (for example `.claude/skills`).
   2. From the repository root, run:
      `python3 <skills>/project-flow/scripts/structure.py init --name "<project name>" --skills <skills>`
      It copies `templates/structure.yml` to `docs/structure.yml` and creates **every file and folder listed in it**, exactly as the tree in `docs/README.md` shows: starter content from `templates/` where one exists, otherwise a stub with `Status: not started`; `.gitkeep` in empty folders. It installs `AGENTS.md` and `CLAUDE.md` at the root (adding the workflow rules at the top if they already exist) and never overwrites other existing files.
   3. If Python is not available, do the same by hand from `templates/structure.yml`, with the same contents.
   4. Show the user the list of created files, then ask who owns each gate and who reviews each perspective, and fill in `docs/project/team.md`.
   Then go to step 2.
2. **Check artifacts.** Run `python3 <skills>/project-flow/scripts/structure.py check` and report every error and warning. Then, for the active stage and earlier stages, check the artifact is filled in (not `Status: not started`) and not stale (for example, requirements that reference dropped stories; design files whose "Last reviewed" is older than the latest related decision record).
3. **Report** briefly: current stage and status; gates passed and by whom; what is missing for the current gate; open questions; open change requests (`project/changes.md`) and high risks (`project/risks.md`).
4. **Route.** Recommend the next skill and why. If the user asks for work that belongs to another stage, name that stage and either switch (if the user agrees) or log a change request in `docs/project/changes.md`.
5. **Update state** after a skill finishes: status, date, artifact link, open items.

## Moving backwards
- Review finds unrequested behavior or a missing requirement → requirements.
- A screen needs data the API lacks → requirements (screen) and architecture-decision (contract) together.
- Implementation breaks a decision record, or a new integration, role, secret or sensitive data appears → architecture-decision.
- An optimization needs a new store, service or cache → architecture-decision.
- Users ask for new things after release → user-stories.

Record the reason in `docs/project/changes.md` under Change log.

## Gates
A gate is passed only when a named person writes their approval in `docs/STATE.md`. You prepare a gate checklist and ask for sign-off; you never sign it yourself.

## Small or urgent work
1. Write one story or bug in `product/stories.md` (or link the issue).
2. Confirm it changes no requirement, decision record, API contract, screen design or credential register entry. If it does, it is not small.
3. Go to implementation and review.

## Changing the structure
`docs/structure.yml` is the source of truth. To change it (for example, replacing `<code>/` with the real code folders after the code-organization decision):
1. Write or link the decision record that justifies the change.
2. Edit `docs/structure.yml`.
3. Run `structure.py render` to redraw the tree in `docs/README.md`, then `structure.py check`.

## Templates
| File | Used for |
|---|---|
| `templates/structure.yml` | Copied to `docs/structure.yml` |
| `templates/docs-README.md` | `docs/README.md` (tree drawn from structure.yml) |
| `templates/AGENTS.md`, `templates/CLAUDE.md` | Repository root |
| `templates/files/docs/...` | Starter content for STATE.md, decisions/README.md, project/team.md, risks.md, changes.md |

Keep STATE.md to one screen. Change requests, the change log, risks and release history live in `docs/project/`.
