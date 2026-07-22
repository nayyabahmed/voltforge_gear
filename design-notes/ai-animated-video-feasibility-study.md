# Feasibility Study: AI-Generated Animated Topic Videos

**Date:** 2026-07-21
**Prepared for:** VoltForge Gear — The Young Engineer's Handbook
**Question:** Can we produce Storyline-Online-style narrated videos — a
recurring animated host, "Professor WagahDagah" (a Thor-like professor),
explaining each topic — through a generative-AI pipeline (Google Flow / Veo
and similar tools), with the on-screen visuals matching the written topic
content?

---

## Executive Summary

**Yes — this is feasible in 2026, but the version that works is a *hybrid*
pipeline rather than a single "prompt in, finished episode out" tool.** Every
component the concept needs now exists at usable quality: consistent character
generation (Google Veo 3.1 "Ingredients to Video"), a single consistent
narration voice (modern text-to-speech), talking/lip-synced delivery, and
original scene illustration. The winning shape is to let generative video
carry the *host and the story/analogy scenes*, while the *technical content*
(diagrams, dimensions, wiring, on-screen numbers) stays deterministic — reusing
the Mermaid diagrams the topics already contain. This mirrors how Storyline
Online itself is built (a reader plus faithful illustration pages) and it
sidesteps the one thing generative video still does badly: accurate technical
detail.

The project is unusually well-suited to automation because the handbook is
already tightly structured. Each topic file carries frontmatter (learning
objectives, difficulty, time), a story hook, plain-then-technical
explanations, Mermaid diagrams, hands-on activities, a summary and a glossary.
That structure lets a per-topic script, shot list and image-prompt set be
generated directly from the topic, which is exactly what keeps the narration
and the visuals locked to the written book.

The two real risks are (1) keeping the professor visually consistent across a
long series of 44 topics, and (2) keeping technical visuals accurate. Both are
manageable by design — a locked character reference sheet for the first, and a
deterministic-diagram rule for the second.

---

## What We Are Matching: Storyline Online

Storyline Online is a SAG-AFTRA Foundation programme in which actors read
children's picture books aloud while the book's own illustrations fill the
screen with gentle motion, interspersed with occasional cutaways to the reader.
Two properties make it effective: a warm, human-sounding voice, and visuals
that track the words exactly.

Our concept keeps those two properties but changes two things:

- **Celebrity reader → recurring animated host.** We generate an original
  character (Professor WagahDagah) rather than filming a person.
- **Existing book art → original explanatory visuals.** Storyline reuses art
  that already exists; we generate scenes to match our text.

Both changes are larger lifts than Storyline's own production, but each is now
achievable with off-the-shelf generative tools.

---

## The Pipeline, Component by Component

**Recurring character — the hardest part, now largely solved.**
Google Flow / Veo 3.1 added "Ingredients to Video": you supply reference images
of a character and the model keeps that character consistent across generated
shots, alongside 4K upscaling and native vertical formats. Consistency is much
improved over earlier models but is *not* frame-perfect across dozens of
episodes, so the professor must be defined once as a locked character sheet
(front and side views, a set of expressions, colour and costume notes) and that
same reference reused for every generation. This is the single biggest quality
risk in the project and the thing most worth investing effort in up front.

**Narration voice — mature.**
A fixed text-to-speech voice (ElevenLabs-class) gives one consistent professor
voice across all 44 topics. For a series this is preferable to re-recording,
and a scripted voice track is what lets the written script and the audio match
word-for-word.

**Talking / lip-sync — workable.**
Veo 3.1 generates native audio and mouth movement, but making the mouth match
*our exact script* is fiddly. The cleaner route is to drive narration from the
TTS track and add a lip-sync/avatar pass, or to keep the professor mainly as a
narrator whose face is not always on screen — which is exactly what Storyline
does (mostly illustrations, the reader shown only occasionally).

**Scene visuals that match the text — workable, with the caveat below.**
Story and analogy scenes (a workshop, a buggy on a track, a jump that breaks
version one) are well within reach of image and video generation, prompted from
the topic's own narrative.

**Assembly — standard.**
A normal video editor stitches host clips, illustrated scenes, diagrams and the
audio track into the finished episode.

---

## The One Limitation to Design Around

Generative video is still poor at *accurate technical content*: correct gear
ratios, wiring diagrams, true dimensions, and legible on-screen text. For a
children's *engineering* handbook this matters more than usual — a plausible
but wrong diagram is worse than no diagram, because a young reader cannot tell
the difference.

The mitigation is a firm production rule: **generative video carries the host
and the story; it never generates the engineering.** Technical panels are
produced deterministically and composited in. The handbook already contains
Mermaid diagrams in every topic, so those are reused as-is rather than
re-drawn by AI. This is the same division Storyline uses between its reader
segments and its faithful illustration pages, and it is what keeps the videos
technically trustworthy.

---

## Why the Source Material Makes This Tractable

A review of a reference topic (Topic 2.1, *Workshop Safety and Setup*) confirms
that each topic is already structured for this. The frontmatter lists learning
objectives, difficulty and time; the body moves from a story hook to a plain
explanation to a technical one; Mermaid diagrams are embedded; hands-on
activities, a summary, review questions, a glossary ("New Words") and a
"Looking Ahead" preview all follow a fixed template.

That structure is ideal for auto-generating a per-topic **script → shot list →
image-prompt set**. The requirement that "the written and video content must
match" is satisfied *by construction*: the script is derived from the topic
file, so the narration and the visuals stay tied to the book rather than
drifting into whatever the model invents.

---

## Practical Constraints to Price In

**Clip length.** Veo 3.1 clips are a maximum of 8 seconds. Scene extension can
chain up to roughly 20 clips (about 140 seconds and beyond), analysing the last
second of each clip for continuity, though 4K is not available for extended
scenes. Longer explanations must therefore be storyboarded into short beats.

**Cost (order-of-magnitude, not a quote).** Google AI Ultra is US$249.99/month
and includes roughly 250 "Quality" Veo generations (more on the faster, lower
quality tiers); AI Pro is US$19.99/month for roughly 10 Quality Veo videos.
API rates run from about US$0.03/second (Lite, no audio) to US$0.40/second
(with audio). Re-rolls are a real cost — expect to generate a given shot two to
four times before getting a keeper. As a rough guide, a five-minute episode
with around two minutes of AI host footage is on the order of fifteen usable
clips, so a single Ultra plan realistically finishes a handful of topics per
month, using the cheaper draft tiers for iteration. Completing all 44 topics is
therefore a multi-month effort on one plan, faster with parallel budget.

| Constraint | Implication for production |
| --- | --- |
| 8-second clip limit | Storyboard each explanation into short beats; chain with scene extension |
| Character consistency imperfect | Lock a character reference sheet; reuse it on every generation |
| Weak technical accuracy | Never AI-generate diagrams; composite the existing Mermaid figures |
| Re-roll rate | Budget 2–4× generations per usable shot; draft on cheap tiers |
| Extended scenes capped at 720p | Reserve 4K for single hero shots, not long sequences |

---

## Recommended Shape

A hybrid pipeline:

- **Host and story scenes** — generated with Google Flow / Veo 3.1, driven by a
  locked Professor WagahDagah reference.
- **Technical panels** — deterministic, reusing each topic's existing Mermaid
  diagrams and any real photographs or CAD.
- **Voice** — one consistent TTS voice across the whole series.
- **Script and storyboard** — generated per topic from the topic file, so audio
  and visuals stay locked to the written book.
- **Assembly** — a standard editor combining the above.

The linchpin is the character reference: get the professor locked and
consistent first, because everything else depends on it.

---

## Conclusion and Next Step

The concept is feasible and a good fit for this handbook, precisely because the
source material is already well-structured. The main risks — character
consistency across a long series, and technical accuracy — are both handled by
design rather than by hope.

If this direction is approved, the natural next step is a concrete plan
covering: a locked character brief for Professor WagahDagah; a per-topic
script → storyboard → prompt template driven from the topic frontmatter; a
tool shortlist for each pipeline stage; a single-topic pilot (Topic 2.1 is a
clean candidate); and a cost and schedule model for the full 44-topic run.

---

## Sources

- Veo 3.1 — Google DeepMind: https://deepmind.google/models/veo/
- Veo 3.1 "Ingredients to Video" / character consistency — CineD:
  https://www.cined.com/google-veo-3-1-ingredients-to-video-update-adds-native-vertical-format-4k-upscaling-and-enhanced-character-consistency/
- Veo 3.1 clip length and scene-extension rules — UlazAI:
  https://ulazai.com/how-long-veo3-videos/
- Veo 3.1 pricing and Flow credits — buildfastwithai:
  https://www.buildfastwithai.com/blogs/google-veo-3-1-ai-video-generator
- Storyline Online: https://storylineonline.net/
