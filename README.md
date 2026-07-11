# RC Buggy Engineering Handbook

**Learn real engineering by designing, building and racing your own 3D printed brushless RC buggy.**

This is not a build manual and not a school textbook. It is a project-based engineering handbook: every concept — forces, tolerances, gearing, electronics, CAD — is introduced exactly when the buggy project needs it, explained first through stories and hands-on experiments, and only then given its proper engineering name.

> **Who is this for?**
> Curious builders aged about **11 and up** (and any adult who wants to learn alongside them).
> You do **not** need to know engineering, own a 3D printer, or have built an RC car before.
> You only need curiosity and the willingness to build, test and learn.

---

## What Makes This Handbook Different

Every chapter follows the same promise to the reader:

1. **Concept before vocabulary.** You will understand an idea *before* you learn its technical name. Nothing is defined before it is experienced.
2. **Hands-on from the start.** Each chapter includes a simple experiment you can do with household materials — no special tools required until the workshop chapters.
3. **Everything builds toward the buggy.** No isolated theory. Each chapter ends with a practical engineering task and leads directly into the next one.
4. **Written like real engineers work.** Notebooks, measurement sheets, design reviews, testing, iteration — the habits matter as much as the knowledge.

## Anatomy of a Chapter

Every chapter is a self-contained Markdown file (roughly 2,000–4,000 words, or 8–15 book pages) with a consistent structure:

| Section | Purpose |
| --- | --- |
| YAML front matter | Title, part, chapter number, difficulty, time estimate, prerequisites, learning objectives |
| Introduction & story | A relatable scenario or analogy that motivates the idea |
| Concrete explanation | The idea in plain language, grounded in the buggy |
| Engineering explanation | The same idea with proper terms, diagrams and numbers |
| Mermaid diagrams | Visual explanations, GitHub-renderable, used wherever they genuinely help |
| Hands-on experiment | A simple experiment to feel the concept physically |
| "Thinking Like an Engineer" | How professionals apply the idea in the real world |
| Challenge | A practical engineering task |
| Summary & checklist | Self-assessment before moving on |
| Looking ahead | A preview that sets up the next chapter |

A growing [`glossary.md`](glossary.md) collects every term the moment it is formally introduced, so there is always one place to look things up.

---

## The Five Parts

| Part | Theme | Status |
| --- | --- | --- |
| **Part 1 — Engineering Mindset** | Systems thinking, motion, forces, measurement, tolerances, drawings, the design process | ✅ Chapters 00–10 written (review quiz pending) |
| **Part 2 — Workshop Skills** | 3D printing, CAD, fasteners, bearings, materials, tools and safety | 📋 Planned |
| **Part 3 — RC Car Systems** | Electronics, brushless motors, ESCs, batteries, gearing, suspension, steering | 📋 Planned |
| **Part 4 — Design & Build** | Planning, chassis design, printing, assembly, testing, tuning, iteration | 📋 Planned |
| **Part 5 — Advanced Topics** | Engineering materials (nylon, CF), aerodynamics & CFD, telemetry, autonomy | 📋 Planned |

See [`SUMMARY.md`](SUMMARY.md) for the full chapter-by-chapter table of contents and progress.

## Repository Layout

```text
rc-buggy-handbook/
│
├── README.md              ← you are here
├── SUMMARY.md             ← full table of contents & progress tracker
├── glossary.md            ← every term, defined once, in one place
│
├── Part-1-Engineering-Mindset/    chapters 00–10
├── Part-2-Workshop-Skills/        chapters 11–19
├── Part-3-RC-Car-Systems/         chapters 20–29
├── Part-4-Design-and-Build/       chapters 30–39
├── Part-5-Advanced-Topics/        chapters 40–49
│
├── assets/                diagrams, photos and images used by chapters
├── activities/            printable worksheets and checklists
├── experiments/           stand-alone hands-on exercise sheets
├── design-notes/          the evolving design story of the buggy itself
├── CAD/                   CAD sources, links and screenshots
├── STL/                   printable part files
├── BOM/                   bill of materials, suppliers and costs
├── teacher-notes/         optional extensions and challenges for older readers
└── troubleshooting.md     symptoms → causes → fixes, grown during the build
```

> Directories are created as their first content lands — the layout above is the target shape of the finished handbook.

## How the Handbook Is Being Built

The handbook is written in **sprints**, one part at a time, so each part is coherent and internally cross-referenced before the next begins:

| Sprint | Deliverable | Approx. size |
| --- | --- | --- |
| 1 | Part 1 — Engineering Mindset | 50–70 pages |
| 2 | Part 2 — Workshop Skills | 70–90 pages |
| 3 | Part 3 — RC Car Systems | ~100 pages |
| 4 | Part 4 — Design & Build | ~120 pages |
| 5 | Part 5 — Advanced Topics | ~80 pages |

Working conventions:

- **One file = one complete chapter**, self-contained and ready to commit.
- Plain GitHub-flavoured Markdown throughout; all diagrams are Mermaid so they render directly on GitHub with no build step.
- Chapters are reviewed, versioned and improved over time — the handbook is maintained like a software project, not published once.

The finished handbook is expected to reach roughly **300–500 pages** across **40+ chapters**, with **300+ diagrams**, quizzes, printable worksheets, a troubleshooting guide and a complete bill of materials — somewhere between *The Way Things Work*, an engineering textbook, and an RC build manual.

## How to Read It

Start at [Chapter 00 — How to Use This Handbook](Part-1-Engineering-Mindset/00-How-to-Use-This-Handbook.md) and read in order. The chapters deliberately build on each other: each one assumes the experiments, vocabulary and checklists of the ones before it. Keep an **engineering notebook** from day one — the chapters will tell you what to put in it.

## Contributing & Feedback

Spotted an error, an unclear explanation, or an experiment that didn't work? Open an issue or a pull request. Clarity fixes and better analogies are just as valuable as technical corrections — the target reader is 11 years old.

## License

License to be confirmed. The intent is for this to be an open handbook that is free to read, print and use in classrooms.
