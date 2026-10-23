# Rules: UX and art direction

Used in stage 2, part D. Output: `docs/design/ux.md` plus frames in Figma (or the team's design tool).

## 1. Screens and flows
- For each Must epic: the path a persona takes from entry to outcome, including error and exit paths (user-flow diagram, `diagrams` skill).
- Screen index with an ID per screen (`S-01`…), linked to stories.

## 2. Art direction
**If the team supplies one** (brand guide, reference products, an existing Figma library): record it in `ux.md` and use it.

**If there is none**, the agent proposes 2–3 directions. Each direction:
- mood in 3 words (for example "calm, precise, editorial");
- palette (primary, neutral, accent, success / warning / error) with contrast checked;
- typography (heading and body fonts, size scale);
- component library to start from;
- 2–3 reference products that look this way;
- one key screen sketched in that direction.

A named person picks one. Record the choice and why in `ux.md`.

## 3. Fidelity (pick per screen)
| Level | Use when |
|---|---|
| Sketch / low-fi (default start) | Flow and layout not agreed |
| Mid-fi wireframe | Layout agreed, content uncertain |
| High-fidelity | Layout and content agreed |
| Interactive prototype | Usability is risky or must be tested |

## 4. Design system
| Option | Use when |
|---|---|
| **Existing component library, lightly themed (default)** | Internal tools, small teams, speed matters |
| Library + custom tokens and a few custom components | Brand matters, team is small |
| Custom design system | Several products share one brand, dedicated designers |

Tokens (color, type, spacing) are defined once in the library, not per screen.

## 5. Figma first, then code
1. Design each Must screen in Figma with **all states**: default, loading, empty, error, no permission, partial data, long content.
2. Frames: one page per epic; frame names start with the screen ID (`S-04 Search results / empty`); status on every frame: `exploring` → `in review` → `ready` → `built`.
3. If a Figma connection (MCP or API) is available, agents may create draft frames from the chosen direction and read `ready` frames and tokens; they edit only frames marked `exploring` unless asked.
4. Implementation generates code from `ready` frames and runs it end to end; the result is compared with the frame in review.
5. `ux.md` holds the index, flows, decisions and **links to frames**. Never paste screens into the docs.

## 6. Handoff checklist (per screen, before `ready`)
- [ ] Linked to stories (US-xxx) and requirements.
- [ ] All states designed.
- [ ] Uses library components and tokens; new components flagged.
- [ ] Responsive behavior or breakpoints specified.
- [ ] Copy final or marked as placeholder.
- [ ] Accessibility: contrast, keyboard path, focus order, labels.
- [ ] Data shown is covered by the data requirements in `requirements.md` (matched to the API in stage 3).

## Output: docs/design/ux.md

```markdown
# UX
Owner: · Audience: developers, product · Last reviewed:
Sources: product/stories.md, Figma <file link>

## Art direction
<chosen direction, or link to brand guide; why>

## Design system
<library and link>

## Flows
<Mermaid user flows>

## Screen index
| ID | Screen | Stories | Figma frame | Status |
|---|---|---|---|---|
| S-01 | | US-001 | <link> | ready |
```
