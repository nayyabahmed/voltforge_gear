# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

VoltForge Gear: a project-based engineering handbook teaching a curious
11-year-old (UK-based) to design and build a 3D printed brushless RC buggy.
It is a Markdown book, not a software project - there is no build, lint or
test step. Mermaid diagrams render directly on GitHub.

The finished book is 44 topics in five parts, numbered per part (Part 1 →
Topics 1.1-1.9, Part 2 → 2.1-2.10, … Part 5 → 5.1-5.4), plus the front-matter
Topic 0.0 ("How to Use This Handbook", which sits outside Part 1) and an
unnumbered Part 1 capstone. The files keep a global two-digit sequence prefix
on disk (`00-` … `43-`) even though the displayed number is part-relative.
`SUMMARY.md` is the single source of truth for the topic plan, numbering and
writing progress - always check it before referencing a topic by number, and
update the topic's status row whenever you create or materially revise a topic.

## The Three Governing Documents

Read these before writing or editing any topic:

- `style-guides-principles/STYLE-GUIDE.md` - the authoring rules: topic
  template, voice, vocabulary budget, analogy bank, visuals policy, safety
  callout format, and the publishing checklist. Topics 2.1 and 2.2 in
  `Part-2-Workshop-Skills/` are the reference implementations of it.
- `style-guides-principles/GUIDING-PRINCIPLES.md` - the project's engineering
  philosophy (buy precision / build structure, spend progressively, staged
  builds, modularity). Topic content must not contradict it; Part 4's
  topic sequence mirrors its build stages.
- `style-guides-principles/improvement-suggestions.md` - the original
  readability review of the Part 1 topics (2026-07-11), kept frozen as a
  record (it still uses the old chapter numbering). The WORKING copies live
  in `backlog/`: `backlog/PLAN.md` is the phased implementation plan (per-topic
  loop with research pass), the `backlog/chapter-NN.md` files hold the live
  per-topic items (these working files keep their old sequence-numbered names;
  they are not book content), and `backlog/TRACKER.md` is the at-a-glance
  status board (done / in progress / planned per topic and activity). Check
  TRACKER.md first when asked about review status, and keep its rows and
  "Last updated" date current whenever topic work starts or finishes.
  `backlog/WRITING-TRACKER.md` is the equivalent board for AUTHORING new
  topics (Topic 2.3 onwards): it tracks each in-flight topic through the
  research -> draft -> mini project -> glossary -> reference docs ->
  publish pipeline, while `SUMMARY.md` remains the single source of truth
  for numbering and published status.

## Non-Negotiable Conventions

- **Rich characters welcome** (decision 2026-07-12, replacing the old
  ASCII-only rule): emoji and Unicode are encouraged where they make the
  book more presentable, following the emoji registry in STYLE-GUIDE.md
  section 6 - fixed callout markers, at most one emoji per heading, body
  prose kept emoji-light. Engineering notation (`Ø`, `±`, `°`, `×`) is
  used freely.
- **British English** (tyres, organised, colour).
- **First-use gloss**: any term not yet taught gets a bracket gloss plus its
  home-topic pointer. Topic numbers in glosses must match `SUMMARY.md`.
- **Terminology registry** (STYLE-GUIDE.md section 5): "topic" (never
  "chapter") for a numbered unit, "drivetrain" for the whole system,
  "requirement traceability" (singular), "hinge pin" etc.
- **Verify before citing**: external links and technical facts (especially
  print temperatures, battery/LiPo safety, tool safety) are web-verified
  before they go in a topic. Prefer "search X on site Y" over deep URLs.
- **Safety content is strictest**: safety callouts come before the activity
  that needs them and must stay consistent with `SAFETY.md`.

## Publishing a Topic (the full loop)

1. File at `Part-N-Name/NN-Title.md` (the `NN-` prefix keeps the global
   sequence number) with frontmatter including `version` and `status` per
   `VERSIONING.md` (new = "0.1" / "Draft").
2. Add every New Words entry to `glossary.md` (alphabetical `### Term`
   entries under `## Letter` headings, plain-language style).
3. Update the topic's row in `SUMMARY.md` (planned 📋 -> 🟡 v0.1, link the
   file).
4. Verify: emoji follow the STYLE-GUIDE section 6 registry, "Looking Ahead"
   names the real next topic, every activity has a no-equipment variant,
   glosses present.

Reference docs at the root grow alongside topics rather than being written
once: `SAFETY.md`, `TOOLS.md`, `TROUBLESHOOTING.md`, `BOM.md`,
`COST-LEDGER.md` each state in their frontmatter which topics feed them.

## Building the Published Book

`scripts/build_book.py` compiles the source into PDF / EPUB / HTML. See
`BUILD.md` for the full guide - prerequisites, how covers and Mermaid are
handled, usage, and the Windows/WSL quick start.

## Authorship Context

Part 1 (Topics 1.1-1.9 + capstone, plus the front-matter Topic 0.0) was
originally generated by another model and is being upgraded to v0.2 "Reviewed"
by applying the backlog; that work happens on the `review` branch. New topics
(Topic 2.2 onward) are written fresh to the style guide with a research pass
first. Files named like `3D-Printing.md` (no number prefix) in part folders are
unlinked raw material for future topics, not live topics.

## Git Conventions

- Commit in topical chunks (one concern per commit), not one big commit.
- `main` holds published work; topic-improvement passes happen on branches
  (currently `review` for the Part 1 upgrade).
- Empty scaffold directories (`assets/`, `CAD/`, `STL/`, `activities/`,
  `design-notes/`, `experiments/`, `teacher-notes/`, `BOM/`) are intentional
  targets from README's layout; git does not track them until content lands.
