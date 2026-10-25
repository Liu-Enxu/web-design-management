# Agent instructions: project workflow

This project is managed with the team workflow skills, installed at `<skills>/`. Every agent working in this repository, for any task, follows these rules.

## Folder structure rule (mandatory)
1. **`docs/structure.yml` is the source of truth** for every file and folder in `docs/`. `docs/README.md` shows it as a tree. Read one of them before creating, moving or renaming any file.
2. Put every document in the folder its kind belongs to: `docs/product/` (what and why), `docs/decisions/` (history of choices), `docs/design/` (the system as it is today), `docs/project/` (how we run the work). `docs/STATE.md` is the dashboard only.
3. Put code where the code-organization decision record in `docs/decisions/` says.
4. Do not create any file or folder in `docs/` that `docs/structure.yml` does not allow. To change the structure: decision record → edit `docs/structure.yml` → `structure.py render`. If nothing fits, ask.
5. One home per fact: update the existing file and link to it; never copy content into a second place.
6. Never write secret values anywhere in the repository.
7. Before finishing any task that created, moved or renamed files, run `python3 <skills>/project-flow/scripts/structure.py check` and fix every error.

## Workflow rule
1. Read `docs/STATE.md`. If it does not exist, follow `<skills>/project-flow/SKILL.md`.
2. Read the current stage's skill before acting:
   - Stage 1 user stories: `<skills>/user-stories/SKILL.md`
   - Stage 2 requirements and UX: `<skills>/requirements/SKILL.md`
   - Stage 3 architecture: `<skills>/architecture-decision/SKILL.md`
   - Stage 4 planning: `<skills>/task-breakdown/SKILL.md`
   - Stage 5 coding: `<skills>/implementation/SKILL.md`
   - Stage 6 review, security and performance: `<skills>/quality-review/SKILL.md`
   - Stage 7 release and retrospective: `<skills>/release-retro/SKILL.md`
3. Before writing anything under `docs/`, read `<skills>/design-doc/SKILL.md`. For diagrams, read `<skills>/diagrams/SKILL.md`. For a combined document, read `<skills>/doc-assemble/SKILL.md`.
4. Never mark a stage gate as passed. Prepare the work and ask a named person to approve it in `docs/STATE.md`.
5. If a request does not fit the current stage, say which stage it belongs to, then follow that skill or record a change request in `docs/project/changes.md`.

## Commit rule
1. Code: one branch and pull request per task, as in `<skills>/implementation/SKILL.md`. Design docs changed by a task go in that task's pull request.
2. Other doc work and `docs/STATE.md` updates: commit directly to the default branch as `docs(<stage>): <what>`, for example `docs(user-stories): add personas P1–P3`.
3. The first commit is the bootstrap: `chore: bootstrap project workflow`.
