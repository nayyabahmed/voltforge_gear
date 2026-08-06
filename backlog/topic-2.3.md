# Backlog - Topic 2.3 - Slicer Software and First Prints

Source: audit of the v0.1 text (1,172 lines, 15 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **DONE 2026-08-06** (v0.2 on `Part_2_review`). Research pass first,
then every item below applied. First topic of Phase 2; Topic 2.4 next.

Sittings: 3. The only long Part 2 topic still inside the 700-1,200 line
target, but two break markers is one or two short for its length. Seams:
"The Preview Is an X-Ray of the Future Print" (~444), "The First-Print
Launch Routine" (~548), and one before the activities (~819).

## Items to apply

- [x] [C] **No forward glosses at all.** The topic uses Part 3 vocabulary as
  if taught: "battery tray" and "servo mount" (~50), "servo mount" again at
  ~278 and ~310. Add first-use glosses with home topics per `SUMMARY.md`
  (servo 3.5, batteries 3.3).
- [x] [T] **Add one or two break markers** at the seams above. The stretch
  from "The First-Print Launch Routine" (~548) to the activities (~819) is
  the longest unbroken run in the topic and covers the highest-stakes
  material.
- [x] [T] **Only one "Think about it" prompt.** Add a second at
  "Orientation: The First Design Decision" (~294) - the reader will not
  predict that rotating a part changes its strength rather than just its
  looks, and the U-shaped servo mount example at ~310 already sets it up.
  "Files from the Internet Are Not Instructions" (~631) is the alternative.
- [x] [E] **One Learn More box in 1,172 lines.** Add up to two more, inline,
  next to the sections they serve: official slicer documentation at
  "Download from the Official Source" (~130) and a first-layer / bed
  adhesion reference at "Watch the First Layer" (~688). Manufacturer
  knowledge bases (Prusa, Bambu) are approved sources and are the right fit
  here.
- [x] [V] **Figures: 4 against a budget of 10-14** (STYLE-GUIDE 7.4,
  skill topic). At 1,172 lines the topic currently runs one figure per
  ~293; the target is one per 40-80. This is the largest single item in
  this file. See `references/ref-002.md` for the taxonomy.
  The `[Signature visual:` at ~457 already covers the slicer preview well -
  leave it. Gaps: "Orientation" (~294) beyond the existing sketch, "The Seam"
  (~425), "Bed Adhesion Helpers" (~385) as an F7 skirt/brim/raft array, and
  "Removing and Inspecting the Print" (~723).
  Conventions to apply to every figure, existing ones included (7.2/7.3):
  type tag `[F1-F7 ...]`, `Figure 2.3.k` number, a one-sentence caption
  saying what to notice, and alt text.
- [x] [V] **F3 pairs for the 10 Common Beginner Mistakes.** The highest-value
  figure type in the book and currently unused here - a right-versus-wrong
  pair per mistake, or one combined F3 array. Prose alone cannot show a
  reader what the wrong version looks like.
- [x] [T] **Add `# Answers 🔑`** (STYLE-GUIDE 3 item 15, 13.3) with model
  answers numbered to match the 12 Review Questions. Needed for the HTML
  reveal and for a mentor running a session.
- [x] [T] **Check the estimate section (~495) has a fully worked example.**
  Style guide section 2 requires any maths to show question, known values,
  rule, calculation, then the meaning in words. Verify the print-time and
  filament-cost estimates follow that shape.
- [x] [C] **Printing vocabulary defined here vs in 2.2.** "Wall",
  "perimeter", "seam", "island" and "travel move" are this topic's New
  Words, but some are used in Topic 2.2. Confirm 2.2 either glosses them
  forward to 2.3 or avoids them, so first use and formal definition line up
  across the two topics.
- [x] Verify: all 15 New Words in `glossary.md` (they are, as of `4074569`);
  Looking Ahead names Topic 2.4 (it does); every activity has a no-equipment
  variant (Activities 1-3 are equipment-free, Activity 4 is the controlled
  first print); mini project keeps its adult-check line and Watch-the-build
  box.
- [x] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

- **Slicer UI churn - the big one.** The topic names slicers, menus,
  buttons and profile names throughout. Re-verify every named control and
  every version claim against the current releases of Bambu Studio,
  OrcaSlicer, PrusaSlicer and Cura. Anything that has moved must be
  described by function rather than by menu path.
- "Download from the Official Source" (~130): confirm the official download
  locations named are still correct, and that the advice matches current
  guidance on avoiding repackaged installers.
- Temperature, speed and layer-height defaults quoted anywhere in the core
  settings sections (~318-425) - verify against manufacturer profiles.
- Bed adhesion helpers (~385): skirt, brim and raft advice.
- Feed `TROUBLESHOOTING.md` from "When a Print Fails" (~797) - that
  document currently has no Topic 2.x references at all and this is its
  most natural source in the whole part.
- Mini project: re-verify the Watch-the-build sources for the Laminated
  Cardboard Cable Guide still exist.

## Research notes (2026-08-06)

**Facts confirmed:**

- All four slicers in the table are still current in 2026, all free, all
  open source: Bambu Studio, PrusaSlicer (2.9.4 stable, 3.0 in pre-release),
  UltiMaker Cura (300+ machine profiles) and OrcaSlicer. The table's
  "start with the one your manufacturer recommends" advice holds.
- The worked example at "Estimate Before You Print" was already complete and
  correct: question, known values, rule, calculation, meaning. 18 g of a
  1 kg spool at GBP 20 is GBP 0.36. No change needed.

**The UI-churn research item resolved itself.** The backlog asked for every
named control to be re-verified against current releases. The topic
deliberately does not name controls - "This topic teaches that journey rather
than one exact set of buttons" - so there is nothing version-specific to rot.
That is a deliberate authoring choice and a good one; recorded as considered
and kept, rather than an item to fix. The same approach is worth copying in
Topic 2.4, where CAD tools churn just as fast.

**Notes:**

- Figures went from 4 to 13, which needed two renumbering passes because the
  new ones were not inserted in document order. Worth doing the numbering
  pass last on the remaining topics.
- Both Mermaid blocks were checked against the visuals policy and both are
  genuine flows (the slicer's decision inputs, and the five launch gates).
  Kept as F0 and numbered, unlike the spatial Mermaid deleted in 2.1 and 2.2.
- OrcaSlicer is now widely described as the strongest all-round slicer, but
  the topic's framing - "better after you know the basics" - is right for an
  11-year-old on a first print. Kept deliberately.
