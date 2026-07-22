# Backlog - Chapter 08 - Engineering Drawings

Source review: 1,569 lines. Line numbers refer to the original v0.1 text.
Created 2026-07-22 from the frozen review (improvement-suggestions.md
Chapter 08 section) plus the 2026-07-12/14 conventions.

Reader-facing name: Topic 1.8 - Engineering Drawings. (Internal "08"
review ID kept per PLAN.md.)

Status note: bumped to v0.2 "Reviewed" EARLY in dd772e8 with ~half applied
(a Phase 1 partial). Already-applied work is recorded [x] below; remaining
items are [ ]. Frontmatter is already 0.2 and stays so.

Sittings: really three topics stitched together; seams after Isometric
Views (~490) and after Surface Finish/Material (~850).

## Already applied in dd772e8 (verified present)

- [x] [V] View-alignment three-view sketch (~273) - the review's top
  visual priority; replaces the weak ASCII.
- [x] [T] First/third-angle projection explicitly deferred ("pick one,
  label it in the title block, keep it consistent"). Research confirms
  this is the right call: BS 8888 vs the Europe-first/US-third convention
  is genuinely muddy, so deferring avoids stating a wrong UK default.
- [x] [T] "Design intent" short version added early (~94), with a pointer
  to the full section near the end.
- [x] [C] "interfaces" glossed on first use (~91, "places where parts
  connect - remember Topic 1.2").
- [x] [E] Learn More (isometric/orthographic) present (needs the 📚 marker).

## Remaining items - all applied 2026-07-22

- [x] [V] Keep the line-type ASCII snippets (they work) but add a "line
  types at a glance" table (visible / hidden / centre - look + meaning).
- [x] [V] Section views (~369): replace the process mermaid with a
  labelled sketch (outside view + cut plane + hatched section).
  Countersink vs counterbore (~637): add a side-by-side comparison table.
- [x] [C] Gloss on first use: tolerance stack-up (~575, back-ref to Topic
  1.7), heat-set insert (~692), nut trap (~392), STL/CAD (~1012, "covered
  in Part 2").
- [x] [T] Reference dimension (~536): show the bracket convention "(50)".
- [x] [E] Add the 📚 marker to the existing Learn More box; add a second
  Learn More at Section Views (Onshape Learning Centre "drawings",
  approved source).
- [x] [C] Add "first-angle / third-angle projection" to glossary.md
  (the section stays).
- [x] [T] "Think about it" prompts (max two): the cup that is a rectangle
  from the side and a circle from above (why one view is not enough);
  dimensioning the same width in two views, then changing one (why a
  feature gets one controlling dimension).
- [x] [T] Topic Mini Project: the Blueprint Challenge - build a small
  object from card or bricks, draw it in three aligned views with
  dimensions, then hand ONLY the drawing to someone who rebuilds it and
  compare. Embodies "a drawing lets another person build without asking".
  Adult-check + scissors safety. Keep drawing + both builds for the shelf.
- [x] [T] De-staccato sweep of narrative passages; keep one-liners for
  steps, callout definitions and worked callouts.
- [x] Break markers at the two seams (~490 after Isometric Views, ~850
  after Material) plus one before the hands-on activities.
- [x] Emoji pass: all eight template headings carry their fixed emoji.
- [x] Verify: New Words in glossary.md; gloss numbers match SUMMARY.md;
  Looking Ahead names Topic 1.9 - The Engineering Design Process;
  adult-check the mini project; estimated_time bump.
- [x] Final pass: verify checklist, tick rows here, update SUMMARY.md
  status (already v0.2) + TRACKER.md.

## Research notes (2026-07-22)

Facts confirmed:
- Countersink = cone-shaped recess for angled/flat screw heads; counterbore
  = flat-bottomed cylindrical recess for socket-head cap screws, washers,
  nuts or a bearing shoulder (sources: Xometry, Wevolver, Rockler). The
  chapter's definitions and CSK/C'BORE callouts are correct.
- First-angle vs third-angle: genuinely ambiguous for the UK (BS 8888:2006
  is cited for third-angle as the modern UK default, while first-angle is
  the traditional Europe/UK convention and third-angle the US one). The
  chapter deliberately does NOT claim a UK default and tells the reader to
  pick one and label it - the safest, truthful framing. Leave as-is.

Links verified (bbc.co.uk blocks the crawler; Bitesize via curriculum
wording per the Ch02/04/05/06/07 method):
- BBC Bitesize KS3 D&T "isometric and orthographic drawing" (kept).
- Onshape Learning Centre "drawings" - beginner walkthrough of turning a
  3D model into a dimensioned drawing (approved source; Section Views).

Mini project:
- The Blueprint / drawing-exchange challenge is a standard technical-
  drawing teaching exercise (cf. TeachEngineering "Seeing All Sides:
  Orthographic Drawing"). Needs only household materials + paper.
