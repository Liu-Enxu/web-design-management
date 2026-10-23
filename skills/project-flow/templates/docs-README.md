# <Project name>: project docs

Run with the team workflow skills. Start any session with **project-flow**; it reads `STATE.md` and says what's next.

**Every agent working in this repository must follow the structure below.** `AGENTS.md` (loaded by `CLAUDE.md` for Claude Code) makes this mandatory.

## Project structure

Defined in `docs/structure.yml` (the source of truth); the tree below is drawn from it.

<!-- structure:begin -->
```
<project repo>/
├── <code>/                  code; layout set in stage 3
├── AGENTS.md                rules every agent must follow
├── CLAUDE.md                loads AGENTS.md for Claude Code
├── README.md                run, test, deploy
├── build/                   doc-assemble snapshots; contents not committed
└── docs/                    project docs; never deployed
    ├── README.md            this map
    ├── structure.yml        source of truth for this tree
    ├── STATE.md             dashboard: stage, gates
    ├── product/             WHAT and WHY
    │   ├── stories.md       personas, user stories, bugs
    │   └── requirements.md  FR/NFR, scope, priorities
    ├── decisions/           HISTORY; never edited
    │   ├── README.md        decision index
    │   └── 0001-<title>.md  one decision each
    ├── design/              system AS IT IS TODAY
    │   ├── README.md        one line per file, reading order
    │   ├── architecture.md  parts and connections
    │   ├── diagrams/        Mermaid sources
    │   ├── data-model.md    entities, data types, DB
    │   ├── api.md           API contract summary
    │   ├── api/             full API spec
    │   ├── ux.md            art direction, screens
    │   ├── security.md      threats, admins, keys
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
<!-- structure:end -->

`project-flow` creates every file and folder above on the first run. Files say `Status: not started` until a skill fills them. `<code>/` is replaced by the real code folders after the code-organization decision.

## Skills in development sequence

```
project-flow                   router: state → next skill
├── 1  user-stories            stories, personas
├── 2  requirements            requirements, scope, priority
│   └── rules/ux-art.md        art direction, Figma first
├── 3  architecture-decision   AI proposes, team decides
│   ├── stacks.md              team default stacks
│   ├── menus/ (12)            options incl. <code>/ layout
│   ├── perspectives/ (5)      BE, FE, security, ops, UX
│   └── rules/                 data, API, security design
├── 4  task-breakdown          tasks; scaffold <code>/
├── 5  implementation          Figma → code, run end to end
├── 6  quality-review          check vs requirements, design
│   └── rules/                 security and perf. testing
└── 7  release-retro           ship, security, retro

Cross-cutting (any stage)
design-doc                     what goes where in docs/
├── diagrams                   Mermaid from docs
└── doc-assemble               combined doc per audience
```

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
| quality-review | R | R | W performance.md | U changes.md | R `<code>/` · W for optimization |
| release-retro | R | R | R (audit) | W releases/ · U archive/, plan.md | U STATE.md |
| design-doc | rules | rules | rules + audit | rules | |
| diagrams | R | R | W diagrams/ · U files that embed them | | |
| doc-assemble | R | R | R | W exports/ | W snapshot outside `docs/` |

## IDs

`US` story · `BUG` bug · `FR`/`NFR` requirement · `DR` decision · `S` screen · `TH` threat · `T` task

## Rules

- Every agent follows this folder structure; no new top-level folders without a decision record.
- Not in `docs/`, not decided.
- One home per fact; link, don't copy.
- A named person approves every gate.
- No secret values anywhere in the repository.
