# Backlog - Topic 2.6 - 3D Printing Materials

Source: audit of the v0.1 text (1,998 lines, 14 new words) against
`STYLE-GUIDE.md` on 2026-08-06. See
[part-2-book-wide.md](part-2-book-wide.md) for method. Line numbers refer to
the v0.1 text at commit `70ccdda`.

Status: **NOT STARTED**. Phase 2 of the Part 2 review.

Sittings: 5. Well over the length target, but with **five** break markers it
is the best-paced of the long topics - add at most one, around "Moisture -
The Invisible Ingredient" (~919).

> **This topic carries the heaviest research load in Part 2.** It quotes
> material properties, temperatures and drying figures for seven filament
> families. Budget the research pass accordingly and do it before any
> editing - several items below cannot be resolved until the numbers are
> verified.

## Items to apply

- [ ] [E] **Verify every material number before anything else.** See the
  research topics below. Until that is done, treat all quoted temperatures,
  Shore hardness values, drying times and heat-resistance claims as
  unconfirmed.
- [ ] [V] **Figures: 1 against a budget of 10-14** (STYLE-GUIDE 7.4,
  skill topic). At 1,998 lines the topic currently runs one figure per
  ~1998; the target is one per 40-80. This is the largest single item in
  this file. See `references/ref-002.md` for the taxonomy.
  The thinnest ratio in Part 2 - one placeholder across 1,998 lines. The
  property map at ~715 is the signature visual; everything else is missing.
  Priority: "Test Coupon 1 - The Bend Bar" (~1199), "Test Coupon 2 - The
  Screw Pad" (~1228), "Read the Failure Surface" (~1260) where the reader
  must tell ductile from brittle by eye, plus F7 arrays for the seven
  filament families (~383-648) and "A Sensible Grit Progression" of moisture
  damage at "Moisture - The Invisible Ingredient" (~919).
  Conventions to apply to every figure, existing ones included (7.2/7.3):
  type tag `[F1-F7 ...]`, `Figure 2.6.k` number, a one-sentence caption
  saying what to notice, and alt text.
- [ ] [V] **F3 pairs for the 12 Common Beginner Mistakes.** The highest-value
  figure type in the book and currently unused here - a right-versus-wrong
  pair per mistake, or one combined F3 array. Prose alone cannot show a
  reader what the wrong version looks like.
- [ ] [T] **Add `# Answers 🔑`** (STYLE-GUIDE 3 item 15, 13.3) with model
  answers numbered to match the 12 Review Questions. Needed for the HTML
  reveal and for a mentor running a session.
- [ ] [E] **Trailing `# Learn More` section at ~1981** - outside the
  template order. Break into inline boxes: a manufacturer material guide at
  "The Working Material Set" (~689) and a moisture or filament-drying
  reference at "Moisture - The Invisible Ingredient" (~919).
- [ ] [C] **Forward glosses are partial.** The topic points at Topic 3.6
  once, but uses "the ESC" (~311) and "steering-servo mounts" (~182) with
  no pointer at first use. Gloss per `SUMMARY.md` (ESC 3.6, servo 3.5,
  motors 3.7).
- [ ] [T] **Two "Think about it" prompts already present** - confirm they
  sit at the counter-intuitive claims. The strongest candidate is
  "Stiffness" versus "Toughness" (~167 / ~193): a reader will assume the
  stiffer material is the stronger one, and Hands-On Activity 2
  "Stiffness Is Not Toughness" (~1352) already exists to resolve it. Also
  consider "Creep: The Slow Failure" (~262) - a part that passes every test
  and then fails a week later.
- [ ] [T] **Six hands-on activities plus a mini project** is the most in
  Part 2. Confirm this is not activity fatigue: check each earns its place,
  and that Activity 6 "Printed Material Comparison" (~1456) does not
  duplicate the mini project's sample board (~1556).
- [ ] [T] **Check the worked example is complete.** "Worked Example -
  Choosing a Bumper Material" (~772) is the topic's teaching centrepiece;
  confirm it shows question, known values, rule, decision and the meaning
  of the result in words, per style guide section 2.
- [ ] [C] **Traceability** (~a New Word here) already exists in the
  glossary from Part 1 with a measurement sense; the glossary entry gained
  the material sense on 2026-08-06. Confirm the topic's use and the
  glossary now agree.
- [ ] [T] **Typographic consistency.** The topic uses curly quotation marks
  in headings and prose (e.g. ~136 “Strong” Is Not One Property). Unicode
  is welcome per section 6, but confirm the quote style is consistent with
  the rest of Part 2 rather than mixed within the file.
- [ ] Verify: all 14 New Words in `glossary.md` (they are); Looking Ahead
  names Topic 2.7 (it does); every activity has a no-equipment variant
  (Activities 1-4 are equipment-free; 5 and 6 need a printer); mini project
  keeps its adult-check line and Watch-the-build box.
- [ ] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update `SUMMARY.md` + `WRITING-TRACKER.md`.

## Research topics (run before editing)

**Every number in the material sections needs a source.** Work through them
family by family against Prusa and Bambu knowledge bases and manufacturer
technical data sheets:

- PLA (~383), PETG (~435), TPU (~482), ASA and ABS (~547), Nylon (~591),
  Polycarbonate (~621), composites (~648): print temperature, bed
  temperature, glass transition temperature, and whether an enclosure is
  required.
- Heat resistance claims (~294) - especially any statement about a part
  softening in a hot car or in sunlight, which the buggy story invites.
- UV and weather resistance (~326) - the PLA-degrades-outdoors claim and
  the ASA-is-UV-stable claim both need sources.
- Creep (~262) - confirm the plain-language description matches how the
  phenomenon actually works, and that the buggy example is realistic.
- Shore hardness (~482) - confirm the scale is described correctly and that
  any TPU hardness values quoted are typical.
- Drying: temperatures and times per material (~919, ~949), and confirm the
  storage advice (desiccant, sealed containers) matches current guidance.
- Nozzle wear from composite filaments (~648, ~1043) - confirm the hardened
  nozzle recommendation and any wear rate claimed.
- Sustainability claims (~1066) - PLA compostability in particular is
  widely overstated; verify carefully or soften the claim.
- Cross-check every safety-adjacent statement (fumes from ABS/ASA,
  enclosure ventilation) against `SAFETY.md`.
- Mini project: re-verify Watch-the-build sources for the Material
  Behaviour Sample Board.

## Research notes

(To be filled during the pass.)
