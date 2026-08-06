# Backlog - Topic 2.3 - Slicer Software and First Prints

Source: audit of the v0.1 text (1,172 lines, 15 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 2 of the Part 2 review.

Sittings: 3. The only long Part 2 topic still inside the 700-1,200 line
target, but two break markers is one or two short for its length. Seams:
"The Preview Is an X-Ray of the Future Print" (~444), "The First-Print
Launch Routine" (~548), and one before the activities (~819).

## Items to apply

- [ ] [C] **No forward glosses at all.** The topic uses Part 3 vocabulary as
  if taught: "battery tray" and "servo mount" (~50), "servo mount" again at
  ~278 and ~310. Add first-use glosses with home topics per `SUMMARY.md`
  (servo 3.5, batteries 3.3).
- [ ] [T] **Add one or two break markers** at the seams above. The stretch
  from "The First-Print Launch Routine" (~548) to the activities (~819) is
  the longest unbroken run in the topic and covers the highest-stakes
  material.
- [ ] [T] **Only one "Think about it" prompt.** Add a second at
  "Orientation: The First Design Decision" (~294) - the reader will not
  predict that rotating a part changes its strength rather than just its
  looks, and the U-shaped servo mount example at ~310 already sets it up.
  "Files from the Internet Are Not Instructions" (~631) is the alternative.
- [ ] [E] **One Learn More box in 1,172 lines.** Add up to two more, inline,
  next to the sections they serve: official slicer documentation at
  "Download from the Official Source" (~130) and a first-layer / bed
  adhesion reference at "Watch the First Layer" (~688). Manufacturer
  knowledge bases (Prusa, Bambu) are approved sources and are the right fit
  here.
- [ ] [V] **Figures: 4 against a budget of 10-14** (STYLE-GUIDE 7.4,
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
- [ ] [V] **F3 pairs for the 10 Common Beginner Mistakes.** The highest-value
  figure type in the book and currently unused here - a right-versus-wrong
  pair per mistake, or one combined F3 array. Prose alone cannot show a
  reader what the wrong version looks like.
- [ ] [T] **Add `# Answers 🔑`** (STYLE-GUIDE 3 item 15, 13.3) with model
  answers numbered to match the 12 Review Questions. Needed for the HTML
  reveal and for a mentor running a session.
- [ ] [T] **Check the estimate section (~495) has a fully worked example.**
  Style guide section 2 requires any maths to show question, known values,
  rule, calculation, then the meaning in words. Verify the print-time and
  filament-cost estimates follow that shape.
- [ ] [C] **Printing vocabulary defined here vs in 2.2.** "Wall",
  "perimeter", "seam", "island" and "travel move" are this topic's New
  Words, but some are used in Topic 2.2. Confirm 2.2 either glosses them
  forward to 2.3 or avoids them, so first use and formal definition line up
  across the two topics.
- [ ] Verify: all 15 New Words in `glossary.md` (they are, as of `4074569`);
  Looking Ahead names Topic 2.4 (it does); every activity has a no-equipment
  variant (Activities 1-3 are equipment-free, Activity 4 is the controlled
  first print); mini project keeps its adult-check line and Watch-the-build
  box.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
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

## Research notes

(To be filled during the pass.)
