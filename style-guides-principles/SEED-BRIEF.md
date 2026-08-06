# Seed Authoring Brief

**For:** whoever or whatever writes the first draft of a topic.
**Date:** 2026-08-06
**Read with:** `STYLE-GUIDE.md` (the rules) and `references/ref-002.md`
(why figures matter so much here).

A seed draft is not a finished topic. It goes through a review pass that fixes
numbering, glossary entries, cross-references and factual verification. Those
are cheap to fix and need knowledge of the whole book, so **do not spend
effort on them.**

What is *expensive* to fix later is engagement: the analogy that makes an idea
land, the prompt that makes a reader wonder, the picture that shows what a
paragraph cannot, the build they will keep. Retrofitting those into finished
prose costs far more than writing them in. **That is the job of a seed draft.**

---

## 1. The one rule that saves the most work

> **Mark what you are unsure of. Never invent precision.**

A missing item is cheap - it is visible and gets filled in. A confidently
wrong item is expensive, because somebody has to *notice* it first.

Use these markers and keep them exactly as written, so they can be found
mechanically:

| Situation | Write this | Never write |
| --- | --- | --- |
| A term taught in a later topic | `[GLOSS: servo -> Part 3]` | "the servo (Topic 3.5)" |
| A number needing verification | `[VERIFY: nozzle temperature for PETG]` | "245 °C" |
| An external link or source | `[SOURCE: a beginner soldering video]` | An invented URL |
| The next topic in Looking Ahead | `[NEXT TOPIC]` | A guessed topic number |
| A safety rule you are unsure of | `[SAFETY-CHECK: charging supervision]` | An invented rule |

Topic numbers, glossary entries and verified figures are added during review
against `SUMMARY.md`, `glossary.md` and `SAFETY.md`. Guessing at them creates
work; marking them removes it.

**Safety content is the strictest case.** If you are not certain a safety
statement is correct, mark it rather than writing it. A plausible-sounding
wrong safety rule is the single worst thing a seed draft can contain.

---

## 2. What "engaging" means here, concretely

Not exclamation marks. Not "Isn't that amazing?". The reader is a curious
11-year-old who wants to *build a fast buggy* — engagement means the topic
keeps answering "why does this matter to my buggy?".

Per topic, aim for:

| Element | Quota | Why it earns its place |
| --- | --- | --- |
| **Figures** (see section 3) | 6-16 by topic type, per STYLE-GUIDE 7.4 | The biggest single engagement gap in the book today |
| **Concrete analogy before every formal term** | every abstract idea | "Pushing both ends of a straw" before "buckling" |
| **Think about it prompts** | 1-2, at the most counter-intuitive claim | Let the reader be wrong first; it is the moment learning sticks |
| **Story hook opening** | 1, in Before We Begin | A scene, not a definition |
| **Buggy connection** | within the first 150 words, then in every major section | The buggy is the classroom |
| **Topic Mini Project** | 1, household materials, keepable artifact | The thing they still own in a year |
| **Common Beginner Mistakes** | 5-7, each a real failure | Where the reader recognises themselves |
| **Hands-On Activities** | 2-4, at least one needing no equipment | Never gate learning behind a purchase |

Use the analogy bank in STYLE-GUIDE section 1 rather than inventing weaker
analogies. One strong analogy beats three vague ones.

---

## 3. Figures are the priority

This is where seed drafts have been weakest, and where retrofitting is most
expensive. The book currently averages one figure per ~500 lines; the target
is one per 40-80.

**You are not drawing anything.** You are writing the brief for each figure, in
place, so an illustrator or a CAD export can produce it later.

Format, with the type tag from STYLE-GUIDE section 7.1:

> **[F3 right-versus-wrong: two panels of the same M3 screw entering a printed
> boss. Left, started straight - threads aligned, screw upright, labelled
> "turn backwards until it clicks". Right, cross-threaded - screw visibly
> tilted, torn thread material at the hole mouth. Same viewing angle in both.]**

Rules that make a brief usable:

- **Say what is shown, what is labelled, and what the reader should notice.**
  "A diagram of a servo" is not a brief.
- **Pick the type deliberately** — F1 photo, F2 cross-section, F3
  right-versus-wrong, F4 sequence strip, F5 force overlay, F6 measured
  drawing, F7 comparison array.
- **Every Common Beginner Mistake wants an F3 pair.** This is the highest-value
  figure type in the book and the most under-used.
- **Every Think about it wants a figure of the setup**, so the reader can see
  what to try.
- **Mermaid (F0) is capped at two per topic** and only for flows and cycles.
  If it shows what something looks like, where it is, or which way a force
  points, it is not Mermaid. Do not reach for Mermaid as the default visual —
  that habit is what this brief exists to break.

---

## 4. What not to spend effort on

These are handled during review and are cheaper there. Doing them in a seed
draft usually creates work rather than saving it:

- **Topic numbers in cross-references** — use `[GLOSS: ...]` markers.
- **The glossary** — write the New Words table in the topic; the glossary is
  synced afterwards.
- **Verified facts and figures** — temperatures, torques, currents, drying
  times, standards. Mark them.
- **External links** — mark them; they are verified before they land.
- **Exact line counts and break-marker placement** — write the content; break
  markers are placed during review.
- **Emoji on template headings** — apply them if convenient, but they are
  applied mechanically later, so do not agonise.

---

## 5. Per-topic self-check before handing over

- [ ] Opens with a story or scene, not a definition
- [ ] Connects to the buggy within the first 150 words
- [ ] Every abstract idea has a concrete analogy *before* the formal term
- [ ] 1-2 Think about it prompts at genuinely counter-intuitive claims, each
      followed by a single resolving paragraph
- [ ] Figure briefs meet the section 7.4 budget, each with a type tag, and
      each says what to notice
- [ ] Every Common Beginner Mistake has an F3 right-versus-wrong brief
- [ ] A Topic Mini Project from household materials, producing something
      keepable, ending in a reflection step
- [ ] At least one activity needs no special equipment
- [ ] Mermaid used twice at most, and only for flows or cycles
- [ ] Every uncertain term, number, link and safety rule carries its marker
- [ ] New Words table present, at most ~15 entries
- [ ] Review Questions written, with an `# Answers` section matching them
- [ ] British English throughout

---

## 6. Why this division of labour

Seed drafting and review are good at different things. Drafting is good at
volume, structure, analogy and variety. Review is good at consistency,
cross-referencing and verification — because it can see the whole book at
once and check claims against sources.

Sending consistency work upstream produces confident guesses that must then be
hunted down. Sending engagement work downstream produces prose that has to be
reopened and rewritten. **Put creativity first and consistency second, and
both halves get cheaper.**
