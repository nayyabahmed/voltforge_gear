# Backlog - Topic 2.5 - Designing Simple Parts

Source: audit of the v0.1 text (1,922 lines, 14 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 2 of the Part 2 review.

Sittings: 5. Well over the length target (1,922 lines against a 1,200
ceiling) with only **two** break markers - the worst length-to-marker ratio
in Part 2 alongside 2.7 and 2.9. Seams: "Shape Beats Bulk" (~341), "Holes
Have Jobs" (~475), "Guided Design - Universal Cable-Tie Mount" (~814),
"Step 11 - Print the Risk, Not the Part" (~1156), and one before the
activities (~1333).

## Items to apply

- [ ] [T] **Add three or four break markers** at the seams above. Do this
  first - at 1,922 lines this is the item that most changes the reading
  experience. Per the standing decision, no split.
- [ ] [C] **No forward glosses at all.** "receiver mounts" (~60) and the
  receiver requirement worked through ~113-118 are the clear offenders;
  "battery stops" and "electronics tray" also appear early. Gloss on first
  use with home topics per `SUMMARY.md` (receiver 3.4, batteries 3.3).
- [ ] [E] **Trailing `# Learn More` section at ~1906** - between Topic
  Checklist and Looking Ahead, outside the template order and far from what
  it supports. Break it into inline `> **📚 Learn more**` boxes next to the
  relevant sections: design-for-printing guidance at "Design for
  Support-Free Printing" (~656) and a structures reference at "Shape Beats
  Bulk" (~341) or "Ribs" (~388).
- [ ] [V] **Five sketch placeholders is the best count in Part 2**, but the
  topic is also the second longest and almost every section is spatial.
  Gaps worth filling: "Keep Holes Away from Edges" (~504), "Capturing a
  Nut" (~574), "Avoid Knife-Edge Features" (~638). Confirm the signature
  visual is unambiguous - the load-path or shape-beats-bulk illustration is
  the right candidate for the hardest idea.
- [ ] [T] **Two "Think about it" prompts already present** - confirm
  placement. The strongest candidate in the topic is "Shape Beats Bulk"
  (~341): a sheet of paper held flat versus folded into a channel. It is
  also in the analogy bank territory and needs no equipment.
- [ ] [T] **The guided design runs from ~814 to ~1252** - twelve numbered
  steps plus a coupon test plan. Confirm it reads as a build a reader can
  actually follow, that each step states its pass condition, and that
  "Read the Failure" (~1252) closes the loop. This is the longest
  continuous instruction sequence in Part 2.
- [ ] [T] **Check the maths has a fully worked example.** Critical
  dimensions (~264), hole-to-edge distance (~504) and the coupon test plan
  (~1184) all involve numbers.
- [ ] [C] **Terminology check: "Wall".** This topic defines wall as a thin
  sheet-like region of a part; Topic 2.3 defines it as a printed loop around
  a layer. Both senses are legitimate and the glossary now carries both, but
  confirm this topic acknowledges the other meaning on first use so the
  reader is not tripped up.
- [ ] [C] **"Captive nut" vs "captured nut".** This topic says captive
  (~574); Topic 2.7 says captured (~898). Pick one for the terminology
  registry and apply it in both topics - the glossary currently leads with
  Captive Nut and cross-references the other.
- [ ] Verify: all 14 New Words in `glossary.md` (they are); Looking Ahead
  names Topic 2.6 (it does); every activity has a no-equipment variant
  (Activities 1-4 are equipment-free; Activity 5 needs CAD); mini project
  keeps its adult-check line and Watch-the-build box.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
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

## Research notes

(To be filled during the pass.)
