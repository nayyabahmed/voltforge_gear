---
title: "Glossary"
project: "VoltForge Gear — The Young Engineer's Handbook"
scope: "Seeded from Topics 1.1-2.1, growing with each new topic (currently through Topic 4.10)"
version: "0.1"
status: "Draft (living document)"
---

# Glossary

This glossary collects the engineering terms introduced in the topics written so far.

It is a living document. New terms should be added as later topics are written.

Terms are listed alphabetically.

---

## 0-9

### 3MF

A project file that can store a model, its position on the plate and its print settings all together.

Unlike an STL, a 3MF remembers how you set the print up.

---

## A

### Abrasion

Wear caused by one surface repeatedly rubbing against another.

A wire resting on a sharp printed edge does not fail on day one. It fails after a hundred bumps have worn through the insulation.

---

### Abrasive

A hard material that wears another surface away by rubbing.

Sandpaper is an abrasive. Some filaments are abrasive too, and slowly wear the nozzle out.

---

### Acceleration

A change in speed or direction.

A buggy accelerates when it speeds up, slows down, or turns.

---

### Access Clearance

Empty space left on purpose so that a hand or a tool can reach a feature.

A screw you cannot reach with a driver is a screw you cannot tighten.

---

### Accuracy

How close a measurement is to the true value.

A measurement can be precise without being accurate.

---

### Ackermann Steering Geometry

A steering layout that turns the inside wheel more sharply than the outside one.

In a corner the inside wheel follows a tighter circle, so it has to point further round or it drags.

---

### Actual Size

The measured size of a real part.

This may differ slightly from its nominal size.

---

### Actuator

A device that produces controlled movement when it is told to.

A servo is an actuator; a motor driving a wheel is one too.

---

### Additive Manufacturing

Making a part by adding material layer by layer instead of cutting it away.

3D printing is the most common example.

---

### Allowance

An intentional size difference between two mating parts.

Example:

```text
Battery width = 47.0 mm
Tray width = 48.0 mm
Allowance = 1.0 mm total
```

---

### Ampere

The unit of electric current, written A.

Often shortened to "amp".

---

### Anisotropic

Having different properties in different directions.

A printed part is anisotropic: strong across its layers, weaker between them. See also Anisotropy.

---

### Anisotropy

A condition where a material behaves differently in different directions.

3D printed parts are often anisotropic because they are built in layers.

---

### Antenna

The part of a radio that sends or receives radio waves.

---

### Assembly Drawing

A drawing that shows how several parts fit together.

It may include:

- exploded views
- item numbers
- fasteners
- assembly order
- a bill of materials

---

### Assembly Sequence

The order in which parts and fasteners have to be fitted.

Some parts can only go in before others, so the sequence is part of the design.

---

### Assembly Traveller

A checklist that travels with the build, recording what was done and checked at each step.

It is how you answer "did I actually tighten that one?" three sessions later without taking the buggy apart.

---

### Assumption

Something treated as true without full proof.

Important assumptions should be written down and tested.

---

### Average

The sum of several values divided by the number of values.

Averages can help reduce random measurement variation.

---

### Axial Load

A force acting along the length of a shaft.

---

## B

### Back EMF

A voltage produced by a spinning motor that pushes back against the voltage driving it.

The faster the motor spins, the more it pushes back - which is why a motor draws most current at the moment it starts.

---

### Backing Board

Scrap material placed under the work so a drill or knife breaks through into it instead of into the bench.

---

### Backlash

The small amount of free movement between parts before they actually push each other.

Turn a gear gently back and forth: the little bit of nothing before the next gear moves is backlash.

---

### Balance Charging

Charging that watches each cell group in a pack and keeps them level with each other.

---

### Balance Lead

The thin extra plug on a battery pack that lets a charger read each cell group separately.

The fat main lead carries the current; the balance lead carries the information. A balance charger uses it to keep every cell at the same voltage.

---

### Baseline Dimensioning

A way of locating several features from one common reference, or datum.

This can reduce accumulated positional error.

---

### Baseline Test

A test that records how something behaves BEFORE you change anything.

Without a baseline you cannot say an upgrade improved the buggy. You can only say it feels different.

---

### Battery

A device that stores energy chemically and releases it as electrical energy.

---

### Battery Chemistry

The materials and reactions a battery uses to store and release energy.

LiPo and NiMH are two different chemistries, and they need different chargers and rules.

---

### Battery Eliminator Circuit (BEC)

A circuit, usually inside the ESC, that supplies a steady low voltage to the receiver and servo.

It "eliminates" the need for a second battery just for the electronics.

---

### Battery Pack

One or more cells joined together and wrapped as a single usable power source.

---

### Battery Passport

A written record of one pack: what it is, how it has been used, and what condition it is in.

---

### Bearing

A component that supports a rotating shaft while reducing friction.

---

### Bellcrank

A pivoting lever that changes the direction motion travels in.

---

### Benchmarking

Comparing existing solutions to learn from them before designing your own.

---

### Bending

Loading that stretches one side of a part while squeezing the other side.

---

### Bilateral Tolerance

A tolerance that allows variation above and below a nominal size.

Example:

```text
10.0 ± 0.2 mm
```

---

### Bill of Materials

A list of the parts and quantities required for an assembly.

It is often shortened to **BOM**.

---

### Bill Of Materials (BOM)

The controlled list of every item and quantity a design needs.

A shopping list that has been checked. If it is not on the BOM, it does not exist on the buggy.

---

### Binding

Pairing a receiver with a transmitter so they only listen to each other.

---

### Blind Hole

A hole that stops inside the part instead of passing all the way through.

---

### Boss

A raised pad around a hole or fixing point that adds material where the load goes in.

---

### Bottom Layers

The solid layers that form the base surfaces of a print.

---

### Bottoming Out

Suspension reaching the end of its travel with a hard thump.

---

### Brake Force

How hard an ESC asks the motor to resist turning when you brake.

It is a setting, not a fixed property of the buggy. Too little and it runs on past the corner; too much and the wheels lock and slide.

---

### Breakthrough

The moment a drill reaches the far side of the material.

This is the moment a drill is most likely to grab, so ease off as you approach it.

---

### Brim

A thin flat border printed around the bottom edge of a model to give it more grip on the build plate.

---

### Brittle

A material behaviour where failure happens with little visible bending or stretching.

---

### Brownout

A short dip in voltage that makes control electronics reset.

If the receiver browns out mid-drive, the buggy stops obeying you until it restarts.

---

### Brush

A sliding electrical contact that feeds current into a spinning brushed motor.

---

### Buckling

Sudden sideways bending of a long, thin part under compression.

---

### Build Log

A running record of what was made, what went wrong and what was changed.

A build log with no problems in it usually means nobody was paying attention.

---

### Build Plate

The flat surface a 3D print is built on, often heated to help the first layer stick.

Also called the bed.

---

### Build Volume

The space a printer can reach and print inside.

Anything bigger than the build volume has to be split into several parts.

---

### Bump Steer

Unwanted steering change caused by the suspension moving up and down.

---

### Burr

A rough or sharp edge left behind by cutting, drilling or another process.

---
### Bush

A plain sleeve that supports a rotating or sliding shaft.

Simpler and cheaper than a ball bearing, and good enough for a cardboard prototype's axles.

---


## C

### Camber Gain

The way a wheel's lean changes as the suspension moves up and down.

A wheel that stands upright when parked may lean when the suspension compresses. Camber gain decides how much tyre stays flat on the ground in a corner.

---

### Cell Count

How many cells are joined in a line inside a battery pack, written with an S.

A 3S pack has three cells in series. More cells means more voltage, not more capacity.

---

### Centre Of Mass

The single balance point of all the mass in an object or system.

Balance a ruler on one finger and you have found its centre of mass. Where the buggy's sits decides how it behaves in a corner.

---

### Clamp

To hold two mating faces together with a controlled force.

One of the four jobs a fastener can do, alongside locate, retain and adjust. A screw clamps; it should not be asked to locate as well.

---

### Command Matrix

A table matching every driver input to the response you expect and the response you actually saw.

Written before the first powered test, so a wrong answer is obvious rather than a surprise.

---

### Commissioning

The controlled sequence of checks run when a new system is first switched on.

Not "turning it on" - a planned order of steps where each one is proved before the next is allowed.

---

### Component Model

A simplified stand-in that keeps the dimensions and interfaces a test needs.

A card box the size of your ESC, with its wires drawn on. It cannot control a motor, but it can prove the ESC will not fit.

---

### Compound Gear Train

Two or more gear ratio stages working one after the other.

Each stage multiplies the one before it, so two modest reductions produce a large one. This is how a fast, weak motor turns a wheel slowly and strongly.

---

### Configuration Baseline

The controlled record of exactly which parts, settings and conditions define one version.

Without it, a test result belongs to no particular buggy and cannot be compared with anything.

---

### Contingency

Money set aside for uncertainty you have already identified.

Not a slush fund and not optimism. It is the honest admission that some parts will cost more than the first estimate.

---

### Controlled Dimension

A recorded value that can only change through a documented revision.

Controlled does not mean permanent. It means a change needs a reason, a new revision and updated evidence.

---

### Corrective Action

A change made to remove or control the cause of a known problem.

Fixing the symptom is a repair. Fixing the cause so it cannot happen again is corrective action.

---

### Cost Ledger

The running record of what the project was estimated to cost and what it actually cost.

The gap between the two columns is where the learning is.

---

### Coulomb

The unit for an amount of electric charge, written C.

One amp flowing for one second moves one coulomb. It counts charge the way a litre counts water.

---

### Coupon Ladder

A single test print containing several labelled size variants of the same feature.

Print one ladder of hole sizes and measure which fits, instead of reprinting a whole chassis to find out.

---

### C-Rating

A claimed discharge rate for a battery, written as a multiple of its capacity.

---

### CAD

Computer-Aided Design.

Software used to create precise 2D drawings and 3D models.

---

### Calibration

Comparing a measuring tool with a trusted reference.

Calibration helps identify or correct measurement bias.

---

### Calipers

A tool for measuring outside, inside, depth and step dimensions.

A digital caliper shows the reading on a display and can be zeroed before use.

---

### CAM

Computer-aided manufacturing: software that plans how a machine will make the design.

---

### Camber

The tilt of a wheel seen from the front of the buggy.

---

### Capacity

How much electrical charge a battery holds, usually written in Ah or mAh.

---

### Captive Nut

A nut held in a shaped pocket so it cannot spin or fall out while the screw is tightened.

Also called a captured nut.

---

### Cause

Something that creates a change.

---

### Cause and Effect

A relationship where one event produces another.

---

### Cell

One unit of a battery that stores chemical energy.

A pack is made of cells, in the same way a chocolate bar is made of squares.

---

### Centre Line

A drawing line used to mark the centre of:

- a hole
- a shaft
- a circular feature
- a symmetrical part

---

### Centre-to-Centre Spacing

The distance from the centre of one feature to the centre of another.

Often used for mounting-hole spacing.

---

### Chain Dimensioning

A way of locating each feature from the previous feature.

Small errors may accumulate along the chain.

---

### Challenge Report

A document that records:

- problem
- measurements
- requirements
- concepts
- tests
- results
- revisions
- conclusions

---

### Chamfer

A sloped edge.

Chamfers often help guide parts together during assembly.

---

### Channel

One separate control route in a radio system, used for one job.

Steering uses one channel; throttle uses another.

---

### Channel Reverse

A setting that flips which way a channel responds.

Use it when the servo moves the right way mechanically but the wrong way on screen.

---

### Chassis

The main structural frame of the buggy.

It supports and connects the other systems.

---

### Circuit

A connected loop that electric charge can travel around.

---

### Clamp Force

The squeeze that a tightened screw applies to the parts it joins.

Clamp force is what actually holds a joint together, not the screw itself.

---

### Clearance

The empty space between mating parts.

For a shaft and hole:

```text
Clearance = Hole size - Shaft size
```

---

### Clearance Fit

A fit where the opening is larger than the inserted part.

This allows movement or easy assembly.

---

### Clearance Hole

A hole made slightly larger than the fastener, so the fastener slides through instead of biting into it.

---

### Closed-Loop Control

Control that checks the result and corrects itself.

A servo does this constantly: it compares where it is with where it was told to be, and keeps moving until they match.

---

### Cold Joint

A solder joint that never got hot enough, so the solder sat on the metal instead of bonding to it.

Cold joints look dull and lumpy, and often fail later once the buggy starts vibrating.

---

### Command Path

The route the driver's instructions travel along to reach the part that acts on them.

Your thumb, the transmitter, the receiver, the ESC, the motor - information all the way.

---

### Commutation

Switching current through a motor's windings in the order needed to keep it turning.

---

### Commutator

The segmented rotating contact that switches current inside a brushed motor.

---

### Compensation

A deliberate CAD or slicer adjustment used to achieve the desired real printed size.

---

### Composite

A material made by combining two or more different materials.

---

### Compression

A pushing load that tries to shorten, squash, or crush a part.

---

### Concept

One possible design solution.

---

### Concept Card

A short record describing:

- how a concept works
- advantages
- risks
- questions
- likely materials
- assembly method

---

### Concept Generation

The process of creating several possible solutions before choosing one.

---

### Conductor

The metal inside a wire that carries the electricity.

---

### Confirmation Bias

Seeing what you hoped to see rather than what is really there.

In measurement, it means repeating a reading until you get the expected number instead of recording the honest result.

---

### Constraint

A limit within which a design must work.

Examples:

- budget
- printer size
- available tools
- chosen battery
- build time

In CAD, the word has a second, narrower meaning: a rule that controls a
geometric relationship in a sketch, such as parallel, equal or centred.

---

### Contact Patch

The small piece of tyre actually touching the ground.

All your grip comes through four patches roughly the size of postage stamps.

---

### Continuity

An unbroken electrical path between two points.

---

### Continuity Test Lead

A pair of soldered wires used to check whether an electrical path exists between two points.

---

### Continuous Current

The current a component can carry all day under stated conditions.

---

### Control Variable

A factor kept the same during a fair test.

---

### Convergent Thinking

Narrowing many ideas down to the few best ones, using evidence and criteria.

---

### Coordinate

A set of numbers saying where a point sits along the X, Y and Z axes.

---

### Counterbore

A flat-bottomed cylindrical recess, often used for:

- cap screw heads
- nuts
- washers
- bearings

---

### Countersink

A cone-shaped recess for a countersunk screw head.

---

### Creep

Slow permanent deformation under a steady load.

Creep is often worse when plastic is warm.

---

### Crimp

A connection made by squeezing a metal terminal tightly onto a wire with the correct tool.

---

### Critical Dimension

A dimension that strongly affects fit, function, or safety.

---

### Cross-Check

Checking a result using a second method.

---

### Cross-Member

A structural piece connecting two chassis rails.

It stops the rails moving relative to each other, which is what turns two beams into a frame.

---

### Cross-Threading

Thread damage caused by a screw starting crooked and cutting a new, wrong thread.

It damages both the screw and the part, so always start a screw by turning it backwards until it drops into the existing thread.

---

### Current

How much electric charge flows past a point each second.

---

## D

### Damper

A device that resists suspension movement and stops it bouncing.

A spring alone would keep bouncing; the damper calms it down.

---

### Datum

A chosen reference point, line, or surface used for measurement or dimensioning.

---

### Debugging

The structured process of finding and correcting the cause of unwanted behaviour.

Structured is the important word. Changing things until the symptom disappears is guessing, and it teaches you nothing.

---

### Deburring

Removing burrs without changing the shape the part is meant to be.

---

### Decimal Place

A digit position to the right of a decimal point.

More decimal places do not automatically mean a more trustworthy measurement.

---

### Decision Log

A record of a choice, the evidence behind it, and what would make you revisit it.

Six weeks later it answers "why did I do it this way?" - a question you will definitely ask.

---

### Decision Matrix

A table used to compare design concepts against selected criteria.

---

### Decomposition

Breaking a large problem into smaller, manageable questions.

---

### Definition of Done

A clear set of conditions that must be met before a task or design version is considered complete.

---

### Dependent Variable

The result measured during a test.

---

### Depth

The distance inward from a surface.

---

### Desiccant

A material that soaks up moisture inside a sealed container.

Filament is usually stored with a desiccant pack to keep it dry.

---

### Design

A plan for building something.

---

### Design Freeze

A temporary pause on design changes so a complete version can be built and tested.

---

### Design Intent

The reason a feature has a particular:

- shape
- size
- relationship
- location

---

### Design Review

A structured check of a design before moving to the next stage.

---

### Detail View

An enlarged drawing view of a small feature.

---

### Diameter

The distance across a circle through its centre.

The symbol is often:

```text
Ø
```

---

### Differential

A gear system that sends motion to both driven wheels while letting them
turn at different speeds, so the outside wheel can travel farther than
the inside wheel during a turn.

---

### Dimension

A numerical description of a feature's size or location.

---

### Discriminating Test

A test chosen specifically to tell two competing explanations apart.

If both explanations predict the same result, the test proves nothing. Design one where they disagree.

---

### Divergent Thinking

Producing many possible ideas before judging them.

---

### Donor

An existing product or assembly used to supply proven parts for a new design.

Buy precision, build structure: the donor supplies the bearings, gears and hinge pins you cannot make.

---

### Donor Interface Atlas

The controlled record of a donor's identity, condition, datums, dimensions, motion and service interfaces.

Everything you measured off the donor, written down once, so the CAD never has to guess.

---

### Drag Brake

A gentle braking effort some ESCs apply when the throttle sits at neutral.

It stops a buggy rolling away on a slope. Useful for a crawler, annoying for a racer, and a setting either way.

---

### Drive Ratio

The relationship between input and output rotation in a transmission.

The same idea as a gear ratio, whether it is achieved with gears, pulleys or friction.

---

### Driver Profile

The shaped recess in a screw head, and the matching tool shape that turns it.

Using the wrong driver profile rounds the recess out.

---

### Driveshaft

A shaft that carries rotation and torque from one place to another.

---

### Drivetrain

The parts that carry motor rotation to the driven wheels.

Typical parts include:

- pinion
- spur gear
- differential
- driveshafts
- axles
- wheels

---

### Droop

How far a wheel can drop below its normal resting height.

---

### Dual Rate

A setting that changes how much total movement a channel commands.

---

### Ductile

A material behaviour where noticeable bending or stretching happens before failure.

---

### Dummy Battery

An inert block matching a real battery's size and weight, used for fit tests.

It lets you prove the tray, strap and removal path with no stored energy anywhere near the bench.

---

### Duty Cycle

The fraction of each rapid switching cycle that is spent switched on.

Half on and half off is a duty cycle of 50%.

---

### Dynamic Load

A load that changes with time.

Examples:

- bumps
- steering inputs
- acceleration
- landing forces

---

## E

### Effect

The result of a cause.

---

### Efficiency

The share of energy put in that comes out as useful work.

The rest usually leaves as heat.

---

### Elastic Deformation

A temporary change in shape that disappears after the load is removed.

---

### Elasticity

How well a material springs back towards its original shape once a load is removed.

---

### Electronic Commutation

Switching the power between a brushless motor's windings electronically, in time with the rotor.

A brushed motor does this with sliding metal brushes. A brushless motor gives the job to the ESC, which is why it needs three wires and cleverer electronics.

---

### Electronic Speed Controller (ESC)

The module that controls how much electrical power reaches the motor.

It is the buggy's throttle: the receiver tells it what you want, and it feeds the motor to match.

---

### Elephant's Foot

Outward spreading of the first printed layer.

It can make printed parts wider at the bottom.

---

### Endpoint

A set limit on how far a channel is allowed to move in one direction.

---

### Endurance

The ability to keep working through a defined time or number of cycles.

One good lap proves the buggy can move. Twenty laps prove it was built.

---

### Energy

The ability to do work or cause change.

A battery stores electrical energy.

---

### Energy Path

The route useful electrical energy takes to reach the part that does the work.

---

### Engineer

Someone who designs, tests, improves, and understands how things work.

---

### Engineering Cycle

A repeating process of:

```text
Think -> Design -> Build -> Test -> Learn -> Improve
```

---

### Engineering Drawing

A precise visual instruction describing the shape, size, and important details of a part or assembly.

---

### Error

The difference between a measured value and the true value.

---

### Error Stacking

Small dimensional errors adding together across several parts.

Also called tolerance stack-up.

---

### Evidence

Measurements, observations, photographs, or test results used to support a conclusion.

---

### Exploded Diagram

A drawing showing every part of an assembly separated but still in order.

The picture in a flat-pack instruction sheet. Photograph your own before dismantling a donor.

---

### Exploded View

An assembly view showing parts separated along their assembly direction.

---

### Exponential

A setting that changes how sensitive a control feels near its centre.

---

### Extruder

The motor mechanism in a 3D printer that grips the filament and pushes it into the hot end.

---

### Extrusion

In CAD, stretching a flat shape in a straight line to add or remove material.

This is a different idea from the printer's extruder, which pushes filament.

---

## F

### Failsafe

What the buggy is set to do if the radio signal is lost.

A sensible failsafe cuts the throttle rather than leaving it where it was.

---

### False Precision

Reporting more detail than the measurement can justify.

False precision can make weak data look more scientific than it really is.

---

### Fastener

Any part whose job is to hold other parts together: a screw, nut, pin or clip.

---

### Fastener Map

A record matching every screw, nut, washer and spacer to the position it came from.

Made during disassembly, when you still know. Not attempted afterwards from a pile.

---

### Fatigue

Failure caused by repeated loading.

A part may fail from many small load cycles even if one cycle does not break it.

---

### Fault Finding

Tracing a problem step by step to find its cause.

---

### FDM (Fused Deposition Modelling)

A 3D printing method that melts plastic filament and lays it down in fused layers.

---

### Feature

One modelling step that creates or changes geometry in a CAD model.

---

### Feature History

The ordered record of the sketches and features used to build a model.

Because the history is kept, you can go back and change an early step.

---

### Feedback

Information about a result that is used to decide what to do next.

---

### Filament

The raw material for FDM printing: a long plastic strand, usually 1.75 mm thick, wound onto a spool.

---

### Fillet

A rounded inside corner.

Fillets can reduce stress concentration.

---

### First-Angle and Third-Angle Projection

Two standard ways of arranging the views in an orthographic drawing.

Different countries prefer different systems, so a drawing should state which one it uses.

---

### Fit

The relationship between two connected parts.

---

### Fit Library

A record of tested dimensions and the real fits they produced.

---

### Fit Template

A cheap physical pattern used to check an interface before committing material.

A piece of card with the hole pattern on it costs nothing and catches the mistake a printed chassis would make expensive.

---

### Five Whys

A method of repeatedly asking "why?" to trace a problem back to its root cause.

---

### Flux

A material that cleans hot metal so solder can flow across it and stick.

Most electronics solder has flux built into its core.

---

### Footprint

The area a stationary part occupies in one view.

Only the first of three questions. Movement envelope and service envelope are the other two, and they are usually bigger.

---

### Force

A push or a pull.

---

### Force Path

The route force follows through a machine or structure.

---

### Fracture

A crack or complete break.

---

### Free Play

Small unwanted movement in a linkage before anything actually moves.

Wiggle a steering rod and feel the slack before the wheel turns. Free play makes a buggy feel vague, and it adds up through every joint.

---

### Frequency

How many repeating cycles happen each second.

---

### Friction

A force that resists movement between surfaces.

Friction can be useful or wasteful.

---

### Friction Drive

A transmission that drives another surface by rubbing directly against it.

Simple enough to build from a motor and a rubber band, and it slips when overloaded - which for a first prototype is a feature.

---

### Front View

An orthographic view chosen to show the most useful front-facing shape of a part.

---

### Full Scale

A representation whose measurements match the real object exactly, written 1:1.

Half-size looks convincing and proves nothing. You cannot check finger access on a small drawing.

---

### Functional Feature

A piece of geometry with a job to do, such as a hole, a locating lip or a cable slot.

---

### Functional Prototype

A prototype used to test how something works.

---

### Functional Requirement

A requirement describing what a design must do.

---

## G

### G-code

The list of simple move-and-extrude instructions a 3D printer follows, produced by the slicer.

---

### Gear Mesh

How a pair of gear teeth sit together, including the clearance between them.

Too tight binds and wears; too loose rattles and skips.

---

### Gear Ratio

A comparison between the sizes or tooth counts of connected gears.

For a simple gear pair:

```text
Gear ratio = Driven gear teeth / Driving gear teeth
```

---

### Grip

The tyre's ability to transfer force to the ground without slipping.

---

### Grit

A number describing how coarse an abrasive is.

Lower numbers are coarser, higher numbers are finer.

---

### Ground Clearance

The smallest gap that matters between the buggy and the ground.

---

### Gusset

A reinforcing web, often triangular, added where two walls meet.

---

## H

### Hard Constraint

A limit that must not be broken.

---

### Hatching

Diagonal lines used in a section view to show cut material.

---

### Hazard

Something that could cause harm, such as a sharp blade or a hot tool.

The hazard stays the same; the situation decides the risk.

---

### Heat-Set Insert

A metal threaded sleeve installed into plastic using controlled heat.

It gives a printed part a proper metal thread that can be undone many times.

---

### Heat-Shrink Tubing

Plastic sleeving that shrinks tightly when heated, insulating and protecting a connection.

---

### Hidden Line

A dashed drawing line showing an edge or feature hidden behind a visible surface.

---

### Hole Callout

Drawing text describing a hole's:

- diameter
- depth
- quantity
- type

---

### Hot End

The heated part of a 3D printer that melts the filament before it leaves the nozzle.

---

### Hot Zone

The agreed bench area where hot tools and parts are allowed to be while they cool.

---

### Hygroscopic

Able to pull moisture out of the surrounding air.

Hygroscopic filament prints badly unless it is kept dry.

---

## I

### Idler Gear

A gear placed between two others mainly to pass motion along or reverse its direction.

It changes which way the output turns and can bridge a gap, but it does not change the overall ratio.

---

### Impact Load

A force applied very quickly.

Examples:

- crash
- jump landing
- wheel striking a rock

---

### Incremental Freedom Testing

Checking that everything still moves freely after each part is added.

When something binds, you know which part caused it, because it moved a moment ago.

---

### Independent Variable

The factor deliberately changed during a test.

---

### Inertia

An object's resistance to a change in motion.

---

### Infill

The internal pattern that partly fills a 3D printed part, chosen as a percentage.

20-40% suits most buggy parts.

---

### Input

Something entering a system.

Examples:

- energy
- information
- movement
- force
- material

---

### Inside Diameter

The diameter of a circular opening.

---

### Inspection Record

A completed table of checks with real results, kept as evidence.

---

### Installation Order

A planned sequence for fitting parts that preserves access, inspection and safe commissioning.

Fit the thing that traps other things last, not first.

---

### Installation Sequence

The order in which parts are fitted during assembly.

---

### Insulation

The protective covering around a conductor that stops it touching things it should not.

---

### Interface

The place where two parts or systems connect.

---

### Interface Control Drawing

A drawing focused on how one component connects to another.

---

### Interface Requirement

A requirement describing how parts or systems must connect.

---

### Interface-Control Table

A record of the datums, dimensions and rules shared by two connected modules.

It is the agreement between two parts. Change one side without updating it and the parts stop fitting.

---

### Interference Fit

A fit where the inserted part is larger than the opening.

Assembly requires the parts to deform slightly.

---

### Island

A section of a layer that begins with nothing underneath it.

---

### Isometric View

A 3D-looking drawing view showing several faces at once.

---

### Iteration

One pass through the design-build-test-improve cycle.

---

## K

### Kerf

The width of material removed by a cutting tool such as a saw.

Because the kerf has width, you cut on the waste side of the line, not down the middle of it.

---

### kV Rating

Roughly how many revolutions per minute a motor turns for each volt applied, with no load.

A higher kV motor spins faster but pulls harder on the battery.

---

## L

### Lateral Runout

Side-to-side wobble of a rotating part.

A wheel with lateral runout scrubs the tyre sideways every revolution and steals motion.

---

### Layer Height

The thickness of each printed layer.

A typical value is 0.2 mm.

---

### Lead-In

A feature that guides parts into alignment during assembly.

Examples:

- chamfer
- taper
- rounded entry

---

### Linear Motion

Movement along a path.

---

### Linkage Route

The path a moving connection follows between its pivots.

Two linkages can join the same two points and still behave differently, because the route decides what the movement feels like at each end.

---

### LiPo

A rechargeable lithium-polymer battery, the type most used in radio-controlled models.

LiPo packs hold a lot of energy for their weight, which is exactly why their safety rules are strict.

---

### LiPo Bag

A fire-resistant pouch that a rechargeable battery is charged inside.

It contains flame and sparks if a pack fails, which buys time - it does not
make charging unattended safe.

---

### Load

A force or combination of forces acting on a part.

In electrical work the word has a second meaning: the component that turns
electrical energy into something else. A motor is the buggy's biggest
electrical load.

---

### Load Path

The route a load follows through a structure or machine.

---

### Load Transfer

The way weight shifts between tyres when a vehicle accelerates, brakes or corners.

Brake hard and the front tyres are pressed down while the rear tyres go light. The buggy's total weight has not changed, only where it is carried.

---

### Local Modifier

A region of a model given different slicer settings from the rest.

It lets you put solid material only where a screw goes, instead of printing the whole part solid.

---

### Locate

To place a part accurately using a datum or feature.

One of the four fastener jobs. A tab or a datum face locates; a screw should not be forced to.

---

### Locational Fit

A fit used to position one part accurately.

---

### Low-Power Prototype

A version built with deliberately limited energy so its behaviour can be studied safely.

It still teaches you drive ratio, torque reaction and commissioning - just without enough power to hurt anyone.

---

### Low-Voltage Cut-Off (LVC)

An ESC setting that reduces power when the battery drops to a set voltage.

It protects the pack from being drained past the point where it is damaged.

---

### Lower Limit

The smallest acceptable size allowed by a tolerance.

---

## M

### Machine

Something made from parts working together to perform useful work.

---

### Main Lead

The thick pair of wires carrying the working current between a battery and the ESC or charger.

Thick because it carries the whole current the motor asks for. Not to be confused with the thin balance lead.

---

### Manual Card

A short controlled record of one component's exact identity, instructions and warnings.

So that "check the manual" means one specific document rather than a search.

---

### Marking Out

Transferring dimensions, lines and hole positions from a drawing onto the real material.

---

### Mass

The amount of matter in an object.

Usually measured in grams or kilograms.

---

### Material Property

A measurable way a material behaves, such as how easily it bends, stretches or softens.

---

### Material Substitution

Replacing a specified material with a different one, having checked the part still does its job.

---

### Measurement

Comparing something with an agreed standard.

---

### Measurement Plan

A short plan describing:

- what must be measured
- which tool to use
- which dimensions are critical
- how many times to measure

---

### Measurement Uncertainty

The amount of doubt associated with a measurement.

---

### Mechanical Advantage

A force increase gained by trading speed or distance.

---

### Mechanical Stop

A physical feature that will not let a part move any further.

Once a servo reaches a mechanical stop, extra command becomes heat and force instead of movement. Finding the stops before powering up protects the servo.

---

### Median

The middle value once results are put in order.

Less easily fooled by one strange run than the mean. Topic 1.6 introduces it; Topic 4.10 uses it on real test data.

---

### Millimetre

A metric unit of length equal to one thousandth of a metre.

Abbreviation:

```text
mm
```

---

### Minimum Viable Prototype

The simplest prototype that can answer the current design question.

---

### Mission

A short statement of what the project should become and how it will be used.

Written before anything is bought. It is what every later argument gets settled against.

---

### Module

A group of parts with one clear job and defined connections.

The steering module, the drivetrain module. Modules can be changed one at a time, which is the whole reason for them.

---

### Momentum

The motion carried by a moving mass.

Momentum increases with mass and speed.

---

### Motion

A change in position.

---

### Motion Path

The route rotation and movement follow through a machine.

---

### Motor

A device that converts electrical energy into rotation.

---

### Movement Envelope

Every position a part passes through when all its movements are combined.

A steering arm sweeps a shape, not a line. Nothing else may be put inside that shape.

---

### Multimeter

An instrument for measuring electrical quantities such as voltage, current and resistance.

---

## N

### Native File

The editable master model saved in the CAD program's own format.

Keep the native file: an exported STL cannot easily be edited back into a design.

---

### Near Miss

An event that could have caused harm but did not.

Near misses are free lessons and should be recorded.

---

### Neutral

The command a spring-centred control gives when you let go of it.

Neutral steering means straight ahead; neutral throttle means no drive requested. Checking neutral is the first step of almost every setup.

---

### NiMH

A rechargeable nickel-metal hydride battery, tougher and heavier than a LiPo.

---

### No-Load Speed

How fast a motor spins with nothing attached to its shaft.

It is the fastest a motor will ever turn and the least useful, because a motor doing no work produces no useful output.

---

### Nominal

A convenient named value used to describe something, rather than its exact measured value.

A "3.7 V" cell is named that way; the real voltage moves around as it charges and discharges.

---

### Nominal Size

The named or target size of a part.

The actual measured size may differ.

---

### Nominal Voltage

The convenient named voltage used to label a cell or pack.

A LiPo cell is called 3.7 V even though it is 4.2 V when full and lower when nearly empty. The name is for classifying; the measurement is for deciding.

---

### Non-Destructive Test

A test that leaves the part usable.

---

### Nozzle

The small metal tip (usually 0.4 mm) where melted plastic leaves a printer's hot end.

---

### Nyloc Nut

A nut with a nylon ring inside that grips the thread and resists shaking loose.

---

## O

### Ohm

The unit of electrical resistance, written Ω.

---

### Ohm's Law

The rule linking voltage, current and resistance: V = I × R.

---

### One-Way Operation

A step that cannot be undone, so it has to be checked before it is started.

Cutting, drilling and sanding are all one-way: the material does not go back on.

---

### Operating Envelope

The range of conditions in which something has been shown to work acceptably.

Outside it you are not driving your buggy, you are testing an untested one.

---

### Operation Plan

A written list of every stage of a build, in order, with the safety check for each one.

Professionals write one before touching material, because the expensive mistakes are ordering mistakes.

---

### Origin

The fixed reference point where a model's X, Y and Z coordinates are all zero.

---

### Orthographic Projection

A method of showing an object using flat views from different directions.

---

### Outlier

A measurement far from the other results.

Outliers should be investigated before being removed.

---

### Output

Something leaving a system.

Examples:

- movement
- sound
- heat
- information
- wear

---

### Output Spline

The toothed shaft on a servo that a horn clamps onto.

---

### Outside Diameter

The diameter measured across the outside of a round part.

---

### Overhang

A part of a 3D model that leans out with nothing below it to build on.

Beyond about 45 degrees it usually needs support material.

---

## P

### Packaging Board

A full-size layout used to test component space, movement, routes and access.

The cheapest experiment in the whole build, and the one that catches the most expensive mistakes.

---

### Packaging Envelope

The total space needed for a component, including:

- wires
- movement
- access
- cooling
- removal

---

### Packaging Model

A simplified model used to test component size, position, and arrangement.

---

### Parallax Error

A reading error caused by viewing a scale from an angle.

---

### Parallelism

The condition where two lines or surfaces stay the same distance apart.

Axles that are not parallel fight each other, and the buggy curves even with perfect steering.

---

### Parameter

A named value that controls one or more parts of a design.

---

### Parametric Model

A model controlled by dimensions, named values and relationships, so changing one value updates the geometry.

---

### Part Brief

A short written description of a part's job, its limits, and how you will know it passed.

---

### Part Number

A unique identifier assigned to a part.

---

### Peak Current

The larger current a component can carry for a short time only.

---

### Peer Review

A review performed by another person.

---

### Performance Requirement

A requirement describing how well a function must be performed.

---

### Perimeter

Another name for a printed wall following a layer's boundary.

See Wall.

---

### Permanent Deformation

A shape change that remains after the load is removed.

---

### Phase

One of the separately switched winding paths in a brushless motor.

A brushless motor has three, which is why it has three fat wires. The ESC energises them in turn to pull the rotor round.

---

### Pilot Hole

A smaller hole drilled first to guide a later, larger one.

---

### Pinion

The small driving gear on the motor shaft.

See Pinion Gear.

---

### Pinion Gear

The small gear attached to the motor shaft.

---

### Pinout

A record of what each contact in a connector does, and its polarity.

Two plugs can mate perfectly and still have their pinouts in a different order.

---

### Pitch

The distance from one thread ridge to the next.

An M3 screw normally has a pitch of 0.5 mm.

---

### Polarity

Which terminal or direction is positive and which is negative.

Getting polarity wrong can destroy electronics instantly.

---

### Position Error

The difference between where a servo has been told to go and where it actually is.

The servo's electronics keep measuring this gap and driving the motor until it is small. A gap that will not close means something is blocking the linkage.

---

### Positive Feedback

Feedback that makes a change grow larger.

Example:

```text
Loose wheel -> more wobble -> even looser wheel
```

---

### Power

How quickly energy is transferred or work is done.

In an electrical circuit, power = voltage × current (P = V × I), measured
in watts.

---

### PPE

Personal protective equipment.

Things worn to reduce harm, such as safety glasses and closed shoes.

---

### Precision

How closely repeated measurements agree with one another.

---

### Preload

Spring compression already present before the suspension takes any load.

Winding a collar down squeezes the spring in advance. It changes ride height and the initial stiffness, not the spring itself.

---

### Press Fit

An interference fit assembled using force.

---

### Pre-Test Certificate

A signed checklist confirming the required safety and function evidence exists before driving.

The moment where the answer to "is it ready?" stops being a feeling and becomes a record.

---

### Preview

The slicer's layer-by-layer view of the paths the printer will actually attempt.

---

### Problem Statement

A clear description of:

- what is wrong
- who experiences it
- when it happens
- why it matters

---

### Process

What a system does with an input.

---

### Profile

A saved group of related slicer settings for a printer, material or type of print.

---

### Proof of Concept

A test showing whether an idea can work in principle.

---

### Protocol

The agreed format and rules two devices use to exchange information.

---

### Prototype

A practice or learning version of a design.

Its purpose is to answer questions.

---

### Provisional

Chosen for the current test, but still open to change on evidence.

The opposite of a controlled dimension. Keep provisional values visible, so they are never frozen by accident.

---

### Pulse-Width Modulation (PWM)

Controlling power by switching it on and off very fast and changing how long it stays on.

The motor feels the average, so a longer "on" time means more power.

---

## Q

### Qualitative Data

Descriptive information.

Examples:

- smooth
- noisy
- cracked near hole
- difficult to insert

---

### Quantitative Data

Numerical information.

Examples:

- 0.4 mm movement
- 42 second removal time
- 62 °C temperature

---

## R

### Radial Load

A force acting sideways across a shaft.

---

### Radial Runout

Apparent up-and-down movement of a rotating rim or surface.

A wheel with radial runout bounces once per revolution, even on a flat floor.

---

### Radius

The distance from the centre of a circle to its edge.

```text
Radius = Diameter / 2
```

---

### Raft

A disposable printed platform underneath a model.

---

### Random Error

Unpredictable variation between repeated measurements.

---

### Range

The difference between the largest and smallest values in a set.

---

### Range Check

A controlled test that the radio still works reliably at a stated distance.

Do one before every session - it is how you find a radio problem in the garden instead of at speed.

---

### Reaction Force

A force produced in response to another force.

---

### Reamer

A tool that removes a small amount from an existing hole to bring it to its final size and finish.

---

### Receiver

The module on the buggy that picks up radio commands from the transmitter.

---

### Reduction

A gear arrangement where the output turns fewer times than the input.

Reduction trades speed for turning force. A motor that spins fast and weakly becomes a wheel that turns slowly and strongly.

---

### Reference Dimension

A trusted known dimension used to help interpret other dimensions.

---

### Regression Testing

Repeating earlier tests to check that a change has not broken something that used to pass.

Fixing the steering can quietly break the throttle. Only a repeated test finds that out before the floor does.

---

### Repeatability

Getting similar results when the same person measures the same thing with the same method and tool.

---

### Reproducibility

Getting similar results when something important changes, such as the person, tool or location.

---

### Requirement

A clear, testable statement of what a design must do.

---

### Requirement Traceability

Linking each requirement to the test or inspection used to check it.

---

### Resistance

How strongly something opposes electric current.

---

### Resolution

The smallest change a measuring tool can display or distinguish.

---

### Retain

To stop a part escaping from its intended position.

One of the four fastener jobs. A clip retains a battery; it does not locate or clamp it.

---

### Retention

The method used to prevent a part from moving or escaping.

---

### Reverse Engineering

Learning enough about an existing part to describe it, connect to it, or improve on it.

You are not copying the donor. You are measuring it well enough to design something that fits it.

---

### Revision

A recorded version of a design or drawing.

---

### Revision ID

A label identifying one documented state of a design.

Two parts that fit are usually two parts from the same revision. Write it on the physical part.

---

### Revolution

One complete turn of a rotating part.

---

### Rib

A thin supporting wall added to increase stiffness.

---

### Ride Height

Where the chassis sits when the buggy is resting normally.

---

### Risk

Something uncertain that could cause trouble.

In safety, risk means how likely harm is and how serious it would be. The same hazard can be low risk or high risk depending on the situation.

---

### Rolling Resistance

Resistance that acts against a rolling wheel.

---

### Root Cause

The underlying reason a problem occurred.

---

### Rotational Motion

Turning around a centre.

---

### Rotor

The part of a motor that spins.

---

### Rounding

Reducing a number to a sensible level of detail.

---

### RPM

Revolutions per minute.

A measure of rotational speed.

---

### Running Fit

A fit designed for repeated movement.

---
### Running Mode

The set of rules an ESC follows for forward, braking and reverse.

Forward-and-brake-only suits racing; forward-brake-reverse suits a bashing buggy. Trigger position does not tell you what will happen until you know the mode.

---
### Runout

How far a rotating surface departs from the path it is supposed to follow.

Measured as the difference between the largest and smallest reading during one full turn.

---



## S

### Sacrificial Feature

A cheap, replaceable feature designed to fail first and protect something more valuable.

See also Sacrificial Part.

---

### Sacrificial Part

A cheap, replaceable part intended to fail before a more expensive part.

---

### Safety Factor

Extra load capacity added beyond the expected load.

---

### Safety Requirement

A requirement intended to reduce harm or damage.

---

### Scale

The relationship between drawing size and real size.

Examples:

```text
1:1 = full size
2:1 = twice real size
1:2 = half real size
```

---

### Scope Creep

Uncontrolled growth of project goals.

---

### Seam

The visible line or marks where each layer's wall loops start and finish.

---

### Section View

A drawing view showing internal features using an imaginary cut.

---

### Self-Tapping Screw

A screw designed to form or cut its own thread as it enters a suitable hole.

---

### Sensored

A brushless motor with sensors that report where the rotor is.

Knowing the rotor position lets the ESC start it smoothly from a standstill.

---

### Sensorless

A brushless system that works out the rotor position from the motor's own electrical behaviour.

Fewer wires and cheaper than a sensored system, but starting from a standstill can be less smooth because there is nothing to sense yet.

---

### Series Connection

A connection in a single path, where cell voltages add together.

Two 3.7 V cells in series give 7.4 V.

---

### Service Envelope

The space needed to install, disconnect, inspect or remove a part.

The suitcase analogy again: the case has to fit, and you still need room to open it and grab the handle.

---

### Service Loop

A planned bit of spare wire left at a connection, so it can move or be repaired without pulling on the joint.

---

### Serviceability

How easily a part can be:

- inspected
- removed
- cleaned
- repaired
- replaced

---

### Servo

An actuator that moves to a commanded position and holds it.

---

### Servo Angle

How far the servo's output shaft has rotated.

It is not the same as the wheel angle: the linkage in between changes one into the other.

---

### Servo Horn

The arm or disc bolted to a servo's output spline.

---

### Servo Saver

A part that gives way under a heavy steering knock so the servo does not.

It is a deliberate weak link - cheaper to replace than a servo.

---

### Shear

A load that tries to slide one part of material past another.

---

### Shore Hardness

A scale describing how resistant a soft or rubbery material is to being pressed in.

---

### Short Circuit

An unintended low-resistance path that lets current rush through.

---

### Side View

A view of an object looking from one side, often showing thickness and step heights.

---

### Significant Figures

Digits that meaningfully describe a measurement.

---

### Skeleton CAD

An early model containing only datums, axes, envelopes and interfaces.

Get the relationships right while they are still cheap to move, then add material.

---

### Sketch

A controlled two-dimensional drawing used to create or locate three-dimensional features.

---

### Skirt

A line printed around the model, but not touching it, to start the flow and check the first layer.

---

### Slicer

Software that cuts a 3D model into layers and plans the printer's path and settings.

---

### Sliding Fit

A fit designed for controlled sliding with limited wobble.

---

### Snap Fit

A connection made by temporary elastic bending.

---

### Soft Constraint

A preferred limit that may be negotiable.

---

### Solder

A metal alloy that melts at a low temperature and joins metal surfaces that have been heated properly.

---

### Solder Bridge

Unwanted solder joining two conductors or terminals that should have stayed separate.

---

### Speed

How quickly something moves.

---

### Spring Rate

How much extra force a spring needs for each further millimetre it squashes.

---

### Sprung Mass

The part of the buggy's mass held up by the suspension.

---

### Spur Gear

The larger gear driven by the pinion.

---

### Stage Gate

An evidence check that has to pass before the next commitment is made.

It is what stops a build spending money to find out something a piece of card could have told you.

---

### Stall

A condition where a motor is commanded to turn but cannot.

---

### Stall Current

The large current drawn when an actuator is commanded to move but is held still.

This is the worst case a wire, ESC or battery has to survive.

---

### State of Charge

An estimate of how much charge is left in a battery.

---

### Static Load

A load that changes slowly or remains mostly steady.

---

### Stator

The part of a motor that stays still.

---

### Steering Arm

The short lever on a steering knuckle where the steering link attaches.

Its length decides how much wheel angle you get for a given amount of servo movement.

---

### Steering Axis

The line a wheel knuckle pivots around when you steer.

---

### Steering Centre

The repeatable straight-ahead condition of the whole steering system.

Centre is something you set and check, not something you hope for. A buggy that will not hold centre will not drive straight.

---

### Steering Link

The rod that carries push and pull between the steering parts.

It has to be stiff in both directions, because a rod that flexes turns a clear command into a vague one.

---

### Steering Throw

How far the steering can move across its whole range.

---

### STEP

A neutral file format used to share accurate solid geometry between different CAD programs.

---

### Stiffness

Resistance to bending, stretching, or twisting.

---

### STL

A file format describing a part's outer surface as many small triangles.

It is the usual handover from CAD to slicer.

---

### Strain

The amount a material changes shape compared with its original shape.

This term is introduced here for future use.

---

### Strain Relief

Mechanical support that keeps pulling and repeated bending away from an electrical joint.

---

### Stranded Wire

Wire whose conductor is made from many thin strands, which makes it flexible.

Buggy wiring uses stranded wire because it moves and vibrates.

---

### Strength

The ability of a material or part to withstand stress before failure.

---

### Stress

How concentrated a load is inside a material.

A simple idea is:

```text
Stress = Force / Area
```

---

### Stress Concentration

A small region where stress becomes much higher than in the surrounding material.

Common causes include:

- holes
- sharp corners
- notches
- cracks
- sudden thickness changes

---

### Structural Acceptance

The decision that a printed part is fit for the load-bearing job it was designed for.

A decision made on coupon evidence, not on how solid the part feels in your hand.

---

### Structural Depth

The distance through a beam or folded section that helps it resist bending.

Fold a flat card strip into a U and it barely bends. Same card, same span - the depth did that.

---

### Sub-Assembly

A group of parts joined together that then becomes one part of a larger assembly.

---

### Sub-Trim

A fine transmitter adjustment to a channel's neutral position.

---

### Subsystem

A smaller system inside a larger system.

---

### Support Material

Sacrificial scaffolding printed under overhangs and removed after printing.

---

### Support Path

The route forces follow from the ground through the structure.

---

### Support-Free

Designed to print in the chosen orientation without needing temporary support material.

---

### Surface Radio

A transmitter and receiver system intended for ground or water models.

Not interchangeable with an aircraft system, even where the plugs fit.

---

### Suspension

The system that lets the wheels move up and down over bumps while staying attached to the car.

It keeps the tyres pressed against the ground so the buggy stays controllable.

---

### Suspension Travel

How far a wheel can move up and down relative to the chassis.

---

### Swept Volume

The full space occupied by a part as it moves.

---

### System

A group of parts working together to perform one job.

---

### System Architecture

A high-level view of a system's modules and how they connect.

---

### System Boundary

An imaginary line showing what is inside and outside the system being studied.

---

### Systematic Error

A consistent measurement shift in the same direction.

---

### Systems Thinking

Studying the whole system and the relationships between its parts.

---

## T

### Target

A level of performance you want, which may be traded against another target.

Different from a requirement: a requirement must be met, a target is what you aim at.

---

### Template

A reusable pattern used to transfer the same shape or hole positions onto other parts.

---

### Tension

A pulling load that tries to stretch a part.

---

### Test Coupon

A small printed sample used to test one feature or process.

Examples:

- hole sizes
- peg sizes
- snap tabs
- bearing fits

---

### Test Plan

A written description of:

- what will be tested
- why
- equipment
- procedure
- measurements
- pass condition
- safety precautions

---

### Thermal Protection

An ESC or motor response that cuts power when it gets too hot.

It is evidence, not a fault to reset past. Something is asking more of the system than it can deliver without overheating.

---

### Thermoplastic

Plastic that softens when heated and hardens again when cooled.

---

### Thread

The spiral ridge on a screw, or inside a nut, that pulls parts together as it turns.

---

### Threaded Fit

A connection involving screw threads.

---

### Threadlocker

A liquid applied to suitable threads to stop them shaking loose.

---

### Thread-Locking Product

A chemical used in specified metal threaded joints to resist loosening.

A chemical, so it comes with chemical rules and an adult handles it. Never used on printed plastic threads.

---

### Throttle Calibration

Teaching the ESC which receiver commands mean full forward, neutral and full reverse.

---

### Throttle Limit

A setting or design choice that reduces the maximum motor output that can be commanded.

The single most useful safety setting on a first drive, and the easiest to forget to restore afterwards.

---

### Tie Rod

A link that pushes and pulls between steering parts.

---

### Tinning

Putting a thin coat of solder on a soldering tip, or on the end of a wire, before joining.

---

### Title Block

An information box on an engineering drawing.

It may include:

- part name
- part number
- revision
- material
- scale
- units
- date
- designer

---

### Toe-In

Wheels set so their front edges point slightly towards each other.

---

### Toe-Out

Wheels set so their front edges point slightly away from each other.

---

### Tolerance

The allowed amount a dimension may vary.

---

### Tolerance Stack-Up

Accumulation of dimensional variation across several parts.

---

### Tool Path

The space a tool or moving part travels through.

Keep hands and body parts out of it.

---

### Top Layers

The solid layers that close the upper surfaces of a print.

---

### Top View

An orthographic view looking down on an object.

---

### Topping Out

When suspension reaches the far end of its extension and can droop no further.

The wheel stops following the ground and the buggy goes light. You hear it as a knock over crests. The opposite of bottoming out.

---

### Torque

Twisting force around a centre.

---

### Torque Reaction

The opposite turning effect felt by a motor and its mount when the motor drives a load.

Hold a running drill and feel it twist against your hand. The buggy's motor mount feels the same thing.

---

### Torsion

A twisting load along the length of a part.

---

### Toughness

How much energy and damage a material can absorb before it breaks.

Toughness is not the same as strength: a material can be strong but snap easily.

---

### Traceability

The ability to follow a measurement or design decision back to:

- tool
- method
- date
- revision
- person
- original data

The same idea applies to materials: being able to connect a result back to the
exact filament and settings that produced it.

---

### Track Width

The distance between the stated left and right wheel reference positions.

Manufacturers measure it from different places, so write down which reference you used.

---

### Trade-Off

A benefit gained while accepting a cost somewhere else.

---

### Transform

A change to a model's position, rotation or scale.

---

### Transition Fit

A fit near the boundary between clearance and interference.

---

### Transmitter

The handheld controller that sends your commands to the buggy by radio.

---

### Travel Move

A nozzle movement between places, where nothing should be printed.

---

### Trim

A small adjustment that shifts a channel's neutral point.

Use it when the buggy pulls slightly to one side while you are holding the steering straight.

---
### Tuning

Adjusting a working system to trade one acceptable behaviour for another.

Tuning is not debugging. Debugging fixes something wrong; tuning chooses between two things that both work.

---


## U

### Unilateral Tolerance

A tolerance that allows variation mainly in one direction.

---

### Unit

An agreed amount used for comparison.

Examples:

- millimetre
- kilogram
- second
- degree

---

### Unsprung Mass

The mass that moves with the wheel rather than being carried by the suspension.

Wheels, tyres and hubs are unsprung; keeping them light helps the tyre follow the ground.

---

### Upper Limit

The largest acceptable size allowed by a tolerance.

---

### User Need

Something the user must be able to do or experience.

---

## V

### Validation

Checking that a design works for its real purpose.

---

### Ventilation

Replacing stale or contaminated air with cleaner air.

---

### Verification

Checking that a design meets a stated requirement.

---

### Verification Method

The way evidence is produced: inspection, measurement, demonstration, test or calculation.

Every requirement needs one. A requirement nobody can check is a wish.

---

### Version

A labelled stage of a design.

Example:

```text
V0.1
V0.2
V1.0
```

---

### Visible Line

A solid drawing line showing an edge that can be seen.

---

### Voltage

The electrical push that drives charge around a circuit.

---

## W

### Wall

Two related meanings:

- **In printing:** a solid printed loop around the outside of a layer, or around a hole in it. Also called a perimeter.
- **In part design:** a thin sheet-like region that forms or connects the surfaces of a part.

---

### Warping

Corners of a print curling upward as the plastic cools and shrinks unevenly.

It is worst on large flat parts.

---

### Washer

A thin disc that spreads the load beneath a screw head or nut.

---

### Waste Side

The side of a cut line that is going to be removed.

Always cut on the waste side, so the kerf eats the scrap and not the part.

---

### Watt

The unit of power, written W.

---

### Watt-Hour

A unit of energy, written Wh.

It tells you how much energy a pack holds, which is more useful than capacity alone when comparing packs of different voltages.

---

### Weight

The force created when gravity pulls on mass.

---

### Weight Transfer

A change in how strongly different tyres are pressed against the ground during:

- acceleration
- braking
- turning

---

### Wetting

Molten solder spreading across the metal and bonding to it, instead of balling up on top of it.

---

### Wheel Angle

How far a steered wheel points away from straight ahead.

This is the angle that actually decides where the buggy goes, which is why it is measured at the wheel and not at the servo.

---

### Wheelbase

The distance between the front and rear axle lines.

One of the two numbers that set how the buggy turns; track width is the other.

---

### Wheelspin

A condition where a driven tyre rotates faster than the vehicle moves.

---

### Wheels-Up Test

A powered check with the driven wheels safely raised off the surface.

The buggy cannot run away from you, so a wrong setting is a lesson rather than a chase.

---

### Whole Cost

The full cost of something including delivery, missing items, service parts and adapters.

The cheap donor that needs two adapters and a new set of bearings was not the cheap donor.

---

### Winding

A coil of wire in a motor that becomes a magnet when current flows through it.

---

### Witness Line

A thin visible line that shows where the finished boundary should be while material is being removed.

---

### Workholding

The way a part is secured so it cannot slip, lift, spin or vibrate while being worked on.

---

### Workplane

A flat digital surface on which shapes are placed or sketches are drawn.

---

### Worst-Case Analysis

Checking the most extreme allowed combination of dimensions or conditions.

---

## Z

### Zero Error

A measurement shift caused by a tool not reading zero when it should.

---

# Suggested Maintenance Rules

When adding new terms:

1. Use the same plain-language style.
2. Define the idea before using advanced wording.
3. Keep each definition short.
4. Add an RC buggy example where helpful.
5. Add cross-links only after the topic filenames are stable.
6. Avoid duplicate terms with slightly different wording.
7. Prefer one main definition and note related terms underneath.

---

# Future Expansion

Later parts of the handbook will likely add terms from:

- workshop safety
- soldering
- 3D printing
- slicers
- CAD
- materials
- fasteners
- bearings
- electronics
- batteries
- brushless motors
- steering geometry
- suspension
- radio systems
- testing
- telemetry

---
