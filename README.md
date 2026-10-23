# Project Workflow Skills

A shared, agent-neutral workflow for running a project as a team. Everyone (people and AI agents) moves through the same stages, makes decisions from the same option menus, and leaves the same artifacts behind, so the team can always tell where a project is and why it looks the way it does.

## Bootstrap (do this once per project)

Run these from the **project's** root folder. Copy only the contents of `skills/`; do **not** copy this README or this repo's `AGENTS.md` (the first run creates the project's own `AGENTS.md`, and the project keeps its own `README.md`).

**1. Install the skills: one real copy in `.claude/skills/`**

```bash
mkdir -p .claude/skills
cp -r /path/to/project-workflow/skills/* .claude/skills/
```

**2. Let your other agents see the same copy** (only for the agents your team uses; links, not copies, so they never drift)

| Agent | Skills folder it reads | Instruction file it reads | Command |
|---|---|---|---|
| Claude Code | `.claude/skills/` | `CLAUDE.md` (created; loads `AGENTS.md`) | none, step 1 is enough |
| Codex | `.agents/skills/` | `AGENTS.md` | `mkdir -p .agents && ln -s ../.claude/skills .agents/skills` |
| Qwen Code | `.qwen/skills/` | `QWEN.md` and `AGENTS.md` | `mkdir -p .qwen && ln -s ../.claude/skills .qwen/skills` |
| Deep Code (DeepSeek) | `.deepcode/skills/` | not documented; tell it to read `AGENTS.md` | `mkdir -p .deepcode && ln -s ../.claude/skills .deepcode/skills` |
| Others (Cursor, Copilot, Gemini…) | not needed | `AGENTS.md` (its paths point to `.claude/skills/`) | none |

On Windows, symlinks need Developer Mode; otherwise copy the folder instead and re-copy whenever you update the skills.

**3. First run: creates the whole project structure**

| Agent | Say or type |
|---|---|
| Claude Code, Qwen Code | `/project-flow` |
| Codex, Deep Code, others | "Read `.claude/skills/project-flow/SKILL.md` and run it." |
| No agent | `python3 .claude/skills/project-flow/scripts/structure.py init --name "<project>" --skills .claude/skills` |

It creates every file and folder in `docs/structure.yml`, plus `AGENTS.md` and `CLAUDE.md` at the root (existing ones are kept, with the workflow rules added at the top), then asks who owns each gate.

**4. Commit** `.claude/skills/`, the agent links, `AGENTS.md`, `CLAUDE.md` and `docs/`, so every teammate and agent gets the same setup on clone.

**Updating the skills later:** replace `.claude/skills/` with the new version and commit. Don't run `init` again; `project-flow` sees `docs/STATE.md` and reports the current stage.

## The pipeline

```
project-flow                   router: state → next skill
├── 1  user-stories            stories, personas
├── 2  requirements            requirements, scope, priority
│   └── rules/ux-art.md        art direction, Figma first
├── 3  architecture-decision   AI proposes, team decides
│   ├── stacks.md              team default stacks
│   ├── menus/ (12)            options incl. <code>/ layout
│   ├── perspectives/ (4)      BE, FE, security, ops
│   └── rules/                 data, API, security design
├── 4  task-breakdown          tasks; scaffold <code>/
├── 5  implementation          Figma → code, run end to end
├── 6  review                  check vs requirements, design
│   └── rules/                 security and perf. testing
└── 7  release-retro           ship, security, retro

Cross-cutting (any stage)
design-doc                     what goes where in docs/
├── diagrams                   Mermaid from docs
└── doc-assemble               combined doc per audience
```

Seven stages in order. Any stage can send the project back to an earlier one.

## Where each skill works

W = writes · U = updates · R = reads · `docs/` paths unless noted

| Skill | product/ | decisions/ | design/ | project/ | Other |
|---|---|---|---|---|---|
| project-flow | W all stubs | W README.md | W all stubs | W all stubs · team.md | W README.md, structure.yml, STATE.md · root AGENTS.md, CLAUDE.md · runs check |
| user-stories | W stories.md | | | | U STATE.md |
| requirements | R stories · W requirements.md | | W ux.md | U risks.md | U STATE.md · Figma |
| architecture-decision | R | W records + README.md | W architecture.md, data-model.md, api.md, api/, security.md | U risks.md | U STATE.md |
| task-breakdown | R | R | R | W plan.md · R risks.md | U STATE.md |
| implementation | R | R | U per update triggers | U plan.md, changes.md | W `<code>/` · Figma status |
| review | R | R | W performance.md | U changes.md | R `<code>/` · W for optimization |
| release-retro | R | R | R (audit) | W releases/ · U archive/, plan.md | U STATE.md |
| design-doc | rules | rules | rules + audit | rules | |
| diagrams | R | R | W diagrams/ · U files that embed them | | |
| doc-assemble | R | R | R | W exports/ | W snapshot outside `docs/` |

## Principles

1. **Documents, not chat, hold the state.** If it is not in `docs/`, it was not decided.
2. **Four doc folders, four purposes** (see `design-doc`):
   - `product/`: what we build and why (stories, requirements).
   - `decisions/`: history of choices, one record per decision, never edited.
   - `design/`: the system as it is today, kept current with every change.
   - `project/`: how we run the work (team, plan, risks, changes, releases).
   `STATE.md` is a one-screen dashboard on top.
3. **Humans pass the gates.** Agents prepare drafts and options; a named person approves each stage in `docs/STATE.md`.
4. **Decisions come from menus, and every affected team is heard.** Pick a named option, record why, and collect perspective reviews for one-way decisions.
5. **One pipeline for everyone.** Frontend, backend, design and security work all trace to the same stories: `US` → `FR/NFR` → design (`S-`, API operation, `TH-`) → `T` → PR.
6. **Stack-neutral menus, team default stacks.** Menus describe categories of options; `architecture-decision/stacks.md` lists the team's preferred stacks; each project names its tools in decision records.
7. **No secrets in docs.** The credential register records owners and locations, never values.

## Layout

This repo (the skills):
```
skills/
  project-flow/            router
    scripts/structure.py   init, render, check (from structure.yml)
    templates/             structure.yml, docs-README.md, AGENTS.md,
                           CLAUDE.md, files/ (starter content)
  user-stories/  requirements/
  architecture-decision/
    stacks.md              team default stacks (TODO)
    menus/                 12 decision menus + _template.md
    perspectives/          BE, FE, security, ops checklists
    rules/                 data.md, api.md, security.md
    templates/decision.md  decision record template
  requirements/rules/      ux-art.md
  task-breakdown/  implementation/
  review/rules/            security-test.md, performance.md
  release-retro/
  design-doc/  diagrams/   cross-cutting
  doc-assemble/
    templates/             spec template + 6 audience profiles
AGENTS.md                  copy of the template project-flow installs
```

What `project-flow` creates in each project repo on the first run, drawn from `templates/structure.yml` (the same tree appears in `docs/README.md`):
```
<project repo>/
├── <code>/                  code; layout set in stage 3
├── AGENTS.md                rules every agent must follow
├── CLAUDE.md                loads AGENTS.md for Claude Code
├── README.md                run, test, deploy
└── docs/                    project docs; never deployed
    ├── README.md            this map
    ├── structure.yml        source of truth for this tree
    ├── STATE.md             dashboard: stage, gates
    ├── product/             WHAT and WHY
    │   ├── stories.md       personas, user stories
    │   └── requirements.md  FR/NFR, scope, priorities
    ├── decisions/           HISTORY; never edited
    │   ├── README.md        decision index
    │   └── 0001-<title>.md  one decision each
    ├── design/              system AS IT IS TODAY
    │   ├── README.md        overview, reading order
    │   ├── architecture.md  parts and connections
    │   ├── diagrams/        Mermaid sources
    │   ├── data-model.md    entities, data types, DB
    │   ├── api.md           API contract summary
    │   ├── api/             full API spec
    │   ├── ux.md            art direction, screens
    │   ├── security.md      threats, admins, keys
    │   ├── operations.md    deploys, runbooks, alerts
    │   └── performance.md   budgets, optimization log
    └── project/             HOW we run the work
        ├── team.md          people, roles, RACI
        ├── plan.md          current milestone tasks
        ├── risks.md         risks, assumptions
        ├── changes.md       change requests, log
        ├── releases/        one file per release
        ├── exports/         combined-doc specs
        └── archive/         finished plans
```

## Notes

- The skills use the common `SKILL.md` format (a folder per skill, YAML frontmatter with `name` and `description`).
- People new to the workflow: read `skills/project-flow/SKILL.md` first, then `skills/design-doc/SKILL.md`.
- Keep this folder in its own git repo and change it through pull requests, so the whole team runs the same version.

## Extending

- New decision category: copy `skills/architecture-decision/menus/_template.md`.
- New perspective (for example data science or hardware): add a checklist to `perspectives/` and a row to its README.
- New combined-doc profile: copy `skills/doc-assemble/templates/_spec.md`.
- New stage: copy any stage skill, keep the section layout (Entry criteria, Steps, Decision points, Output, Gate, Handoff), and add it to `project-flow`.
