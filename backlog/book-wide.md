# Backlog - Book-Wide Items

From `style-guides-principles/improvement-suggestions.md` (review of
2026-07-11). These apply across chapters: work them into each chapter pass
(see PLAN.md), then tick them here only when the whole of Part 1 is swept.

Legend: [T] textual, [C] context awareness, [V] visual aid, [E] external reference.

- [ ] [T] **One-sentence-per-line fatigue.** Keep one-line-per-sentence for
  steps and cautions; merge 2-4 connected sentences into short paragraphs for
  stories and explanations (door/shelf/dartboard/bath-tap narrative passages
  are the worst offenders).
  - Progress: applied to Ch 00, and to the story openers of Ch 02 and Ch 06
    in dd772e8; Ch 02 swept fully 2026-07-14. Remaining chapters pending.
- [ ] [T] **Chapter length.** Every chapter from 02 onwards is too long for
  one sitting. Add break markers at the natural seams listed per chapter
  ("Good place to pause..." format, STYLE-GUIDE section 4). Chapter 04 gets
  explicit Part A / Part B headings (see PLAN.md standing decision - no real
  split).
- [ ] [C] **First-use gloss convention.** Any term not yet taught gets a
  one-line bracket gloss plus its home-chapter pointer. Offender list lives
  in the per-chapter files. Verify every chapter number against `SUMMARY.md`
  (the review's own example "ESC - Chapter 22" is stale; ESC is Chapter 25).
- [ ] [C] **Terminology to reconcile across chapters:**
  - [x] "gearbox" (Ch02) vs "drivetrain" (Ch03/04) - add the bridging line in
    Ch03 ("the gearbox from Chapter 2 is part of what engineers call the
    drivetrain"); registry says "drivetrain" for the whole system.
    APPLIED 2026-07-14 in Ch03 "A Common Mistake".
  - [ ] "requirement traceability" (Ch10/glossary) vs "requirements
    traceability" (Ch09) - standardise on the singular form.
  - [x] "Hinge pin" vs "hinge-pin" (Ch04) - standardise as "hinge pin"
    (two words, per the terminology registry). APPLIED 2026-07-14 in the
    Ch04 pass (one hyphenated instance fixed).
  - [ ] Ch05 "measurement uncertainty" vs Ch06 "error/range/repeatability" -
    add one sentence in Ch06 linking the two vocabularies.
- [ ] [E] **"Learn More" box pattern.** 2-3 links max, next to the relevant
  section, approved sources only (STYLE-GUIDE section 8). Placements listed
  per chapter. Plan the electricity/magnetism links now for Part 3.
- [ ] [V] **Weak mermaid pattern.** Replace mermaid that merely restates a
  bullet list. Mermaid for flows and cycles; tables for comparisons; sketch
  placeholders for spatial ideas.
- [ ] [T] **"Think about it" prompts** (reader feedback on Ch 01, now
  STYLE-GUIDE section 2): wherever a chapter asserts a surprising
  consequence without letting the reader wonder why, add a think-prompt
  (tiny on-the-spot experiment) before the explanation, with a sketch
  placeholder if spatial. One or two per chapter at most. Specific
  placements are in the chapter files; check for candidates in every pass.
- [ ] [E] **Bitesize search terms use curriculum wording** (reader feedback
  on Ch 01, now STYLE-GUIDE section 8): when adding or verifying Learn More
  boxes, prefer the national-curriculum term ("mechanical systems", "fair
  testing") over informal synonyms.
- [ ] [T] **Chapter Mini Projects - "learning by doing"** (reader feedback,
  2026-07-12; now STYLE-GUIDE section 3): every teaching chapter ends its
  activities with a small household-materials build producing a keepable
  artifact, closed by a reflection step tying it to the chapter's idea.
  Every mini project's safety callout OPENS with the adult-check line -
  show a responsible adult the plan first, build with them nearby
  (decision 2026-07-14, STYLE-GUIDE section 3; Ch 01/02/03 retrofitted).
  Candidates researched and web-verified 2026-07-12 (re-check the source
  during each chapter's research pass):
  - Ch 01: cotton reel crawler (rubber-band-through-spool classic; sources:
    Instructables "Cotton reel tanks", minieco.co.uk) - reflection: find
    each system; the missing one is control. APPLIED 2026-07-12.
  - Ch 02: mini chain-reaction machine from kitchen objects (Exploratorium
    Tinkering "Chain Reaction @ Home") - reflection: name each interface
    and what it carries; trace the cause-and-effect chain.
    APPLIED 2026-07-14 (source re-verified in the research pass).
  - Ch 03: cardboard gear pair on skewer axles, different tooth counts
    (4-H "Make Your Own Cardboard Gears" PDF; Instructables "working
    gears from junkmail and cardstock"; Technovation gearbox guide -
    Experiland dropped, could not re-verify) - reflection: count turns to
    feel the ratio, feel the torque trade. APPLIED 2026-07-14.
  - Ch 04: paper bridge tested to failure with coins (Science Buddies
    "Build the Best Paper Bridge"; PBS Kids) - reflection: read the
    failure - what bent, what buckled, why shape beat material.
    APPLIED 2026-07-14 (source re-verified; Scientific American "Paper
    Bridges" replaced the unconfirmed PBS Kids link).
  - Ch 05: cardboard sliding caliper (Instructables "Make a Cardboard
    Caliper"; ikatbag) - reflection: zero it, then measure five household
    objects and record them properly.
  - Ch 06: craft-stick catapult with fixed launch setup (Steam Powered
    Family / Little Bins for Little Hands) - reflection: ten launches,
    chart the spread; accuracy vs precision live, fair-test rules.
  - Ch 07: matchbox-style sliding drawer sized to a chosen treasure -
    tune the fit: too tight jams, too loose rattles (packaging classic;
    weakest single source - needs its own write-up in the research pass).
  - Ch 08: drawing-exchange build (TeachEngineering "The Universal
    Language of Engineering Drawings"): draw three views of a small
    object, swap with a family member, build from each other's drawing -
    reflection: where the drawing failed as a contract. Artifact: object
    + drawing displayed together.
  - Ch 09: cardboard phone stand through the full design cycle (Science
    Buddies / DiscoverE "Make a Cell Phone Stand") - requirements,
    concepts, decision matrix, prototype, fair test, iterate. Genuinely
    useful artifact.
  - Ch 00 and capstone: none - Ch 00 has no technical content (at most,
    set up the showcase shelf and notebook); the capstone IS the project.
