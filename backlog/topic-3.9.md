# Backlog - Topic 3.9 - Steering Systems

Source: audit of the merged text (1,101 lines) against `STYLE-GUIDE.md` on
2026-08-06, re-audited the same day against the section 13 conventions. See
[part-3-book-wide.md](part-3-book-wide.md) for method, for the standing
decision that deep links are KEPT, and for the sweeps that apply to every
topic.

Status: **NOT STARTED**.

## What this topic already has

- **Figures: 12**, all tagged, numbered, captioned and with alt text. **Do not
  add figures.**
- **Answers:** 12, matching its 12 review questions.
- **Think-about-it prompts:** 2, each followed immediately by its resolution.
- **Length:** 1,101 lines, inside the target.
- **Looking Ahead** names the correct next topic (3.10).
- **BBC Bitesize is already cited** (linkages, mechanical systems).
- **The Ackermann worked example is properly structured** - known values, the
  rule, the calculation, then the meaning. It is the model the rest of the
  part's maths should match.

## Links in this topic (keep them - verify and flag)

| Link | Where | Check result 2026-08-06 |
| --- | --- | --- |
| Tekno RC EB48 2.1 manual (PDF) | Learn More | 200 - **rot-prone CDN path** |
| ARRMA TLR Tuned Typhon manual (PDF) | Learn More | 200 - **rot-prone CDN path** |
| Team Associated DR10 manual (PDF) | Learn More | 200 - **rot-prone CDN path** |
| BBC Bitesize - linkages, mechanical systems | Watch the build | search form, no URL |

## Items to apply

- [ ] [E] **Verify all three URLs and flag anything wrong.** This topic has
  the highest concentration of rot-prone links in the part: every one of its
  three external references is a manufacturer PDF on a CDN path.
- [ ] [E] **Add search fallbacks to all three manual PDFs.**
- [ ] [E] **Split the single Learn More box:** Tekno beside the Ackermann
  section, ARRMA beside the ride-height and bump-steer section, Team
  Associated beside the inside/outside wheel-angle explanation.
- [ ] [C] **6 New Words missing from `glossary.md`:**
  `Ackermann steering geometry`, `Free play`, `Movement envelope`,
  `Steering arm`, `Steering centre`, `Steering link`.
- [ ] [T] **Break markers: 1.** At 1,101 lines this wants three.
- [ ] [T] **Re-check the Ackermann arithmetic.** The worked example uses a
  300 mm wheelbase, 240 mm track and 600 mm centre radius to derive 32.0° and
  22.6°. Recompute both, confirm the wheelbase and track are plausible for the
  buggy the book is building, and confirm the simplified angle rule is
  described as simplified.
- [ ] Verify: New Words in `glossary.md`; every gloss number correct against
  `SUMMARY.md`; every activity has a no-equipment variant; safety callouts sit
  before the hazard and agree with `SAFETY.md`.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + the board in
  part-3-book-wide.md.

## Research topics (run before editing)

- Confirm all three manuals still contain the geometry pages the topic points
  the reader at.
- Recompute the Ackermann example and check the plausibility of its inputs.
- Cross-check every safety-adjacent statement against `SAFETY.md`.

## Research notes

(To be filled during the pass.)
