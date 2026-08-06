# Backlog - Part 3 Book-Wide Items

Sweeps that apply across the whole of Part 3 (Topics 3.1-3.10). Work them into
each topic's pass (per-topic loop in [PLAN.md](PLAN.md)), then tick them here
only when every Part 3 topic is swept.

Legend: [T] textual, [C] context awareness, [V] visual aid, [E] external reference.

Created 2026-08-06. Re-audited against the updated `STYLE-GUIDE.md`
(section 13 conventions, 2026-08-06) the same day.

## How this backlog differs from Parts 1 and 2

**Part 3 arrived already revised.** The topics were externally revised against
`STYLE-GUIDE.md` and `references/ref-002.md` before this backlog was written,
and it shows. The audit found the structural work essentially done, so this is
a much shorter list than Part 2's - almost everything here is external
references, the glossary, and pacing.

Items were derived by auditing the ten topics directly. Line numbers refer to
the text as merged at `ec92b4d`.

## Standing decision - deep links are KEPT (2026-08-06)

The first draft of this backlog carried an item to convert Part 3's 33 deep
URLs into the `search X on site Y` form that `STYLE-GUIDE.md` section 8
prefers. **That item is withdrawn.** The decision, taken 2026-08-06:

> Part 3 keeps its deep links. They are the difference between "read about an
> ESC" and "read the actual manual of a real ESC", and the whole part is built
> on comparing the handbook's reasoning with manufacturer documentation. A
> search term cannot carry a reader to page 4 of a specific manual.

What replaces the conversion item:

1. **Verify every link, and flag - never silently delete - anything wrong.**
   Any link that has rotted, moved, changed meaning or turned into a sales
   page is reported in the Part 3 review report, with a recommendation. The
   decision to drop a link is the author's, taken on the evidence, not a
   mechanical sweep.
2. **Rot-prone links get a search fallback alongside the URL, not instead of
   it.** Thirteen of the links are CDN or `wp-content` PDF paths containing
   build hashes (`.../default/dwb9935bc5/Manuals/...`). These are exactly the
   URLs section 8 warns about. Keeping the link AND naming the search term
   gives the reader both the direct route today and a way back if it breaks.
3. **Section 8 is extended rather than broken.** Part 3 cites RC and component
   manufacturers that the approved-source list never anticipated. See the item
   below.

## Status board

Last updated: 2026-08-06

**Legend:** ✅ done | 🔨 in progress | 📋 planned | ➖ not applicable

| Topic | Backlog file | Research pass | Items applied | v0.2 bumped | Overall |
| --- | --- | --- | --- | --- | --- |
| 3.1 Meet the RC Electronics | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.2 Voltage, Current, Resistance and Power | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.3 Batteries and Battery Safety | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.4 Radio Transmitters and Receivers | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.5 Steering Servos | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.6 Electronic Speed Controllers | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.7 Brushed and Brushless Motors | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.8 Gears and the Drivetrain | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.9 Steering Systems | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| 3.10 Suspension, Wheels and Grip | ✅ created | 📋 | 📋 | 📋 | 📋 planned |
| Book-wide sweeps | ✅ this file | ➖ | 📋 | ➖ | 📋 planned |

## Items to apply

- [ ] [E] **Verify all 33 unique external links and flag every problem.** An
  automated reachability check on 2026-08-06 returned HTTP 200 for 30 of 33.
  The three exceptions and the two policy concerns are listed under "Link
  verification" below. Re-check each during the topic's research pass, confirm
  the page still says what the topic claims it says, and record the verdict.
  **Flag, do not delete.**
- [ ] [E] **Add a search fallback to the 13 rot-prone PDF links.** Keep the
  URL; append the site and search term that would find the document again.
  Affected: 3.3 (1), 3.4 (2), 3.5 (1), 3.6 (2 + 1 in Watch the build), 3.7 (1),
  3.8 (1), 3.9 (3), 3.10 (2, plus one repeat in Watch the build).
- [ ] [E] **Extend `STYLE-GUIDE.md` section 8's approved-source list.** Part 3
  cites 19 domains; most are outside the list, which names only BBC Bitesize,
  PhET, Explain That Stuff, Tinkercad, Onshape, NASA/ESA and manufacturer
  knowledge bases (Prusa, Bambu - both 3D printing).

  | Domain group | Uses | On the list? |
  | --- | ---: | --- |
  | phet.colorado.edu, explainthatstuff.com, tinkercad | 6 | yes |
  | gov.uk, london-fire.gov.uk, ofcom.org.uk | 4 | official safety guidance - yes |
  | horizonhobby, spektrumrc, teknorc, futabausa, hobbywingdirect | 18 | RC manufacturers - not named |
  | pololu, maxongroup, khkgears, fluke | 8 | component manufacturers - not named |
  | nist.gov | 1 | standards body - not named |
  | sciencebuddies.org | 3 | educational - not named |

  These are the right sources for the subject - a topic about ESCs should cite
  ESC manufacturers. Extend section 8 to cover RC and component manufacturer
  documentation, national standards and metrology bodies, and Science Buddies,
  with the existing quality conditions (verify it exists, say why it is worth
  reading, avoid sales-heavy pages). Do this **before** the topic passes, so
  the passes work to a settled rule.
- [ ] [C] **35 New Words are missing from `glossary.md`.** Part 3's glossary was
  backfilled on 2026-08-06 from the pre-revision text; the revisions then added
  vocabulary. Exact per-topic lists are in the topic backlog files. 3.1 is the
  only topic fully covered.
- [ ] [T] **Break markers are thin.** Eight topics carry a single
  `☕ Good place to pause` across 1,074-1,200 lines; 3.3 has two and 3.1 has
  three. The guide wants a seam roughly every 25-30 minutes of reading, which
  at this length is three or four. This is the cheapest change that improves
  the reading experience across the whole part.
- [ ] [E] **One Learn More box per topic, and it sits at the very end.**
  Section 8 wants boxes "placed next to the relevant section". Every topic
  instead has a single `# Learn More` heading between Topic Checklist and
  Looking Ahead - a heading that is not in the section 3 template either.
  Split each into inline boxes next to the sections they serve. (The mid-topic
  `🎬 Watch the build` boxes are already correctly placed; only the Learn More
  block needs moving.)
- [ ] [E] **Five topics have no BBC Bitesize entry: 3.2, 3.3, 3.4, 3.5, 3.6.**
  The other five already cite it. Topic 3.2 is the strongest candidate in the
  whole book - voltage, current, resistance and power are core KS3 physics and
  the reader meets them at school under those exact words. Use
  national-curriculum wording as the search term, per section 8.
- [ ] [T] **One bare link outside any box:** `3.2` line 536 drops a raw
  PhET markdown link into prose. Fold it into a proper reference box.
- [ ] [V] **Confirm each Mermaid block is a genuine flow.** Only 3.1 and 3.4
  use Mermaid, one block each, so this is a two-minute check rather than a
  sweep. Apply the section 7.1 test: if it shows what something looks like,
  where it is, or which way a force points, it is not Mermaid.

## Link verification (automated check, 2026-08-06)

33 unique URLs. Method: `curl -L` with a browser user-agent, 25 s timeout.

| Result | Count | Detail |
| --- | ---: | --- |
| HTTP 200 | 30 | Reachable, including all 13 CDN/PDF manual links |
| HTTP 403 | 3 | All `sciencebuddies.org` - bot protection, not rot |

**Issues to carry into the report:**

1. **Science Buddies returns 403 to automated checks** (3.2 paper circuit, 3.5
   lever lesson plan, 3.5 pantograph). This is Cloudflare-style bot
   protection, not a dead page. Confirm each by hand in a browser during the
   research pass and record the result - do not remove them on the strength of
   a 403.
2. **`hobbywingdirect.com/products/quicrun-10-brushed-esc` is a product page**
   (3.6 Learn More). Section 8 says avoid sales-heavy pages. It is cited for
   its published specification table, which is a legitimate reason, and the
   manufacturer publishes those specs nowhere more stable. Keep it, and record
   it in the report as a deliberate, argued exception.
3. **13 links carry build hashes or `wp-content` paths.** They work today and
   are the correct documents. They are the most likely thing in Part 3 to
   break in a year. Hence the search-fallback item above.
4. **Two links point at the same Tekno RC documents from both a Watch the
   build box and a Learn More box** in 3.10. Not a fault, but when the Learn
   More box is split, do not leave the reader the same link twice in one
   screen.

## Checked and found compliant (do not re-litigate)

Recorded so the review pass does not spend time re-deriving these:

- **Figures: done, and done well.** Every topic carries 11 or 12 figures
  against a 10-12 budget for component topics, every one tagged F1-F7 or
  Signature visual, every one with a number, a caption and alt text. Part 3
  is the best-illustrated part in the book. **Do not add figures.**
- **Section 13 (authoring for three outputs): already met.** This is the newest
  part of the style guide and Part 3 needs nothing for it. Every code fence
  carries a language tag (`text` or `mermaid`); no fence is being used to lay
  out a table; there is no raw HTML anywhere in the part; the fixed callout
  markers are used exactly as registered (24 ⚠️ SAFETY, 19 🤔 Think about it,
  10 📚 Learn more, 10 🎬 Watch the build, 13 ☕ Good place to pause); and
  Topic Checklists use `- [ ]`.
- **Think-about-it resolutions are correctly placed.** Section 13.3 forbids
  anything between the prompt and its answer. All 19 prompts in Part 3 are
  followed immediately by a single resolution paragraph, with the figure
  placeholder after it. Checked mechanically, all ten topics.
- **Answers: complete.** Every topic has `# Answers 🔑` with exactly 12
  answers against 12 review questions.
- **Looking Ahead: correct in all ten**, 3.1 → 3.2 through 3.9 → 3.10, and
  3.10 → Topic 4.1 to open Part 4.
- **Length: within target.** 1,074-1,200 lines against a 700-1,200 ceiling -
  the first part in the book that does not overrun it.
- **Think-about-it prompts:** two or more in every topic except 3.1, which has
  one.
- **Terminology registry: clean.** "gearbox" appears seven times in Topic 3.8
  and every use is correct - it refers to a real enclosed gear assembly or a
  donor module, which is exactly what the registry reserves the word for. No
  "chapter", no "hinge-pin", no "captured nut", no "requirements
  traceability".
- **British English: clean.** The only `meters` hit is inside a PhET link
  description and refers to instruments, which is correct.
- **Backward glosses are healthy** - 10 pointers to Topic 1.5, 8 to 1.9, 7 to
  1.4, 6 each to 1.2 and 2.1, plus 2.9. Part 3 connects back to Parts 1 and 2
  properly.
- **Topic 3.3 does not drift from `SAFETY.md`.** All three LiPo
  non-negotiables are present and expanded: charge in a fire-resistant bag,
  never unattended, never a puffed or damaged pack, correct charger and
  settings, plus balance charging. This is the failure that had to be
  corrected in Topic 2.1, and it did not recur here.

## Corrections to the first audit (2026-08-06)

The first pass of this file made two claims the re-audit disproved. Recorded
so they are not repeated:

- ~~"No BBC Bitesize anywhere in Part 3."~~ **Wrong.** Bitesize is cited in
  3.1, 3.7, 3.8, 3.9 and 3.10 - mostly inside Watch the build boxes, which is
  why a Learn More-only grep missed it. Five topics lack it, not ten.
- ~~"Topic 3.1 is the only topic with no external links at all."~~ **Wrong.**
  3.1 carries three references in Learn More and two in Watch the build. They
  are already in search form, with no URLs - which is why a URL grep returned
  zero. 3.1 is the model the rest of the part is being measured against, not
  the gap.
