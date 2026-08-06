# Backlog - Topic 3.7 - Brushed and Brushless Motors

Source: audit of the merged text (1,190 lines) against `STYLE-GUIDE.md` on
2026-08-06, re-audited the same day against the section 13 conventions. See
[part-3-book-wide.md](part-3-book-wide.md) for method, for the standing
decision that deep links are KEPT, and for the sweeps that apply to every
topic.

Status: **NOT STARTED**.

## What this topic already has

- **Figures: 12**, all tagged, numbered, captioned and with alt text. **Do not
  add figures.**
- **Answers:** 12, matching its 12 review questions.
- **Think-about-it prompts:** 2 - the kV-label trap and the stall question,
  each followed immediately by its resolution. Both land on genuinely
  counter-intuitive claims, which is exactly what section 2 asks for.
- **Length:** 1,190 lines, inside the target.
- **Looking Ahead** names the correct next topic (3.8).
- **BBC Bitesize is already cited** (electromagnets and motors, in Watch the
  build).

## Links in this topic (keep them - verify and flag)

| Link | Where | Check result 2026-08-06 |
| --- | --- | --- |
| Maxon - Motion Control for Newbies (PDF) | Learn More | 200 - **rot-prone `sys_master` path** |
| Maxon - Motor constants | Learn More | 200 |
| Pololu - Choosing the motor and power system | Learn More | 200 |
| Explain That Stuff - Electric motors | Watch the build | 200 |
| BBC Bitesize - electromagnets and motors | Watch the build | search form, no URL |

## Items to apply

- [ ] [E] **Verify all four URLs and flag anything wrong.**
- [ ] [E] **Add the search fallback to the Maxon PDF.** The `sys_master` path
  is a content-management artefact and will not survive a site change.
- [ ] [E] **Split the single Learn More box:** the two Maxon references beside
  the kV and motor-constants section, Pololu beside the selection section.
- [ ] [C] **4 New Words missing from `glossary.md`:** `No-load speed`,
  `Phase`, `Sensored`, `Sensorless`.
- [ ] [T] **Break markers: 1.** At 1,190 lines this wants three or four.
- [ ] [T] **Re-check the kV worked example.** The topic states a speed
  constant, multiplies it by a voltage and then argues about what the answer
  does not prove. The arithmetic and the units both need re-checking, and the
  result must be read back in words per section 2.
- [ ] [T] **Check the stall claim.** "Back EMF collapses, current rises, the
  energy becomes heat" is the topic's most important safety-adjacent
  statement. Confirm it against the Maxon motor-constants page.
- [ ] Verify: New Words in `glossary.md`; every gloss number correct against
  `SUMMARY.md`; every activity has a no-equipment variant; safety callouts sit
  before the hazard and agree with `SAFETY.md`.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + the board in
  part-3-book-wide.md.

## Research topics (run before editing)

- Confirm kV, back EMF and torque-constant relationships as stated.
- Confirm the no-load / stall current behaviour the topic describes.
- Cross-check every safety-adjacent statement against `SAFETY.md`.

## Research notes

(To be filled during the pass.)
