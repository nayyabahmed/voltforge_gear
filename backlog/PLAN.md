# Part 1 Review - Implementation Plan

Plan for upgrading the Part 1 chapters (00-09 + capstone) from v0.1 "Draft"
to v0.2 "Reviewed" by applying the readability backlog. Work happens on the
`review` branch, one chapter at a time, one commit per chapter.

Sources: `style-guides-principles/STYLE-GUIDE.md` (the rules),
`style-guides-principles/improvement-suggestions.md` (the original review,
2026-07-11, now frozen), `style-guides-principles/GUIDING-PRINCIPLES.md`.
The working copies of the backlog items live in this folder - tick items
here as they are applied.

---

## Current State (as of 2026-07-12)

| Chapter | File | Status | Backlog file |
| --- | --- | --- | --- |
| 00 How to Use This Handbook | `00-...md` | v0.2 done (dd772e8) | none (not in review scope) |
| 01 What Are We Building? | `01-...md` | v0.1, no backlog exists | to be generated (see Phase 4) |
| 02 Systems Thinking | `02-...md` | bumped to v0.2 but ~half applied | [chapter-02.md](chapter-02.md) |
| 03 How Machines Move | `03-...md` | not started | [chapter-03.md](chapter-03.md) |
| 04 Forces and Why Parts Break | `04-...md` | not started | [chapter-04.md](chapter-04.md) |
| 05 Measurement | `05-...md` | not started | [chapter-05.md](chapter-05.md) |
| 06 Accuracy, Precision and Error | `06-...md` | bumped to v0.2 but ~half applied | [chapter-06.md](chapter-06.md) |
| 07 Tolerances and Fits | `07-...md` | not started | [chapter-07.md](chapter-07.md) |
| 08 Engineering Drawings | `08-...md` | bumped to v0.2 but ~half applied | [chapter-08.md](chapter-08.md) |
| 09 The Engineering Design Process | `09-...md` | not started | [chapter-09.md](chapter-09.md) |
| Part 1 Capstone | `Part-1-Capstone-...md` | not started | [capstone.md](capstone.md) |
| Glossary | `glossary.md` | one of two items done | [glossary.md](glossary.md) |
| Book-wide items | (all chapters) | applied per chapter as we go | [book-wide.md](book-wide.md) |

Note: the original review calls the capstone "Chapter 10" - numbering has
since changed (Chapter 10 is now Part 2's Workshop Safety). Backlog gloss
pointers written against the old numbering must be re-verified against
`SUMMARY.md` before use (e.g. ESC's home chapter is 25, not 22).

## Order of Work

Finish the half-done chapters first so their "Reviewed" status becomes
honest, then take the rest in numeric order.

1. **Phase 1 - finish the partials:** Chapter 02, Chapter 06, Chapter 08.
2. **Phase 2 - untouched chapters, numeric order:** Chapter 03, Chapter 04,
   Chapter 05, Chapter 07, Chapter 09, Capstone.
3. **Phase 3 - cross-chapter sweep:** glossary items, terminology
   reconciliation (book-wide.md), and a final check that every applied gloss
   points at the correct chapter number per `SUMMARY.md`.
4. **Phase 4 - Chapter 01:** it was never reviewed, so review it against the
   style guide first, write its backlog file here, then apply it.

## Per-Chapter Loop (definition of done)

For each chapter, in this order:

1. Read the chapter and its backlog file in this folder.
2. **Research pass** (before any editing) - the chapter's topics are listed
   in "Research Topics by Chapter" below:
   a. Web-verify the chapter's technical claims, especially anything about
      safety, temperatures, materials, tolerances or standards ("verify
      before citing", CLAUDE.md). Check safety statements stay consistent
      with `SAFETY.md`.
   b. Confirm every planned "Learn More" source exists and the suggested
      search term actually surfaces the intended page; keep the
      "search X on site Y" form.
   c. Check explanations are pitched right by comparing against how the UK
      KS2/KS3 curriculum introduces the same idea (Bitesize is the
      reference).
   d. Record findings as a short "Research notes" section at the bottom of
      the chapter's backlog file: facts confirmed, facts corrected, links
      verified, anything deferred. This is the traceability record.
3. Apply the items: first-use glosses, de-staccato story passages, visuals
   (sketch placeholders per STYLE-GUIDE section 7), Learn More boxes,
   break markers at the listed seams - correcting any facts the research
   pass flagged.
4. Apply any book-wide items that touch this chapter (see book-wide.md).
5. Verify: `rg -n '[^\x00-\x7F]'` is clean outside mermaid/notation,
   every gloss chapter number matches `SUMMARY.md`, "Looking Ahead" names
   the real next chapter, New Words entries exist in `glossary.md`.
6. Set frontmatter `version: "0.2"` / `status: "Reviewed"` (only now).
7. Tick the chapter's items in its backlog file (and in book-wide.md where
   relevant).
8. Update the chapter's row in `SUMMARY.md` (v0.1 yellow -> v0.2 blue).
9. Commit: one chapter per commit, message like
   `Apply Part 1 review to Chapter 05 (v0.2)`.

## Research Topics by Chapter

What the research pass (loop step 2) must check per chapter. Add topics as
they surface; strike nothing - mark it done in the Research notes instead.

- **Chapter 02 - Systems Thinking:** confirm BBC Bitesize KS3 D&T
  "systems and control" and control/feedback pages exist; sanity-check the
  input-process-output framing against how Bitesize teaches it; confirm
  "2-cell battery" wording matches how Chapter 22 will teach cells.
- **Chapter 03 - How Machines Move:** torque/moments at KS3 level; PhET
  "Forces and Motion: Basics" simulation exists; Explain That Stuff "gears"
  article exists; realistic pinion/spur tooth counts for a 1/10 buggy (is
  10T/40T plausible); correct plain-language statement of Newton's third
  law; friction and momentum resources.
- **Chapter 04 - Forces and Why Parts Break:** elastic vs plastic
  deformation and fracture pitched to KS3; layer adhesion/anisotropy facts
  for FDM prints (verify against Prusa/Bambu knowledge bases); fatigue
  basics; kid-friendly structures/bridges resource; a 3D-printing explainer
  suitable for the print-orientation section.
- **Chapter 05 - Measurement:** UK KS2/KS3 units and scale-reading pages
  exist (units of length, mm/cm/m conversion, reading scales, parallax);
  correct caliper technique description; thermal expansion facts and a
  matching Bitesize page.
- **Chapter 06 - Accuracy, Precision and Error:** Bitesize "accuracy and
  precision" and "errors in measurement" pages (already cited in dd772e8 -
  re-verify); zero-error description matches real caliper behaviour;
  mean/median/mode/range and rounding pages exist.
- **Chapter 07 - Tolerances and Fits:** typical FDM clearance values for
  clearance/transition/press fits (verify against Prusa/Bambu guidance
  before stating numbers); PETG properties as described; hole shrinkage and
  reaming advice; Bitesize KS3 D&T tolerances page exists.
- **Chapter 08 - Engineering Drawings:** which projection convention the UK
  actually uses (first-angle, per BS 8888) so the deferral text stays
  truthful; countersink vs counterbore definitions; Bitesize "isometric and
  orthographic drawing" page; a beginner drawing-reading tutorial worth
  citing.
- **Chapter 09 - The Engineering Design Process:** Bitesize KS3 D&T
  iterative design page; KS2/KS3 "fair testing and variables" pages (must
  map onto the chapter's independent/dependent/control wording);
  data-recording resources.
- **Capstone - First Engineering Challenge:** Tinkercad Learn and Onshape
  Learning Centre still offer beginner CAD paths; a cardboard-prototyping
  maker resource; sanity-check any component dimensions the packaging
  exercise quotes (ESC, receiver, servo sizes).
- **Chapter 01 (Phase 4) and every chapter:** verify each Learn More search
  term surfaces the intended page; cross-check safety-adjacent statements
  against `SAFETY.md`.

## Standing Decisions

- **Chapter 04 split:** the review calls it the strongest split candidate,
  but a real split would renumber every later chapter and break gloss
  pointers book-wide. Decision: keep it one file with explicit "Part A /
  Part B" headings, break markers at the seam, and a mid-chapter recap
  table. Revisit a true split only if the whole book is ever renumbered.
- **Version bumps:** a chapter moves to 0.2/"Reviewed" only in the commit
  that completes its backlog. Chapters 00/02/06/08 were bumped early in the
  WIP commit; rather than revert, Phase 1 finishes them first.
- **Visuals:** no new ASCII art. Weak ASCII/mermaid is replaced by sketch
  placeholders (spatial ideas) or tables (comparisons) per the visuals
  policy. Each chapter keeps one signature visual for its hardest idea.
- **Line numbers in backlog items** refer to the original v0.1 text and
  drift as edits land - treat them as approximate locators.
- `improvement-suggestions.md` stays untouched as the frozen review record;
  this folder is the single working copy for progress tracking.
