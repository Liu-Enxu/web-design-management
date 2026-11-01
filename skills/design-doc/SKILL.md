---
name: design-doc
description: Cross-cutting skill for the team workflow. Use whenever design or development documentation is created, updated, read or reorganized. It defines how docs/ is structured, where each kind of information lives, what does not belong, size budgets and when sections must be updated. Use before writing anything into docs/design/, and to audit the docs for staleness or bloat.
---

# Design and development doc

Goal: one design doc that people actually read. Every fact has exactly one home; the doc describes the system as it is now, and links instead of copying.

These rules apply to **every agent and person** working in a managed repository; `AGENTS.md` at the repository root makes them mandatory.

## Four folders, four purposes

| Folder | One line | Changes | Owner |
|---|---|---|---|
| `product/` | **What we build and why**: users, stories, requirements, scope, priorities | When needs or scope change | Product owner |
| `decisions/` | **History of choices**: one record per decision, in order, with the reasoning; never edited, only superseded | A new record per decision | Decider named in each record |
| `design/` | **The system as it is today**: architecture, data, API, screens, security; always kept current, describes the system rather than repeating the code | In the same PR as the change it describes | Whoever changes it (see "Last updated") |
| `project/` | **How we run the work**: plan, risks, changes, releases and retros | Every milestone or as events happen | Project lead |

Plus `docs/STATE.md`: a one-screen dashboard (current stage, gate status, and one-line links to the open questions blocking the current gate; each question lives in the doc it is about). Nothing else goes in it.

If a piece of text mixes purposes, split it: reasoning → a decision record; current state → `design/`; status, plans and history of the work → `project/`.

## docs/ layout

The layout is defined in **`docs/structure.yml`**, the single source of truth (template: `project-flow/templates/structure.yml`). `docs/README.md` shows it as a tree drawn from that file. Do not copy the layout anywhere else.

- `project-flow` creates every file and folder in it on the first run; files say `Status: not started` until a skill fills them. When you fill a file, remove that line.
- `structure.py check` (in `project-flow/scripts/`) reports anything in `docs/` that is not in `structure.yml`, and missing root files. Code folders and anything else beside `docs/` are not checked.
- To add or move a file or folder: decision record → edit `structure.yml` → `structure.py render` → `structure.py check`.
- Starter formats for `STATE.md`, `decisions/README.md`, `design/README.md`, `risks.md` and `changes.md` are in `project-flow/templates/files/`.
- When a milestone closes, move its plan section to `project/archive/<milestone>.md` and start the next one in `plan.md`.

## Section contract

Every file in `design/` starts with this header:

```markdown
# <Title>
Audience: <who reads this> · Last updated: <date> by <name>
Sources: <DR-xxxx, FR-xxx, Figma link> 
```

Whoever changes a file updates its "Last updated" line: today's date and the git user name (`git config user.name`), or `contributor` if none is set.

## What belongs and what does not

| Belongs in design/ | Does not belong (put it here instead) |
|---|---|
| Current structure, flows, contracts, data shapes | Why we chose it → decision record |
| Diagrams with their source | Screenshots of whiteboards → retro or nowhere |
| Short examples that clarify a contract | Full code listings → the code itself |
| Links to Figma frames, specs, dashboards | Copied Figma screens, copied specs |
| Who owns what, who holds which credential | Secret values, passwords, keys → secret store, never docs |
| Known limitations of the current design | Task status, TODO lists → plan / tracker |
| | Meeting notes, chat logs → nowhere, or summarized into a decision |
| | Alternatives considered → decision record |

## Writing rules
1. **Link, don't copy.** If it exists elsewhere (spec, Figma, decision record, code), link to it with one line on what to find there.
2. **One home per fact.** Before adding, search `docs/` for the fact. If it exists, update it there and link.
3. **Write for the reader named in Audience.** Overview for newcomers and stakeholders; component sections for engineers.
4. **Respect budgets** (see Size budgets). If a file grows past its budget, split by component or move detail to a linked sub-file, not to an appendix.
5. **Present tense, current state.** No "we will" (that is the plan) and no "we used to" (that is history in decision records).
6. **Diagrams from text.** Use the `diagrams` skill; never paste an image without its source.

## Size budgets

| File | Budget |
|---|---|
| `STATE.md` | One screen, about 40 lines |
| `design/README.md` | One line per file |
| Other `design/*.md` | About 300 lines; past that, split by component into a linked sub-file (add it to `docs/structure.yml` first) |
| `product/` and `project/` files | No limit; finished plans move to `project/archive/` |

## Update triggers
Update the named file in the same PR as the change:

| Change | Update |
|---|---|
| New or superseded decision record | architecture.md, affected diagrams |
| API or data shape change | api.md / api/, data-model.md |
| New screen or flow | ux.md |
| New role, integration, secret or data type | security.md (redo `architecture-decision/rules/security.md` for it) |
| Performance budget or result changes | performance.md |
| Design file added, removed or repurposed | design/README.md (one line per file) |

## Audit (run before each release, or on request)
1. For each `design/` file: is "Last updated" older than the last related decision record or merged change? Mark stale.
2. Find duplicated facts (same table or paragraph in two files). Keep one, link from the other.
3. Find content that belongs elsewhere (see table above) and move it.
4. Check each file is within budget.
5. Report findings as a short list; fix only after a person approves.

## Combined documents
The docs stay split. When one document is needed for a reader (review pack, stakeholder overview, handover), use the `doc-assemble` sub-skill: it selects content per audience from an export spec and builds a snapshot outside `docs/`.

## Handoff
Used by stages 3–7. The `diagrams` skill produces figures; `requirements` owns ux.md, `architecture-decision` owns architecture, data-model, api and security, `quality-review` owns performance.md.
