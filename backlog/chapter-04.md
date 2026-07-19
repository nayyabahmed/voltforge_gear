# Backlog - Chapter 04 - Forces and Why Parts Break

Source review: 1,687 lines, 27 new words (actually 28 in the table). Line
numbers refer to the original v0.1 text. Created 2026-07-14 from the frozen
review (improvement-suggestions.md) plus the 2026-07-12/14 conventions.
Status: COMPLETE 2026-07-14 (research pass + all items applied in one pass
on `review-chapter-4`, out of PLAN.md phase order at user request).

Standing decision (PLAN.md): NO real split. Explicit Part A / Part B
headings - Part A "How Parts Are Loaded" (through Buckling, ~669), Part B
"Designing So Parts Do Not Break" - with a mid-chapter recap table and a
break marker at the seam.

Break points: after Impact Loads (~449, load types -> stress/strength);
the Part A/B seam (~669); before Hands-On Activity 1 (~1251).

- [x] [C] "shock tower" used at ~204 but only explained at ~1141;
  "servo saver" (~1093), "screw boss" (~756), "gear mesh" (~1184) never
  defined - gloss on first use (servo saver home: Ch28 Steering Systems;
  gear mesh home: Ch27 Gears and the Drivetrain).
- [x] [C] Add backward refs: torque -> Ch03 (~111, ~289); reaction forces ->
  Ch03's ground-push passage (~368, honouring Ch03's "more in Chapter 4"
  forward ref); "trace the full load path" -> Ch02 systems thinking (~1502).
- [x] [T] Materials run (elastic -> permanent -> fracture, ~555-609) reads
  like flashcards - tighten into short paragraphs.
- [x] [T] De-staccato sweep of the chapter's other narrative passages
  (book-wide item; the whole chapter is one-line-per-sentence heavy).
- [x] [V] Bending mermaid (~232) does not look like a bending beam -
  replace with a labelled sketch of a beam bowing (top squeezed, bottom
  stretched).
- [x] [V] Fillet ASCII "|_ vs |)" (~745) is unreadable - replace with a
  labelled sharp-vs-rounded corner sketch.
- [x] [V] Shear mermaid (~272) reads as a list - card-stack sketch with
  offset arrows. Same treatment for the tension/compression/torsion arrow
  mermaids and the five-loads tree (~141): fold them into one signature
  five-load-types sketch panel (the chapter's signature visual).
- [x] [V] Photo of a real broken RC part (fracture surface) at "Fracture"
  (~596) and "Reading a Failure" (~1413) - sketch/photo placeholders.
- [x] [E] Learn More boxes: Bitesize forces & elasticity at Elastic
  Deformation (~555); pressure (force/area) at Stress (~451); materials
  (brittle/ductile) at ~613; Explain That Stuff bridges/structures at
  "Why Shape Matters" (~671); fatigue source at ~882; kid-friendly
  3D-printing explainer at Print Orientation (~973). Verify all in the
  research pass; use curriculum wording for Bitesize search terms.
- [x] [T] "Think about it" prompts (max two): one at the paper-bridge
  story (~73) - fold and test before the chapter explains why shape wins;
  one at Stress Concentration (~734) - tear paper with and without a tiny
  nick, why does the nick matter so much?
- [x] [T] Chapter Mini Project (STYLE-GUIDE section 3): paper bridge
  tested to failure with coins (sources: Science Buddies "Build the Best
  Paper Bridge", PBS Kids - re-verify in research pass). Builds on
  Activity 1 and the beam-shapes challenge: design-build-test-iterate to
  a best bridge, read the failure in the reflection (what bent, what
  buckled, why shape beat material). Safety callout opens with the
  adult-check line (2026-07-14 convention). Keep the winning bridge +
  failure notes for the showcase shelf.
- [x] [T] Activity 4 (paperclip fatigue) mentions eye protection and
  supervision in the materials list - promote to a proper SAFETY callout
  before the steps.
- [x] Part A / Part B headings + mid-chapter recap table at the seam.
- [x] Break markers at the three seams listed above.
- [x] Emoji pass per STYLE-GUIDE section 6.
- [x] Check all 28 New Words exist in glossary.md ("Bending" looks absent
  from the glossary heading list - add if missing); estimated_time bump
  for the mini project.
- [x] Final pass: verify checklist (PLAN.md step 5), bump frontmatter to
  0.2/Reviewed, tick rows here, update SUMMARY.md + TRACKER.md.

## Research notes (2026-07-14)

- **Mini project source: confirmed.** Science Buddies "Build the Best
  Paper Bridge" exists (sciencebuddies.org/stem-activities/
  build-best-bridge; pennies as the load, folded cross-sections beat flat
  paper - exactly the chapter's shape-beats-material lesson). Scientific
  American runs the same activity as "Paper Bridges"; used instead of the
  unconfirmed PBS Kids page in the Watch-the-build box.
- **Explain That Stuff: both articles confirmed** - "How bridges work"
  (explainthatstuff.com/bridges.html - bridges as balanced tension and
  compression, matches the chapter's framing) and "How do 3D printers
  work?" (explainthatstuff.com/how-3d-printers-work.html - layer-by-layer
  FDM, right for Print Orientation).
- **Bitesize pages (verified indirectly - bbc.co.uk blocks the crawler):**
  KS3 Physics "pressure" (pressure = force ÷ area is KS3 curriculum
  content) for the Stress section; GCSE Physics "forces and elasticity"
  (official BBC podcast transcript exists; AQA topic name) for Elastic
  Deformation, flagged as a look-ahead; GCSE D&T "materials and their
  working properties" (AQA spec heading, covers brittle/ductile/tough)
  for Brittle and Ductile Failure, look-ahead.
- **Curriculum wording note:** school physics says elastic vs INELASTIC
  (or plastic) deformation where the chapter says "permanent
  deformation" - one-line vocabulary bridge added in the chapter.
- **Fatigue Learn More box: dropped.** No page on an approved source
  could be verified for fatigue at this level (industrial/engineering
  sites only). The paperclip activity carries the idea; revisit if a
  Bitesize or ETS page turns up.
- **Anisotropy facts: chapter is accurate.** Industry knowledge bases
  agree layer bonds are the weak direction (Z strength commonly quoted
  ~30-50% of XY for FDM). The chapter stays qualitative - no numbers
  added; detailed treatment correctly deferred to the printing chapters.
- **Glossary check: "Bending" is missing from glossary.md** (jumps from
  Bearing to Bilateral Tolerance) - add it during the apply pass.
- No safety-critical claims in this chapter; Activity 4 (paperclip
  fatigue) gets a proper SAFETY callout with the adult-check line.
