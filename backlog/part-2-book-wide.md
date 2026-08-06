# Backlog - Part 2 Book-Wide Items

Sweeps that apply across the whole of Part 2 (Topics 2.1-2.9). Work them
into each topic's pass (see the per-topic loop in [PLAN.md](PLAN.md)), then
tick them here only when every Part 2 topic is swept.

Legend: [T] textual, [C] context awareness, [V] visual aid, [E] external reference.

Created 2026-08-06. Status: **NOT STARTED** - no Part 2 topic has begun its
review pass; all of 2.1-2.9 is still v0.1 Draft.

## Status board

Part 1's review had its own board in [TRACKER.md](TRACKER.md), which is now
closed. Rather than add a fourth tracker file, Part 2's review board lives
here. Update the row whenever a topic's work starts or finishes (per-topic
loop step 8), and keep the "Last updated" line current.

Last updated: 2026-08-06

**Legend:** ✅ done | 🔨 in progress | 📋 planned | ➖ not applicable

| Topic | Backlog file | Research pass | Items applied | Emoji pass | Mini project | v0.2 bumped | Overall |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2.1 Workshop Safety and Setup | ✅ created | ✅ | ✅ | ✅ | ✅ Safety Card | ✅ | ✅ done (2026-08-06) |
| 2.2 3D Printing Fundamentals | ✅ created | 📋 | 📋 | 📋 owed | 📋 owed | 📋 | 📋 planned |
| 2.3 Slicer Software and First Prints | ✅ created | 📋 | 📋 | ✅ already | ✅ already | 📋 | 📋 planned |
| 2.4 CAD Fundamentals | ✅ created | 📋 | 📋 | ✅ already | ✅ already | 📋 | 📋 planned |
| 2.5 Designing Simple Parts | ✅ created | 📋 | 📋 | ✅ already | ✅ already | 📋 | 📋 planned |
| 2.6 3D Printing Materials | ✅ created | 📋 | 📋 | ✅ already | ✅ already | 📋 | 📋 planned |
| 2.7 Hand Tools and Fasteners | ✅ created | 📋 | 📋 | ✅ already | ✅ already | 📋 | 📋 planned |
| 2.8 Cutting, Drilling and Finishing | ✅ created | 📋 | 📋 | ✅ already | ✅ already | 📋 | 📋 planned |
| 2.9 Soldering and Wire Connections | ✅ created | 📋 | 📋 | ✅ already | ✅ already | 📋 | 📋 planned |
| Book-wide sweeps | ✅ this file | ➖ | 📋 | ➖ | ➖ | ➖ | 📋 planned |

Topic 2.10 (Workshop Skills Challenge) is not yet written, so it has no
review row. It joins this board once it is authored - see
[WRITING-TRACKER.md](WRITING-TRACKER.md).

## How this backlog differs from Part 1's

Part 1's backlog was transcribed from a frozen external readability review
(`style-guides-principles/improvement-suggestions.md`, 2026-07-11). **No such
review exists for Part 2.** The items in these files were derived on
2026-08-06 by auditing the nine published topics directly against
`STYLE-GUIDE.md`, section by section. Line numbers refer to the v0.1 text as
committed at `70ccdda` and will drift as edits land - treat them as
approximate locators, exactly as in Part 1.

Because the items are audit findings rather than a reviewer's prose notes,
each one names the style-guide rule it fails. If a finding turns out to be a
deliberate authoring choice, record that in the topic's Research notes and
tick it as "considered, kept" rather than deleting it.

## File naming

Part 1's files keep legacy `chapter-NN.md` names because their internal
review IDs predate the topic renumbering. Part 2 has no such legacy, so
these files are named for the reader-facing topic number: `topic-2.1.md`
through `topic-2.9.md`. No mapping table is needed.

## Order of work

Unlike Part 1 there are no half-finished topics to rescue, so the order is
simply the reading order, with one exception at the front:

1. **Phase 1 - the pre-convention pair: Topics 2.1 and 2.2.** Both were
   written before the mini-project, think-prompt and emoji conventions
   existed and are missing all three. They are also the two shortest topics,
   so they are the cheapest way to get the whole part consistent.
2. **Phase 2 - the long topics in order: 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9.**
3. **Phase 3 - cross-topic sweep:** tick the items below, verify every gloss
   number against `SUMMARY.md`, and reconcile the section-pattern
   inconsistencies listed under "Structural consistency".

## Items to apply

- [ ] [C] **Forward-reference glosses are largely missing.** Part 2 uses
  buggy vocabulary from Part 3 as if it were already taught. Topics 2.2,
  2.3, 2.4, 2.5, 2.7 and 2.8 contain **no Topic 3.x pointers at all**, while
  freely using "servo", "receiver", "ESC", "motor mount" and "battery tray".
  Topic 2.9 is the model to copy: it glosses seven distinct forward
  references. Correct home topics per `SUMMARY.md`: batteries 3.3, receiver
  3.4, servo 3.5, ESC 3.6, motors 3.7. Per-topic offender lists are in the
  topic files.
- [ ] [C] **Verify every gloss number against `SUMMARY.md`.** One confirmed
  error already: Topic 2.4 (~661) cites "the packaging envelope from Topic
  1.2"; packaging envelope is taught in Topic 1.5 and the Part 1 Capstone,
  and Topic 1.2 is Systems Thinking. Assume there are more.
- [ ] [T] **Length and break markers.** Every topic from 2.4 onwards exceeds
  the 700-1,200 line target, four of them by more than 700 lines (2.5 1,922;
  2.6 1,998; 2.7 1,917; 2.8 2,268; 2.9 2,101). Per the Part 1 standing
  decision on Chapter 04, **do not split** - splitting renumbers every later
  topic and breaks gloss pointers book-wide. Instead bring break-marker
  density to roughly one per 300-400 lines. Current counts are badly uneven:
  2.6 has five and 2.8 has four, but 2.5, 2.7 and 2.9 have only two each.
- [ ] [T] **"Think about it" prompts are thin.** Style guide asks for one or
  two per topic at the most counter-intuitive claims. Topics 2.1 and 2.2
  have **none**; 2.3, 2.7, 2.8 and 2.9 have exactly one each despite being
  the longest topics in the book. Candidate placements are in the topic
  files.
- [ ] [E] **Learn More coverage is thin and inconsistently placed.** Six
  topics carry a single box; only 2.7 has three. Worse, the placement
  pattern splits two ways: 2.1, 2.5, 2.6, 2.8 and 2.9 park a trailing
  top-level `# Learn More` section near the end of the file, while 2.3, 2.4
  and 2.7 use inline boxes. Style guide section 8 wants the box "next to the
  relevant section". Standardise on inline boxes and retire the trailing
  sections.
- [ ] [V] **Visual placeholders are thin in the longest topics.** Counts,
  including both the `[Sketch:` and `[Signature visual:` markers:

  | Topic | 2.1 | 2.2 | 2.3 | 2.4 | 2.5 | 2.6 | 2.7 | 2.8 | 2.9 |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Placeholders | 1 | 4 | 4 | 3 | 5 | 1 | 3 | 2 | 2 |
  | Lines | 543 | 530 | 1,172 | 1,510 | 1,922 | 1,998 | 1,917 | 2,268 | 2,101 |

  The problem cases are 2.6 (one across 1,998 lines), 2.8 (two across 2,268)
  and 2.9 (two across 2,101). Per-topic priorities are in the topic files.
  **Check the existing signature visual before adding anything** - several
  topics already cover their hardest idea well, and the first draft of this
  backlog recommended visuals that turned out to exist.
- [ ] [V] **Two different placeholder markers are in use.** The visuals
  policy (section 7) specifies `> **[Sketch: …]**`, but 2.3, 2.4, 2.7, 2.8
  and 2.9 also use `> **[Signature visual: …]**` for their headline
  illustration - while 2.6 marks its signature visual with a plain
  `[Sketch:` under a section titled "The Signature Visual", and 2.1, 2.2 and
  2.5 have no signature marker at all. The two-marker convention is a good
  idea; either adopt it in STYLE-GUIDE section 7 and apply it everywhere, or
  drop it. Do not leave it half-applied.
- [ ] [C] **Terminology registry.** One confirmed violation: "hinge-pin"
  appears twice in Topic 2.8 (~902, ~970); the registry says "hinge pin",
  two words. This is the same fix applied to Chapter 04 in Part 1. Re-run
  the check across the part after edits.
- [ ] [T] **Structural consistency across the part.** Optional sections were
  applied unevenly, which makes the part feel less like one book:
  - "Thinking Like an Engineer" appears in 2.3, 2.4, 2.5, 2.6, 2.8 and 2.9
    but not 2.7.
  - "Stop Point Before ..." appears in 2.3, 2.4, 2.5, 2.6, 2.8 and 2.9 but
    not 2.7.
  - Topic 2.9 alone carries "Cheapest Valid Prototype" and "What to Buy,
    Reuse and Make" - the build-topic pattern from STYLE-GUIDE section 11,
    which is specified for Parts 3-5. Decide whether that pattern belongs in
    a Part 2 teaching topic at all, then apply the decision consistently.
  Decide each pattern deliberately: either it belongs in every teaching
  topic of the part or in none.
- [ ] [T] **Emoji pass (2.1 and 2.2 only).** Neither topic carries a single
  template-heading emoji; all seven fixed headings are bare in both files.
  Topics 2.3-2.9 already comply.
- [ ] [T] **Topic Mini Projects (2.1 and 2.2 only).** Neither has one.
  Every other Part 2 topic does, with a Watch-the-build box and the
  adult-check line. Candidates are proposed in `topic-2.1.md` and
  `topic-2.2.md`.

## Checked and found compliant (do not re-litigate)

Recording these so the review pass does not spend time re-deriving them:

- **Vocabulary budget.** Every topic sits at or under the ~15 new-words
  budget (2.1 has 7; the rest are 14-15, so six topics sit exactly at the
  ceiling rather than comfortably under it).
- **Glossary coverage.** All New Words from 2.3-2.9 were added to
  `glossary.md` on 2026-08-06 (commit `4074569`). 2.1 and 2.2 were already
  covered.
- **British English.** No US spellings found across the part. ("meter" in
  2.3 and 2.9 refers to the measuring instrument, which is correct; "metre"
  is the unit.)
- **Mini project materials rule.** The seven existing mini projects are
  genuinely household-and-scrap only. Topic 2.7 offers a no-fasteners
  fallback and Topic 2.9 models a wiring harness in paper and string with an
  explicit "never use on real wiring" warning - both correct readings of the
  rule for tool-heavy topics.
- **Adult-check line.** Present in all seven existing mini projects.
- **Looking Ahead targets.** Correct in 2.1 and 2.3-2.9. Topic 2.2 is the
  one exception (see `topic-2.2.md`).
- **Safety callout density.** Appropriate where it matters most: 2.8 has
  nine and 2.9 has eleven. Topic 2.1 is the one to re-examine.
- **Code fences.** The 189 ```text blocks across the part are worked
  examples, data and simple arrow flows, not the weak ASCII art the visuals
  policy prohibits.

## Research topics for the whole part

Run per topic during loop step 2, but these cut across several:

- **Safety-critical numbers** appear far more often in Part 2 than Part 1:
  print and bed temperatures, glass transition points, filament drying
  temperatures and times, soldering iron temperatures, drill speeds. Every
  such number needs verifying against a manufacturer knowledge base before
  the topic can go to v0.2.
- **Software UI churn.** Topics 2.3 and 2.4 name menus, buttons and free
  tiers in slicers (Bambu Studio, OrcaSlicer, PrusaSlicer, Cura) and CAD
  tools (Tinkercad, Onshape, FreeCAD). These change often - re-verify every
  named control and every "free for personal use" claim.
- **Consumables that can harm.** Threadlocker chemistry on plastics (2.7),
  flux fume and lead-free versus leaded solder (2.9), and sanding dust from
  printed plastics (2.8) all need current guidance, cross-checked against
  `SAFETY.md`.
- **Reference-doc feeds.** `TROUBLESHOOTING.md` has no Topic 2.x references
  at all despite 2.3 and 2.6 being natural feeders, and `TOOLS.md` (46
  lines) is missing everything Topic 2.8 introduces. Feed both as part of
  the relevant topic's pass rather than leaving it to a later sweep.
