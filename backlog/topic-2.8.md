# Backlog - Topic 2.8 - Cutting, Drilling and Finishing

Source: audit of the v0.1 text (2,268 lines, 15 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 2 of the Part 2 review.

Sittings: 6. **The longest topic in the book** at 2,268 lines - nearly
double the 1,200-line ceiling. Four break markers is two or three short.
Seams: "Workholding: The Part Must Stay Still" (~375), "Cutting Tools Are
Not Interchangeable" (~501), "Drilling: A Rotating Cutting Tool" (~668),
"Burrs: The Sharp Leftovers" (~1016), "Abrasives: Thousands of Tiny
Cutters" (~1103), and one before the activities (~1571).

## Items to apply

- [ ] [C] **Terminology violation - confirmed.** "hinge-pin" appears at
  ~902 and ~970; the registry says "hinge pin", two words. Same fix as was
  applied to Chapter 04 in Part 1.
- [ ] [T] **Add two or three break markers** at the seams above. At this
  length it is the highest-value single change in the topic.
- [ ] [C] **No forward glosses at all.** "servo locating pockets" (~1228)
  and the hinge pin references (~902, ~970) use vocabulary the reader has
  not met. Gloss per `SUMMARY.md` (servo 3.5); hinge pin is taught in Topic
  1.4, so that one is a backward pointer.
- [ ] [V] **Two placeholders across 2,268 lines** - the thinnest visual
  coverage in the book relative to length, in a topic that is almost
  entirely about physical technique. Both existing ones are good and should
  be left alone: the `[Signature visual:` at ~738 is the four-panel clean
  hole sequence, and the `[Sketch:` at ~160 already shows the datum, witness
  line and shaded waste side. Priority additions:
  - "Breakthrough: The Last Millimetre Is Different" (~750) - why the exit
    is where the drill grabs.
  - "Countersinks and Chamfers" (~980) - a cross-section with the screw
    head sitting flush.
  - "A Sensible Grit Progression" (~1125) - a strip showing coarse to fine.
  - "Files Cut Best with a Plan" (~1084) - stroke direction.
- [ ] [T] **Only one "Think about it" prompt** in 2,268 lines. Add a second
  at "Kerf: The Tool Has Width" (~232) - a reader will not expect that
  cutting exactly on the line makes the part too small. "Breakthrough"
  (~750) is the alternative: why the last millimetre is where the drill
  grabs.
- [ ] [E] **Trailing `# Learn More` section at ~2243** - outside the
  template order. Break into inline boxes next to the sections they serve:
  a hand-tool technique reference near "The Safe Tool Routine" (~444) and a
  drilling-safety reference near "Power Drill Safety" (~816).
- [ ] [T] **Nine safety callouts - the right instinct for this material.**
  Verify each sits BEFORE the technique it covers rather than after, and
  that every one is consistent with `SAFETY.md`. This topic is the largest
  single feeder that document has.
- [ ] [T] **Check the worked example and the fair test are complete.**
  "Worked Example - Shortening a Brace" (~264) needs question, known
  values, rule, calculation, meaning. "Fair Test - Does Backing Improve the
  Exit?" (~1518) must state the question, the independent, dependent and
  control variables, the procedure and a pass/fail condition, per the
  Topic 1.9 fair-test pattern.
- [ ] [T] **Six hands-on activities plus a mini project** - confirm each
  earns its place at this length, and that Activity 2 "Backing Board
  Comparison" (~1597) is not simply the fair test (~1518) done twice.
- [ ] Verify: all 15 New Words in `glossary.md` (they are); Looking Ahead
  names Topic 2.9 (it does); every activity has a no-equipment variant
  (Activity 5 is correctly a supervised dry run rather than a real drilling
  exercise); mini project keeps its adult-check line and Watch-the-build
  box.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

- **Dust from sanding printed plastics (~1245, ~1274) - safety-critical.**
  Verify current guidance on particulate exposure when sanding PLA, PETG
  and composite filaments, whether wet sanding is the right recommendation
  for a child, and what respiratory protection (if any) the topic should
  specify. Cross-check `SAFETY.md`.
- **Power drill safety (~816)** - confirm the topic's rules match current
  guidance, including eye protection, securing the work, loose clothing and
  hair, and adult operation versus adult supervision at this age.
- **Craft knife technique (~543)** - "light passes, not heroic force" is
  the right instinct; confirm the blade-direction and cutting-mat advice
  and that blade changing is specified as an adult job.
- Drill speed, pressure and heat (~779) - any speeds or feed guidance
  quoted needs a source, especially for plastics where melting is the
  failure mode.
- Drilling printed parts (~879) and opening an undersized printed hole
  (~936) - confirm the recommended approach and that it agrees with the
  hole-shrinkage material in Topic 1.7.
- Reaming (~958) and countersink angles (~980) - confirm the standard
  included angle quoted for metric countersunk screws.
- Grit progression (~1125) - confirm the grit numbers recommended.
- Heat from sanding plastic (~1274) - confirm the melting/smearing
  explanation.
- **Feed `TOOLS.md`** from the cutting, drilling and finishing tool
  sections. That document is 46 lines and currently references only Topics
  2.2, 2.7 and 2.9 - none of this topic's tools are listed.
- Mini project: re-verify Watch-the-build sources for the Reusable Buggy
  Hole-Pattern Template.

## Research notes

(To be filled during the pass.)
