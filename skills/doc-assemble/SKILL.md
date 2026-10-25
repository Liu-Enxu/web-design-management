---
name: doc-assemble
description: Sub-skill of design-doc. Use when someone needs one combined document from the project docs (design review pack, stakeholder overview, onboarding guide, client handover, security review, release sign-off). Selects what to include per audience and purpose from an export spec, at a chosen depth per source, then builds a versioned snapshot. Never a plain concatenation; never edited by hand.
---

# Doc assemble (combined documents)

Goal: a single document that answers one audience's questions, selected from `docs/` and nothing more. The split files stay the source of truth; the combined doc is a generated snapshot.

## 1. Write or pick an export spec

Every combined document starts from a spec in `docs/project/exports/<name>.md`. Copy a ready profile from `templates/` (or `templates/_spec.md` for a new one) and adjust it to the project.

```markdown
# Export: <name>
Audience: <who reads it> · Purpose: <decision or action it supports>
Owner: <person> · Sensitivity: internal | client | public

## Questions this document must answer
1. 
2. 

## Selection
| Source | Depth | Filter |
|---|---|---|
| product/stories.md | summary | Must stories, current release |
| decisions/ | key table | accepted, one-way |
| design/architecture.md | full | |
| design/security.md | omit | |

## Never include
- 

## Order
1. <section>
```

## 2. Depth levels

| Depth | What goes in | Use when |
|---|---|---|
| **full** | The section as written | The reader must act on the details |
| **summary** | A short summary written for this audience, with a link to the source | The reader needs the point, not the detail |
| **key table** | Only selected rows or columns (for example Must FRs, accepted one-way decisions) | The reader needs a checklist or overview |
| **link** | One line saying what the source contains, and where | Useful to some readers, not needed to read through |
| **omit** | Nothing | Not relevant or not allowed for this audience |

## 3. Filters

Apply before writing: priority (Must / Should), status (accepted, not superseded; `ready` screens), release slice or milestone, date range, ID list. State the filters in the document's front matter so readers know what was left out.

## 4. Profiles (starting points, ready to copy from `templates/`)

| Profile | Audience | Questions it answers | Includes (depth) | Never includes |
|---|---|---|---|---|
| **Design review** | Engineers, reviewers | Is the design sound? What are the risks? | stories (summary), requirements (key table: Must + all NFRs), decisions (full: one-way), architecture, data model, API (full), security threats (key table), risks (key table) | credential register, task status |
| **Stakeholder overview** | Management, sponsors | What are we building, by when, at what risk? | stories (summary by epic), scope in/out (full), release slices, plan milestones (key table), top risks (key table), architecture (container diagram only) | API, data model, security details, credentials |
| **Onboarding** | New team members | How does it work, where do I start? | design overview, architecture (full), decisions (key table: all accepted), code layout (from code-organization decision) | risks, change log, credentials |
| **Client handover** | Client or operator taking over | How do we run, change and support it? | scope, architecture, API (link to spec), roles (key table, no names unless agreed), decisions (key table) | internal risks, retros, credential register (hand over secrets through the secret manager, never in the doc) |
| **Security review** | Security reviewer, auditor | What can go wrong and what protects it? | trust-boundary diagram, threats (full), roles and environment access (full), credential register (owners and storage only), auth decisions (full), data sensitivity (key table) | secret values (always) |
| **Release sign-off** | Approver of a release | Is this release ready? | release file (full), Must FRs with test status (key table), security re-check, performance budgets (key table), open risks (key table) | design detail beyond what changed |

## 5. Build steps
1. Read the spec. If a question in it has no source in `docs/`, report it as a gap; do not invent content.
2. For each source, apply the filter, then the depth. Write summaries for the stated audience; every summary links to its source.
3. Re-check **Never include** and the sensitivity level. Security and credential content defaults to omit for anything above `internal`.
4. Add front matter: title, version or commit, date, audience, filters applied, list of sources with their "Last updated" dates.
5. Render diagrams from their Mermaid sources.
6. Output to a build folder that is not part of `docs/` (for example `build/docs/<name>-<version>.md`, then PDF or Word via a converter). Link the snapshot from the release file; do not commit it into `docs/`.
7. Ask the spec owner to approve before it is sent.

## Rules
- Fix errors in the source files, then rebuild. Never edit the snapshot.
- One spec per recurring document; a one-off request still gets a spec, so it can be rebuilt.
- If the combined doc needs content that exists nowhere in `docs/`, that is a missing source: add it to the right folder first (per `design-doc`).
