# Backlog - Part 3 Book-Wide Items

Sweeps that apply across the whole of Part 3 (Topics 3.1-3.10). Work them into
each topic's pass (per-topic loop in [PLAN.md](PLAN.md)), then tick them here
only when every Part 3 topic is swept.

Legend: [T] textual, [C] context awareness, [V] visual aid, [E] external reference.

Created 2026-08-06. Status: **NOT STARTED**.

## How this backlog differs from Parts 1 and 2

**Part 3 arrived already revised.** The topics were externally revised against
`STYLE-GUIDE.md` and `references/ref-002.md` before this backlog was written,
and it shows. The audit on 2026-08-06 found the structural work essentially
done, so this is a much shorter list than Part 2's - almost everything here is
external references, the glossary, and pacing.

Items were derived by auditing the ten topics directly. Line numbers refer to
the text as merged at `ec92b4d`.

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

- [ ] [E] **40 deep URLs, against a style-guide rule that prefers search
  form.** Section 8: "prefer `search X on site Y` over deep URLs likely to
  rot". Part 3 links directly to specific pages in every topic except 3.1.
  Counts: 3.2 six, 3.3 five, 3.5 five, 3.6 five, 3.10 five, 3.7 four, 3.8
  four, 3.4 three, 3.9 three. This is the largest single item in Part 3 and
  it is mechanical - convert each to the search form, keeping the half-line
  saying why the link is worth the reader's time.
- [ ] [E] **The approved-source list does not cover Part 3's subject, and
  needs a decision before the URLs are rewritten.** Section 8 lists BBC
  Bitesize, PhET, Explain That Stuff, Tinkercad, Onshape, NASA/ESA and
  manufacturer knowledge bases (naming Prusa and Bambu). Part 3 cites 19
  domains, most outside that list:

  | Domain | Uses | On the list? |
  | --- | ---: | --- |
  | phet.colorado.edu | 3 | yes |
  | explainthatstuff.com | 1 | yes |
  | gov.uk, london-fire.gov.uk, ofcom.org.uk | 4 | official safety guidance - yes |
  | horizonhobby, spektrumrc, teknorc, futabausa, hobbywingdirect | 18 | RC manufacturers - not named |
  | pololu, maxongroup, khkgears, fluke | 8 | component manufacturers - not named |
  | nist.gov | 1 | standards body - not named |
  | sciencebuddies.org | 3 | educational - not named |

  These are mostly good sources for the subject. The likely answer is to
  **extend section 8** to cover RC and component manufacturer documentation
  and national standards bodies, rather than to strip the links. Make that
  decision first, record it here, then rewrite.
- [ ] [E] **No BBC Bitesize anywhere in Part 3.** Electricity is core KS3
  physics and Topic 3.2 maps onto it almost exactly - voltage, current,
  resistance, power, circuits. The style guide is explicit that Bitesize
  search terms should use national-curriculum wording, and that it matches
  what the reader hears at school. At minimum 3.2 and 3.3 should carry one.
- [ ] [C] **33 New Words are missing from `glossary.md`.** Part 3's glossary
  was backfilled on 2026-08-06 from the pre-revision text; the revisions then
  added vocabulary. Per-topic lists are in the topic files. 3.1 is the only
  topic fully covered.
- [ ] [T] **Break markers are thin.** Every topic runs 1,074-1,200 lines with
  a single `☕ Good place to pause` - except 3.1 (three) and 3.3 (two).
  Guide suggests a seam roughly every 25-30 minutes of reading; at this
  length that is three or four. This is the cheapest change that improves the
  reading experience across the whole part.
- [ ] [T] **Only one Learn More box per topic.** Each holds three links, so
  the 3-link cap is respected, but section 8 wants boxes "next to the
  relevant section" rather than one block per topic. Split each into two or
  three inline boxes when the URLs are rewritten - the two jobs touch the
  same lines.
- [ ] [V] **Confirm each Mermaid block is a genuine flow.** Only 3.1 and 3.4
  use Mermaid, one block each, so this is a two-minute check rather than a
  sweep. Apply the section 7.1 test: if it shows what something looks like,
  where it is, or which way a force points, it is not Mermaid.

## Checked and found compliant (do not re-litigate)

Recorded so the review pass does not spend time re-deriving these:

- **Figures: done, and done well.** Every topic carries 11 or 12 figures
  against a 10-12 budget for component topics, every one tagged F1-F7 or
  Signature visual, every one with a number, a caption and alt text. Part 3
  is the best-illustrated part in the book. **Do not add figures.**
- **Answers: complete.** Every topic has `# Answers 🔑` with exactly 12
  answers against 12 review questions.
- **Looking Ahead: correct in all ten**, 3.1 → 3.2 through 3.9 → 3.10, and
  3.10 → Topic 4.1 to open Part 4.
- **Length: within target.** 1,074-1,200 lines against a 700-1,200 ceiling -
  the first part in the book that does not overrun it.
- **Think-about-it prompts:** two in every topic except 3.1, which has one.
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
