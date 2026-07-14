# Backlog - Chapter 03 - How Machines Move

Source review: 1,423 lines. Line numbers refer to the original v0.1 text.
Status: DONE - applied 2026-07-14, chapter bumped to v0.2.

Break point: after "The Price of More Torque" (~640); Part B starts at
Friction.

- [x] [C] Undefined jargon: "wheel hex" (~470), "motor timing" (~1168),
  "brushless" (~318), "output cup" (~1294) - gloss or simplify.
  (Also glossed while there: ESC -> Ch 25, transmitter/receiver -> Ch 23.)
- [x] [C] Newton's third law is used (tyre pushes ground, ~88, ~404) but
  never named - add "engineers call this action and reaction - more in
  Chapter 4". (Named at Step 6, echoed in the walking analogy.)
- [x] [C] Book-wide terminology item lands here: bridge "gearbox" (Ch02) to
  "drivetrain" ("the gearbox from Chapter 2 is part of what engineers call
  the drivetrain"). (In "A Common Mistake".)
- [x] [T] "Power" section (~867) is the most abstract - add a concrete
  analogy (carrying shopping upstairs quickly vs slowly - see the analogy
  bank) and shorten.
- [x] [V] Door-handle torque mermaid (~255) reads as a sequence, not a
  lever - replace with a labelled top-view sketch of a door with force
  arrows and distances.
- [x] [V] Differential flowchart (~367) - replace with a top-down sketch of
  the buggy on a curve showing the two wheel arc lengths.
- [x] [V] Photo/sketch of a real 10T/40T gear pair at "A Simple Gear Pair"
  (~497). (Signature visual; plus a reality-check line on real 1/10 tooth
  counts - see Research notes.)
- [x] [V] Side-view sketch of the buggy squatting/diving (weight transfer,
  ~761).
- [x] [E] BBC Bitesize KS2/KS3 forces at "Force" (~143); PhET "Forces and
  Motion: Basics" at ~168; BBC Bitesize KS3 moments + Explain That Stuff
  "gears" at Torque (~217) and Gears (~477); friction resources at ~643;
  momentum at ~828. (Five Learn More boxes; momentum flagged as a GCSE
  look-ahead.)
- [x] [T] "Think about it" prompts (STYLE-GUIDE section 2, added
  2026-07-12), pick the two most counter-intuitive: torque (push a door
  shut right next to the hinge, then from the handle - why is one so much
  harder?); differential (walk around a tight corner side by side with a
  friend on your outside - who has to take bigger steps, and what would
  happen if you were forced to match steps?). Weight-transfer bus prompt
  not used (two-per-chapter cap).
- [x] [T] Chapter Mini Project (STYLE-GUIDE section 3): cardboard gear pair
  with different tooth counts on skewer/pencil axles (sources: 4-H "Make
  Your Own Cardboard Gears", Instructables, Technovation gearbox guide -
  re-verified; Experiland dropped). Reflection: turn the big gear once and
  count the small gear's turns (the ratio made visible), then feel which
  gear is harder to stop (the torque trade).
- [x] Break marker at the seam listed above.
- [x] Emoji pass per STYLE-GUIDE section 6 (fixed callout markers, one
  meaningful emoji on content headings that earn one).
- [x] Final pass: verify checklist (PLAN.md step 5), bump to v0.2, tick rows
  here, update SUMMARY.md. (Glossary gained the two missing entries:
  Differential, Revolution. Weak two-box mermaids also replaced/removed:
  linear-vs-rotational, pinion-spur, gearing comparison -> table.)

## Research notes (2026-07-12)

- **PhET "Forces and Motion: Basics"** confirmed live at
  phet.colorado.edu/en/simulations/forces-and-motion-basics - four screens
  (net force tug-of-war, motion, applied force, friction slider). The
  friction screen doubles as the friction-section resource.
- **Explain That Stuff "gears"** confirmed at explainthatstuff.com/gears.html
  (Chris Woodford) - speed/force trade-off explained at the right level.
- **BBC Bitesize**: bbc.co.uk blocks direct fetching, so individual pages
  could not be deep-verified; kept in "search X on site Y" form per
  STYLE-GUIDE section 8. Curriculum wording used: "forces" and "friction"
  (KS3 physics), "moments" (KS3 - the national curriculum names "moment as
  the turning effect of a force"), "mechanical systems" (KS3 D&T - matches
  the Ch 01 box). "Momentum" is GCSE, not KS3 - the box at the Momentum
  section flags it as a look-ahead.
- **Newton's third law**: chapter's tyre-pushes-back/ground-pushes-forward
  description is correct as written; named "action and reaction" with a
  Chapter 04 pointer per the backlog item.
- **10T/40T gear pair**: fine as an abstract teaching pair (clean 4:1
  maths) but NOT typical buggy hardware - real 1/10 buggies run fine-pitch
  (48P/Mod 0.6) spurs of roughly 70-90 teeth with 15-30 tooth pinions
  (checked against RC gearing guides, e.g. Roger's Hobby Center "RC Gearing
  101"). Added a reality-check sentence after the example rather than
  changing the maths. The 20T/60T = 3:1 worked example is plausible for
  coarse-pitch gears and kept.
- **Mini project sources re-verified**: 4-H "Make Your Own Cardboard Gears"
  PDF confirmed on 4-h.org (Gears and More Gears activity sheet);
  Technovation "How to Make a Gearbox with Moving Parts" confirmed;
  Instructables "How to Build Working Gears From Junkmail and Cardstock"
  confirmed (photo tutorial). Experiland could not be re-confirmed -
  dropped in favour of the Instructables photo build. Corrugated-strip
  teeth (exposed flutes glued around a card disc) is the proven method.
- Deferred: nothing safety-critical in this chapter; no SAFETY.md
  cross-checks needed beyond scissors/craft-knife callout in the mini
  project.
