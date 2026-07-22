# Character Brief: Professor WagahDagah (Google Flow / Veo 3.1)

**Date:** 2026-07-21
**Prepared for:** VoltForge Gear — The Young Engineer's Handbook
**Purpose:** The locked, reusable character reference for our animated host.
This is the "ingredient" we feed to Google Flow / Veo 3.1 so the professor
looks and sounds the same in every topic video. Generate the reference images
from the master description below **once**, approve them, then reuse those
images plus the short identity string in every shot.

> **Design decisions made here (say the word to change any of them):**
> warm golden-tan skin; long blond hair; a *building* hammer with a gear-shaped
> head (never a weapon); the VoltForge palette of volt-blue + forge-orange +
> brushed steel. He is a **kind hero-teacher**, strong but never intimidating —
> this is for an 11-year-old.

---

## 1. Concept in One Line

Professor WagahDagah is what you get if a Norse thunder-god retrained as a
friendly makerspace engineering teacher: heroic, strong and larger-than-life,
but warm, curious and endlessly encouraging. His "power" is engineering, and he
*forges* understanding the way Thor forges with thunder.

**Tone he must always read as:** safe, warm, excited to teach — never scary,
never a warrior. Big smile, kind eyes, welcoming posture.

---

## 2. Master Character Description (paste this to generate the reference images)

> A friendly, heroic engineering professor named Professor WagahDagah, a
> cross between a Norse thunder-god and a warm university maker-teacher. A tall,
> broad-shouldered man in his 40s with a strong but approachable build and a
> big welcoming smile. Warm golden-tan skin, bright electric-blue eyes that
> sparkle with curiosity, and kind laugh-lines. Long golden-blond hair,
> half pulled into a top-knot with the rest loose to his shoulders, and a neat
> short golden-blond beard. A pair of clear safety goggles pushed up onto his
> forehead. He wears a rugged maker's apron-jerkin of deep volt-blue canvas and
> tan leather over a simple tunic, with brushed-steel forearm bracers subtly
> etched with gear teeth, and a heavy engineer's coat with a forge-orange
> lining that billows like a heroic cape. A leather tool-belt holds engineering
> tools — a spanner, calipers, a small screwdriver. In one hand he holds a
> friendly forge hammer whose head is shaped like a chunky metal gear; it is
> clearly a building and shaping tool, never a weapon. Sturdy work boots.
> Clean, bright, colourful 3D-animated feature-film style, soft warm lighting,
> friendly and child-appropriate. Full body, neutral studio background.

Keep this wording stable. When you re-generate or extend, change only the
scene, camera and action around him — not his identity words.

---

## 3. Locked Physical Attributes (do not drift)

| Feature | Locked value |
| --- | --- |
| Apparent age / presence | 40s, timeless, heroic-but-kind |
| Build | Tall, broad-shouldered, strong; relaxed friendly posture |
| Skin | Warm golden-tan |
| Eyes | Bright electric-blue, kind, a faint spark |
| Hair | Long golden-blond, half-up top-knot, rest loose to shoulders |
| Beard | Neat, short, golden-blond |
| Signature accessory | Clear safety goggles pushed up on the forehead |
| Body wear | Volt-blue canvas + tan leather maker's apron-jerkin over a tunic |
| Arms | Brushed-steel bracers etched with gear teeth |
| Coat | Rugged engineer's coat, forge-orange lining, capes/billows heroically |
| Belt | Leather tool-belt: spanner, calipers, small screwdriver |
| Signature prop | "Forge hammer" with a gear-shaped metal head — a build tool, not a weapon |
| Footwear | Sturdy dark work boots |

---

## 4. Colour Palette (VoltForge Gear)

- **Volt blue** — primary (apron, core costume). Bright electric blue.
- **Forge orange / ember** — accent (coat lining, warm glow, highlights).
- **Brushed steel / graphite grey** — metal (bracers, hammer, tools).
- **Warm gold** — hair, beard, small metallic trims.
- Keep backgrounds and scenes bright, warm and clean. Avoid dark, moody or
  menacing lighting — this is a cheerful teaching series.

---

## 5. Expression & Pose Set (for the reference sheet)

Generate the professor in each of these so Flow has a consistent range to draw
from. Same identity wording, only the expression/pose changes:

- Neutral friendly, looking at camera (the default host pose).
- Big warm smile, mid-explanation, one hand gesturing.
- Curious / eyebrows raised, holding the forge hammer up to inspect a part.
- Encouraging thumbs-up, goggles down over the eyes (workshop-ready).
- Gentle "let's think" pose, hand on beard.
- Three-quarter turnaround and side profile (for consistency across camera
  angles).

---

## 6. Personality & Voice (for script and narration)

**Personality:** warm, enthusiastic, patient and curious. He treats every
mistake as a useful experiment, never talks down to the young engineer, and
gets visibly delighted when something works. A touch of playful, mythic
grandeur — occasional lines like *"By the sparks of the forge!"* — but used
sparingly so it stays charming, not cheesy.

**Voice (for the fixed TTS voice we lock for the whole series):**

- Deep, warm baritone; friendly and reassuring, not booming or scary.
- Moderate, unhurried pace suitable for an 11-year-old.
- Clear plain language; technical terms are introduced gently, exactly as the
  handbook does.
- British-English friendly (matches the book's spelling and idiom).

---

## 7. Reusable Prompt Building Blocks

**Identity string** — prepend to *every* shot prompt (keep it short and fixed):

> Professor WagahDagah — tall heroic golden-blond bearded engineer-professor,
> safety goggles on forehead, volt-blue maker's apron and forge-orange-lined
> coat, brushed-steel gear-etched bracers, holding a gear-headed forge hammer;
> bright friendly 3D-animated style —

**Example shot prompt (host to camera):**

> [identity string] standing in a warm, tidy workshop, smiling at the camera and
> gesturing with one hand as he explains, gentle soft lighting, medium shot,
> camera slowly pushing in.

**Example shot prompt (story/analogy scene):**

> [identity string] kneeling beside a small 3D-printed RC buggy on a workbench,
> pointing at its wheels with the forge hammer, curious expression, bright
> colourful workshop background, medium-wide shot.

**Rule:** the professor narrates and tells the story; **he never draws the
technical diagrams.** Gear ratios, wiring, dimensions and any on-screen numbers
are composited in afterwards from the handbook's existing Mermaid figures — see
the feasibility study. Do not ask Flow to generate technical diagrams or
readable text.

---

## 8. Negative / Avoid List

- No weapon framing, no menace, no battle poses — the hammer only *builds*.
- No dark, scary, or moody lighting; no horror or peril.
- No generated technical diagrams, charts, or blocks of readable text on screen.
- No changing his hair colour, skin tone, costume colours or signature props
  between shots.
- No overly realistic/photographic human render — keep the friendly animated
  feature-film look so he stays a character, not a person.

---

## 9. How to Use This in Google Flow

1. Paste the **master description** (section 2) and generate the reference
   images; produce the **expression/pose set** (section 5). Approve the best,
   most on-model set.
2. Save those approved images as the character **ingredient** in Flow.
3. For each shot, use the ingredient **plus** the **identity string** (section
   7) plus only the scene/action/camera wording.
4. Keep clips to the 8-second limit and chain with scene extension for longer
   beats (see feasibility study).
5. Composite the handbook's Mermaid diagrams and any real photos/CAD over the
   top for all technical content.

---

## 10. Open Choices Worth Confirming

- **Skin tone / heritage** — currently warm golden-tan; easy to change for a
  different look or broader representation.
- **Signature prop** — the gear-headed forge hammer; could instead be a glowing
  spanner or a "spark of understanding" he conjures.
- **Catchphrase** — *"By the sparks of the forge!"* is a placeholder; happy to
  design a signature line and a repeatable sign-off for the series.
- **Name spelling / pronunciation** — "WagahDagah" as given; confirm the
  intended pronunciation so the TTS voice says it consistently.
