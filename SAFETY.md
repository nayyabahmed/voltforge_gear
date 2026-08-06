---
title: "Safety Reference"
project: "VoltForge Gear — The Young Engineer's Handbook"
version: "0.2"
status: "Reviewed (covers every hazard taught through Topic 4.10)"
feeds_from: "Topics 2.1, 2.2, 2.8, 2.9, 3.1-3.10, 4.1-4.10"
---

# Safety Reference

The quick-reference card for the whole project. Topic 2.1 (Workshop Safety
and Setup) *teaches* safe working; this page *summarises* the rules so any
topic can link to them. If a topic's safety box and this page ever
disagree, tell an adult and trust the stricter rule.

> **The one rule above all others**
>
> If you are not sure whether something is safe: stop, and ask an adult.
> Every activity in this handbook assumes adult supervision is available.

> **⚠️ If there is smoke or flame**
>
> Do not try to move it, cover it or put it out.
> Get out, stay out, and call `999`.
> This applies to a battery, a charger, a printer or anything else.

---

## General Workshop (taught in Topic 2.1)

- **Pause, Plan, Protect** before every task: spot the hazards, choose the
  safe method, prepare the space.
- Clear space, good light, stable table, no food or drinks near the work.
- Tie back long hair; no dangling cords, jewellery or loose gloves near
  anything that spins.
- Safety glasses for drilling, cutting rigid material and clipping wire.
  Look for the EN 166 mark - ordinary spectacles are not impact-tested and
  leave the sides open. PPE is the last line of defence, not a substitute
  for a safe method.
- Clamp the work before drilling - never hold a small part in your fingers.
- Power off is the default: disconnect the battery before touching gears,
  wheels or wiring. Do not trust the transmitter switch alone.
- Stop work if a tool sounds wrong, anything smokes, a blade slips twice,
  or you feel tired, frustrated or unsure. Stopping is a skilled decision.
- End every session with the tidy routine: power off, hot tools cooling,
  blades covered, batteries stored, next step written down.

## Hot Tools - 3D Printer and Soldering Iron (Topics 2.2, 2.9, 4.7)

- A printer nozzle runs at 200-250 °C and stays hot after it stops.
  The build plate can reach 60-85 °C. Never touch either during printing or
  cooling.
- Keep hands out of a moving printer. Print in a ventilated room, using the
  material in the environment its manufacturer requires.
- Stop a print for smoke, an unusual smell, scraping, detached parts or any
  unsafe printer behaviour.
- **Never print a safety-critical precision part** - a battery component,
  gear, high-speed shaft or wheel hub - just to avoid buying it (Topic 4.7).

## Soldering (taught in Topic 2.9)

- Live soldering needs direct supervision by a responsible adult or trained
  instructor, every time.
- **Use fume extraction at the source**, positioned to pull the plume away
  from your breathing zone. An open window is not a substitute. Keep your
  head out of the plume.
- Safety glasses: clipped leads and solder droplets fly.
- Stable heat-resistant surface, iron always in its proper stand, cables out
  of walking paths.
- Use lead-free electronics solder. Treat unknown old solder as possibly
  leaded and let an adult handle it. Wash hands afterwards.
- Use only flux and solder intended for electronics. **Never plumbing acid
  flux** - it stays corrosive and destroys conductors.
- **Never solder to a battery, a battery lead, a LiPo cell or a live
  circuit**, and never attempt to repair a battery pack. Practise on
  disconnected scrap wire only.
- Heat-shrink needs a controlled heat source and adult supervision. Never an
  open flame. Let joints cool before handling.
- Desoldering: the tool and removed solder stay hot; never pull a component
  while the solder is solid.

## Cutting, Drilling and Finishing (taught in Topic 2.8)

- **Craft knives**: adult-approved and directly supervised. Proper cutting
  mat, suitable ruler, other hand out of the blade path, cut away from your
  body in several light passes, retract or cover the blade immediately.
  Never a loose, damaged or blunt blade.
- **Saws**: supervised. Safety glasses, hair and sleeves secured, both hands
  clear of the blade path. Never test the teeth with a finger.
- **Cutters and clippers**: fragments and clipped cable ties fly. Safety
  glasses, cut pointed away from people, one hand out of the path.
- **Powered drilling**: direct supervision by a responsible adult or trained
  instructor. Work clamped - never held by hand. Eye protection, hair tied,
  no dangling cords. Chuck key out before starting. Hands away until the bit
  has fully stopped. Isolate power before changing a bit or clearing a jam.
- **Files**: correct file for the material, fitted handle, work clamped,
  hands behind the cutting direction. Clean with a file brush, never bare
  fingers.
- **Dust is the hidden hazard.** Ask an adult to identify the material
  first. **A cloth face covering is not dust protection** - a proper
  filtering mask (FFP2 / N95 or better), fitted by an adult, plus eye
  protection. Never casually sand unknown composites or glass- or
  carbon-filled materials. **Better still, stop the dust existing**: wet
  sanding keeps the particles stuck down.

## Electricity (taught in Topics 3.1-3.2)

- Our project voltages are low, but a short circuit still makes intense
  current, heat, burns and fire. **Never deliberately short** a battery,
  cell, power supply or charged capacitor.
- Keep real RC batteries physically disconnected while planning, mapping,
  measuring or building. Do not rely on a switch alone.
- **Meters**: extra-low-voltage educational circuits only, under
  supervision. Check the manual, lead sockets, selector, range and
  connection before every measurement. Continuity and resistance are
  measured only on unpowered, isolated circuits.
- **Never probe mains electricity**, household sockets, chargers, exposed
  power supplies or damaged batteries.
- Never insert metal objects into connectors.

## LiPo and Rechargeable Batteries (taught in Topic 3.3)

LiPo batteries store a lot of energy and are the most serious hazard in this
hobby. Topic 3.3 teaches the full four-gate routine. The non-negotiables,
which every later topic repeats rather than relaxes:

1. **Adult-led, every time.** A responsible adult who has read the exact
   battery, charger and vehicle instructions supervises every real battery
   activity.
2. **Charge correctly.** Compatible charger, and the chemistry, cell count
   and current settings the manufacturer specifies. For LiPo, use the
   specified balance connection.
3. **Charge in a fire-resistant setup** - a LiPo safety bag or approved
   container, on a non-flammable surface, away from anything that burns and
   away from escape routes.
4. **Never unattended.** An adult stays present and attentive throughout.
   Never charge overnight or while leaving the building.
5. **Never a damaged pack.** No charging or use of a battery that is
   swollen, punctured, crushed, wet, leaking, unusually hot, or behaving
   differently from normal.
6. **Never modify.** Do not short, open, puncture, crush, bend, dismantle or
   solder directly to a pack.
7. **Stop and tell an adult** for unusual heat, smell, hissing, smoke or any
   unexpected behaviour. Do not touch a suspicious pack - move away.
8. **Storage and disposal** follow the manufacturer's guidance and the local
   council's route. A retired battery never goes in household rubbish.
9. **Disconnect after every session.**

A suitable NiMH system is a valid lower-complexity choice, and Topic 4.4's
first powered prototype deliberately uses ordinary cells. **No battery
chemistry makes careless handling safe** - never mix old and new cells, mix
chemistries, or reverse polarity.

## Rotating Machinery and Powered Testing (Topics 3.4-3.9, 4.4, 4.5, 4.9, 4.10)

This is the hazard that arrives once the buggy can move under its own power.

- **Disable drive before any powered setup.** Use the manufacturer's
  approved method - disconnect the motor, remove the pinion, or raise the
  driven wheels on a stable stand. Binding, calibration, direction, endpoint
  and failsafe checks all happen wheels-up.
- **Treat the battery connector as live** whenever the battery is
  connected. An ESC switch may not isolate it fully.
- **Disconnect the battery before touching** gears, shafts, joints, wheels,
  linkages, mounts or wiring - and before adjusting any of them.
- Keep fingers, hair, loose clothing, jewellery, tools and wires away from
  horns, tie rods, gears, shafts, fans and tyres. **Never stop a powered
  drivetrain by hand.**
- Keep gear covers fitted for powered running.
- Never stand in front of or behind driven wheels during a powered check.
- **Stop immediately** for unexpected movement, servo buzz, stall, loss of
  control, heat, smell, smoke, sparking, damaged insulation, a loose battery
  or an unexplained indicator.
- Powered servos create pinch points and can move without warning.

### Driving Version 1 (Topic 4.10)

- The adult approves the test area, configuration, procedures, pass limits,
  stop conditions and battery plan **before** the first run, and directs
  every powered test.
- A permission-controlled area only, away from roads, stairs, water, people,
  animals and fragile objects, with **more run-off space than the worst
  stopping distance**.
- Lowest useful speed first, and every gate completed in order. A failed or
  incomplete gate blocks the next one.
- Switch off and disconnect before touching, recovering, adjusting or
  inspecting the buggy.
- Stop for any written stop condition, or whenever the adult says stop.
- **Never deliberately crash, stall, overheat, immerse or jump the buggy to
  "test the limit"**, and never run it at a person.

## Chemicals (Topics 2.9, 4.8)

- An adult opens, reads the safety data for, and handles any chemical
  product - thread-locker, lubricant, adhesive or flux.
- Use only where the component manual specifies, in a tiny controlled
  amount, and allow the stated cure time.
- Keep thread-locking products away from incompatible plastics: they can
  craze and weaken a printed part.
- Keep chemicals off skin and eyes, and away from food and drink.

## Dismantling a Donor Model (Topic 4.6)

- Show the adult the donor, the plan, the tools and the battery condition
  first. Remove and isolate all power before inspection or disassembly.
- **Springs, clips and loaded suspension parts can release suddenly** - eye
  protection where the adult's risk assessment requires it.
- Never use, charge or dismantle an unknown, damaged, swollen, leaking or
  modified battery. The adult arranges safe local disposal.
- Correct driver every time; never force a seized fastener.
- Cover sharp shafts, and keep small parts away from young children and
  pets.

## Household Mini Projects and Card Models (all teaching topics)

Every mini project in this book is built from paper, card and scrap, and
every one opens with the same rule:

- **Show a responsible adult or guardian what you plan to build before you
  start, and build with them nearby.** They can see your actual materials
  and surroundings; the book cannot.
- Age-appropriate scissors on a clear table, cutting away from your body.
  An adult handles any craft knife or difficult cut.
- **Never add a real battery, charger, motor, powered servo or mains-powered
  item to a card model.** Paper connectors are models only and must never be
  used on real wiring.
- Keep elastic bands and bent rulers low and away from faces.
- Cover sharp pivot ends, or use rolled-paper pivots instead.

---

## Maintenance Rules

1. Every topic safety box should link here; this page links back to the
   topic that teaches the full detail.
2. New hazard category = new section here, added with its topic.
3. Review this page whenever a topic reaches v0.3 Prototype-tested.
4. **This page never relaxes a topic's rule.** Where they differ, the
   stricter one applies, and the difference is a defect to be fixed.
