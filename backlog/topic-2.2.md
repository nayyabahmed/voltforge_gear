# Backlog - Topic 2.2 - 3D Printing Fundamentals

Source: audit of the v0.1 text (530 lines, 15 new words) against
`STYLE-GUIDE.md` on 2026-08-06. No frozen external review exists for Part 2
- see [part-2-book-wide.md](part-2-book-wide.md). Line numbers refer to the
v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 1 of the Part 2 review (with Topic 2.1).

Sittings: 1-2. Inside the length target; the two existing break markers are
adequate. Natural seam is at "What Printers Do Badly" (~308), where the
topic turns from how printing works to what it costs and constrains.

**Context:** like Topic 2.1, written before the 2026-07-12 conventions.

## Items to apply

- [ ] [T] **Emoji pass.** No template heading carries its fixed emoji. All
  seven need it: Learning Objectives 🎯 (~29), Common Beginner Mistakes ❌
  (~432), Topic Summary 📝 (~460), New Words 📖 (~475), Review Questions ❓
  (~497), Topic Checklist ✅ (~511), Looking Ahead 🔭 (~524). Check the
  single safety callout uses the `> **⚠️ SAFETY**` marker and the two Learn
  More boxes use `> **📚 Learn more**`.
- [ ] [T] **Looking Ahead does not name the next topic.** It describes the
  slicer topic accurately (~526-528) but never says "Topic 2.3", then names
  "Topic 2.4 (CAD Fundamentals)" (~530) as the one after. A reader skimming
  the section comes away with 2.4 as the next number. Style guide section 3
  item 14 requires the ACTUAL next topic to be named and its number
  verified. Name Topic 2.3 - Slicer Software and First Prints explicitly.
- [ ] [T] **Topic Mini Project is missing.** Candidate: a **contour-stack
  model** - trace a simple curved solid (a cone, a hill, a buggy wheel
  hub) as a set of card contours, cut them, stack and glue them into a
  keepable physical "print". It embodies this topic's core idea directly
  (layers approximate a shape) and produces the staircase effect on curves
  as a visible, touchable result. Hands-On Activity 1 "Slice a Shape by
  Hand" (~384) is already the first half of this build - extend it into the
  mini project rather than inventing a second, unrelated one. Needs the
  adult-check line, a Watch-the-build box, a reflection step, and a
  "keep it for the showcase shelf" close.
  Note: keep it visibly distinct from Topic 2.3's Laminated Cardboard Cable
  Guide, which is also a card-lamination build - this one is about
  approximating a curve, that one is about a working part.
- [ ] [T] **No "Think about it" prompts.** Two strong candidates, both at
  claims the reader will not predict:
  - "Layers Are the Weak Direction" (~193) - the anisotropy claim is the
    most counter-intuitive thing in the topic. Use the deck-of-cards
    analogy from the analogy bank: push a stack of cards sideways versus
    squash it flat.
  - "Overhangs and Supports" (~269) - why the printer cannot simply draw
    plastic in mid-air.
  Pick one or both; the anisotropy one is the priority.
- [ ] [C] **No forward glosses at all.** The topic uses buggy vocabulary
  from Part 3 with no pointers: "servo and motor mounts" (~92) is the clear
  offender. Add first-use glosses with home topics per `SUMMARY.md` (servo
  3.5, motors 3.7). Check the "Why This Matters for Our Buggy" section
  (~83) as a whole - that is where the forward references cluster.
- [ ] [C] **Filament and temperature vocabulary.** "PLA vs PETG" (~354)
  arrives late but the terms are used earlier. Confirm each is bolded and
  glossed on FIRST use, and that the topic defers material depth to Topic
  2.6 explicitly rather than half-teaching it.
- [ ] [E] **Learn More.** Two boxes exist, which is acceptable for a topic
  this length - verify both sources still exist, use approved sources, and
  use curriculum wording for any Bitesize search term. Consider a third at
  "Layers Are the Weak Direction" if a good anisotropy explainer verifies.
- [ ] [V] **Visuals are in reasonable shape** - four sketch placeholders,
  two mermaid blocks. Confirm the mermaid at each location is a genuine flow
  or cycle rather than a bullet list drawn as boxes (visuals policy), and
  confirm the topic has one clear signature visual for its hardest idea
  (layer adhesion / the weak direction is the right candidate).
- [ ] Verify: all 15 New Words in `glossary.md` (they are); every activity
  has a no-equipment variant (Activities 1 and 2 are equipment-free,
  Activity 3 is correctly marked "if you have a printer"); `estimated_time`
  bumped for the new mini project.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

- Print and bed temperature figures for PLA and PETG, and any layer-height
  or speed numbers quoted - verify against Prusa or Bambu knowledge bases
  before they go to v0.2.
- Layer adhesion and anisotropy: confirm the plain-language explanation of
  WHY the layer direction is weaker matches how manufacturers describe it.
- Warping (~253): confirm the stated causes and the first-layer advice.
- Whether a Bitesize KS3 D&T page covers 3D printing or additive
  manufacturing in curriculum wording, for the Learn More boxes.
- Mini project: find at least one photo or video tutorial for a
  contour-stack / card-lamination model for the Watch-the-build box.

## Research notes

(To be filled during the pass.)
