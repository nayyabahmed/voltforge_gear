# Backlog - Topic 3.5 - Steering Servos

Source: audit of the merged text (1,196 lines) against `STYLE-GUIDE.md` on
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
- **Length:** 1,196 lines, inside the target.
- **Looking Ahead** names the correct next topic (3.6).

## Links in this topic (keep them - verify and flag)

| Link | Where | Check result 2026-08-06 |
| --- | --- | --- |
| Pololu - Introduction to Servos | Learn More | 200 |
| Pololu - Electrical characteristics of servos | Learn More | 200 |
| Spektrum DX Pro+ manual (PDF) | Learn More | 200 - **rot-prone CDN hash path** |
| Science Buddies - Lifting with a Lever | Watch the build | **403 to automated check** |
| Science Buddies - Pantograph | Watch the build | **403 to automated check** |

## Items to apply

- [ ] [E] **Verify all five links and flag anything wrong.** Both Science
  Buddies pages return 403 to automated checks - bot protection, not rot.
  Confirm each by hand in a browser and record the verdict. Do not delete on
  the strength of a 403.
- [ ] [E] **Add the search fallback to the Spektrum manual PDF.**
- [ ] [E] **No BBC Bitesize entry.** Levers, linkages and mechanical systems
  are KS3 D&T, and the topic's linkage section maps onto them directly. Use
  national-curriculum wording ("mechanical systems", not "mechanisms").
- [ ] [E] **Split the single Learn More box:** the two Pololu articles beside
  the feedback and servo-electrics sections, the Spektrum manual beside the
  travel/reverse/sub-trim section.
- [ ] [C] **5 New Words missing from `glossary.md`:** `Linkage route`,
  `Mechanical stop`, `Position error`, `Servo angle`, `Wheel angle`.
- [ ] [T] **Break markers: 1.** At 1,196 lines this wants three or four.
- [ ] [T] **Check the stall and binding content.** The topic's central safety
  claim is that commanding past a mechanical stop turns into heat and current
  rather than movement. Confirm the described consequence matches the cited
  Pololu article.
- [ ] Verify: New Words in `glossary.md`; every gloss number correct against
  `SUMMARY.md`; every activity has a no-equipment variant; safety callouts sit
  before the hazard and agree with `SAFETY.md`.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + the board in
  part-3-book-wide.md.

## Research topics (run before editing)

- Hand-verify both Science Buddies activities still exist and are buildable
  from household materials.
- Confirm the servo pulse timings and travel angles the topic states.
- Cross-check every safety-adjacent statement against `SAFETY.md`.

## Research notes

(To be filled during the pass.)
