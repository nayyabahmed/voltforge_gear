# Backlog - Topic 2.9 - Soldering and Wire Connections

Source: audit of the v0.1 text (2,101 lines, 15 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 2 of the Part 2 review, and the last teaching
topic before the Part 2 capstone (Topic 2.10, not yet written).

Sittings: 6. Well over the length target with only **two** break markers.
Seams: "Soldering Is Not Hot Glue" (~249), "The Reliable Joint Sequence"
(~520), "Heat-Shrink Tubing" (~789), "Connectors Make Modules Replaceable"
(~923), "Inspection: Read the Joint Before Testing" (~1024), and one before
the activities (~1305).

> **Credit where it is due:** this is the best-glossed topic in Part 2 - it
> carries forward pointers to all seven Part 3 topics. Use it as the model
> when fixing the gloss gaps in 2.2-2.8, rather than inventing a new
> pattern.

## Items to apply

- [ ] [T] **Add four break markers** at the seams above. At 2,101 lines
  with two markers, this is the item that most changes the reading
  experience.
- [ ] [V] **Figures: 2 against a budget of 10-14** (STYLE-GUIDE 7.4,
  skill topic). At 2,101 lines the topic currently runs one figure per
  ~1050; the target is one per 40-80. This is the largest single item in
  this file. See `references/ref-002.md` for the taxonomy.
  The `[Signature visual:` at ~292 covers wetting and the `[Sketch:` at ~155
  the wire cross-section - leave both. Gaps: "Common Joint Faults and What
  They Teach" (~1176) is a whole section about visual recognition with no
  visual (check the signature visual does not already cover these before
  drawing them twice); "Strain Relief" (~827) and "Service Loops" (~854) as
  F5 routing overlays; "The Reliable Joint Sequence" (~520) as an F4 strip;
  "Crimping" (~953) as an F4 strip.
  Conventions to apply to every figure, existing ones included (7.2/7.3):
  type tag `[F1-F7 ...]`, `Figure 2.9.k` number, a one-sentence caption
  saying what to notice, and alt text.
- [ ] [V] **F3 pairs for the 15 Common Beginner Mistakes.** The highest-value
  figure type in the book and currently unused here - a right-versus-wrong
  pair per mistake, or one combined F3 array. Prose alone cannot show a
  reader what the wrong version looks like.
- [ ] [T] **Add `# Answers 🔑`** (STYLE-GUIDE 3 item 15, 13.3) with model
  answers numbered to match the 12 Review Questions. Needed for the HTML
  reveal and for a mentor running a session.
- [ ] [T] **Only one "Think about it" prompt** in 2,101 lines. Add a second
  at "Wetting" (~270) or at "Pull the Connector, Not the Wire" (~903) -
  the latter is the claim a reader is most likely to ignore in practice and
  the failure it causes is invisible until it strands them.
- [ ] [E] **Trailing `# Learn More` section at ~2070** - outside the
  template order. Break into inline boxes next to the sections they serve:
  a soldering technique reference near "The Reliable Joint Sequence"
  (~520) and a fume or workshop-safety reference near "Soldering Safety"
  (~318). Note the mini project's Watch-the-build box already cites
  Adafruit Learn, SparkFun Learn and HSE - avoid duplicating those three.
- [ ] [T] **Decide the build-topic pattern question.** This topic alone
  carries "Cheapest Valid Prototype" (~1806) and "What to Buy, Reuse and
  Make" (~1829) - the pattern STYLE-GUIDE section 11 specifies for build
  topics in Parts 3-5, not for Part 2 teaching topics. It reads well here,
  so the choice is genuine: either justify it as a deliberate bridge into
  the Part 2 capstone and leave it, or move the material into Topic 2.10.
  Whatever is decided, record it as a standing decision in
  [part-2-book-wide.md](part-2-book-wide.md) so 2.10 is written to match.
- [ ] [T] **Eleven safety callouts - the highest count in the book, and
  correctly so.** Verify each sits BEFORE the technique it covers, that the
  continuity-testing rules (unpowered scrap only, ~1076) are stated before
  any activity that could tempt otherwise, and that everything agrees with
  `SAFETY.md`.
- [ ] [T] **Seven hands-on activities plus a mini project** - the most in
  the book. Confirm each earns its place and that Activity 4 "Make a First
  Scrap-Wire Solder Joint" (~1398) is not redundant with "A Simple Practice
  Joint" (~769) in the body.
- [ ] [T] **Check the worked example and the fair test are complete.**
  "Worked Example - Choosing a Wire Cut Length" (~658) needs question,
  known values, rule, calculation and meaning in words. "Fair Test - Does
  Strain Relief Protect the Joint?" (~1257) must state the question, the
  independent, dependent and control variables, the procedure and a
  pass/fail condition, per the Topic 1.9 pattern.
- [ ] [C] **Verify the seven forward pointers.** They are the topic's
  strength, so make sure every number is right against `SUMMARY.md`:
  3.1 Meet the RC Electronics, 3.2 Voltage/Current/Resistance/Power,
  3.3 Batteries, 3.4 Receivers, 3.5 Servos, 3.6 ESCs, 3.7 Motors.
- [ ] Verify: all 15 New Words in `glossary.md` (they are, as of
  `4074569`); Looking Ahead names Topic 2.10 (it does); every activity has
  a no-equipment variant (Activities 1-3 are equipment-free; the mini
  project is deliberately a paper-and-string model); mini project keeps its
  adult-check line and Watch-the-build box.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

**This topic and Topic 2.6 carry the heaviest research load in Part 2. Every
safety claim here needs a current source.**

- **Lead-free versus leaded solder (~404) - decide and justify.** Verify
  current UK guidance on which is appropriate for a supervised child,
  what RoHS does and does not require of a hobbyist, and confirm the topic's
  own point (~ in the review questions) that lead-free is not a reason to
  relax about flux fume.
- **Flux fume (~296, ~318) - safety-critical.** Verify against HSE guidance
  on rosin-based solder flux fume: extraction or ventilation requirements,
  head position, and what is realistic in a home setting. The mini project
  already cites HSE, so keep the body consistent with it.
- **Soldering iron temperature (~426, ~453)** - confirm the temperature
  range quoted for electronics work and that tip-temperature advice matches
  manufacturer guidance.
- **Heat source for heat-shrink tubing (~789)** - confirm what the topic
  recommends is safe and appropriate; a lighter or naked flame would not
  be, and a soldering iron barrel is a common but poor substitute.
- **Continuity testing (~1066, ~1098)** - the unpowered-only rule is
  already stated well; verify the multimeter setup instructions are
  correct and that nothing in the activities contradicts them.
- Wire size as a design choice (~192) - any current-carrying or gauge
  figures need a source, and they must agree with what Topic 3.2 will
  teach.
- Crimping (~953) and screw terminals (~984) - confirm the technique
  advice, especially the warning against tinning stranded wire before
  putting it into a screw terminal if the topic makes that claim.
- Desoldering and rework (~1195) - confirm the braid or pump technique
  described.
- Feed `TOOLS.md` and `TROUBLESHOOTING.md` from the fault sections
  (~1176, ~1195).
- Mini project: re-verify the three Watch-the-build sources (Adafruit
  Learn, SparkFun Learn, HSE) still resolve.

## Research notes

(To be filled during the pass.)
