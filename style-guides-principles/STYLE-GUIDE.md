# VoltForge Gear - Chapter Style Guide

How to write a chapter of this handbook. Applies to every new chapter and to
revisions of existing ones. Derived from the readability review of Chapters
00-10 (see `improvement-suggestions.md`) and the project guiding principles.

---

## 1. Audience and Voice

- Target reader: a curious 11-year-old (and up), UK-based, no prior knowledge.
- British English throughout: tyres, organised, colour, metre.
- Tone: encouraging, direct, never condescending. Failure is information.
- Second person ("you") for the reader, first person plural ("we") for the
  journey.
- Every abstract idea gets a concrete everyday analogy BEFORE the formal
  definition. The formal term should feel like a useful label for something
  the reader already understands.

  Good: "Imagine pushing both ends of a drinking straw. It suddenly bends
  sideways. Engineers call this **buckling**."
  Avoid: "Buckling is an instability phenomenon caused by compressive loading."

- Analogy bank - reuse these rather than inventing weaker ones (one strong
  analogy beats several weak ones):

  | Abstract idea | Preferred analogy |
  |---|---|
  | torque | opening a jam jar / pushing a door near vs far from the hinge |
  | power | carrying shopping upstairs quickly vs slowly |
  | datum | measuring everyone's height from the same floor |
  | feedback | correcting your direction on a bicycle |
  | accuracy vs precision | darts on a dartboard |
  | packaging envelope | a suitcase plus room to open the lid and grab the handle |
  | tolerance stack-up | slightly-too-long blocks placed in a row |
  | anisotropy / layers | a deck of cards or stack of card strips |
  | verification vs validation | fits the drawing vs survives real use |
  | workshop safety | the family kitchen (hot, sharp, spinning - and safe) |

## 2. Sentence and Paragraph Style

- One-sentence-per-line is for: steps, warnings, definitions, punchlines.
- Stories, examples and explanations use short paragraphs of 2-4 sentences.
- If three or more consecutive one-liners could be joined with "and" or
  "because", join them.
- Sentences under ~20 words. One idea per sentence.
- For a dense idea, climb this ladder: analogy -> plain explanation -> formal
  term -> buggy example -> optional detail.
- Any maths gets one fully worked example: the question, the known values, the
  rule, the calculation, then the meaning of the result in words.
- **Think about it prompts.** Never just assert a surprising consequence
  ("without suspension, every bump would launch the buggy into the air").
  Give the reader a moment to work out WHY before you explain. Format: a
  blockquote opening with **Think about it.**, a tiny physical experiment
  they can do on the spot, then a short paragraph resolving it - plus a
  sketch placeholder if the idea is spatial:

  > **Think about it.** Jump off a low step and land with stiff, straight
  > legs. Now jump again and land with bent knees. Which landing felt
  > softer - and where did the "thump" go?

  Aim for one or two per chapter at the most counter-intuitive claims; more
  than that and they stop feeling special.

## 3. Chapter Template (in this order)

1. YAML frontmatter: title, part, chapter, version ("0.1"), status ("Draft"),
   difficulty, estimated_time, prerequisites (list of chapter titles),
   learning_objectives (3-6 bullets).
2. `# Chapter NN - Title` (ASCII hyphen, zero-padded number).
3. A short blockquote hook (a quote or a one-line big idea).
4. `# Learning Objectives` - "By the end of this chapter you will be able to:"
5. `# Before We Begin` - a story or hands-on hook, written as paragraphs.
6. Content sections.
7. Hands-on activities (`# Hands-On Activity N - Name`). Always include at
   least one activity that needs NO special equipment (no printer, no
   calipers), with the equipment version as an upgrade.
8. `# Chapter Mini Project - Name` - the learning-by-doing build (see the
   rules below). Teaching chapters only; build chapters and the capstone
   already produce artifacts.
9. `# Common Beginner Mistakes` (numbered `## Mistake N - Name`).
10. `# Chapter Summary`
11. `# New Words` - a table, `| Word | Meaning |` with `|---|---|` divider.
12. `# Review Questions` - 8-12 numbered questions mixing recall, explanation,
    application and troubleshooting.
13. `# Chapter Checklist` - `- [ ]` items confirming meaningful capability.
14. `# Looking Ahead` - preview of the ACTUAL next chapter (verify the number).

Connect the topic to the buggy within the first 150 words of the chapter.

### Chapter Mini Projects (learning by doing)

Reading about an idea fades; a thing you built and kept does not. Every
teaching chapter ends its activities with one mini project: a small build
that produces a **keepable, working artifact** for the reader's showcase
shelf.

- Materials: household and scrap only - paper, card, rubber bands, pencils,
  spools, tape, glue, string. No printer, no calipers, nothing bought
  specially. 30-60 minutes.
- The build must embody the chapter's core idea, not just decorate it
  (a paper bridge tested to failure for the forces chapter, not a paper
  buggy that only looks nice).
- It always ends with a **reflection step** that ties the artifact back to
  the chapter: label which subsystem each part is, read the failure, chart
  the spread. The reflection is where the learning lands.
- Point out what the artifact does NOT have when that teaches something
  ("your crawler has no control system - you are its brain").
- Prefer proven classic builds, verified in the research pass, over
  invented ones; adapt the framing to the buggy story.
- Include a **Watch the build** box (same format and rules as Learn More,
  max 3 links, verified, search-form) with at least one photo tutorial or
  video, so the reader can SEE the materials and method before building.
  Place it after the safety callout, before the build steps. YouTube
  entries say "with an adult".
- Every mini project gets a safety callout BEFORE the steps (per section
  9), and its FIRST line is always the adult-check: the reader shows a
  responsible adult/guardian what they plan to build before starting, and
  builds with them nearby. The supervising adult - not the book - can see
  the reader's actual materials and surroundings, so the judgement call on
  whether a specific build is safe sits with them (decision 2026-07-14,
  consistent with SAFETY.md "every activity assumes adult supervision").
  Anything sharp or hot adds its specific warnings after that line.
- Close by telling the reader to keep the artifact: the showcase shelf is
  the book's trophy cabinet.

## 4. Length and Break Markers

- Target 700-1,200 lines. If the material genuinely needs more, split the
  chapter or add explicit break markers.
- Insert a break marker at every natural seam (roughly every 25-30 minutes of
  reading):

  > **Good place to pause.** Stretch, get a drink, or try Activity 1 now.
  > The next section starts a new idea.

## 5. Vocabulary Rules

- First-use gloss: any term not yet taught gets a bracket gloss and a pointer
  to its home chapter, e.g. "the ESC (the motor's speed controller - Chapter
  22)". This includes terms from LATER chapters and hobby jargon.
- New terms introduced in this chapter are **bolded** on first use, defined in
  plain language, and listed in the New Words table.
- Budget: at most ~15 new words per chapter. More than that means the chapter
  should split.
- Every New Words entry must also be added to `glossary.md` (alphabetical,
  same plain-language style).
- Terminology registry (never vary these):
  - "drivetrain" for the whole motor-to-wheel system; "gearbox" means only the
    enclosed gear assembly inside it
  - "requirement traceability" (singular "requirement")
  - "chassis", "wheel hex", "hinge pin" (two words)
  - "3D printing" / "printed part" (not "additive part")
  - "revision" = a documented design change; "version" = a project stage
    (V0.1, V1.0)
  - "test coupon" and "packaging envelope", never vague equivalents
- When an older chapter used a different word, bridge explicitly: "the gearbox
  from Chapter 2 is part of what engineers call the drivetrain."

## 6. Characters and Emoji

Unicode is welcome (decision 2026-07-12, replacing the old ASCII-only
rule): the book should look lively and presentable on GitHub. Emoji are
purposeful markers, not confetti.

- **Fixed callout markers** (book-wide, never vary):
  - `> **⚠️ SAFETY**`
  - `> **🤔 Think about it.**`
  - `> **📚 Learn more**`
  - `> **🎬 Watch the build**`
  - `> **☕ Good place to pause.**`
- **Template headings** carry a fixed emoji at the END of the heading:
  Learning Objectives 🎯, Chapter Mini Project 🛠️, Common Beginner
  Mistakes ❌, Chapter Summary 📝, New Words 📖, Review Questions ❓,
  Chapter Checklist ✅, Looking Ahead 🔭.
- **Content headings**: at most one emoji, at the end, meaningfully chosen
  ("# System 1 - The Brain 🧠"). Not every heading needs one.
- **Body prose stays emoji-light**: an emoji earns its place by marking
  something (a warning, a milestone 🏆), not decorating sentences.
- Tables, code blocks, file names and frontmatter stay emoji-free.
- Real engineering notation is used freely: `Ø` (diameter), `±`
  (tolerance), `°` (degrees), `×` (e.g. `4 × Ø3.2 THRU`).
- Plain `-` and `->` remain fine in prose; `→` is also allowed.
- Inside ```mermaid blocks, any character is allowed (unchanged).

## 7. Visuals Policy

Pick the form that fits the idea:
- **Mermaid**: flows, cycles, cause-effect chains, system trees. Never use
  mermaid to restate a bullet list as boxes, and never for spatial/physical
  ideas (a bending beam is not a flowchart).
- **Tables**: comparisons (3+ similar things), decision matrices, specs.
- **Sketch placeholders**: spatial ideas (fits, views, force arrows, part
  anatomy). Format:

  > **[Sketch: three-view drawing of a simple bracket, holes aligned across
  > views]**

  These mark where a real illustration or photo belongs.
- Small ASCII line samples (`- - - -`) are fine for line types and dimension
  arrows. Never keep weak ASCII art just because it already exists - replace
  it with a sketch placeholder.
- **Signature visual**: every technical chapter gets one strong visual for its
  hardest idea (four-dartboard panel for accuracy, three-fit cross-section for
  fits, aligned three views for drawings, dashed envelope for packaging, a
  meshing gear pair for ratios).

## 8. Learn More Boxes

A recurring box, max 3 links, placed next to the relevant section:

> **Learn more**
> - BBC Bitesize (KS3 Design & Technology): search "3D printing"
> - Explain That Stuff: how 3D printers work

Approved sources: BBC Bitesize (KS2/KS3 science, maths, D&T), PhET simulations
(phet.colorado.edu), Explain That Stuff (explainthatstuff.com), Tinkercad
Learn (tinkercad.com/learn), Onshape Learning Centre, NASA/ESA kids resources,
manufacturer knowledge bases (Prusa, Bambu) and official safety guidance.
Verify a link exists before citing it; prefer "search X on site Y" over deep
URLs likely to rot; avoid sales-heavy pages; say in half a line why the link
is worth the reader's time. For Bitesize, use the UK national-curriculum
wording as the search term ("mechanical systems", not "mechanisms";
"fair testing", not "experiments") - curriculum terms are what the pages
are organised around, and they match what the reader hears at school.

## 9. Safety Callouts

For anything hot, sharp, electrical, chemical or spinning:

> **SAFETY**
>
> The nozzle reaches 200 °C. Never touch it while the printer is on or
> cooling. Ask an adult before every print.

- Safety callouts come BEFORE the activity that needs them, not after.
- LiPo battery content additionally requires: charge supervised, use a LiPo
  bag, never charge damaged/puffed packs, correct charger settings.

## 10. Cross-Referencing

- Backward: "Remember X from Chapter N" whenever reusing a taught concept.
- Forward: "(covered in Chapter N / Part N)" for anything not yet taught.
- Each chapter's "Looking Ahead" must name and match the real next chapter.
- Tie content back to the buggy within every major section: the buggy is the
  classroom.

## 11. Build Chapters (Parts 3-5)

Per the guiding principles "Handbook Writing Rule", every build chapter also
includes: learning goal, cheapest valid prototype, parts to buy / reuse /
make, cost checkpoint, modular interfaces, test plan, upgrade path, and a
stop point before the next purchase.

Every test in a build chapter states: the question being tested, the
independent, dependent and control variables (the fair-test pattern from
Chapter 9), the procedure, and a pass/fail condition.

## 12. Publishing a Chapter

1. Save as `Part-N-Name/NN-Chapter-Title.md` (zero-padded, hyphenated).
2. Add New Words to `glossary.md`.
3. Update the chapter's row in `SUMMARY.md` (planned -> v0.1 Draft) and link
   the file.
4. Check: emoji follow the section 6 registry (fixed callout markers, one
   per heading max), Looking Ahead points to the real next chapter, every
   activity has a no-equipment variant, every not-yet-taught term is
   glossed, and the mini project builds from household materials, opens
   its safety callout with the adult-check line, and ends with its
   reflection step.
5. Teaching check: concrete example before each formal term, an analogy for
   each abstract idea, a worked example for any maths, one signature visual
   for the hardest idea, a "Think about it" prompt at the chapter's most
   counter-intuitive claim, and the buggy connection within the first 150
   words.
