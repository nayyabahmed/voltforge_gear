# Backlog - Chapter 02 - Systems Thinking

Source review: 1,194 lines. Line numbers refer to the original v0.1 text.
Status: COMPLETE 2026-07-14 (research pass + all remaining items applied on
`review-chapter-2`; earlier half was dd772e8).

Break points to add: after the cause-and-effect chain (~line 480); second
seam before Hands-On Activity 1 (~line 892).

- [x] [C] ESC first used at ~232 but only expanded at ~833 - expand on first
  use. *(done dd772e8: glossed at the Processes list as "the motor's
  electronic speed controller - Chapter 25")*
- [x] [C] Drivetrain part names (pinion, spur, differential, driveshafts,
  ~380) and "torque" (~434) used before Ch03 defines them - add "(we'll meet
  these in Chapter 3)". *(done dd772e8)*
- [x] [C] "2-cell battery" (~717) - "cell" never explained. *(done
  2026-07-14: glossed in Making Requirements Concrete - "two smaller
  units, called cells - Chapter 22")*
- [x] [T] "Before We Begin" (41-77): merge the one-line runs into 2-3 short
  paragraphs. *(done dd772e8)*
- [x] [T] "Cause and Effect" (482-514): merge the one-line runs into short
  paragraphs. *(done 2026-07-14, plus a full de-staccato sweep of the
  chapter's other narrative passages: bath story, outputs, boundaries,
  connections, interfaces, mistakes, summary)*
- [x] [T] The abstract systems-thinking definition (~125) lands before any
  concrete example - move the toaster example first or add a buggy hook
  line. *(done dd772e8: bath/tap/buggy bridging paragraph added)*
- [x] [V] Add a labelled photo/sketch of the real buggy annotated with the
  six subsystems next to the "system of systems" tree (~388).
  *(done dd772e8: sketch placeholder added)*
- [x] [V] Photo of a pinion meshing with a spur gear at the Interfaces
  section (~785). *(done 2026-07-14: sketch placeholder per the visuals
  policy)*
- [x] [V] Convert the ASCII "Larger tyres" chain (~946) to mermaid for
  consistency. *(done 2026-07-14)*
- [x] [E] BBC Bitesize D&T "systems and control" at Input-Process-Output
  (~135); BBC Bitesize control/feedback at Feedback (~518); KS3 energy at
  "Connections Carry Things" (~413). *(done 2026-07-14 with substitutions
  from the research pass - see Research notes below: GCSE "systems
  approach to designing" at IPO, Explain That Stuff "thermostats" at
  Feedback, KS3 "energy stores and transfers" at Connections)*
- [x] [T] "Think about it" prompts (STYLE-GUIDE section 2, added
  2026-07-12): one before the cause-and-effect ripple - let the reader
  predict what fitting larger tyres would change before the chain is
  revealed - and one at Feedback (try walking a dead-straight line with
  your eyes closed; why do you drift without noticing?). Max two.
  *(done 2026-07-14: larger-tyres prompt opens A Chain of Dependence;
  eyes-closed line walk now opens Feedback in prompt form)*
- [x] [T] Topic Mini Project (STYLE-GUIDE section 3): mini chain-reaction
  machine from kitchen/household objects (source: Exploratorium Tinkering
  "Chain Reaction @ Home" - re-verify in research pass). Reflection: name
  each interface and what it carries (push, roll, pull), then trace the
  cause-and-effect chain on paper - the chapter's two key ideas made
  physical. *(done 2026-07-14: "The Kitchen Chain Reaction", source
  re-verified, safety callout + Watch the build box, no-feedback
  observation ties back to the Feedback section)*
- [x] Break markers at both seams listed above. *(done 2026-07-14: before
  Feedback and before Hands-On Activity 1)*
- [x] Emoji pass per STYLE-GUIDE section 6 (fixed callout markers, one
  meaningful emoji on content headings that earn one). *(done 2026-07-14)*
- [x] Final pass: verify checklist (PLAN.md step 5), tick rows here, update
  SUMMARY.md. *(done 2026-07-14: all 13 New Words confirmed present in
  glossary.md; gloss numbers checked against SUMMARY.md; Looking Ahead now
  names Chapter 3; estimated_time updated for the mini project; extra
  glosses added for servo horn - Ch24 - and wheel hex - Ch29)*

## Research notes (2026-07-14)

- **Bitesize "systems and control" (planned for Input-Process-Output):
  could not confirm a KS3 page by that name.** The IPO + feedback material
  lives in the GCSE D&T (AQA) topic "systems approach to designing" -
  confirmed as the spec heading via spec-aligned revision sites (Study
  Rocket, Revision World). Use search term "systems approach to designing"
  and flag as a look-ahead (same pattern as Ch03's momentum box). Note:
  bbc.co.uk blocks the crawler, so Bitesize pages are verified indirectly
  via third-party references to them.
- **Bitesize KS3 Physics "energy stores and transfers": confirmed** (guide
  z99jq6f, referenced by several UK school home-learning documents). Used
  at "Connections Carry Things" instead of the vaguer "KS3 energy".
- **Feedback section source:** Explain That Stuff "thermostats" article
  confirmed (explainthatstuff.com/thermostats.html) - a thermostat is the
  classic everyday negative-feedback machine; clearer for an 11-year-old
  than the GCSE open/closed-loop page.
- **IPO framing sanity check: passes.** Curriculum teaching (Eduqas/AQA):
  inputs are what make the system work, processes change input into
  output, outputs act on the world and give feedback. The chapter's wider
  input list (energy, information, material, movement, command) is
  consistent with it.
- **"2-cell battery":** Chapter 22 is "Batteries and Battery Safety" per
  SUMMARY.md - gloss "cell" there. Wording "a battery is built from one or
  more cells" is how Ch22 will teach it (2-cell = "2S" in hobby jargon -
  jargon deferred to Ch22).
- **Mini project source: confirmed.** Exploratorium Tinkering "Chain
  Reaction @ Home" page exists (exploratorium.edu/tinkering/our-work/
  chain-reaction-at-home), plus the main Chain Reaction project page and a
  downloadable photo instruction guide (PDF). Kitchen-object builds
  (spoons, dominoes, tubes, ramps) are exactly the household-materials
  brief; "start with a simple sequence" advice adopted in the steps.
- **Extra gloss offenders found in Interfaces section:** "servo horn"
  (home: Chapter 24 Steering Servos) and "wheel hex" (home: Chapter 29
  Suspension, Wheels and Grip) - glossed in this pass.
- No safety-critical technical claims in this chapter; ESC thermal
  protection and low-voltage alarms (Fast and Slow Feedback section) are
  standard behaviour - fine as stated.
