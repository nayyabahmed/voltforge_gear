# VoltForge Gear - Topic Style Guide

How to write a topic of this handbook. Applies to every new topic and to
revisions of existing ones. Derived from the readability review of Topics
0.0-2.1 (see `improvement-suggestions.md`) and the project guiding principles.

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

  Aim for one or two per topic at the most counter-intuitive claims; more
  than that and they stop feeling special.

## 3. Topic Template (in this order)

1. YAML frontmatter: title, part, topic, version ("0.1"), status ("Draft"),
   difficulty, estimated_time, prerequisites (list of topic titles),
   learning_objectives (3-6 bullets).
2. `# Topic X.Y - Title` (ASCII hyphen; part-relative number, e.g. `1.5`).
   The file keeps its zero-padded `NN-` name on disk (see section 12).
3. A short blockquote hook (a quote or a one-line big idea).
4. `# Learning Objectives` - "By the end of this topic you will be able to:"
5. `# Before We Begin` - a story or hands-on hook, written as paragraphs.
6. Content sections.
7. Hands-on activities (`# Hands-On Activity N - Name`). Always include at
   least one activity that needs NO special equipment (no printer, no
   calipers), with the equipment version as an upgrade.
8. `# Topic Mini Project - Name` - the learning-by-doing build (see the
   rules below). Teaching topics only; build topics and the capstone
   already produce artifacts.
9. `# Common Beginner Mistakes` (numbered `## Mistake N - Name`).
10. `# Topic Summary`
11. `# New Words` - a table, `| Word | Meaning |` with `|---|---|` divider.
12. `# Review Questions` - 8-12 numbered questions mixing recall, explanation,
    application and troubleshooting.
13. `# Topic Checklist` - `- [ ]` items confirming meaningful capability.
14. `# Looking Ahead` - preview of the ACTUAL next topic (verify the number).
15. `# Answers` - model answers, numbered to match the Review Questions. Last
    in the topic so the reader has to travel to reach them, and so the HTML
    build can collapse them behind a reveal (section 13.3).

Connect the topic to the buggy within the first 150 words of the topic.

### Topic Mini Projects (learning by doing)

Reading about an idea fades; a thing you built and kept does not. Every
teaching topic ends its activities with one mini project: a small build
that produces a **keepable, working artifact** for the reader's showcase
shelf.

- Materials: household and scrap only - paper, card, rubber bands, pencils,
  spools, tape, glue, string. No printer, no calipers, nothing bought
  specially. 30-60 minutes.
- The build must embody the topic's core idea, not just decorate it
  (a paper bridge tested to failure for the forces topic, not a paper
  buggy that only looks nice).
- It always ends with a **reflection step** that ties the artifact back to
  the topic: label which subsystem each part is, read the failure, chart
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
  topic or add explicit break markers.
- Insert a break marker at every natural seam (roughly every 25-30 minutes of
  reading):

  > **Good place to pause.** Stretch, get a drink, or try Activity 1 now.
  > The next section starts a new idea.

## 5. Vocabulary Rules

- First-use gloss: any term not yet taught gets a bracket gloss and a pointer
  to its home topic, e.g. "the ESC (the motor's speed controller - Topic
  3.3)". This includes terms from LATER topics and hobby jargon.
- New terms introduced in this topic are **bolded** on first use, defined in
  plain language, and listed in the New Words table.
- Budget: at most ~15 new words per topic. More than that means the topic
  should split.
- Every New Words entry must also be added to `glossary.md` (alphabetical,
  same plain-language style).
- Terminology registry (never vary these):
  - "topic" for a numbered unit of the book (Part N holds Topics N.1, N.2 …;
    "How to Use This Handbook" is the front-matter Topic 0.0). Never "chapter".
  - "drivetrain" for the whole motor-to-wheel system; "gearbox" means only the
    enclosed gear assembly inside it
  - "requirement traceability" (singular "requirement")
  - "chassis", "wheel hex", "hinge pin" (two words)
  - "3D printing" / "printed part" (not "additive part")
  - "revision" = a documented design change; "version" = a project stage
    (V0.1, V1.0)
  - "test coupon" and "packaging envelope", never vague equivalents
- When an older topic used a different word, bridge explicitly: "the gearbox
  from Topic 1.2 is part of what engineers call the drivetrain."

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
  Learning Objectives 🎯, Topic Mini Project 🛠️, Common Beginner
  Mistakes ❌, Topic Summary 📝, New Words 📖, Review Questions ❓,
  Topic Checklist ✅, Looking Ahead 🔭, Answers 🔑.
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

This is an engineering book. A reader learns what a cross-threaded screw looks
like by *seeing one*, not by reading a paragraph about it. Figures are teaching,
not decoration, and the budget below is a floor rather than a ceiling.

### 7.1 Figure types

Every figure is one of these. Naming the type lets a topic's figures be
specified before anything is drawn, and keeps the whole book looking like one
book.

| Tag | Type | What it does | Typical use |
| --- | --- | --- | --- |
| F0 | Mermaid | Flows, cycles, cause-effect chains, system trees | The design cycle, input-process-output |
| F1 | Annotated photograph | A real object with labels | Tools, fasteners, filament, a finished joint |
| F2 | Cross-section | Cuts a part open to show the invisible | Fits, countersinks, inserts, layer structure |
| F3 | Right-versus-wrong pair | Correct beside incorrect | Every Common Beginner Mistake |
| F4 | Sequence strip | 3-5 panels of a process over time | Drilling a clean hole, making a joint |
| F5 | Force / motion overlay | Arrows on a real shape | Load paths, torque, weight transfer |
| F6 | Measured drawing | Dimensioned and to scale | Part briefs, coupons, hole patterns |
| F7 | Comparison array | 3+ variants side by side | Materials, infill percentages, gear ratios |

**F0 is capped at two per topic.** Mermaid draws *relationships*; it cannot
draw *things*. Never use it for a spatial or physical idea - a bending beam is
not a flowchart, and a bench layout is not a tree. If the reader needs to know
what something looks like, where it is, or which way a force points, it is not
Mermaid.

**Tables** remain the right answer for comparisons of 3+ similar things,
decision matrices and specs. Small ASCII line samples (`- - - -`) are fine for
line types and dimension arrows. Never keep weak ASCII art because it already
exists.

### 7.2 Placeholder format

Until the artwork exists, mark its place - with the type tag, so figures can be
counted and costed per production stream:

> **[F2 cross-section: a printed boss with a heat-set insert pressed in.
> Callouts on the insert's knurling, the melt zone, and the screw engaging
> the metal thread.]**

The signature visual of a topic uses the same form with `Signature visual`:

> **[Signature visual, F4: four panels of the same plate being drilled...]**

Write the placeholder as a real art brief - what is shown, what is labelled,
what the reader should notice. A vague placeholder becomes a vague figure.

### 7.3 Numbering, captions and alt text

Every figure carries all three:

- **Number** - `Figure N.M.k` in topic order, so prose can say "see Figure
  3.9.2" instead of "the sketch above".
- **Caption** - one sentence saying *what to notice*, never a restatement of
  the title. The caption is where the teaching lands.
- **Alt text** - one sentence describing the figure for a reader who cannot
  see it. It is also the fastest test of whether a figure has a point: if the
  alt text is hard to write, the figure is unclear.

### 7.4 Figure budget per topic

| Topic type | Figures |
| --- | --- |
| Concept topics (Part 1) | 6-8 |
| Skill topics (Part 2) | 10-14 |
| Component topics (Part 3) | 10-12 |
| Build topics (Part 4) | 12-16 |
| Capstones and challenges | 4-6 |

Anchor them to the template: the signature visual takes the hardest idea, every
"Think about it" shows its setup, every mini project gets a sequence strip plus
a photo of the finished artifact, every Common Beginner Mistake gets an F3 pair,
and any New Word naming a physical thing gets a thumbnail.

### 7.5 House rules for artwork

- **Source format is SVG** for anything drawn, so labels stay selectable and
  correctable, it scales to print, and it can be made theme-aware later.
  Photographs are raster; their labels are added as vector.
- **Never generate accuracy-critical artwork.** A beautiful but wrong diagram
  is worse than no diagram, because a young reader cannot tell. Technical
  figures are drawn by a human, derived from CAD, or photographed.
- **Palette**: the VoltForge identity - volt-blue, forge-orange, brushed
  steel. One accent colour per figure carries the meaning (forge-orange =
  look here / danger / the part that moves); everything else stays neutral.
- **Every figure must survive greyscale.** Never encode meaning in colour
  alone - use position, labels or hatching as well.
- Labels are British English, sentence case, and kept as text, never
  rasterised into the image.

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

- Backward: "Remember X from Topic N.M" whenever reusing a taught concept.
- Forward: "(covered in Topic N.M / Part N)" for anything not yet taught.
- Each topic's "Looking Ahead" must name and match the real next topic.
- Tie content back to the buggy within every major section: the buggy is the
  classroom.

## 11. Build Topics (Parts 3-5)

Per the guiding principles "Handbook Writing Rule", every build topic also
includes: learning goal, cheapest valid prototype, parts to buy / reuse /
make, cost checkpoint, modular interfaces, test plan, upgrade path, and a
stop point before the next purchase.

Every test in a build topic states: the question being tested, the
independent, dependent and control variables (the fair-test pattern from
Topic 1.9), the procedure, and a pass/fail condition.

## 12. Publishing a Topic

1. Save as `Part-N-Name/N.M-Title.md`, where `N.M` is the topic's displayed
   part-relative number (`1.5-Measurement.md`, `2.1-Workshop-Safety-and-Setup.md`).
   Cover art matches the same number (`assets/topic_covers/Topic 1.5 Cover.png`),
   and the build's `--chapters` selection takes those numbers too.
2. Add New Words to `glossary.md`.
3. Update the topic's row in `SUMMARY.md` (planned -> v0.1 Draft) and link
   the file.
4. Check: emoji follow the section 6 registry (fixed callout markers, one
   per heading max), Looking Ahead points to the real next topic, every
   activity has a no-equipment variant, every not-yet-taught term is
   glossed, and the mini project builds from household materials, opens
   its safety callout with the adult-check line, and ends with its
   reflection step.
5. Teaching check: concrete example before each formal term, an analogy for
   each abstract idea, a worked example for any maths, one signature visual
   for the hardest idea, a "Think about it" prompt at the topic's most
   counter-intuitive claim, and the buggy connection within the first 150
   words.
6. Figure check (section 7): the topic meets its figure budget, every figure
   has a type tag, a number, a caption and alt text, no Mermaid is doing a
   spatial job, and F0 blocks number two or fewer. **A topic does not reach
   v0.1 without its figure list specified** - retrofitting figures into
   finished prose is the expensive path.

## 13. Authoring for Three Outputs

The book is written once in Markdown and published three ways: GitHub (the
working preview), print PDF and EPUB, and an interactive HTML edition. Markdown
stays the source; HTML is a build output (see `references/ref-001.md` section
7 for the decision and its reasoning).

That places one obligation on authoring: **the Markdown must be structured
enough for a build step to turn it into components reliably.** The good news is
that most of the conventions in this guide already do that - they were written
for consistency, and consistency is what makes them parseable.

### 13.1 The governing rule

> A convention may only be adopted if it still reads well as plain Markdown.
> Nothing is added to source purely to serve the HTML build.

Every rule below is invisible-cost: it changes what you write, not how much.

### 13.2 What already works (do not change it)

| Convention | Becomes in HTML |
| --- | --- |
| `> **⚠️ SAFETY**` and the section 6 marker registry | Styled callouts that cannot be skimmed past |
| `- [ ]` in Topic Checklist | Tickable boxes with saved progress |
| `# New Words 📖` table + `glossary.md` | Hover and tap tooltips on first use |
| `### Term` glossary entries | The tooltip source, alphabetically addressable |
| "Topic N.M" written in prose | Auto-linked cross-reference - no new syntax needed |
| ATX headings | Navigation, anchors and search index |

The fixed callout markers are the single most valuable thing here. Vary them
and the HTML build cannot tell a safety warning from a tip.

### 13.3 What needs care

- **"Think about it" resolution.** The paragraph *immediately after* the
  prompt blockquote is the resolution, and the HTML build collapses it so the
  reader genuinely pauses. Keep it to one paragraph, and never put anything
  between the prompt and its answer.
- **Review Questions need answers.** Without them there is nothing to reveal,
  and a parent or mentor running a session has nothing to check against. Put
  them at the end of the topic under `# Answers 🔑`, numbered to match. New
  topics include them from v0.1.
- **One idea per heading.** Headings become anchors and navigation entries, so
  a heading covering two ideas produces a link that lies about its
  destination.
- **Tables stay real tables.** Never lay data out with spaces inside a code
  fence; a pipe table becomes a responsive HTML table, a code fence does not.
- **Code fences carry a language tag** (```text, ```mermaid). The build uses it
  to decide what to render and what to leave alone.

### 13.4 Raw HTML in source

Permitted only where Markdown genuinely cannot express the layout - currently
the F3 right-versus-wrong pairs and F7 comparison arrays of section 7. Keep it
to a single wrapper element, never inside prose, and prefer a build shortcode
once one exists. Everything else stays Markdown so the GitHub preview and the
review diffs stay readable.

### 13.5 Applying this to already-written topics

These conventions arrived on 2026-08-06, after Part 1 and Topic 2.1 reached
v0.2. Retro-fitting them everywhere at once would stall the review programme,
so:

- **New topics** follow them from v0.1.
- **Topics still to be reviewed** pick them up during their existing review
  pass - the figure list and the answers are added as backlog items rather
  than as a separate sweep.
- **Topics already at v0.2** carry the gap as recorded debt, cleared at v0.3
  Prototype-tested. Record it in the part's book-wide backlog file rather than
  silently reopening finished work.

This is deliberate: a rule that forces thirty files to be reopened the day it
is written is a rule that will be ignored.
