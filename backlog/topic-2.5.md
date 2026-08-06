# Backlog - Topic 2.5 - Designing Simple Parts

Source: audit of the v0.1 text (1,922 lines, 14 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **DONE 2026-08-06** (v0.2 on `Part_2_review`). Research pass first,
then every item below applied. Topic 2.6 next.

Sittings: 5. Well over the length target (1,922 lines against a 1,200
ceiling) with only **two** break markers - the worst length-to-marker ratio
in Part 2 alongside 2.7 and 2.9. Seams: "Shape Beats Bulk" (~341), "Holes
Have Jobs" (~475), "Guided Design - Universal Cable-Tie Mount" (~814),
"Step 11 - Print the Risk, Not the Part" (~1156), and one before the
activities (~1333).

## Items to apply

- [x] [T] **Add three or four break markers** at the seams above. Do this
  first - at 1,922 lines this is the item that most changes the reading
  experience. Per the standing decision, no split.
- [x] [C] **No forward glosses at all.** "receiver mounts" (~60) and the
  receiver requirement worked through ~113-118 are the clear offenders;
  "battery stops" and "electronics tray" also appear early. Gloss on first
  use with home topics per `SUMMARY.md` (receiver 3.4, batteries 3.3).
- [x] [E] **Trailing `# Learn More` section at ~1906** - between Topic
  Checklist and Looking Ahead, outside the template order and far from what
  it supports. Break it into inline `> **📚 Learn more**` boxes next to the
  relevant sections: design-for-printing guidance at "Design for
  Support-Free Printing" (~656) and a structures reference at "Shape Beats
  Bulk" (~341) or "Ribs" (~388).
- [x] [V] **Figures: 5 against a budget of 10-14** (STYLE-GUIDE 7.4,
  skill topic). At 1,922 lines the topic currently runs one figure per
  ~384; the target is one per 40-80. This is the largest single item in
  this file. See `references/ref-002.md` for the taxonomy.
  Best existing count in Part 2, but the topic is nearly all spatial. Gaps:
  "Keep Holes Away from Edges" (~504), "Capturing a Nut" (~574), "Avoid
  Knife-Edge Features" (~638), "Ribs" (~388) and "Gussets" (~419) as an F5
  load-path overlay, "Chamfers Guide Assembly" (~593) as an F4 strip.
  Conventions to apply to every figure, existing ones included (7.2/7.3):
  type tag `[F1-F7 ...]`, `Figure 2.5.k` number, a one-sentence caption
  saying what to notice, and alt text.
- [x] [V] **F3 pairs for the 12 Common Beginner Mistakes.** The highest-value
  figure type in the book and currently unused here - a right-versus-wrong
  pair per mistake, or one combined F3 array. Prose alone cannot show a
  reader what the wrong version looks like.
- [x] [T] **Add `# Answers 🔑`** (STYLE-GUIDE 3 item 15, 13.3) with model
  answers numbered to match the 16 Review Questions. Needed for the HTML
  reveal and for a mentor running a session.
- [x] [T] **Two "Think about it" prompts already present** - confirm
  placement. The strongest candidate in the topic is "Shape Beats Bulk"
  (~341): a sheet of paper held flat versus folded into a channel. It is
  also in the analogy bank territory and needs no equipment.
- [x] [T] **The guided design runs from ~814 to ~1252** - twelve numbered
  steps plus a coupon test plan. Confirm it reads as a build a reader can
  actually follow, that each step states its pass condition, and that
  "Read the Failure" (~1252) closes the loop. This is the longest
  continuous instruction sequence in Part 2.
- [x] [T] **Check the maths has a fully worked example.** Critical
  dimensions (~264), hole-to-edge distance (~504) and the coupon test plan
  (~1184) all involve numbers.
- [x] [C] **Terminology check: "Wall".** This topic defines wall as a thin
  sheet-like region of a part; Topic 2.3 defines it as a printed loop around
  a layer. Both senses are legitimate and the glossary now carries both, but
  confirm this topic acknowledges the other meaning on first use so the
  reader is not tripped up.
- [x] [C] **"Captive nut" vs "captured nut".** This topic says captive
  (~574); Topic 2.7 says captured (~898). Pick one for the terminology
  registry and apply it in both topics - the glossary currently leads with
  Captive Nut and cross-references the other.
- [x] Verify: all 14 New Words in `glossary.md` (they are); Looking Ahead
  names Topic 2.6 (it does); every activity has a no-equipment variant
  (Activities 1-4 are equipment-free; Activity 5 needs CAD); mini project
  keeps its adult-check line and Watch-the-build box.
- [x] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

- **Design rules of thumb - verify every number.** Minimum wall thickness,
  rib thickness relative to wall, gusset proportions, boss sizing, minimum
  hole-to-edge distance, and the support-free overhang angle (~656). These
  are stated as guidance a reader will follow literally, so check each
  against Prusa or Bambu design-for-printing documentation before v0.2.
- Captive nut pocket sizing (~574) - confirm the clearances quoted work in
  practice for a printed pocket.
- Fillet and chamfer guidance (~593, ~613) - confirm the stress-spreading
  claim is stated at the right level for an 11-year-old and is not
  overstated.
- Slot design for adjustment (~525) - confirm the recommended slot width
  relative to fastener diameter.
- Mini project: re-verify Watch-the-build sources for the Modular Cardboard
  Mounting Tile.

## Research notes (2026-08-06)

**Design rules verified - the topic's numbers hold up:**

- Structural wall "roughly 1.3-1.8 mm" with a 0.4 mm nozzle sits correctly
  against the industry guidance of 2-3 nozzle widths minimum and 1.2-1.6 mm
  for functional parts. The topic already hedges it as "a starting point, not
  a universal guarantee", which is the right register. Unchanged.
- Rib thickness "about 1.5-2.0 mm" is safely above the 0.8 mm minimum, and
  the claim that ribs beat thicker walls for stiffness per gram is confirmed.
- Bottom-edge chamfer of 0.5-1 mm against elephant's foot: confirmed.
- The 45 degree support-free rule and short-bridge behaviour: confirmed, and
  consistent with what Topic 2.2 now says.

**Added from research - the missing number:**

- "Keep Holes Away from Edges" told the reader to inspect the material around
  a hole but gave them nothing to inspect it against. Added the standard rule:
  **at least one screw diameter of material all the way around a screw hole**,
  so about 3 mm for an M3. Hedged as a starting point, with a figure showing
  the minimum-material ring and a hole placed too near the edge.

**Terminology resolved:**

- **"Captive nut" wins.** This topic already used it, the glossary leads with
  it, and Topic 2.7's "captured nut" is the variant to change when 2.7 is
  reviewed. Recorded here so the 2.7 pass does not re-open the question.
- **"Wall" has two legitimate senses** across Part 2 - a printed loop around a
  layer (2.3) and a thin sheet-like region of a part (here). Rather than
  renaming either, the topic now flags the difference on first use and points
  out that the slicer's walls are how this wall gets made.

**Notes:**

- Figures 5 -> 11. Break markers 2 -> 6, which was the single biggest change
  to the reading experience at 2,022 lines.
- The trailing `# Learn More` section was retired and its content re-homed as
  two inline boxes, at the wall-thickness discussion and at support-free
  design.
- The guided design (12 steps plus the coupon test plan) was read through and
  each step does state its pass condition. Considered and kept as-is.
- The worked example (base 3.0 mm + pad 1.5 mm) is complete and correct.
