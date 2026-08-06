---
title: "Troubleshooting Guide"
project: "VoltForge Gear — The Young Engineer's Handbook"
version: "0.2"
status: "Reviewed (seeded from the diagnostic sections of Topics 2.3-2.8, 3.1-3.10 and 4.3-4.10)"
feeds_from: "Topics 1.4, 1.7, 2.2, 2.3, 2.6, 2.8, 3.1-3.10, 4.3-4.10"
---

# Troubleshooting Guide

Symptom → likely causes → fix → the topic that explains why.

Remember the method from Part 1: change one thing at a time, and ask "which
system has failed?" before replacing parts. Topic 4.10 puts it strongest -
**a symptom is not a cause**, and the first job is to find a test that tells
two possible causes apart.

> **⚠️ Before diagnosing anything powered**
>
> Disconnect the battery before touching gears, wheels, linkages or wiring.
> A protection cut-out or an unexplained stop is **evidence** - do not reset
> it, reconnect and try again until you know why it happened (Topic 3.6).

---

## 3D Printing

| Symptom | Likely causes | First fix | Topic |
|---|---|---|---|
| Print detaches mid-print ("spaghetti") | Poor first layer | Watch and re-do the first layer | 2.2, 2.3 |
| Corners lift off the plate | Warping | Heated bed, no draughts, rounded corners, brim | 2.2, 2.3 |
| Hole too small for its shaft | Normal printing behaviour, not a fault | Fit coupon, then adjust the hole size | 1.7, 2.3 |
| Part looks right but snaps easily | Wrong orientation - the load runs across the layers | Reprint with the force along the layers | 1.4, 2.2 |
| Stringing between features | Material and temperature | Check the material's stated range; dry filament | 2.6 |
| Layers separate when flexed | Under-extrusion or too cool | Temperature and flow per the material guide | 2.6 |
| Support impossible to remove cleanly | Geometry, not slicer settings | Redesign for support-free printing where possible | 4.7 |

## Mechanical

| Symptom | Likely causes | First fix | Topic |
|---|---|---|---|
| Part snapped along a flat, clean surface | Layer-line failure - wrong print orientation | Reprint laid so the force runs along the layers | 1.4, 2.2 |
| Buggy curves when pushed, with no steering input | Axles not parallel; skewed chassis | Check diagonals before blaming the steering | 4.3 |
| One wheel drags | Bearing/bush misalignment, tight retainer, rubbing tyre | Spin each wheel separately and compare | 4.3 |
| Wheel bounces once per revolution | Radial runout | Check the wheel and its seat, not the suspension | 4.3 |
| Wheel scrubs sideways | Lateral runout or wrong toe | Measure toe from a datum, not by eye | 4.3, 3.9 |
| Something binds after a part is added | The part just added | Incremental freedom testing - undo the last step | 4.8 |
| Printed part whitens or sinks around a screw | Over-tightened | Stop; seat by hand, then tighten gradually | 4.8 |
| Gears whine, or wear on one side of the teeth | Gear mesh too tight, too loose, or misaligned | Set mesh per the donor manual, then check across the width | 3.8, 4.8 |
| Steering feels vague, wanders off centre | Free play adding up through the joints | Find which joint has the slack; check centre repeatability | 3.9 |
| Suspension knocks over crests | Topping out | Check droop and preload | 3.10 |

## Electronics

| Symptom | Likely causes | First fix | Topic |
|---|---|---|---|
| Nothing responds at all | Energy path, receiver power, switch, model memory | Trace the energy path before touching settings | 3.1, 3.4 |
| Steering works, motor does not | CH2 route, ESC neutral or calibration, motor path | Check the channel first - it is the cheapest test | 3.1, 3.6 |
| Motor works, steering does not | CH1 route, servo lead, receiver supply, linkage | Check the channel, then the linkage by hand | 3.1, 3.5 |
| Trigger moves the steering | Leads in the wrong channels | Swap to the correct channels | 3.4 |
| Left command steers right | Channel reverse, or linkage fitted mirrored | Reverse the channel OR fix the linkage - not both | 3.4, 3.9 |
| Servo buzzes near full lock | Commanded past a mechanical stop | Reduce the endpoint. **Do not leave it buzzing** | 3.5 |
| Receiver restarts when the servo works hard | BEC overloaded - a power fault imitating a radio fault | Trace the BEC path; check for binding | 3.6 |
| Control glitches, or short range | Battery state, receiver power, antenna routing | Check the antenna installation against its manual | 3.4 |
| ESC cuts out during a run | Low-voltage cut-off, or thermal protection | Read the status indication BEFORE resetting anything | 3.6 |
| ESC or motor unusually hot | Gearing too demanding, binding drivetrain, poor cooling | Treat as a system clue, not a motor fault | 3.7, 3.8 |
| Motor starts unexpectedly | Unsafe setup, calibration or signal fault | **Stop. Disconnect the battery.** Then diagnose | 3.1, 3.6 |
| Connector fits but nothing works | Matching shape, different pinout or polarity | Check markings and the wiring diagram, never assume | 3.1, 4.9 |

## Driving and Handling

| Symptom | Likely causes | First fix | Topic |
|---|---|---|---|
| Buggy will not drive straight | Toe, steering centre, or a dragging wheel | Prove it rolls straight unpowered first | 3.9, 4.3 |
| Slides wide in corners | Grip demand exceeds what the tyre has | One variable at a time - surface, tyre, or speed | 3.10 |
| Nose dives under braking | Load transfer, soft front damping | Change one setting and re-run the same test | 3.10 |
| Handling changed after a repair | Something else moved during the repair | Regression test - repeat the tests that used to pass | 4.10 |
| Behaves differently on the second run | Battery state, or temperature | Record conditions with every result | 4.10 |
| Results vary wildly between runs | The test is not controlled | Freeze the configuration before drawing conclusions | 4.10 |

---

## When the Table Does Not Have Your Symptom

Topic 4.10 gives the method for exactly this case:

1. Write the symptom down precisely, with the configuration and conditions.
2. List the possible causes - all of them, before testing any.
3. Design a **discriminating test**: one that gives different results
   depending on which cause is real.
4. Change one main variable, and record what happened.
5. When you find the cause, fix it, then **regression test** - repeat the
   checks that used to pass, because a fix can break something else.
6. Add a row to this guide.

Use the problem report format from Topic 4.10 (`PR-001` onwards) for anything
that takes more than one session to solve.

---

## Maintenance Rules

1. Add a row when a problem is actually solved, with the real cause.
2. Keep one symptom per row; link the topic that teaches the concept.
3. If a symptom keeps recurring, consider whether the design (not the fix)
   needs to change - that is a Part 4 design review topic.
4. Rows seeded from a topic's diagnostic section are starting points. Replace
   them with what actually happened when you hit the problem yourself - a
   real story beats a predicted one.
