---
title: "Glossary"
project: "VoltForge Gear — The Young Engineer's Handbook"
scope: "Seeded from Topics 1.1-2.1, growing with each new topic (currently through Topic 2.9)"
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

### Actual Size

The measured size of a real part.

This may differ slightly from its nominal size.

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

### Anisotropy

A condition where a material behaves differently in different directions.

3D printed parts are often anisotropic because they are built in layers.

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

### Backing Board

Scrap material placed under the work so a drill or knife breaks through into it instead of into the bench.

---

### Baseline Dimensioning

A way of locating several features from one common reference, or datum.

This can reduce accumulated positional error.

---

### Bearing

A component that supports a rotating shaft while reducing friction.

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

### Blind Hole

A hole that stops inside the part instead of passing all the way through.

---

### Boss

A raised pad around a hole or fixing point that adds material where the load goes in.

---

### Bottom Layers

The solid layers that form the base surfaces of a print.

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

### Buckling

Sudden sideways bending of a long, thin part under compression.

---

### Build Plate

The flat surface a 3D print is built on, often heated to help the first layer stick.

Also called the bed.

---

### Build Volume

The space a printer can reach and print inside.

Anything bigger than the build volume has to be split into several parts.

---

### Burr

A rough or sharp edge left behind by cutting, drilling or another process.

---

## C

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

### Chassis

The main structural frame of the buggy.

It supports and connects the other systems.

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

### Cold Joint

A solder joint that never got hot enough, so the solder sat on the metal instead of bonding to it.

Cold joints look dull and lumpy, and often fail later once the buggy starts vibrating.

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

### Continuity

An unbroken electrical path between two points.

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

### Cross-Threading

Thread damage caused by a screw starting crooked and cutting a new, wrong thread.

It damages both the screw and the part, so always start a screw by turning it backwards until it drops into the existing thread.

---

## D

### Datum

A chosen reference point, line, or surface used for measurement or dimensioning.

---

### Deburring

Removing burrs without changing the shape the part is meant to be.

---

### Decimal Place

A digit position to the right of a decimal point.

More decimal places do not automatically mean a more trustworthy measurement.

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

### Divergent Thinking

Producing many possible ideas before judging them.

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

### Ductile

A material behaviour where noticeable bending or stretching happens before failure.

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

### Elastic Deformation

A temporary change in shape that disappears after the load is removed.

---

### Elasticity

How well a material springs back towards its original shape once a load is removed.

---

### Elephant's Foot

Outward spreading of the first printed layer.

It can make printed parts wider at the bottom.

---

### Energy

The ability to do work or cause change.

A battery stores electrical energy.

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

### Exploded View

An assembly view showing parts separated along their assembly direction.

---

### Extruder

The motor mechanism in a 3D printer that grips the filament and pushes it into the hot end.

---

### Extrusion

In CAD, stretching a flat shape in a straight line to add or remove material.

This is a different idea from the printer's extruder, which pushes filament.

---

## F

### False Precision

Reporting more detail than the measurement can justify.

False precision can make weak data look more scientific than it really is.

---

### Fastener

Any part whose job is to hold other parts together: a screw, nut, pin or clip.

---

### Fatigue

Failure caused by repeated loading.

A part may fail from many small load cycles even if one cycle does not break it.

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

### Five Whys

A method of repeatedly asking "why?" to trace a problem back to its root cause.

---

### Flux

A material that cleans hot metal so solder can flow across it and stick.

Most electronics solder has flux built into its core.

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

### Friction

A force that resists movement between surfaces.

Friction can be useful or wasteful.

---

### Front View

An orthographic view chosen to show the most useful front-facing shape of a part.

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

### Impact Load

A force applied very quickly.

Examples:

- crash
- jump landing
- wheel striking a rock

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

## L

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

### Load

A force or combination of forces acting on a part.

---

### Load Path

The route a load follows through a structure or machine.

---

### Locational Fit

A fit used to position one part accurately.

---

### Lower Limit

The smallest acceptable size allowed by a tolerance.

---

## M

### Machine

Something made from parts working together to perform useful work.

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

## N

### Native File

The editable master model saved in the CAD program's own format.

Keep the native file: an exported STL cannot easily be edited back into a design.

---

### Near Miss

An event that could have caused harm but did not.

Near misses are free lessons and should be recorded.

---

### Nominal Size

The named or target size of a part.

The actual measured size may differ.

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

### Outside Diameter

The diameter measured across the outside of a round part.

---

### Overhang

A part of a 3D model that leans out with nothing below it to build on.

Beyond about 45 degrees it usually needs support material.

---

## P

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

### Pilot Hole

A smaller hole drilled first to guide a later, larger one.

---

### Pinion Gear

The small gear attached to the motor shaft.

---

### Pitch

The distance from one thread ridge to the next.

An M3 screw normally has a pitch of 0.5 mm.

---

### Polarity

Which terminal or direction is positive and which is negative.

Getting polarity wrong can destroy electronics instantly.

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

---

### PPE

Personal protective equipment.

Things worn to reduce harm, such as safety glasses and closed shoes.

---

### Precision

How closely repeated measurements agree with one another.

---

### Press Fit

An interference fit assembled using force.

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

### Prototype

A practice or learning version of a design.

Its purpose is to answer questions.

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

### Reaction Force

A force produced in response to another force.

---

### Reamer

A tool that removes a small amount from an existing hole to bring it to its final size and finish.

---

### Reference Dimension

A trusted known dimension used to help interpret other dimensions.

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

### Resolution

The smallest change a measuring tool can display or distinguish.

---

### Retention

The method used to prevent a part from moving or escaping.

---

### Revision

A recorded version of a design or drawing.

---

### Revolution

One complete turn of a rotating part.

---

### Rib

A thin supporting wall added to increase stiffness.

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

### Shear

A load that tries to slide one part of material past another.

---

### Shore Hardness

A scale describing how resistant a soft or rubbery material is to being pressed in.

---

### Side View

A view of an object looking from one side, often showing thickness and step heights.

---

### Significant Figures

Digits that meaningfully describe a measurement.

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

### Spur Gear

The larger gear driven by the pinion.

---

### Static Load

A load that changes slowly or remains mostly steady.

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

### Suspension

The system that lets the wheels move up and down over bumps while staying attached to the car.

It keeps the tyres pressed against the ground so the buggy stays controllable.

---

### Swept Volume

The full space occupied by a part as it moves.

---

### System

A group of parts working together to perform one job.

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

### Torque

Twisting force around a centre.

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

### Trade-Off

A benefit gained while accepting a cost somewhere else.

---

### Transform

A change to a model's position, rotation or scale.

---

### Transition Fit

A fit near the boundary between clearance and interference.

---

### Travel Move

A nozzle movement between places, where nothing should be printed.

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

### Wheelspin

A condition where a driven tyre rotates faster than the vehicle moves.

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
