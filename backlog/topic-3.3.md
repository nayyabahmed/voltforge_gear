# Backlog - Topic 3.3 - Batteries and Battery Safety

Source: audit of the merged text (1,200 lines) against `STYLE-GUIDE.md` on
2026-08-06, re-audited the same day against the section 13 conventions. See
[part-3-book-wide.md](part-3-book-wide.md) for method, for the standing
decision that deep links are KEPT, and for the sweeps that apply to every
topic.

Status: **NOT STARTED**. **This is the highest-risk topic in Part 3** - it
carries the LiPo safety content, so its research pass is not optional.

## What this topic already has

- **Figures: 12**, all tagged, numbered, captioned and with alt text. **Do not
  add figures.**
- **Answers:** 12, matching its 12 review questions.
- **Think-about-it prompts:** 2, each followed immediately by its resolution.
- **Break markers: 2** - only 3.1 has more.
- **Length:** 1,200 lines, at the top of the target.
- **Looking Ahead** names the correct next topic (3.4).
- **Safety: agrees with `SAFETY.md`.** All three LiPo non-negotiables are
  present and expanded - fire-resistant bag, never unattended, never a puffed
  or damaged pack, correct charger and settings, plus balance charging. This
  is the failure that had to be corrected in Topic 2.1 and it did not recur.

## Links in this topic (keep them - verify and flag)

| Link | Where | Check result 2026-08-06 |
| --- | --- | --- |
| London Fire Brigade - Batteries and chargers | Learn More, Watch the build | 200, cited 2× |
| Spektrum - LiPo Battery Safety Sheet (PDF) | Learn More | 200 - **rot-prone CDN path** |
| GOV.UK - Recycling batteries and electrical waste | Learn More | 200 |
| Horizon Hobby - How to charge RC batteries | Watch the build | 200 |

## Items to apply

- [ ] [E] **Verify all four links and flag anything wrong.** Safety guidance
  changes; confirm the LFB and GOV.UK pages still say what the topic claims
  before this topic reaches v0.2.
- [ ] [E] **Add the search fallback to the Spektrum PDF.** Keep the URL and
  name the site and search term, so a reader can find the safety sheet again
  when the CDN path changes.
- [ ] [E] **No BBC Bitesize entry.** Chemical energy stores and cells are KS3
  physics; one entry using national-curriculum wording would connect the
  topic to what the reader hears at school.
- [ ] [E] **Split the single Learn More box** into inline boxes: LFB and the
  Spektrum safety sheet beside the charging-safety section, GOV.UK beside the
  disposal section. The LFB link then appears twice within a few screens -
  keep the Watch the build instance and drop the duplicate wording, not the
  link.
- [ ] [C] **4 New Words missing from `glossary.md`:** `Balance lead`,
  `Cell count`, `Main lead`, `Nominal voltage`.
- [ ] [T] **Break markers: 2.** At 1,200 lines this wants three or four.
- [ ] [T] **Re-check every stated cell voltage and charge rate** against
  `SAFETY.md` and manufacturer guidance - 3.7 V nominal, 4.2 V full, the
  storage voltage, the 1C default. A wrong number here is the one error in
  the book that could hurt someone.
- [ ] Verify: New Words in `glossary.md`; every gloss number correct against
  `SUMMARY.md`; every activity has a no-equipment variant; safety callouts sit
  before the hazard and agree with `SAFETY.md`.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + the board in
  part-3-book-wide.md.

## Research topics (run before editing)

- Re-verify every LiPo safety statement against current UK guidance and
  `SAFETY.md`.
- Confirm the GOV.UK recycling route is still current.
- Re-check every stated voltage, capacity, C-rating and charge current.

## Research notes

(To be filled during the pass.)
