# Backlog - Topic 3.6 - Electronic Speed Controllers

Source: audit of the merged text (1,187 lines) against `STYLE-GUIDE.md` on
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
- **Length:** 1,187 lines, inside the target.
- **Looking Ahead** names the correct next topic (3.7).

## Links in this topic (keep them - verify and flag)

| Link | Where | Check result 2026-08-06 |
| --- | --- | --- |
| Spektrum Firma 25A brushed ESC manual (PDF) | Learn More, Watch the build | 200 - **rot-prone CDN hash path**, cited 2× |
| Spektrum Firma 100A brushless manual (PDF) | Learn More | 200 - **rot-prone CDN hash path** |
| Hobbywing - QuicRun 1060 brushed ESC | Learn More | 200 - **product page, see below** |
| Hobbywing support - QuicRun 1080 install video | Watch the build | 200 |

## Items to apply

- [ ] [E] **Verify all four links and flag anything wrong.**
- [ ] [E] **Decide and record the Hobbywing product-page exception.** Section 8
  says avoid sales-heavy pages, and
  `hobbywingdirect.com/products/quicrun-10-brushed-esc` is a product listing.
  It is cited for its published specification table - motor, battery,
  continuous and peak current, BEC, PWM and protection - which the
  manufacturer publishes nowhere more stable. Recommendation: **keep it and
  record it as an argued exception in the review report**, with the entry's
  half-line making clear the reader is going there to read specifications.
- [ ] [E] **Add search fallbacks to the two Spektrum manual PDFs.**
- [ ] [E] **No BBC Bitesize entry.** Switching, control and electrical power
  are KS3 physics and D&T; one entry fits the PWM section.
- [ ] [E] **Split the single Learn More box:** the Firma manuals beside the
  calibration and running-mode sections, Hobbywing beside the selection-gates
  section. The Firma 25A manual then appears twice within a few screens of the
  mini project - keep both instances only if they serve different jobs.
- [ ] [C] **7 New Words missing from `glossary.md`** - the largest gap in the
  part: `Brake force`, `Drag brake`, `Electronic commutation`,
  `Low-voltage cut-off (LVC)`, `Pulse-width modulation (PWM)`,
  `Running mode`, `Thermal protection`.
- [ ] [T] **Break markers: 1.** At 1,187 lines this wants three or four.
- [ ] [T] **Check the commissioning safety sequence.** The topic's strongest
  claim is that calibration happens adult-led with drive disabled. Confirm it
  is stated before every procedure that needs it and agrees with `SAFETY.md`.
- [ ] Verify: New Words in `glossary.md`; every gloss number correct against
  `SUMMARY.md`; every activity has a no-equipment variant; safety callouts sit
  before the hazard and agree with `SAFETY.md`.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + the board in
  part-3-book-wide.md.

## Research topics (run before editing)

- Confirm both Firma manuals still describe calibration and protection modes
  as the topic claims.
- Confirm the QuicRun specification figures the topic relies on.
- Cross-check every safety-adjacent statement against `SAFETY.md`.

## Research notes

(To be filled during the pass.)
