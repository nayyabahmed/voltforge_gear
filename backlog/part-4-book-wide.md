# Backlog - Part 4 Book-Wide Items

Sweeps that apply across the whole of Part 4 (Topics 4.1-4.10). Work them into
each topic's pass (per-topic loop in [PLAN.md](PLAN.md)), then tick them here
only when every Part 4 topic is swept.

Legend: [T] textual, [C] context awareness, [V] visual aid, [E] external
reference, [S] safety.

Created 2026-08-06 from a direct audit of the ten topics as published at
`6efa822`. Status: **NOT STARTED**.

## How Part 4 differs from Part 3

Part 4 is the **build** part, so `STYLE-GUIDE.md` section 11 applies to every
topic: learning goal, cheapest valid prototype, parts to buy/reuse/make, cost
checkpoint, modular interfaces, test plan, upgrade path, and a stop point
before the next purchase. **All eight are present in all ten topics** (only
4.2 is missing its Learning Goal heading), and the fair-test pattern from
Topic 1.9 is used throughout. That structural work is done.

What is not done divides into four groups: the **figure format**, **safety
callout placement**, the **glossary** (the largest gap in the book so far),
and **pacing**.

The deep-link decision from Part 3 carries over unchanged - see the standing
decision in [part-3-book-wide.md](part-3-book-wide.md) and
`STYLE-GUIDE.md` section 8.1. **Verify and flag; never convert or delete.**

## Status board

Last updated: 2026-08-06

**Legend:** ✅ done | 🔨 in progress | 📋 planned | ➖ not applicable

| Topic | Backlog file | Research pass | Items applied | v0.2 bumped | Overall |
| --- | --- | --- | --- | --- | --- |
| 4.1 Build Strategy and Cost Plan | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.2 Paper and Cardboard Layout | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.3 Rolling Cardboard Chassis | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.4 Low-Power Wire-Frame Car | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.5 Radio-Controlled Prototype | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.6 Choosing and Measuring Donor Parts | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.7 Modular Printed Chassis | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.8 Final Mechanical Assembly | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.9 Electronics Installation | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 4.10 Testing, Debugging and Version 1 | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| Book-wide sweeps | ✅ this file | ➖ | 📋 | ➖ | 📋 planned |

## Items to apply

### The big one

- [ ] [V] **The figure format splits the part in two, and 144 figures are on
  the wrong side of it.** Topic 4.1 uses the section 7.7 form - brief
  blockquote, then a separate `*Figure 4.1.1 - caption.*` line, then a
  separate `*Alt text: …*` line. **Topics 4.2-4.10 fuse all three into one
  blockquote**, with `Caption:` and `Alt text:` written as sentences inside
  the art brief:

  ```text
  > **[Figure 4.3.1, Signature visual, F5 motion overlay: … Caption: Power can
  > move a misaligned chassis… Alt text: Parallel axles roll straight…]**
  ```

  Section 7.3 is satisfied in substance - every figure has a number, a caption
  and alt text. But section 7.7 defines what happens when the artwork arrives:
  the alt text moves into `![…]`, **the caption stays exactly as it was**, and
  the brief becomes an HTML comment. That is a three-way split of one
  blockquote, per figure, 144 times, for whoever draws these. It also means
  the caption never renders as a caption in the meantime.

  Convert 4.2-4.10 to the 4.1 form. This is mechanical and it is the single
  most valuable thing in this backlog.

### Safety

- [ ] [S] **Topic 4.9's LiPo rules are not in a safety callout.** The section
  "LiPo and Rechargeable Battery Boundary" lists nine correct
  non-negotiables - adult-supervised charging, correct chemistry and cell
  count, balance connection, charging bag, never unattended, never a damaged
  pack, stop for heat or smell, storage guidance, disconnect after use - as
  **plain bullets under a plain heading**. Section 9 requires the callout
  form for anything electrical or chemical, and section 13.2 is explicit that
  the fixed markers are what let the HTML build make a warning unskippable.
  This is the highest-priority safety item in the part.
- [ ] [S] **Topic 4.8's thread-locking section needs a callout.** It gives
  chemical-handling instructions - keep away from incompatible plastics, tiny
  controlled amount, stated cure time, adult handles the chemical and reads
  the safety data - in a bullet list. Section 9 names chemical hazards
  explicitly.
- [ ] [S] **Hazard content precedes the single safety callout in six topics.**
  Each topic carries one `⚠️ SAFETY` callout placed before its Topic Build /
  Topic Project. Hazardous instruction appears earlier than that callout in
  4.2, 4.4, 4.6, 4.7, 4.8 and 4.9. Section 9: callouts come BEFORE the
  activity that needs them. Either move the callout earlier or add a second
  one at the first hazard.

### Vocabulary and consistency

- [ ] [C] **71 New Words are missing from `glossary.md`** - twice Part 3's gap
  and the largest in the book. Per-topic lists are in the topic files. No
  topic is fully covered; 4.6 is entirely absent (8 of 8 missing).
- [ ] [T] **Terminology registry breaches.** Section 5 fixes these spellings
  and Part 4 varies them:

  | Registry term | Used in Part 4 as | Hits | Topics |
  | --- | --- | ---: | --- |
  | hinge pin | `hinge-pin` | 7 | 4.6, 4.8 |
  | captive nut | `captured nut` | 6 | 4.6, 4.7, 4.8 |

  `Captive Nut` is already the glossary entry, so `captured nut` is
  inconsistent with the book's own dictionary as well as the registry.
- [ ] [T] **The project heading changes name halfway through the part.**
  Topics 4.1-4.5 use `# Topic Build - …`, Topics 4.6-4.10 use
  `# Topic Project - …`. Section 13.3 makes headings anchors and navigation
  entries, so one name has to win. **Recommendation: `# Topic Build`** - Part
  4 builds the buggy, and it distinguishes these from the household `Topic
  Mini Project` of the teaching parts.
- [ ] [T] **Topic 4.2 has no `# Learning Goal` heading**, where the other nine
  do. Section 11 lists it first among the build-topic requirements.
- [ ] [T] **Curly quotes in Topic 4.1's Learn More box** (`“design
  specification”`) where the rest of the book uses straight quotes.

### Pacing and prompts

- [ ] [T] **Break markers: one per topic, across 876-1,200 lines.** Identical
  to the Part 3 finding. The guide wants a seam roughly every 25-30 minutes;
  at these lengths that is three. All ten topics need two more.
- [ ] [T] **Topic 4.9 has no think-about-it prompt at all**, the only topic in
  Parts 3 or 4 without one. Section 2 asks for one or two at the most
  counter-intuitive claims, and this topic has an obvious candidate: a system
  that worked perfectly in Topic 4.5 must be recommissioned from zero anyway.
- [ ] [T] **Seven topics have exactly one prompt** (4.3-4.8, 4.10). Not a
  breach - the guide says one or two - but each has a second claim worth
  making the reader work for. Add where it earns its place, not to hit a
  number.

### References

- [ ] [E] **Verify all 19 links and flag anything wrong.** The automated check
  on 2026-08-06 returned **HTTP 200 for all 19**. Confirm during each topic's
  research pass that the page still says what the topic claims.
- [ ] [E] **Add search fallbacks to the 8 rot-prone paths.** Keep the URL and
  name the search term: the two Spektrum/Horizon CDN hash manuals (4.5, 4.9),
  the Firma manual (4.9), Futaba (4.5), Energizer (4.4), Mitutoyo (4.3), and
  the two NASA `wp-content` PDFs (4.1/4.2/4.10 and 4.3).
- [ ] [E] **Six links are cited twice inside one topic** for the same reason:
  JPL in 4.1 and 4.2, all three printing references in 4.7, the Firma manual
  in 4.9, and NASA V&V plus JPL in 4.10. Keep the instance that teaches.
- [ ] [E] **One Learn More box per topic, at the very end**, under a
  `# Learn More` heading that is not in the section 3 template - the same
  finding as Part 3, and the same fix. Split each box and place the entries
  beside the sections they serve. The mid-topic `🎬 Watch the build` boxes are
  already correctly placed.
- [ ] [V] **Confirm the four Mermaid blocks are genuine flows** (4.7, 4.8,
  4.9, 4.10). Section 7.1: if it shows what something looks like, where it is
  or which way a force points, it is not Mermaid.

## Link verification (automated check, 2026-08-06)

19 unique URLs. Method: `curl -L` with a browser user-agent, 25 s timeout.

| Result | Count | Detail |
| --- | ---: | --- |
| HTTP 200 | 19 | Every link in the part is reachable |
| Broken | 0 | |

Sources used: NASA and NASA/JPL (7 links), Prusa, Bambu Lab and UltiMaker (4),
Spektrum, Horizon Hobby and Futaba (4), SKF, Mitutoyo, Pololu and Energizer
(4), GOV.UK (1). Every one of these is inside the approved-source list as
extended on 2026-08-06 (`STYLE-GUIDE.md` section 8), so Part 4 needs no
further source decision.

**Note:** `www1.grc.nasa.gov/.../center-of-gravity/` carries a US spelling.
That is NASA's own page title and is correct as cited - it is not a British
English breach.

## Checked and found compliant (do not re-litigate)

- **Section 11 build-topic rules: complete.** Cheapest valid prototype, what
  to buy/reuse/make, cost checkpoint, modular interfaces, test plan, upgrade
  path and stop point are present in all ten topics; Learning Goal in nine.
- **Fair-test pattern: present throughout.** Independent, dependent and
  control variables and pass conditions appear in every topic's test plan.
- **Figure budget: met.** 16 figures per topic against a 12-16 budget for
  build topics. **Do not add figures.**
- **Answers: complete.** Twelve answers against twelve review questions in all
  ten topics.
- **Looking Ahead: correct in all ten**, 4.1 → 4.2 through 4.9 → 4.10, and
  4.10 → Topic 5.1 to open Part 5.
- **Length: within target.** 876-1,200 lines against a 700-1,200 ceiling.
- **Section 13: met.** Every code fence carries a language tag (`text` or
  `mermaid`), no fence lays out a table, there is no raw HTML anywhere in the
  part, and Topic Checklists use `- [ ]`.
- **Heading emoji: clean.** Template headings carry their registered emoji and
  no content heading carries a stray one.
- **British English: clean** apart from the NASA page title noted above.
