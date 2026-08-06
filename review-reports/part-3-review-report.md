---
title: "Part 3 Review Report - Electronics and Vehicle Systems"
part: "Part 3 - Electronics and Vehicle Systems"
topics: "3.1-3.10"
review_date: "2026-08-06"
branch: "Part_3_review"
outcome: "All ten topics at v0.2 Reviewed"
---

# Part 3 Review Report

Topics 3.1-3.10, reviewed against `style-guides-principles/STYLE-GUIDE.md`
including the section 13 conventions added on 2026-08-06.

**Outcome: all ten topics moved from v0.1 Draft to v0.2 Reviewed.**

---

# 1. Headline 🎯

Part 3 arrived in better shape than any part before it. It had been revised
against the style guide and the figure system before this review started, and
the audit confirmed that: the figures are complete and well specified, the
answers are complete, the safety content holds, and the newest and least-tested
part of the style guide - section 13, written the same week - needed nothing at
all.

What was actually wrong was narrower than expected and almost entirely about
**pacing, the glossary and where references sit on the page**. Three of the
four biggest items in the original backlog turned out, on re-audit, to be
wrong or overstated.

| Measure | Before | After |
| --- | --- | --- |
| Topics at v0.2 | 0 | 10 |
| New Words missing from `glossary.md` | 35 | 0 |
| Topics with a single break marker | 8 | 0 |
| Break markers per topic | 1-3 | 3 |
| Reference boxes at the end of the topic | 10 | 0 |
| Topics with no BBC Bitesize entry | 5 | 0 |
| Unique external links | 33 | 33 |
| Broken links | 0 | 0 |

---

# 2. The deep-link decision 🔗

The backlog written earlier the same day carried an item to convert all 33 deep
URLs into the `search X on site Y` form that section 8 preferred. **That item
was withdrawn on the author's instruction, and the reasoning is now recorded in
the style guide itself** (new section 8.1).

> Part 3 keeps its deep links. They are the difference between reading *about*
> an ESC and reading the actual manual of a real ESC, and the whole part is
> built on comparing the handbook's reasoning against manufacturer
> documentation. A search term cannot carry a reader to the page of a specific
> manual.

Three things were done instead of converting:

1. **Every link was verified.** Results below.
2. **Rot-prone links keep the URL and gain the search term**, rather than
   choosing between them.
3. **Section 8's approved-source list was extended** to cover what Part 3
   actually cites, so the links are compliant rather than tolerated.

## 2.1 Verification results

33 unique URLs. Automated reachability check (`curl -L`, browser user-agent,
25 s timeout), then a content check on everything that did not return 200.

| Result | Count |
| --- | ---: |
| HTTP 200, content matches what the topic claims | 30 |
| HTTP 403 to automated checks, confirmed live by other means | 3 |
| Dead, moved or changed meaning | **0** |

**No link in Part 3 is broken.** Nothing was removed.

## 2.2 Issues flagged 🚩

Four things are worth the author's attention. None of them is a dead link, and
none was resolved by deleting anything.

### 🚩 1. Science Buddies blocks automated verification (3 links)

`sciencebuddies.org/stem-activities/paper-circuit` (Topic 3.2),
`.../teacher-resources/lesson-plans/lifting-with-a-lever` and
`.../stem-activities/pantograph` (both Topic 3.5) return **HTTP 403** to
`curl` *and* to an automated page fetch. This is bot protection, not rot.

All three were confirmed live and correct through the search index: the paper
circuit activity (copper tape, coin cell, LED), the lever lesson plan (ruler,
pencil, bar of soap, pennies) and the pantograph activity (cardboard levers,
scaled copies) all exist and all describe what the topics say they describe.

**Status: kept, verified indirectly.** Worth knowing that any future automated
link-checker will keep reporting these three as failures. They are not.

### 🚩 2. One product page, kept as an argued exception

Topic 3.6 cites `hobbywingdirect.com/products/quicrun-10-brushed-esc`, and
section 8 says avoid sales-heavy pages.

It is kept. The topic sends the reader there to read a real ESC's published
specification table - motor type, battery range, continuous and peak current,
BEC, PWM and protection - and run the six selection gates against it, and the
manufacturer publishes those figures nowhere more stable. The entry's wording
was changed to say so plainly: *"Go there to read the specification table and
run the gates on it, not to buy anything."*

**Status: deliberate exception, recorded here rather than left implicit.**

### 🚩 3. Thirteen links sit on paths that will not age well

These are the most likely thing in Part 3 to break, because the path carries a
build hash, a CMS artefact or a dated upload folder:

| Pattern | Example | Count |
| --- | --- | ---: |
| Spektrum CDN build hash | `.../default/dwb9935bc5/Manuals/...` | 4 |
| Horizon Hobby manuals CDN | `.../default/Manuals/TKR9605_Manual.pdf` | 4 |
| WordPress upload folder | `/wp-content/uploads/2024/07/...` | 3 |
| Maxon CMS path | `/medias/sys_master/root/8812125782046/...` | 1 |
| Spektrum ProdInfo | `/ProdInfo/Files/LOS03028-Manual-EN.pdf` | 1 |

Every one of them works today. Each now keeps its URL **and** names the search
term that would find the document again - for example *"If the link has moved,
search 'Firma 25A ESC manual' on spektrumrc.com."*

**Status: kept, with a route back if they break.**

### 🚩 4. Four documents were cited twice for the same reason

Topic 3.8 cited Pololu's `30:1` gearmotor example in both its Watch the build
and Learn More boxes; Topic 3.10 did the same with both Tekno documents; Topic
3.2 cited PhET three times. In each case the repeat was dropped and the link
kept where it does the teaching. **No link left the topic.**

---

# 3. What changed in the topics ✏️

## 3.1 Reference boxes moved to where they are useful

Every topic ended with a `# Learn More` heading holding all three of its
references, sitting between Topic Checklist and Looking Ahead - a heading that
is not in the section 3 template, in the one place a reader has already stopped
reading. Section 8 asks for boxes "placed next to the relevant section".

All ten blocks were split and the entries moved beside the section each one
serves: NIST beside Ohm's law, Fluke beside meter placement, Ofcom beside the
radio-licensing paragraph, the Spektrum receiver manual beside binding and
failsafe, KHK beside gear types, the Tekno setup guide beside the ride-height
fair test, and so on.

## 3.2 Pacing

Eight topics ran 1,074-1,200 lines behind a single break marker. Every topic
now carries three, placed at real seams - where the subject changes rather than
at a fixed interval.

## 3.3 BBC Bitesize

The first audit claimed Part 3 had no Bitesize anywhere. **That was wrong** -
it was cited in five topics, mostly inside Watch the build boxes, which a
Learn More-only search missed. The five that genuinely lacked it now have one,
using national-curriculum wording per section 8: current and voltage in
circuits (3.2), energy stores and transfers (3.3), waves and communication
(3.4), mechanical systems (3.5), electrical power (3.6).

## 3.4 Glossary

35 New Words introduced by the revisions were missing from `glossary.md`. All
are now present. Four already existed under a different name and were merged
rather than duplicated - `Ackermann Geometry` → `Ackermann Steering Geometry`,
`Low-Voltage Cut-Off` → `Low-Voltage Cut-Off (LVC)`, `Pulse-Width Modulation`
→ `Pulse-Width Modulation (PWM)`, `Sensored Motor` → `Sensored` - so the New
Words table and the glossary now agree, which is what the HTML build's
tooltips key on (section 13.2).

## 3.5 Topic 3.1's second think-about-it prompt

Topic 3.1 was the only topic in the part with one prompt where the others had
two. It now has a second, at the claim a reader will not predict: two plugs
that mate perfectly prove nothing about what is behind them. That is the
reason its eight compatibility checks exist, and it was being asserted rather
than earned.

---

# 4. Maths re-checked 🧮

Every worked example in the part was recomputed. **All correct as written** -
nothing needed changing.

| Topic | Example | Check |
| --- | --- | --- |
| 3.2 | `I = 6 ÷ 12` | 0.5 A ✓ |
| 3.2 | `P = 7.4 × 5` | 37 W ✓ |
| 3.2 | Contact loss at 0.05 Ω, 20 A | 1 V drop, 20 W ✓ |
| 3.2 | I²R claim: 10 A → 20 A | 5 W → 20 W, four times ✓ |
| 3.5 | Arc length `12 × 0.524` | 6.3 mm ✓ (30° = 0.5236 rad) |
| 3.6 | Duty cycle `7 ÷ 10` | 70% ✓ |
| 3.6 | Headroom `40 - 25` | 15 A ✓ |
| 3.7 | kV: `3000 × 7.4` | 22,200 RPM ✓ |
| 3.8 | Ratio `60 / 20`, speed `18,000 / 3` | 3:1, 6,000 RPM ✓ |
| 3.8 | Compound `3 × 2.5`, `15,000 / 7.5` | 7.5:1, 2,000 RPM ✓ |
| 3.9 | Ackermann `arctan(300/480)`, `arctan(300/720)` | 32.0°, 22.6° ✓ |

A 20-tooth pinion on a 60-tooth spur, a 300 mm wheelbase and a 240 mm track
are all plausible for the 1/10-scale buggy the book is building.

---

# 5. Checked and found already compliant ✅

Recorded so no future pass re-derives it.

- **Section 13 (authoring for three outputs) needed nothing.** This is the
  newest and least-tested part of the style guide, written the same week, and
  Part 3 already met all of it: every code fence carries a language tag, no
  fence is being used to lay out a table, there is no raw HTML anywhere in the
  part, the fixed callout markers are used exactly as registered, and Topic
  Checklists use `- [ ]`.
- **Think-about-it resolutions are correctly placed.** Section 13.3 forbids
  anything between the prompt and its answer. All 19 prompts (now 20) are
  followed immediately by a single resolution paragraph, with the figure after
  it. Checked mechanically across all ten topics.
- **Figures: complete and good.** 11 or 12 per topic against a 10-12 budget,
  every one tagged F1-F7 or Signature visual, every one with a number, a
  caption and alt text. Part 3 is the best-illustrated part in the book. No
  figures were added.
- **Answers: complete.** Twelve answers against twelve review questions, in
  all ten topics.
- **Looking Ahead: correct in all ten**, 3.1 → 3.2 through 3.9 → 3.10, and
  3.10 → Topic 4.1 opening Part 4.
- **Length: within target** at 1,074-1,200 lines before the review, 1,085-1,220
  after. The first part in the book that never overran.
- **Terminology registry: clean.** "gearbox" appears seven times in Topic 3.8
  and every use is correct. No "chapter", no "hinge-pin", no "captured nut",
  no "requirements traceability".
- **British English: clean.**
- **Safety: Topic 3.3 does not drift from `SAFETY.md`.** All three LiPo
  non-negotiables are present and expanded, plus balance charging. It also
  defers every charge current, cut-off and storage voltage to the
  manufacturer's instructions rather than printing a number a reader might
  apply to the wrong pack - which is the right call and stays.
- **Mermaid: two blocks in the whole part** (3.1 and 3.4), both genuine flows.

---

# 6. Corrections to the first audit ⚠️

The backlog written the same morning made three claims the re-audit disproved.
Recorded so they are not repeated.

| Claim | Verdict |
| --- | --- |
| "No BBC Bitesize anywhere in Part 3" | **Wrong.** Cited in five topics, inside Watch the build boxes. |
| "Topic 3.1 is the only topic with no external links at all" | **Wrong.** It has five references, already in search form - which is why a URL grep found none. 3.1 was the model, not the gap. |
| "3.2 line 536 drops a bare link into prose" | **Overstated.** It is a PhET entry in an activity's "You will need" list, where a materials entry belongs. Left alone. |

---

# 7. Debts carried forward 📋

Nothing blocking, but recorded honestly.

| Debt | Detail |
| --- | --- |
| Figures are still placeholders | Every figure in Part 3 is a specified art brief, not artwork. This is the same debt the whole book carries; the briefs are good enough to draw from. |
| Automated link checks will report 3 false failures | The Science Buddies pages. See §2.2. |
| 13 links on rot-prone paths | Working today, with search fallbacks in place. Worth a re-check when Part 3 next moves version. |
| Reference docs unfed by Part 3 | `TROUBLESHOOTING.md`, `TOOLS.md`, `BOM.md` and `COST-LEDGER.md` do not yet list Topic 3.x as a feeder, though 3.3 (battery safety), 3.6 (ESC protection modes) and 3.8 (drivetrain wear) are natural sources. |
| `SAFETY.md` unchanged | Part 3's LiPo, radio and commissioning content agrees with it, but SAFETY.md's frontmatter feeds list was not updated to name the Part 3 topics. |

---

# 8. Method

Followed the per-topic loop in `backlog/PLAN.md`, which every review since
Part 1 has used: read the topic and its backlog, run the research pass before
editing, apply the items, apply the book-wide sweeps, verify against the
publishing checklist, then bump the version - only at the end.

Working files: `backlog/part-3-book-wide.md` (kept, with the standing
decisions) and `backlog/topic-3.1.md` … `topic-3.10.md` (deleted on completion
per the project convention - their content, including these research notes, is
in git history).

Commits on `Part_3_review`:

| Commit | Scope |
| --- | --- |
| `2201b37` | Re-audit the backlogs against the updated style guide |
| `85fa7cf` | Extend section 8 for manufacturer sources and deep links |
| `40d657d` | Backfill Part 3's New Words into the glossary |
| `ed2034b` | Apply the review to Topics 3.1-3.3 |
| `0cf95aa` | Apply the review to Topics 3.4-3.6 |
| `cd50b86` | Apply the review to Topics 3.7-3.10 |
