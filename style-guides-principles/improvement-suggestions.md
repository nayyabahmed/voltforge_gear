# Readability Improvement Backlog

Suggestions from a full review of Chapters 02-10 and the glossary (2026-07-11),
aimed at making the handbook easier for an 11-year-old to read.
Grouped as: book-wide issues first, then per-chapter items, then external resources.

Legend: [T] textual, [C] context awareness, [V] visual aid, [E] external reference.

---

## Book-wide

- [ ] [T] **One-sentence-per-line fatigue.** The staccato style works for lists,
  definitions, warnings and procedures, but across 1,200-1,900-line chapters it
  tires the reader. Rule of thumb: keep one-line-per-sentence for steps and
  cautions; merge 2-4 connected sentences into short paragraphs for stories and
  explanations (the door/shelf/dartboard/bath-tap narrative passages are the
  worst offenders).
- [ ] [T] **Chapter length.** Every chapter from 02 onwards is too long for one
  sitting. Add explicit "Part A / Part B" splits or "Good place to take a break -
  try Activity 1 now" markers at the natural seams listed per chapter below.
  Chapter 04 is the strongest candidate for a real split into two chapters.
- [ ] [C] **First-use gloss convention.** Adopt a rule: any term not yet taught
  gets a one-line gloss in brackets plus a pointer to its home chapter, e.g.
  "the ESC (the motor's speed controller - Chapter 22)". Current offenders:
  ESC, torque (Ch02), wheel hex, motor timing, brushless, output cup (Ch03),
  shock tower, servo saver, screw boss, gear mesh (Ch04), press fit (Ch05),
  elephant's foot, micrometer (Ch06), slicer/extrusion vocabulary, PETG,
  reaming (Ch07), STL/CAD, heat-set insert, nut trap, tolerance stack-up (Ch08),
  test coupon, compliant hinge (Ch09), NTS, ESC (Ch10).
- [ ] [C] **Terminology to reconcile across chapters:**
  - "gearbox" (Ch02) vs "drivetrain" (Ch03/04) - pick one or add a bridging line
    in Ch03 ("the gearbox from Chapter 2 is part of what engineers call the
    drivetrain").
  - "requirement traceability" (Ch10, glossary) vs "requirements traceability"
    (Ch09) - standardise (recommend the glossary's singular form).
  - "Hinge pin" vs "hinge-pin" (Ch04) - standardise hyphenation.
  - Ch05 "measurement uncertainty" vs Ch06 "error/range/repeatability" - add one
    sentence in Ch06 linking the two vocabularies.
- [ ] [E] **"Learn More" box pattern.** Add a small recurring box (2-3 links max)
  near the relevant section, pointing to established kid-friendly resources:
  BBC Bitesize (KS2/KS3 science, maths, design & technology), PhET simulations
  (phet.colorado.edu), Explain That Stuff (explainthatstuff.com), Tinkercad
  Learn. Specific placements listed per chapter below. Electricity and magnetism
  links will matter most in Part 3 (electronics chapters) - plan the pattern now.
- [ ] [V] **Weak mermaid pattern.** Several mermaid flowcharts merely restate a
  bullet list as boxes (examples flagged per chapter). Prefer: mermaid for flows
  and cycles; tables for comparisons; labelled sketch/photo placeholders for
  spatial ideas (beams bending, fits, view alignment).

---

## Chapter 02 - Systems Thinking (1,194 lines)

Break point: after the cause-and-effect chain (~line 480); second seam before
Hands-On Activity 1 (~line 892).

- [ ] [C] ESC first used at ~232 but only expanded at ~833 - expand on first use.
- [ ] [C] Drivetrain part names (pinion, spur, differential, driveshafts, ~380)
  and "torque" (~434) used before Ch03 defines them - add "(we'll meet these in
  Chapter 3)".
- [ ] [C] "2-cell battery" (~717) - "cell" never explained.
- [ ] [T] "Before We Begin" (41-77) and "Cause and Effect" (482-514): merge the
  one-line runs into 2-3 short paragraphs.
- [ ] [T] The abstract systems-thinking definition (~125) lands before any
  concrete example - move the toaster example first or add a buggy hook line.
- [ ] [V] Add a labelled photo/sketch of the real buggy annotated with the six
  subsystems next to the "system of systems" tree (~388).
- [ ] [V] Photo of a pinion meshing with a spur gear at the Interfaces section
  (~785).
- [ ] [V] Convert the ASCII "Larger tyres" chain (~946) to mermaid for
  consistency.
- [ ] [E] BBC Bitesize D&T "systems and control" at Input-Process-Output (~135);
  BBC Bitesize control/feedback at Feedback (~518); KS3 energy at "Connections
  Carry Things" (~413).

## Chapter 03 - How Machines Move (1,423 lines)

Break point: after "The Price of More Torque" (~640); Part B starts at Friction.

- [ ] [C] Undefined jargon: "wheel hex" (~470), "motor timing" (~1168),
  "brushless" (~318), "output cup" (~1294) - gloss or simplify.
- [ ] [C] Newton's third law is used (tyre pushes ground, ~88, ~404) but never
  named - add "engineers call this action and reaction - more in Chapter 4".
- [ ] [T] "Power" section (~867) is the most abstract - add a concrete analogy
  (carrying shopping upstairs quickly vs slowly) and shorten.
- [ ] [V] Door-handle torque mermaid (~255) reads as a sequence, not a lever -
  replace with a labelled top-view sketch of a door with force arrows and
  distances.
- [ ] [V] Differential flowchart (~367) - replace with a top-down sketch of the
  buggy on a curve showing the two wheel arc lengths.
- [ ] [V] Photo/sketch of a real 10T/40T gear pair at "A Simple Gear Pair" (~497).
- [ ] [V] Side-view sketch of the buggy squatting/diving (weight transfer, ~761).
- [ ] [E] BBC Bitesize KS2/KS3 forces at "Force" (~143); PhET "Forces and Motion:
  Basics" at ~168; BBC Bitesize KS3 moments + Explain That Stuff "gears" at
  Torque (~217) and Gears (~477); friction resources at ~643; momentum at ~828.

## Chapter 04 - Forces and Why Parts Break (1,687 lines, 27 new words)

Strongest split candidate: Part A "How parts are loaded" (through Buckling,
~669), Part B "Designing so parts don't break". Add a mid-chapter recap table.

- [ ] [C] "shock tower" used at ~204 but defined at ~1141; "servo saver" (~1093),
  "screw boss" (~756), "gear mesh" (~1184) never defined - gloss on first use.
- [ ] [C] Add backward refs: torque -> Ch03 (~111, ~289); reaction forces ->
  Ch03's ground-push passage (~368); "trace the full load path" -> Ch02 systems
  thinking (~1502).
- [ ] [T] Materials run (elastic -> permanent -> fracture, ~555-609) reads like
  flashcards - tighten into short paragraphs.
- [ ] [V] Bending mermaid (~232) does not look like a bending beam - replace with
  a labelled sketch of a beam bowing (top squeezed, bottom stretched).
- [ ] [V] Fillet ASCII "|_ vs |)" (~745) is unreadable - replace with a labelled
  sharp-vs-rounded corner sketch.
- [ ] [V] Shear mermaid (~272) reads as a list - card-stack sketch with offset
  arrows. Same treatment would improve the tension/compression/torsion mermaids.
- [ ] [V] Photo of a real broken RC part (fracture surface) at "Fracture" (~596)
  and "Reading a Failure" (~1413).
- [ ] [E] BBC Bitesize forces & elasticity at Elastic Deformation (~555);
  pressure (force/area) at Stress (~451); materials (brittle/ductile) at ~613;
  Explain That Stuff bridges/structures at "Why Shape Matters" (~671); metal
  fatigue at ~882; a kid-friendly 3D-printing explainer at Print Orientation
  (~973).

## Chapter 05 - Measurement (1,863 lines)

Suggest three sittings: units + what to measure / tools + technique /
recording + activities (seams at ~421 and ~1419).

- [ ] [T] "Before We Begin" (46-66) and "The Shelf That Was Nearly Right"
  (70-105): merge staccato lines into short paragraphs (highest-value textual
  fix in the chapter).
- [ ] [C] "press fit" (~1591) used before Ch07 defines it - gloss + forward ref.
- [ ] [T] "confirmation bias" (~989) - add a plain gloss ("seeing what you hoped
  to see"). "trigonometry" (~1418) - soften or cut.
- [ ] [T] Resolution/accuracy/uncertainty run (~1027-1085) duplicates Ch06 -
  trim to a teaser plus "we cover this properly in Chapter 6".
- [ ] [C] Tool section assumes the reader owns digital calipers - add a cheap
  options / no-calipers fallback note (Activity 3 already models this).
- [ ] [V] Ruler ASCII (~471) is confusing - replace with a labelled sketch/photo
  of a ruler with mm and cm marks called out (top visual priority for Ch05).
- [ ] [V] Centre-to-centre ASCII (~396) - labelled two-circles diagram showing
  centre spacing vs edge gap.
- [ ] [V] Replace the caliper-parts mermaid (~542) with a labelled caliper
  photo/sketch; replace the bearing OD/ID mermaid (~345) with a cross-section
  sketch.
- [ ] [E] BBC Bitesize: units of length (~131), converting mm/cm/m (~185),
  reading scales (~464), parts of a circle (~311), mean/average (~993);
  KS3 "taking measurements" (parallax) at ~487; expansion/contraction at ~1088.

## Chapter 06 - Accuracy, Precision and Error (1,407 lines)

Break point: after Outliers (~717) or after Validation (~810).

- [ ] [V] **Four-dartboard 2x2 labelled sketch** near the opening - the single
  highest-value visual in the chapter (the mermaid at ~58 doesn't do the job).
- [ ] [C] "elephant's foot" (~1160) used before Ch07 defines it - add "(we'll
  explain this in Chapter 7)". Flag slicer/extrusion terms similarly (~1130).
- [ ] [T] Verification vs Validation (~767): lead with the concrete
  cracked-housing example; replace the two-box mermaid (~804) with a small
  "fits spec? / works in use?" table.
- [ ] [T] "Traceability" (~740): introduce as "keeping a paper trail" before the
  formal word.
- [ ] [T] Decimal places vs significant figures (~517): add a one-line contrast
  so kids don't conflate them.
- [ ] [C] Micrometer (~1246) offered as a tool but never introduced - mark
  optional/advanced.
- [ ] [V] Zero-error photo/sketch of a caliper reading 0.18 when closed (~336);
  dot-strip sketch for outliers (~689); tiny scatter sketch for random vs
  systematic error (~255).
- [ ] [E] BBC Bitesize KS3 "accuracy and precision" (~71); errors in measurement
  (~240); rounding decimals (~619); mean/median/mode/range (~642).

## Chapter 07 - Tolerances and Fits (1,845 lines, 28 new words)

Suggest 2-3 sittings (seams ~476 and ~998). Most vocabulary-dense chapter.

- [ ] [T] **Nine "fit" terms arrive in six rapid sections** - add a single
  summary table (fit type | feel | buggy example) before the design guides.
- [ ] [T] "bilateral/unilateral" (~194): lead with "two-sided/one-sided",
  mark the formal terms optional.
- [ ] [T] "datum" (~919): add the everyday analogy (measure everyone's height
  from the same floor, not from each other's heads).
- [ ] [T] Worst-case arithmetic (~806): add the one-line intuition before the
  numbers ("tightest fit = smallest allowed hole + biggest allowed shaft").
- [ ] [C] Printing vocabulary used as if known (extrusion width, over-extrusion,
  slicer, seam blobs, ~480-535) - add "don't worry if these are new - Part 2
  explains printing". Gloss PETG (~1555) and reaming (~1085).
- [ ] [V] **Three-fit cross-section sketch** (clearance/transition/interference
  side by side) - top visual priority; current ASCII is weak and inconsistent.
- [ ] [V] Chamfer ASCII "\ /" (~1130) - replace with a labelled entry-guiding
  sketch; sketch of the physical hole test coupon (~1170); shaded number-line
  for the tolerance band (~134); chassis-outline sketch dimensioned both
  baseline and chain ways (~957-995).
- [ ] [E] BBC Bitesize KS3 D&T tolerances (~74); joining/mechanical fixings at
  Snap Fit (~715); Explain That Stuff 3D printing (~478); expansion/contraction
  (~1032, same link as Ch05).

## Chapter 08 - Engineering Drawings (1,569 lines)

Really three topics stitched together; seams after Isometric Views (~490) and
after Surface Finish/Material (~850).

- [ ] [V] **View-alignment ASCII (~262) is the most important spatial concept**
  and the weakest visual - replace with a labelled three-view sketch or photo.
  Keep the line-type ASCII snippets (they work) but add a "line types at a
  glance" table.
- [ ] [V] Section views (~369): the cake analogy deserves a labelled sketch
  (outside view + cut plane + hatched section). Countersink vs counterbore
  (~637): side-by-side section sketch or comparison table.
- [ ] [C] Gloss on first use: "interfaces" (~91), tolerance stack-up (~576),
  heat-set insert (~693), nut trap (~393), STL/CAD (~1000, "covered in Part 2").
- [ ] [T] First/third-angle projection (~278): explicitly defer ("pick one and
  label it; you'll meet these again in professional CAD").
- [ ] [T] Reference dimension (~537): show the bracket convention "(50)".
- [ ] [T] "Design intent" (~1019) is important but arrives very late - add a
  short version early in the chapter.
- [ ] [E] BBC Bitesize KS3 D&T "isometric and orthographic drawing" (~187);
  a beginner "how to read engineering drawings" tutorial at sections (~369).
- [ ] [C] Add "first-angle / third-angle projection" to the glossary if the
  section stays.

## Chapter 09 - The Engineering Design Process (1,945 lines, ~35 glossary terms)

At least two sittings; seams after Assumptions (~708) and after Design Reviews
(~1398).

- [ ] [T] **Six prototype-type mini-sections (~746-833) -> one comparison table**
  (type | good for | not for). Highest-value change in the chapter.
- [ ] [T] Weighted decision matrix (~622): add a fully worked 3-column example
  with totals.
- [ ] [T] "shall/should/may" (~259): trim to ~3 lines. Divergent/convergent
  (~476): lead with the plain idea, present the terms as "grown-ups call this".
- [ ] [C] Gloss "test coupon" (~685) and reword "compliant hinge" (~828) to
  "flexible (living) hinge". Add "(materials are covered in Part 2)" where
  heat/creep behaviour appears (~714, ~1120).
- [ ] [T] Independent/dependent/control variables (~908): one concrete buggy
  sentence tying all three together.
- [ ] [V] Five Whys ladder as a small mermaid (~1132); concept-card example
  sketch (~549); reversible vs irreversible two-column table (~1245).
- [ ] [E] BBC Bitesize KS3 D&T iterative design (~80); **KS2/KS3 science "fair
  testing and variables"** (~888, maps perfectly onto UK science lessons);
  collecting/recording data (~975).

## Chapter 10 - First Engineering Challenge (1,390 lines)

Length is justified as a do-along project, but group the 27 steps under the
implied phases (Understand / Define / Design / Build & Test / Document); natural
pauses after Step 12 (~518) and Step 22 (~834).

- [ ] [V] **Packaging envelope (~397) is the chapter's signature idea** but the
  mermaid doesn't show the spatial concept - add a labelled 2D sketch (component
  outline + dashed envelope + wire/removal arrows).
- [ ] [V] At least one labelled sketch per concept in Step 13 (~539), or one
  comparison figure - the step literally asks kids to sketch.
- [ ] [T] Spell out "NTS (Not To Scale)" (~866). Gloss ESC (~139).
- [ ] [C] "swept volume" (~179) is used before the envelope section explains
  movement space - reorder or gloss.
- [ ] [C] Standardise "requirement traceability" (see book-wide).
- [ ] [E] Tinkercad Learn (first CAD) and Onshape learning centre at Optional
  Extension 1 (~1135); a cardboard-prototyping maker resource at Step 17 (~665).

## Glossary (1,692 lines)

Strong and kid-usable; spot-checks found no contradictory definitions.

- [ ] Add "first-angle / third-angle projection" entry (used in Ch08).
- [ ] Align "Requirement Traceability" naming with Ch09/Ch10.

---

## Top priorities if you only do a few

1. Add break markers / splits to Chapters 04, 05, 07, 08, 09.
2. Adopt the first-use gloss convention and sweep the offender list above.
3. Add the five highest-value visuals: labelled ruler (Ch05), four-dartboard
   panel (Ch06), three-fit cross-section (Ch07), three-view alignment + section
   view (Ch08), packaging-envelope sketch (Ch10).
4. Convert the story passages from one-sentence-per-line to short paragraphs.
5. Add "Learn More" boxes: fair testing (Ch09), forces (Ch03/04), measurement
   (Ch05/06) first; plan electricity/magnetism links for Part 3.
