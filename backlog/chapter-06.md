# Backlog - Chapter 06 - Accuracy, Precision and Error

Source review: 1,407 lines. Line numbers refer to the original v0.1 text.
Created 2026-07-21 from the frozen review (improvement-suggestions.md
Chapter 06 section) plus the 2026-07-12/14 conventions.

Status note: this chapter was bumped to v0.2 "Reviewed" EARLY in WIP commit
dd772e8 with only ~half its items applied (a Phase 1 partial). The already-
applied work is recorded below as [x] so this file is the honest record; the
remaining items are the [ ] entries. Frontmatter is already 0.2 and stays so.

Sittings: the review suggests a break after Outliers (~717) or after
Validation (~810). Place two or three break markers during the pass.

## Already applied in dd772e8 (verified present)

- [x] [V] Four-dartboard 2x2 labelled sketch near the opening (signature
  visual) - present, replaces the weak opening mermaid.
- [x] [T] "Before We Begin" de-staccato'd into paragraphs.
- [x] [E] Learn More box after Precision: BBC Bitesize "accuracy and
  precision" + "errors in measurement" (still needs the 📚 marker added).
- [x] [V] Random-vs-systematic scatter sketch placeholder (after the
  comparison table).
- [x] [T] Verification vs Validation: the Validation section already leads
  with the concrete cracked-housing example (the two-box mermaid still
  needs replacing - see below).

## Remaining items applied 2026-07-21

- [x] [C] "elephant's foot" glossed with a forward ref to Topic 1.7
  (verified defined in 07-Tolerances-and-Fits.md ~1093). "slicer"/
  "over-extruding" flagged with a "Part 2 explains printing" note.
- [x] [C] Micrometer glossed as "a finer, more advanced measuring tool -
  optional" (verified: never introduced elsewhere in the book).
- [x] [T] Verification vs Validation two-box mermaid replaced with a
  "did we build it as specified? / did we build the right thing?" table
  with buggy examples.
- [x] [T] "Traceability" now introduced as "good measuring leaves a paper
  trail" before the formal word.
- [x] [T] Decimal places vs significant figures - one-line contrast added
  at the top of the Significant Figures section.
- [x] [V] Zero-error sketch placeholder (closed caliper reading 0.18 mm)
  and dot-strip outlier sketch placeholder both added.
- [x] [E] Learn More box added at Rounding: Bitesize "rounding" +
  "mean, median, mode and range". Chapter now has 2 Learn More boxes.
- [x] [T] Two "Think about it" prompts placed: averaging cannot fix a
  systematic bias; a caliper reading 0.18 mm closed adds 0.18 mm to
  everything.
- [x] [T] Topic Mini Project - Accuracy vs Precision Target Game (toss
  counters at a drawn bullseye three ways, measure distances, compute
  average + range, classify against the four dartboards). Adult-check +
  gentle-toss/choking safety; Watch the build box (Carolina + YouTube);
  keep the target for the showcase shelf.
- [x] [T] De-staccato: joined representative narrative passages
  (Accuracy, Precision, Accuracy-and-Precision-together, Systematic
  Error); kept one-liners for steps, definitions and worked examples.
- [x] Break markers at three seams (after Why Precision Can Be Misleading;
  after Outliers; after Validation).
- [x] Emoji pass: all eight template headings carry their fixed emoji; the
  existing Learn More box now has the 📚 marker.
- [x] New Words all in glossary.md (added Decimal Place, False Precision,
  Reproducibility); gloss numbers checked against SUMMARY.md; Looking
  Ahead names Topic 1.7; mini project adult-checked; estimated_time bumped
  to 120-150 min.
- [x] Final pass done: verify checklist, rows ticked, SUMMARY.md and
  TRACKER.md updated. Frontmatter was already 0.2/Reviewed (early bump).

## Research topics (from PLAN.md - run before editing)

- Bitesize "accuracy and precision" + "errors in measurement" (already
  cited in dd772e8) - re-verify the search terms surface the pages.
- Zero-error description matches real caliper behaviour.
- Mean/median/mode/range and rounding pages exist (Bitesize KS3 Maths).
- Mini project: a proven accuracy-vs-precision hands-on that produces a
  keepable artifact and uses household materials.
- Record findings as Research notes here.

## Research notes (2026-07-21)

Facts confirmed:
- Zero error: closing clean caliper jaws should read 0.00 mm; a non-zero
  closed reading (e.g. 0.18 mm) is a constant offset added to every
  measurement, cleared by wiping the jaws and pressing zero (or noted and
  subtracted). Matches the chapter (verified via iFixit / Make: / Bantam
  Tools caliper guides in the Ch05 pass).
- Elephant's foot is defined in Topic 1.7 (07-Tolerances-and-Fits.md
  ~1093) and referenced back from the Part 2 printing topic - so the
  forward ref from Ch06 correctly points to Topic 1.7.
- Micrometer is never introduced anywhere in the book - so it must be
  glossed as optional/advanced where Ch06 mentions it.

Links verified (bbc.co.uk blocks the crawler; Bitesize pages verified
indirectly via curriculum wording, per the Ch02/04/05 method):
- BBC Bitesize KS3 Science "accuracy and precision" (kept from dd772e8).
- BBC Bitesize KS3 Science "errors in measurement" (kept from dd772e8).
- BBC Bitesize KS3 Maths "mean, median, mode and range".
- BBC Bitesize KS3 Maths "rounding".

Mini project source confirmed:
- Carolina Knowledge Center "Accuracy Versus Precision Beanbag Toss" - a
  standard classroom activity: toss counters at a target, measure distance
  from the bullseye and the spread, and compute mean/median/mode/range to
  decide whether a set of tosses is accurate, precise, both or neither.
  Adapts cleanly to household counters/coins + paper + a ruler.
