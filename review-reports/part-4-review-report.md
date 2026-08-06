---
title: "Part 4 Review Report - Design and Build"
part: "Part 4 - Design and Build"
topics: "4.1-4.10"
review_date: "2026-08-06"
branch: "Part_3_review"
outcome: "All ten topics at v0.2 Reviewed"
---

# Part 4 Review Report

Topics 4.1-4.10, reviewed against `style-guides-principles/STYLE-GUIDE.md`,
including section 11 (build topics) and the section 13 conventions.

**Outcome: all ten topics moved from v0.1 Draft to v0.2 Reviewed.**

---

# 1. Headline 🎯

Part 4 is the build part, so the test that mattered most was section 11: does
every topic carry a learning goal, a cheapest valid prototype, parts to
buy/reuse/make, a cost checkpoint, modular interfaces, a test plan, an upgrade
path and a stop point before the next purchase?

**It does - all eight, in all ten topics**, with only Topic 4.2's Learning
Goal heading missing. The fair-test pattern from Topic 1.9 is used throughout.
That is the hardest part of a build topic to retrofit and it was already done.

What was wrong fell into four groups: the **figure format**, **safety callout
form**, the **glossary**, and **pacing**. Two of those had real consequences.

| Measure | Before | After |
| --- | --- | --- |
| Topics at v0.2 | 0 | 10 |
| Figures in the section 7.7 format | 16 of 160 | 160 of 160 |
| New Words missing from `glossary.md` | 71 | 0 |
| Break markers per topic | 1 | 3 |
| Topics with no think-about-it prompt | 1 | 0 |
| Reference boxes at the end of the topic | 10 | 0 |
| Terminology registry breaches | 15 | 0 |
| Project heading names in use | 2 | 1 |
| Unique external links | 19 | 19 |
| Broken links | 0 | 0 |

---

# 2. The two findings that mattered ⚠️

## 2.1 Topic 4.9's LiPo rules were not in a safety callout

The section "LiPo and Rechargeable Battery Boundary" listed nine
non-negotiables - adult-supervised charging, correct chemistry and cell count,
balance connection, charging bag, never unattended, never a damaged pack, stop
for heat or smell, storage guidance, disconnect after use.

**Every rule was correct and consistent with `SAFETY.md` and Topic 3.3. The
form was wrong.** They sat as plain bullets under a plain heading, in the
topic where a real battery enters a real vehicle for the first time. A reader
skimming for the next instruction could pass straight over them, and section
13.2 is explicit that the `⚠️ SAFETY` marker is what lets the HTML build
render a warning that cannot be skimmed past.

They are now a callout, framed with why this topic re-states them: the buggy
is a real vehicle now, and nothing about installing the pack relaxes any rule.

Two more of the same kind were fixed:

- **Topic 4.8's thread-locking guidance** - chemical-handling instructions in
  a bullet list. Section 9 names chemical hazards explicitly.
- **Topic 4.9's "do not crush a soft battery pouch with an over-tight strap"**
  - a LiPo damage warning sitting in ordinary prose.

## 2.2 144 figures were in a format that would have cost someone a day

Topic 4.1 used the section 7.7 form: art brief, then a separate caption line,
then a separate alt-text line. **Topics 4.2-4.10 fused all three into one
blockquote**, with `Caption:` and `Alt text:` written as sentences inside the
brief.

Section 7.3 was satisfied - every figure had a number, a caption and alt text.
But section 7.7 defines what happens when the artwork arrives: alt text moves
into the image brackets, the caption stays exactly as it was, and the brief
becomes an HTML comment. Fused into one blockquote, that is a three-way manual
split, per figure, 144 times, done by whoever is drawing 160 figures.

All 144 were converted mechanically. The pattern matched every one, so no
figure was reworded, renumbered or reinterpreted.

---

# 3. What else changed ✏️

## 3.1 Terminology

| Registry term | Was | Hits | Topics |
| --- | --- | ---: | --- |
| hinge pin | `hinge-pin` | 7 | 4.6, 4.8 |
| captive nut | `captured nut` | 8 | 4.6, 4.7, 4.8 |

`Captive Nut` was already the glossary entry, so `captured nut` disagreed with
the book's own dictionary as well as with section 5.

## 3.2 The project heading changed name halfway through the part

Topics 4.1-4.5 used `# Topic Build - …`; Topics 4.6-4.10 used
`# Topic Project - …`. Section 13.3 makes headings into anchors and navigation
entries, so one had to win. **`Topic Build`** was chosen: Part 4 builds the
buggy, and it keeps these distinct from the household `Topic Mini Project` of
the teaching parts. Nothing outside Part 4 referenced the old name.

## 3.3 Pacing, prompts and references

- **Break markers**: one per topic across 876-1,200 lines, now three.
- **Topic 4.9 had no think-about-it prompt** - the only topic in Parts 3 or 4
  without one. It now has one at the claim the topic rests on: nothing
  electrical changed since Topic 4.5, so why recheck the steering endpoints?
  Because they were never a property of the electronics alone - they belonged
  to the electronics *plus* the mechanism, and the mechanism is new.
- **Learn More blocks** were split out of the end-of-topic `# Learn More`
  heading (not in the template) and placed beside the sections they serve.
- **Topic 4.2 gained its Learning Goal heading.**

## 3.4 Links

All 19 unique URLs returned HTTP 200. Sources: NASA and NASA/JPL (7), Prusa,
Bambu Lab and UltiMaker (4), Spektrum, Horizon Hobby and Futaba (4), SKF,
Mitutoyo, Pololu and Energizer (4), GOV.UK (1) - every one inside the
approved-source list as extended on 2026-08-06, so Part 4 needed no new source
decision.

Eight sit on rot-prone paths (CDN build hashes, `wp-content`, `sys_master`).
Each keeps its URL and now names the search term that would find the document
again. Six were cited twice within one topic for the same reason; the repeat
was dropped and the link kept where it teaches.

**Nothing was removed. 19 links before, 19 after.**

---

# 4. Checked and found already compliant ✅

- **Section 11: complete.** Cheapest valid prototype, buy/reuse/make, cost
  checkpoint, modular interfaces, test plan, upgrade path and stop point in
  all ten topics; Learning Goal in nine, now ten.
- **Fair-test pattern**: independent, dependent and control variables and pass
  conditions appear in every topic's test plan.
- **Figure budget met**: 16 per topic against a 12-16 build-topic budget. No
  figures were added.
- **Answers complete**: 12 against 12 review questions in all ten.
- **Looking Ahead correct in all ten**, 4.1 → 4.2 through 4.9 → 4.10, and
  4.10 → Topic 5.1.
- **Section 13 met**: every code fence tagged, no tables inside fences, no raw
  HTML anywhere in the part, Topic Checklists use `- [ ]`.
- **Heading emoji clean**: template headings carry their registered emoji, no
  content heading carries a stray one.
- **Length within target**: 876-1,200 lines before, 960-1,298 after.

---

# 5. Items withdrawn on inspection 🔍

Two backlog items were wrong or out of scope, and were withdrawn rather than
applied. Recorded so nobody re-raises them.

| Item | Verdict |
| --- | --- |
| "Curly quotes in Topic 4.1's Learn More box; the rest of the book uses straight quotes" | **Out of scope.** Curly quotes are book-wide: 69 in Part 2, 18 in Part 3, 51 in Part 4. Fixing Part 4 alone would make the book *less* consistent. Carried as a book-wide debt below. |
| "The NASA Glenn page uses a US spelling" | **Correct as cited.** `Center of Gravity` is the page's actual title. Not a British English breach. |

---

# 6. Debts carried forward 📋

| Debt | Detail |
| --- | --- |
| Figures are still placeholders | All 160 are art briefs, not artwork - the same debt the whole book carries. They are now in a format that can be replaced cleanly. |
| Curly quotes, book-wide | 138 across Parts 2, 3 and 4; none in Part 1. Needs one decision and one sweep, not a per-part fix. |
| 8 rot-prone links | Working today, with search fallbacks in place. Re-check when Part 4 next moves version. |
| Reference docs unfed by Part 4 | `BOM.md`, `COST-LEDGER.md`, `TOOLS.md` and `TROUBLESHOOTING.md` do not name any Topic 4.x as a feeder, though 4.1 (cost plan), 4.6 (donor parts) and 4.10 (debugging) are the most natural feeders in the whole book. This is now the largest gap in the reference documents. |
| `SAFETY.md` feeds list | Part 4's LiPo, chemical and powered-test content agrees with it, but its frontmatter does not name the Part 4 topics. |
| Only one prompt in seven topics | 4.3-4.8 and 4.10 carry one think-about-it prompt each. That satisfies section 2 ("one or two"), but each has a second claim worth making the reader work for. Worth a pass at v0.3. |

---

# 7. Method

Followed the per-topic loop in `backlog/PLAN.md`. Working files:
`backlog/part-4-book-wide.md` (kept, with the audit results) and
`backlog/topic-4.1.md` … `topic-4.10.md` (deleted on completion per the
project convention - git history keeps them).

The deep-link decision from the Part 3 review carried over unchanged:
verify and flag, never convert or delete (`STYLE-GUIDE.md` section 8.1).

Commits on `Part_3_review`:

| Commit | Scope |
| --- | --- |
| `d72e104` | Add Part 4 review backlogs (Topics 4.1-4.10) |
| `98bcbf3` | Split Part 4's fused figure placeholders into the 7.7 form |
| `8b35d1b` | Apply the Part 4 review to Topics 4.1-4.10 (v0.2) |
| `0d76cad` | Backfill Part 4's New Words into the glossary |
