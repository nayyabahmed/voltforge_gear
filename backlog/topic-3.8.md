# Backlog - Topic 3.8 - Gears and the Drivetrain

Source: audit of the merged text (1,185 lines) against `STYLE-GUIDE.md` on
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
- **Length:** 1,185 lines, inside the target.
- **Looking Ahead** names the correct next topic (3.9).
- **BBC Bitesize is already cited** (gears, mechanical systems - and it
  correctly uses the national-curriculum wording section 8 asks for).
- **Terminology: "gearbox" used correctly** all seven times, for a real
  enclosed gear assembly or a donor module. This is the topic where the
  registry rule was most at risk and it holds.

## Links in this topic (keep them - verify and flag)

| Link | Where | Check result 2026-08-06 |
| --- | --- | --- |
| Pololu - Motors and gearboxes | Learn More, Watch the build | 200, cited 2× |
| KHK - Types of gears | Learn More | 200 |
| Losi Lasernut manual (PDF) | Learn More | 200 - **rot-prone `ProdInfo` path** |
| BBC Bitesize - gears, mechanical systems | Watch the build | search form, no URL |

## Items to apply

- [ ] [E] **Verify all three URLs and flag anything wrong.**
- [ ] [E] **Add the search fallback to the Losi manual PDF.**
- [ ] [E] **Pololu is cited twice** - once in Watch the build for its `30:1`
  gearmotor example and once in Learn More for the same example. When the
  Learn More box is split, do not leave the reader the same link twice for the
  same reason.
- [ ] [E] **Split the single Learn More box:** KHK beside the gear-types
  section, Pololu beside the ratio worked example, the Losi manual beside the
  gear-mesh section.
- [ ] [C] **3 New Words missing from `glossary.md`:** `Compound gear train`,
  `Idler gear`, `Reduction`.
- [ ] [T] **Break markers: 1.** At 1,185 lines this wants three or four.
- [ ] [T] **Re-check every ratio calculation.** This topic is the arithmetic
  centre of Part 3 - tooth counts, reduction ratios, the compound-train
  multiplication and the speed-versus-torque trade. Each worked example needs
  question, known values, rule, calculation and meaning in words, and each
  number needs re-checking.
- [ ] [T] **Check the pinion/spur tooth counts are plausible for a 1/10
  buggy** - the same check Part 1 ran on Topic 1.3.
- [ ] Verify: New Words in `glossary.md`; every gloss number correct against
  `SUMMARY.md`; every activity has a no-equipment variant; safety callouts sit
  before the hazard and agree with `SAFETY.md`.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + the board in
  part-3-book-wide.md.

## Research topics (run before editing)

- Confirm the KHK gear-type descriptions match how the topic uses them.
- Confirm the Pololu `30:1` example still reads as the topic claims.
- Re-check every tooth count, ratio and derived speed or torque figure.

## Research notes

(To be filled during the pass.)
