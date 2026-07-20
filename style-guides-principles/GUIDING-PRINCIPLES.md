# VoltForge Gear — Guiding Principles

## 1. Learn More Than You Spend

The project should maximise learning for every unit of

 money
 time
 effort
 material

We should not build a part from scratch merely because we can.

We should build a part when doing so teaches something valuable.

We should buy a part when making it would require specialist equipment, excessive trial and error, or produce little useful learning.

---

## 2. Buy Precision, Build Structure

Some parts are difficult to make well and inexpensive to buy.

These should usually be purchased

 brushless motors
 ESCs
 radio receivers
 servos
 bearings
 screws
 shafts
 gears
 differentials
 shock absorbers
 battery connectors

These parts depend on precision manufacturing, specialist materials, or established safety standards.

Parts that are good learning opportunities should usually be designed, mocked up, or printed

 chassis plates
 battery trays
 electronics mounts
 servo mounts
 body mounts
 cable guides
 bumpers
 protective covers
 brackets
 modular adapters

The goal is not to manufacture every component.

The goal is to understand how systems fit together.

---

## 3. Spend Progressively

Do not buy the full final system at the beginning.

Each purchase should unlock the next useful experiment.

A possible spending path is

```mermaid
flowchart LR
    Cardboard[Cardboard and simple tools]
    Cardboard -- SmallMotor[Small motor and battery]
    SmallMotor -- Steering[Basic steering parts]
    Steering -- Radio[Radio and receiver]
    Radio -- Brushless[Brushless motor and ESC]
    Brushless -- Drivetrain[Donor drivetrain]
    Drivetrain -- Printer[Printed structural parts]
```

This reduces wasted spending and keeps the project useful even if it pauses.

---

## 4. Prove the Idea Before Improving the Material

Do not begin with a polished printed chassis.

Use the cheapest material that can answer the current question.

Examples

 paper for layout
 cardboard for packaging
 foam board for structure
 wooden skewers for axles
 elastic bands for temporary retention
 low-power motors for early movement tests
 reusable building blocks for geometry studies

Use 3D printing only when shape, repeatability, fit, or mechanical behaviour becomes important.

---

## 5. Build in Layers of Capability

The buggy should grow through working stages.

### Stage 1 — Rolling Mock-Up

 cardboard base
 free-turning wheels
 rough component layout
 no powered drive

Question

 Does the size and layout make sense

### Stage 2 — Simple Powered Car

 low-cost brushed motor
 battery pack
 basic switch
 fixed or simple steering

Question

 Can the structure carry power and move

### Stage 3 — Controlled Wire-Frame Car

 radio control
 steering servo
 simple motor control
 removable component mounts

Question

 Can the car be driven and serviced

### Stage 4 — Modular Printed Chassis

 printed mounts
 adjustable interfaces
 replaceable subassemblies
 reused electronics

Question

 Can we improve fit, stiffness, and serviceability

### Stage 5 — Brushless Buggy

 brushless motor
 suitable ESC
 proven drivetrain
 stronger suspension and chassis
 controlled testing

Question

 Can the system safely handle more speed and power

---

## 6. Every Stage Must Work

Do not treat early versions as disposable failures.

Each version should be a complete learning machine.

A cardboard car should still

 roll
 carry components
 demonstrate layout
 reveal access problems

A low-power car should still

 steer
 stop
 allow battery removal
 survive basic testing

Each stage should produce useful evidence for the next stage.

---

## 7. Modular by Default

The vehicle should be divided into replaceable modules.

Possible modules include

 front suspension module
 rear drivetrain module
 steering module
 battery module
 electronics tray
 motor mount
 bumper
 body mount
 sensor module

```mermaid
flowchart TD
    Chassis[Core chassis]
    Chassis -- Front[Front module]
    Chassis -- Rear[Rear module]
    Chassis -- Battery[Battery module]
    Chassis -- Electronics[Electronics module]
    Chassis -- Body[Body module]
```

A module should have

 a clear job
 known interfaces
 standard fasteners
 defined dimensions
 easy removal
 minimal dependence on unrelated parts

---

## 8. Standardise Interfaces

Different versions should connect through shared interfaces.

Examples

 common M3 mounting grid
 fixed servo mounting pattern
 standard battery tray width
 shared motor-mount pattern
 common chassis datum
 standard electrical connectors

This allows

 swapping parts
 testing alternatives
 reusing hardware
 comparing versions
 upgrading without rebuilding everything

---

## 9. Design for Replacement

Parts will break.

That is expected.

A good design makes breakage

 local
 visible
 inexpensive
 easy to repair

Prefer

 replaceable arms
 removable mounts
 captured nuts
 accessible screws
 sacrificial bumpers
 separate electronics trays

Avoid designs where one small failure requires rebuilding the whole vehicle.

---

## 10. Use Donor Parts Strategically

A donor platform can provide difficult parts such as

 differential
 gearbox
 wheel hubs
 shocks
 driveshafts
 steering knuckles
 suspension geometry

The handbook should teach how to design around donor components rather than pretending they do not exist.

The learner still gains valuable experience in

 measuring interfaces
 packaging
 mounting
 alignment
 force paths
 serviceability
 adaptation

---

## 11. Do Not Reinvent Specialist Components Too Early

Some systems require deep specialist knowledge.

Examples

 gear tooth design
 differential design
 shock valving
 high-speed wheel hubs
 LiPo battery construction
 brushless motor internals

These topics may be studied later.

Early builds should use proven parts.

The learner should first understand how to select, mount, test, and replace them.

---

## 12. One New Difficulty at a Time

Each build stage should introduce only a small number of new challenges.

For example

 first learn layout
 then movement
 then steering
 then radio control
 then printed fits
 then suspension
 then higher power

Do not introduce

 new drivetrain
 new electronics
 new material
 new suspension
 and new chassis

all in one revision.

That makes problems difficult to diagnose.

---

## 13. Reuse Before Rebuying

Whenever a version changes, reuse as much as possible.

Possible reusable parts

 electronics
 batteries
 wheels
 fasteners
 bearings
 servo
 receiver
 donor drivetrain
 wiring
 switches

New spending should improve a real limitation, not merely replace working parts.

---

## 14. Keep a Cost Ledger

Every version should record

 parts purchased
 parts reused
 materials consumed
 failed purchases
 optional upgrades
 cumulative cost

The BOM should separate

 required now
 required later
 optional
 reusable
 donor part
 printable
 consumable

This helps the learner make informed trade-offs.

---

## 15. Prefer Reversible Decisions

Early decisions should be easy to change.

Good early choices

 bolted mounts
 slotted holes
 adjustable brackets
 removable trays
 adapter plates
 standard connectors

Poor early choices

 glued electronics
 trapped batteries
 custom non-standard shafts
 permanent wiring
 single-piece chassis with embedded mounts

Reversible decisions reduce fear and cost.

---

## 16. Prototype Interfaces Before Full Parts

Before printing a large part, test the risky feature.

Examples

 bearing seat coupon
 servo pocket coupon
 hinge-pin hole coupon
 snap-tab coupon
 motor-mount hole pattern
 connector clearance block

This reduces wasted print time and material.

---

## 17. Use Power Appropriate to the Stage

Early prototypes should use low power.

Reasons

 safer
 cheaper
 easier to debug
 less likely to break structures
 lower battery risk
 slower movement makes observation easier

High power should be added only after

 steering works
 braking works
 drivetrain is aligned
 fasteners remain secure
 thermal behaviour is understood
 the structure survives low-speed testing

---

## 18. Serviceability Is a Requirement

A part is not well designed if it works but cannot be reached.

The buggy should allow

 battery removal
 gear inspection
 motor adjustment
 servo replacement
 receiver access
 cleaning
 wiring repair
 suspension replacement

Access should be tested, not assumed.

---

## 19. Compare Versions Using the Same Tests

A modular project allows fair comparison.

Examples

 Chassis A vs Chassis B
 PETG arm vs nylon arm
 short battery tray vs long tray
 low gearing vs high gearing
 soft suspension vs stiff suspension

Use the same

 test surface
 battery
 tyres
 load
 driver
 measurement method

This turns different configurations into useful experiments.

---

## 20. Keep the Project Open to Many Final Forms

The project should not force one final buggy.

It should support

 low-cost learner car
 indoor car
 off-road buggy
 speed-focused version
 durable version
 sensor-equipped version
 autonomous experiment
 different wheelbases
 different batteries
 different donor drivetrains

The handbook should teach a platform, not only one product.

---

# Practical Decision Rule

Before buying or building a part, ask

1. What are we trying to learn
2. Can a cheaper mock-up answer the question
3. Does making this part teach something valuable
4. Does it require specialist precision
5. Is a proven spare safer or cheaper
6. Can the part be reused later
7. Does it preserve modularity
8. Can it be replaced easily
9. What is the smallest useful next step
10. How will we test whether it worked

---

# Handbook Writing Rule

Every future build topic should include

 learning goal
 cheapest valid prototype
 parts to buy
 parts to reuse
 parts to make
 cost checkpoint
 modular interfaces
 test plan
 upgrade path
 stop point before the next purchase

This ensures the handbook teaches engineering rather than shopping.
