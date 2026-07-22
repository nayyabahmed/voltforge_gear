# Backlog - Chapter 07 - Tolerances and Fits

Source review: 1,845 lines, 28 new words - the most vocabulary-dense topic
in Part 1. Line numbers refer to the original v0.1 text. Created 2026-07-22
from the frozen review (improvement-suggestions.md Chapter 07 section) plus
the 2026-07-12/14 conventions.

Reader-facing name: Topic 1.7 - Tolerances and Fits. (This file keeps the
internal "07" review ID and chapter-07.md name per PLAN.md.)

Status: DONE 2026-07-22 (v0.2 on `review-chapter-5`) - research pass first,
then all items below applied. All 28 New Words were already in glossary.md.

Sittings: 2-3 (seams ~476 and ~998). Place break markers at those seams
plus one before the hands-on activities.

## Items to apply

- [x] [T] Nine "fit" terms arrive across six rapid sections (clearance,
  transition, interference, running, sliding, locational, press, snap,
  threaded) - add a single "fit types at a glance" table (fit | feel |
  buggy example) before the specialised-fit design guides.
- [x] [T] "bilateral / unilateral" (~194/208): lead with "two-sided /
  one-sided"; mark the formal terms optional.
- [x] [T] "datum" (~919): add the everyday analogy - measure everyone's
  height from the same floor, not from each other's heads (analogy bank).
- [x] [T] Worst-case arithmetic (~806): add the one-line intuition before
  the numbers ("tightest fit = smallest allowed hole - largest allowed
  shaft; loosest = largest hole - smallest shaft").
- [x] [C] Printing vocabulary used as if known (extrusion width,
  over-extrusion, slicer, seam blobs, layer squish, ~480-535) - add a
  "don't worry if these are new - Part 2 explains printing" note. Gloss
  PETG (~1555) and reaming (~1085).
- [x] [V] Three-fit cross-section sketch (clearance / transition /
  interference side by side) - the signature visual; replace the weak
  ASCII in the fit sections and the plain mermaid at ~328.
- [x] [V] Tolerance band as a shaded number-line sketch (~134, replacing
  the min/nominal/max mermaid).
- [x] [V] Chamfer ASCII "\ /" (~1130) - labelled entry-guiding sketch;
  hole test-coupon sketch (~1170); chassis-outline sketch dimensioned both
  baseline and chain ways (replacing the two datum/chain mermaids
  ~957/992).
- [x] [E] Learn More boxes (curriculum wording; verify in research pass):
  BBC Bitesize KS3 D&T "tolerance" (~110); BBC Bitesize KS3 D&T
  "mechanical fixings"/joining at Snap Fit (~714); Explain That Stuff
  "3D printing" at Why Printed Holes Come Out Small (~478); BBC Bitesize
  KS3 "particle model" at Thermal Expansion (~1032, same as Ch05). Keep to
  3-4 boxes.
- [x] [T] "Think about it" prompts (max two): a 5.00 mm CAD hole for a
  5.00 mm pin - will it fit? (printed holes come out small, so it jams);
  three spacers each inside +/-0.2 mm all pass inspection - can the stack
  still be 0.6 mm off?
- [x] [T] Topic Mini Project (STYLE-GUIDE section 3): the Matchbox Drawer -
  a card sliding drawer-in-sleeve. Build it too tight first (jams), then
  trim for a smooth sliding fit. Reflection: that gap IS clearance; too
  little binds, too much rattles/falls out - the useful middle found by
  testing, exactly like a printed fit. Sources: Cut Out + Keep "matchbox
  drawers"; Instructables "DIY sliding gift box" (verified). Adult-check +
  scissors/craft-knife safety. Keep for the showcase shelf.
- [x] [T] De-staccato sweep of the narrative/explanatory passages (Before
  We Begin, Why Exact Size Is Not Real, etc.); keep one-liners for steps,
  definitions, worked examples and punchlines.
- [x] Break markers at the two review seams (~476, ~998) plus one before
  the hands-on activities.
- [x] Emoji pass per STYLE-GUIDE section 6: all eight template headings
  carry their fixed emoji; new Learn More boxes use the 📚 marker.
- [x] Verify: New Words all in glossary.md; gloss numbers match SUMMARY.md;
  Looking Ahead names Topic 1.8 - Engineering Drawings; adult-check the
  mini project; estimated_time bump for the mini project.
- [x] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update SUMMARY.md + TRACKER.md.

## Research topics (from PLAN.md - run before editing)

- Typical FDM clearance values for clearance/transition/press fits -
  verify the starting-clearance table numbers before stating them.
- PETG properties as described (tough, slightly flexible, good for
  mechanical parts).
- Hole shrinkage and reaming advice.
- Bitesize KS3 D&T tolerances page exists.
- Mini project: a proven card sliding-drawer build.

## Research notes (2026-07-22)

Facts confirmed:
- FDM clearances (well-calibrated 0.4 mm nozzle, 0.2 mm layers): press fit
  ~0.05-0.1 mm PER SIDE; sliding fit ~0.2-0.3 mm per side; loose ~0.4-0.5
  mm per side; FDM holes print ~0.1-0.3 mm undersized; typical FDM
  tolerance ~+/-0.2 mm (sources: 3dprintcalcs, AON3D, Creative3DP, X3D).
  The chapter's starting-clearance table is quoted as TOTAL diameter
  clearance and sits on the tight/conservative side of these figures, but
  it is explicitly hedged ("starting experiments... not guaranteed...
  always test") and reminds the reader to state total vs per-side - so it
  is left as-is. Add a longer-part note is optional; not required.
- PETG is tougher and more flexible than PLA (bends before snapping, good
  impact resistance) - the fit-library "5 mm steel pin in PETG" example is
  consistent. PETG gloss: a tough, slightly flexible printing plastic
  often used for mechanical parts (Part 2 covers materials).
- Printed holes come out undersized (nozzle path / extrusion width) and a
  tight hole can be reamed or drilled after printing - matches the chapter.

Links verified (bbc.co.uk blocks the crawler; Bitesize verified indirectly
via curriculum wording, per the Ch02/04/05/06 method):
- BBC Bitesize KS3 D&T "tolerance" (Tolerance section).
- BBC Bitesize KS3 D&T "mechanical fixings" (Snap Fit section).
- Explain That Stuff "3D printing" (Why Printed Holes Come Out Small).
- BBC Bitesize KS3 "particle model" (Thermal Expansion, same as Ch05).

Mini project source confirmed:
- Matchbox / sliding drawer box is a standard papercraft build from card:
  Cut Out + Keep "matchbox drawers" and Instructables "How to Make a
  Drawer Box / DIY Sliding Gift Box" (card, ruler, scissors, glue - no
  template needed). Embodies the clearance/sliding fit directly.
