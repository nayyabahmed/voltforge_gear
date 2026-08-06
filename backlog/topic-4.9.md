# Backlog - Topic 4.9 - Electronics Installation

Source: audit of the published text (891 lines) against `STYLE-GUIDE.md`
on 2026-08-06. Part 4 is a build part, so section 11 applies to every topic -
see [part-4-book-wide.md](part-4-book-wide.md) for method, for the standing
decision that deep links are KEPT, and for the sweeps that apply to every
topic.

Status: **NOT STARTED**.

## What this topic already has

- **Figures: 16**, every one tagged, numbered, captioned and with alt text.
  Budget for a build topic is 12-16, so this is met. **Do not add figures.**
- **Answers:** 12, matching its 12 review questions.
- **Section 11 build-topic elements:** all eight present.
- **Length:** 891 lines, inside the 700-1,200 target.
- **Looking Ahead** names the correct next topic (4.10).
- **The installation order** is well reasoned and reuses the command/energy
  path framing from Topic 3.1.
- **Recommission from zero** is the right instruction and is stated plainly.

## Items to apply

- [ ] [S] **Put the LiPo rules in a SAFETY callout - highest priority in Part
  4.** The section "LiPo and Rechargeable Battery Boundary" lists nine correct
  non-negotiables as plain bullets under a plain heading. Every rule is right
  and consistent with `SAFETY.md` and Topic 3.3; the FORM is wrong. Section 9
  requires the callout for anything electrical or chemical, and section 13.2
  is explicit that the marker is what lets the HTML build make a warning
  unskippable. A reader skimming for the next instruction can skim straight
  past this.
- [ ] [T] **No think-about-it prompt at all** - the only topic in Parts 3 and 4
  without one. The candidate is already in the text: a control system that
  worked perfectly in Topic 4.5 must still be recommissioned from zero,
  because the geometry, drivetrain and battery it now drives are different.
- [ ] [V] **Convert all 16 figures to the section 7.7 form.** Caption and alt
  text are currently fused inside the art brief blockquote. Split each into
  brief, then `*Figure 4.9.k - caption.*`, then `*Alt text: ...*`,
  matching Topic 4.1.
- [ ] [T] **Break markers: 1.** At 891 lines this wants three. Place
  them at the natural seams where the topic changes subject.
- [ ] [C] **5 New Words missing from `glossary.md`:** `Abrasion`,
  `Dummy battery`, `Installation order`, `Pinout`, `Pre-test certificate`.
- [ ] [E] **Split the single Learn More box.** It sits under a `# Learn More`
  heading between Topic Checklist and Looking Ahead - a heading that is not in
  the section 3 template. Move each entry beside the section it serves.
- [ ] [E] **The Firma ESC manual is cited twice** for the same reason, and both
  it and the Spektrum receiver manual are CDN hash paths needing search
  fallbacks.
- [ ] [S] **Battery-mounting cautions appear before the safety callout** - "do
  not crush a soft battery pouch with an over-tight strap" is a LiPo warning
  sitting in ordinary prose.
- [ ] [V] **Check the Mermaid block** against the section 7.1 test.

- [ ] Verify: New Words in `glossary.md`; every gloss number correct against
  `SUMMARY.md`; safety callouts sit before the hazard and agree with
  `SAFETY.md`; the test plan states its independent, dependent and control
  variables and a pass condition.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + the board in
  part-4-book-wide.md.

## Research topics (run before editing)

- Re-verify every LiPo statement against `SAFETY.md` and Topic 3.3 - they
  must not diverge.
- Confirm both manuals still describe calibration and failsafe as claimed.
- Confirm the strain-relief and abrasion guidance matches Topic 2.9.

## Research notes

(To be filled during the pass.)
