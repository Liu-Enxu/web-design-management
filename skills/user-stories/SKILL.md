---
name: user-stories
description: Stage 1 of the team workflow. Use to collect, write, group and relate user stories for a project or feature, including personas, acceptance criteria and story relationships. Use when the team is discussing ideas, needs or "what should this do". Writes docs/product/stories.md.
---

# User stories (stage 1)

Goal: a shared, written picture of who the users are and what they need, before anyone talks about solutions or technology.

## Entry criteria
- A project or feature name, and at least one person who can speak for users.

## Steps

1. **Personas.** List the user types (2–5 is normal). For each: name, goal, context, what they do today without this product.
2. **Collect stories.** Run an open discussion. Capture every need as a story, even rough ones. Do not judge or rank yet.
   Format: `As a <persona>, I want <capability>, so that <outcome>.`
3. **Clean each story.** Check against INVEST:
   - Independent, Negotiable, Valuable, Estimable, Small, Testable.
   Split stories that hide several needs. Merge duplicates. Rewrite solution-flavored stories ("I want a dropdown") into needs ("I want to pick a jurisdiction quickly").
4. **Acceptance criteria.** For each story, 1–5 criteria in Given/When/Then form. If you cannot write a criterion, the story is not understood yet: add an open question instead.
5. **Group into epics.** An epic is a theme of related stories (for example "search", "reporting", "admin").
6. **Relate stories.** Record relationships explicitly:
   - `depends-on`: B cannot work without A.
   - `conflicts-with`: satisfying A makes B harder (note the tension).
   - `refines`: B is a more specific version of A.
   - `duplicates`: merge, keep one ID.
7. **Map the journey (optional, recommended for 10+ stories).** Order epics along the user's journey, and list the stories under each step. This shows gaps.
8. **Open questions and assumptions.** Anything unknown about users goes here, with an owner.

## Decision points
- **Story granularity:** if a story needs more than about a week of work to deliver, split it.
- **Who speaks for users:** name the person per persona. Stories without a source are marked `assumption`.

## Rules
- No technology words in stories (no "database", "API", "React"). Those belong in stages 2–3.
- IDs are permanent: `US-001`, `US-002`… Deleted stories are marked `dropped`, never reused.
- Bugs (wrong behavior in something already built) go in the Bugs section as `BUG-001`, `BUG-002`…, linked to the story they break.
- Discussion of ideas is welcome here; record outcomes as stories, open questions or explicit "not doing" notes.

## Output: docs/product/stories.md

```markdown
# User stories: <project>

## Personas
| ID | Persona | Goal | Context | Source (who speaks for them) |
|---|---|---|---|---|
| P1 | | | | |

## Epics
- E1 <name>: <one line>

## Stories
### US-001 <short title>
- Epic: E1 · Persona: P1 · Status: draft | agreed | dropped | assumption
- Story: As a …, I want …, so that …
- Acceptance criteria:
  - Given …, when …, then …
- Relations: depends-on US-00x; conflicts-with US-00y (<tension>)
- Source: <interview, ticket, person>

## Relationship map
| Story | Relation | Story | Note |
|---|---|---|---|

## Bugs
### BUG-001 <short title>
- Breaks: US-00x · Status: open | fixed | won't fix
- What happens: …
- What should happen: …
- Steps to reproduce: 1. … 2. …
- Source: <reporter, ticket>

## Open questions and assumptions
| ID | Question | Owner | Due |
|---|---|---|---|

## Not doing (and why)
- 
```

## Gate checklist
- [ ] Every persona has a named source.
- [ ] Every agreed story has acceptance criteria.
- [ ] Relationships recorded; conflicts have a note.
- [ ] Open questions have owners.
- [ ] A person approved in docs/STATE.md.

## Handoff
→ `requirements`. Stories with status `agreed` are the input; `assumption` stories carry forward with a risk flag.
