# Backlog - Topic 2.1 - Workshop Safety and Setup

Source: audit of the v0.1 text (543 lines, 7 new words) against
`STYLE-GUIDE.md` on 2026-08-06. No frozen external review exists for Part 2
- see [part-2-book-wide.md](part-2-book-wide.md) for how these items were
derived. Line numbers refer to the v0.1 text at commit `70ccdda`.

Status: **DONE 2026-08-06** (v0.2 on `Part_2_review`). Research pass first,
then every item below applied. Phase 1 of the Part 2 review; Topic 2.2 next.

> **Deferred to v0.3 - do not reopen at v0.2.** The figure system
> (STYLE-GUIDE section 7) and `# Answers 🔑` (section 3 item 15) were adopted
> later the same day, after this topic was signed off. Topic 2.1 currently
> has 2 figures against the 10-14 budget for a skill topic, neither carrying
> a type tag, number, caption or alt text, no F3 pairs for its 7 Common
> Beginner Mistakes, and no answers for its 11 Review Questions. Per
> STYLE-GUIDE 13.5 this is recorded debt, cleared at v0.3 Prototype-tested,
> rather than a reason to reopen finished work. See `references/ref-002.md`.

Sittings: 1-2. The topic is comfortably inside the length target; its two
existing break markers are adequate. Natural seam is at "Your Workshop Can
Be a Table" (~242), where the topic turns from hazards to workspace setup.

**Context:** this topic was written before the 2026-07-12 conventions
existed (mini project, think prompts, emoji registry, Watch-the-build box).
Most items below are that debt rather than defects in the writing.

## Items to apply

- [x] [T] **Emoji pass.** Not one template heading carries its fixed emoji.
  All seven need it: Learning Objectives 🎯 (~27), Common Beginner
  Mistakes ❌ (~440), Topic Summary 📝 (~472), New Words 📖 (~486), Review
  Questions ❓ (~500), Topic Checklist ✅ (~514), Looking Ahead 🔭 (~539).
  Check the two existing safety callouts use the `> **⚠️ SAFETY**` marker.
- [x] [T] **Topic Mini Project is missing.** The topic already has a strong
  candidate sitting in the wrong clothes: "Engineering Challenge - Your
  Workshop Safety Card" (~408). Promote and reframe it as
  `# Topic Mini Project - Workshop Safety Card 🛠️` - a keepable, laminated
  or card-mounted safety card for the showcase shelf. It needs the full
  treatment: adult-check line first in its safety callout, a Watch-the-build
  box, and a reflection step tying the card back to the hazard/risk
  vocabulary. Verify it produces a keepable artifact (it does) and builds
  from household materials (it does).
- [x] [T] **No "Think about it" prompts.** Two candidates, both at genuinely
  counter-intuitive claims:
  - "Power Off Is the Default" (~136) - why unplugging beats "just being
    careful" around a machine that can start on its own.
  - "Near Misses: Free Lessons" (~422) - why the incident that hurt nobody
    is the most valuable one to write down.
  One is enough if the second feels forced.
- [x] [E] **Learn More is a trailing section, not inline boxes.** `# Learn
  More` sits at ~529, between Topic Checklist and Looking Ahead - outside
  the template order and far from anything it supports. Break it into at
  most two inline `> **📚 Learn more**` boxes placed next to the sections
  they serve (PPE, and battery safety). Approved-source and curriculum
  wording rules apply; verify in the research pass.
- [x] [T] **Template order: "Near Misses: Free Lessons" (~422) sits after
  the activities**, between the Engineering Challenge and Common Beginner
  Mistakes. It is a content section and belongs before
  `# Hands-On Activity 1` (~342). Moving it also puts the near-miss
  think-prompt in front of the activities that could produce one.
- [x] [T] **Safety callout density.** Only two callouts in the book's
  dedicated safety topic, yet it has sections on batteries (~153), hot
  things (~174), sharp things (~188), spinning things (~201) and fumes and
  dust (~215). Each of those five should carry its own `> **⚠️ SAFETY**`
  callout, placed before the hazard is discussed. Cross-check every
  statement against `SAFETY.md` - this topic is what that document
  summarises, so they must not drift.
- [x] [V] **One sketch placeholder in the whole topic.** The four-zone
  workspace (~256) is the topic's signature spatial idea and deserves the
  signature visual: a labelled plan view of a table split into work,
  tools, parts and clear zones. A second placeholder for PPE (~111) would
  help too.
- [x] [C] **Forward glosses.** This topic is one of the better ones - it
  already points at Topic 3.3 and Topic 3.6. Verify both numbers against
  `SUMMARY.md` (batteries 3.3, ESC 3.6) and check nothing else in the
  battery section (~153) is used unglossed.
- [x] Verify: all 7 New Words in `glossary.md` (they are, as of `4074569`);
  Looking Ahead names Topic 2.2 (it does); every activity has a
  no-equipment variant; `estimated_time` bumped to cover the new mini
  project.
- [x] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

- PPE guidance for a home workshop at this age - eye protection in
  particular. Confirm the topic's advice matches current UK guidance and
  `SAFETY.md`.
- LiPo storage and charging claims in "Batteries Need Respect" (~153):
  charge supervised, LiPo bag, never charge damaged or puffed packs,
  correct charger settings (STYLE-GUIDE section 9 requires all four).
- Burn and cut first-aid statements, if any are made - or confirm the topic
  correctly defers to an adult rather than giving first-aid instruction.
- Whether any Learn More source covers workshop safety at KS3 level in
  curriculum wording; if Bitesize has no suitable page, prefer official
  safety guidance over an informal source.
- Mini project: nothing to verify for a card-making build beyond the
  Watch-the-build box needing at least one real photo or video tutorial.

## Research notes (2026-08-06)

**Facts confirmed:**

- Safety glasses: the topic's claim that ordinary glasses are not safety
  glasses is correct and now has a reason attached. Spectacles are not
  impact-tested and leave the sides open; the UK/European standard for eye
  protection is **EN 166**, marked on the frame. Added to the PPE section and
  to `SAFETY.md`, with a note to buy a pair sized for the reader's face.
- LiPo bags: fire-resistant pouches that CONTAIN a failure rather than
  prevent one. Confirmed across RC hobby guidance that a bag does not make
  unattended charging safe - the early warning (swelling, hissing, odd smell)
  only helps if a person is present. Both facts are now in the topic, framed
  as "the bag buys time; you have to be there to use it".
- BBC Bitesize KS3 D&T "health and safety" is correct curriculum wording -
  the KS3 D&T units cover PPE, risk assessment and hazard identification
  under that heading. Verified indirectly via curriculum wording and school
  knowledge organisers, per the Part 1 method (bbc.co.uk blocks the crawler).
- Hazard vs risk as defined in the topic matches standard usage (hazard =
  potential to cause harm; risk = likelihood plus severity). No change.

**Facts corrected:**

- **The battery section contradicted `SAFETY.md`.** SAFETY.md requires
  charging "only in a LiPo-safe bag or container" and "never leave a charging
  battery unattended"; the topic had neither. Both added. This is exactly the
  drift the backlog item warned about - the topic teaches what SAFETY.md
  summarises, so a gap here silently weakens the whole book's battery rules.
- The topic never used the word "LiPo" despite SAFETY.md having a LiPo
  section. Now introduced with a forward gloss to Topic 3.3.
- Soldering iron temperature: stated as "roughly 330-400 °C" to match Topic
  2.9 exactly rather than inventing a second figure. Note that 2.9's range is
  itself still unverified (flagged in `topic-2.9.md`) - if the 2.9 pass
  changes it, change it here too.

**Deferred / notes for later passes:**

- "LiPo bag" was added as an eighth New Word and to `glossary.md`. Budget is
  still well under the ~15 ceiling.
- The four-zone mermaid was removed rather than replaced: it drew a spatial
  layout as a flowchart, which the visuals policy prohibits, and a sketch
  placeholder for the same idea already sat directly beneath it. That sketch
  is now marked as the topic's `[Signature visual:`.
- `TOOLS.md` was not fed from this topic - its kit table points at TOOLS.md
  rather than duplicating it, which is the right split. TOOLS.md still needs
  the Topic 2.7/2.8 content noted in part-2-book-wide.md.
