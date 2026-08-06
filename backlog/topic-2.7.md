# Backlog - Topic 2.7 - Hand Tools and Fasteners

Source: audit of the v0.1 text (1,917 lines, 15 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 2 of the Part 2 review.

Sittings: 5. Well over the length target with only **two** break markers.
Seams: "Reading a Metric Fastener Name" (~284), "Screw Head Shapes" (~421),
"Washers: Snowshoes for Screw Heads" (~819), "Heat-Set Inserts" (~926), and
one before the activities (~1375).

## Items to apply

- [ ] [T] **Add three or four break markers** at the seams above.
- [ ] [T] **The only Part 2 topic missing both optional patterns.** Every
  other teaching topic in the part has a "Thinking Like an Engineer"
  section and a "Stop Point Before ..." section; this one has neither. Per
  the book-wide consistency item, either add both here or drop them
  everywhere - do not leave this topic as the single exception. A natural
  "Thinking Like an Engineer" theme is already latent in "A Fastener
  Selection Routine" (~1222), and a stop point belongs before the tool kit
  shopping advice (~619).
- [ ] [C] **No forward glosses at all.** "a servo must be replaced" (~95),
  the M2.5 "small mounts and some servos" table row (~309) and "A servo or
  motor may require its own manufacturer-specified screw" (~1218) all use
  Part 3 vocabulary as if taught. Gloss on first use per `SUMMARY.md`
  (servo 3.5, motors 3.7).
- [ ] [T] **Only one "Think about it" prompt** in 1,917 lines. Add a second
  at "More Tight Is Not Always More Secure" (~191) - the most
  counter-intuitive claim in the topic, and one an 11-year-old will
  actively disbelieve. Hands-On Activity 1 "The Door Torque Test" (~1375)
  is the ready-made physical hook; the analogy bank already assigns the
  door-hinge analogy to torque.
- [ ] [V] **Figures: 3 against a budget of 10-14** (STYLE-GUIDE 7.4,
  skill topic). At 1,917 lines the topic currently runs one figure per
  ~639; the target is one per 40-80. This is the largest single item in
  this file. See `references/ref-002.md` for the taxonomy.
  The `[Signature visual:` at ~155 covers the spiral ramp - leave it. Gaps:
  "The Four Jobs in Every Screw Joint" (~246) as an F2 cross-section with
  clamp-force arrows, "Reading a Metric Fastener Name" (~284) as a labelled
  M3 x 12, "Heat-Set Inserts" (~926) as an F4 strip, "Driver Profiles" (~444)
  as an F7 array, "Washers" (~819) as an F5 overlay.
  Conventions to apply to every figure, existing ones included (7.2/7.3):
  type tag `[F1-F7 ...]`, `Figure 2.7.k` number, a one-sentence caption
  saying what to notice, and alt text.
- [ ] [V] **F3 pairs for the 10 Common Beginner Mistakes.** The highest-value
  figure type in the book and currently unused here - a right-versus-wrong
  pair per mistake, or one combined F3 array. Prose alone cannot show a
  reader what the wrong version looks like.
- [ ] [T] **Add `# Answers 🔑`** (STYLE-GUIDE 3 item 15, 13.3) with model
  answers numbered to match the 12 Review Questions. Needed for the HTML
  reveal and for a mentor running a session.
- [ ] [E] **Three Learn More boxes - the best coverage in Part 2.** Verify
  all three sources still exist and use curriculum wording for any Bitesize
  search term, but no new boxes are needed.
- [ ] [C] **"Captured nut" vs "captive nut".** This topic says captured
  (~898); Topic 2.5 says captive (~574). Settle it in the terminology
  registry and apply to both topics. The glossary currently leads with
  Captive Nut and notes the variant.
- [ ] [T] **Check the worked example is complete.** "Worked Example:
  Choosing Screw Length" (~379) must show question, known values, rule,
  calculation and the meaning in words, per style guide section 2.
- [ ] Verify: all 15 New Words in `glossary.md` (they are); Looking Ahead
  names Topic 2.8 (it does); every activity has a no-equipment variant
  (Activities 1-3 are equipment-free); mini project keeps its adult-check
  line, its no-fasteners fallback and its Watch-the-build box.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

- **Threadlocker on plastics (~1089) - treat as safety-critical.** Several
  common threadlockers and cyanoacrylates attack or craze thermoplastics
  such as ABS and polycarbonate. Verify what the topic recommends is
  actually safe on printed parts, that it names the right product type, and
  that its handling advice (ventilation, skin contact, adult supervision)
  matches manufacturer guidance and `SAFETY.md`.
- **Heat-set insert installation (~926):** confirm the recommended
  temperature range and that the advice does not have a child holding a hot
  iron unsupervised. Cross-check against the soldering-iron safety rules in
  Topic 2.9 so the two topics agree.
- **Metric fastener designation and pitch (~284, ~321):** verify the
  standard designations, the coarse-thread pitch values quoted for M2, M2.5,
  M3, M4 and M5, and how length is measured for countersunk versus other
  heads (~360).
- **Torque guidance (~220, ~715, ~1125):** any torque figures or "quarter
  turn past snug" style rules need a source, especially tightening into
  printed plastic (~1125) and into TPU (~1158).
- Self-tapping screws in plastic (~969) and printed threads (~997) -
  confirm the recommended hole sizes.
- Grub screws on rotating parts (~1175) - confirm the advice is right for
  buggy drivetrain use, and gloss the drivetrain reference forward.
- Feed `TOOLS.md` from "A Small Buggy Hand-Tool Kit" (~619). That document
  is 46 lines and this is its most natural source in the part.
- Mini project: re-verify Watch-the-build sources for the Buggy Fastener
  Training Board.

## Research notes

(To be filled during the pass.)
