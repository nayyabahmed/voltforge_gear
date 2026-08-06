# Backlog - Topic 2.4 - CAD Fundamentals

Source: audit of the v0.1 text (1,510 lines, 15 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 2 of the Part 2 review.

Sittings: 4. Over the length target by ~300 lines; three break markers is
one or two short. Seams: "Two Ways to Build a Solid" (~330), "Your First CAD
Part - A Two-Hole Mounting Plate" (~737), and one before the activities
(~1063).

## Items to apply

- [ ] [C] **Wrong gloss number - confirmed.** ~661 reads "Start with the
  packaging envelope from Topic 1.2". Packaging envelope is taught in Topic
  1.5 (Measurement) and used again in the Part 1 Capstone; Topic 1.2 is
  Systems Thinking. Fix to Topic 1.5 and re-check every other backward
  pointer in the topic against `SUMMARY.md`.
- [ ] [C] **No forward glosses at all.** "battery trays, electronics mounts,
  servo brackets, bumpers and adapters" (~65) is the offending cluster.
  Gloss on first use with home topics per `SUMMARY.md` (servo 3.5,
  batteries 3.3).
- [ ] [V] **Three placeholders across 1,510 lines, in the most spatial
  subject in Part 2.** The hardest idea is already covered: the `[Signature
  visual:` at ~540 is a four-panel constrained-sketch sequence, which serves
  the under/fully/over-defined material at ~485. The remaining gaps are the
  foundational ones a reader meets first:
  - "X, Y and Z" (~255) - the axes as they appear on screen.
  - "Workplanes" (~285) - a sketch sitting on a plane through a solid.
  - "Extrusion: Giving a Sketch Thickness" (~520) - flat profile to solid.
- [ ] [T] **Add one or two break markers** at the seams above. The guided
  build from ~737 to ~1063 is a single long run of instructions.
- [ ] [E] **One Learn More box in 1,510 lines.** Tinkercad Learn and the
  Onshape Learning Centre are both approved sources and both belong here -
  place them inline next to "Choosing a CAD Tool" (~159), not in a trailing
  block. A third at "Save Revisions, Not Mystery Copies" (~697) would suit
  if a good version-control-for-beginners reference verifies.
- [ ] [T] **Two "Think about it" prompts already present** - confirm they
  sit at the genuinely counter-intuitive claims. "Design Intent" (~452) is
  the topic's best candidate if one needs relocating: why two models that
  look identical behave differently when a dimension changes.
- [ ] [T] **Check the maths sections have fully worked examples.** The
  two-hole mounting plate (~737 onwards) and the parameters section (~586)
  both involve numbers; style guide section 2 wants question, known values,
  rule, calculation, meaning in words.
- [ ] [T] **Path A / Path B structure** (~792 and ~856) splits the guided
  build by CAD tool type. Confirm both paths reach the same artifact and
  that a reader on either path can follow "Inspect Before Exporting"
  (~944) onwards without gaps.
- [ ] Verify: all 15 New Words in `glossary.md` (they are); Looking Ahead
  names Topic 2.5 (it does); every activity has a no-equipment variant
  (Activity 1 "Human Coordinates" and Activity 2 "The Constraint Puzzle"
  are equipment-free); mini project keeps its adult-check line and
  Watch-the-build box.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

- **CAD tool churn - the big one.** "Choosing a CAD Tool" (~159) and both
  guided paths name tools, menus and free tiers. Re-verify for Tinkercad,
  Onshape and FreeCAD: that each still exists, what its current free or
  educational tier actually allows, whether an account or age minimum
  applies, and whether the named controls still carry those names. Onshape's
  free plan makes documents public - confirm the topic says so, because it
  matters for a child's work.
- STEP and 3MF export claims (~1003) - confirm what each format preserves
  and that the recommended export route is current.
- "Units First" (~307) - confirm the advice about setting units before
  modelling matches how the named tools actually behave.
- Whether a Bitesize KS3 D&T page covers CAD or computer-aided design in
  curriculum wording, for a Learn More box.
- Mini project: re-verify Watch-the-build sources for the Dimension-Driven
  Workshop Phone Stand. Note Topic 1.9's mini project was also a cardboard
  phone stand - confirm this one is clearly different in aim (dimension-
  driven CAD, not the design cycle) or change it.

## Research notes

(To be filled during the pass.)
