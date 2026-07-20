# ⚡ VoltForge Gear — The Young Engineer's Handbook

**Design it. Print it. Wire it. Race it.**

Somewhere in your future there is a fast, 3D printed, brushless RC buggy — and *you* designed every part of it. You chose the motor. You worked out the gearing. You made the suspension survive the jump that broke version one. This handbook is the path from "I've never built anything" to that buggy.

And here's the secret: the buggy is just the beginning. **VoltForge Gear** is about everything that runs on *volts* and moves with *gears*. The same skills you forge building the buggy — designing parts, reading drawings, choosing motors, debugging electronics, testing and iterating — are the skills behind drones, robots, e-bikes, RC boats and planes, and machines nobody has invented yet. Finish the buggy and you won't just own a fast RC car; you'll know how to build the *next* thing.

> **Who is this for?**
> Curious builders aged about **11 and up** (and any adult who wants to learn alongside them).
> You do **not** need to know engineering, own a 3D printer, or have built an RC car before.
> You only need curiosity and the willingness to build, test and learn.

This is not a build manual and not a school textbook. It is a project-based engineering handbook: every concept — forces, tolerances, gearing, electronics, CAD — is introduced exactly when the buggy project needs it, explained first through stories and hands-on experiments, and only then given its proper engineering name.

---

## What Makes This Handbook Different

Every topic follows the same promise to the reader:

1. **Concept before vocabulary.** You will understand an idea *before* you learn its technical name. Nothing is defined before it is experienced.
2. **Hands-on from the start.** Each topic includes a simple experiment you can do with household materials — no special tools required until the workshop topics.
3. **Everything builds toward the buggy.** No isolated theory. Each topic ends with a practical engineering task and leads directly into the next one.
4. **Written like real engineers work.** Notebooks, measurement sheets, design reviews, testing, iteration — the habits matter as much as the knowledge.

## Anatomy of a Topic

Every topic is a self-contained Markdown file (roughly 2,000–4,000 words, or 8–15 book pages) with a consistent structure:

| Section | Purpose |
| --- | --- |
| YAML front matter | Title, part, topic number, difficulty, time estimate, prerequisites, learning objectives |
| Introduction & story | A relatable scenario or analogy that motivates the idea |
| Concrete explanation | The idea in plain language, grounded in the buggy |
| Engineering explanation | The same idea with proper terms, diagrams and numbers |
| Mermaid diagrams | Visual explanations, GitHub-renderable, used wherever they genuinely help |
| Hands-on experiment | A simple experiment to feel the concept physically |
| "Thinking Like an Engineer" | How professionals apply the idea in the real world |
| Challenge | A practical engineering task |
| Summary & checklist | Self-assessment before moving on |
| Looking ahead | A preview that sets up the next topic |

A growing [`glossary.md`](glossary.md) collects every term the moment it is formally introduced, so there is always one place to look things up.

---

## The Five Parts

| Part | Theme | Status |
| --- | --- | --- |
| **Part 1 — Engineering Mindset** | Systems thinking, motion, forces, measurement, tolerances, drawings, the design process | ✅ Topic 0.0 + Topics 1.1–1.9 + capstone written (review quiz pending) |
| **Part 2 — Workshop Skills** | Workshop safety, 3D printing, slicers, CAD, materials, hand tools, soldering | ✍️ In progress (Topic 2.2 drafted) |
| **Part 3 — RC Systems** | Electricity basics, batteries, radio, servos, ESCs, motors, drivetrain, steering, suspension | 📋 Planned |
| **Part 4 — Design and Build** | From cardboard mock-up to driving buggy, one working stage at a time | 📋 Planned |
| **Part 5 — Advanced Topics** | Maintenance, sensors & telemetry, advanced materials, design your own variant | 📋 Planned |

See [`SUMMARY.md`](SUMMARY.md) for the full topic-by-topic table of contents and progress.

## Repository Layout

```text
rc-buggy-handbook/
│
├── README.md              ← you are here
├── SUMMARY.md             ← full table of contents & progress tracker
├── VERSIONING.md          ← the document lifecycle: Draft → Reviewed → Prototype-Tested → Released
├── CONTRIBUTING.md        ← how to help
├── style-guides-principles/
│   ├── STYLE-GUIDE.md         how topics are written (voice, template, conventions)
│   ├── GUIDING-PRINCIPLES.md  the project's engineering philosophy
│   └── improvement-suggestions.md  the readability review backlog
├── glossary.md            ← every term, defined once, in one place
├── BOM.md                 ← bill of materials, grown stage by stage
├── COST-LEDGER.md         ← what was actually spent, purchase by purchase
├── TOOLS.md               ← every tool, when it's first needed, and fallbacks
├── SAFETY.md              ← the quick-reference safety card for the whole project
├── TROUBLESHOOTING.md     ← symptoms → causes → fixes, grown during the build
│
├── Part-1-Engineering-Mindset/    Topic 0.0 + Topics 1.1–1.9 + capstone
├── Part-2-Workshop-Skills/        Topics 2.1–2.10
├── Part-3-RC-Systems/             Topics 3.1–3.10
├── Part-4-Design-and-Build/       Topics 4.1–4.10
├── Part-5-Advanced-Topics/        Topics 5.1–5.4
│
├── assets/                diagrams, photos and images used by topics
├── activities/            printable worksheets and checklists
├── posters/               printable posters
└── teacher-notes/         optional extensions and challenges for older readers
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

- **One file = one complete topic**, self-contained and ready to commit.
- **Every document has a version and status** in its front matter and matures through a fixed lifecycle — v0.1 Draft → v0.2 Reviewed → v0.3 Prototype-Tested → v1.0 Released. See [VERSIONING.md](VERSIONING.md).
- Plain GitHub-flavoured Markdown throughout; all diagrams are Mermaid so they render directly on GitHub with no build step.
- Topics are reviewed, versioned and improved over time — the handbook is maintained like a software project, not published once.

The finished handbook is expected to reach roughly **300–500 pages** across **40+ topics**, with **300+ diagrams**, quizzes, printable worksheets, a troubleshooting guide and a complete bill of materials — somewhere between *The Way Things Work*, an engineering textbook, and an RC build manual.

## How to Read It

Start at [Topic 0.0 — How to Use This Handbook](Part-1-Engineering-Mindset/00-How-to-Use-This-Handbook.md) and read in order. The topics deliberately build on each other: each one assumes the experiments, vocabulary and checklists of the ones before it. Keep an **engineering notebook** from day one — the topics will tell you what to put in it.

## Contributing & Feedback

Spotted an error, an unclear explanation, or an experiment that didn't work? Open an issue or a pull request — see [CONTRIBUTING.md](CONTRIBUTING.md) for the conventions. Clarity fixes and better analogies are just as valuable as technical corrections — the target reader is 11 years old.

## License

License to be confirmed. The intent is for this to be an open handbook that is free to read, print and use in classrooms.
