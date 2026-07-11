---
title: "Glossary"
project: "RC Buggy Engineering Handbook"
scope: "Seeded from Chapters 01-10, growing with each new chapter (currently through Chapter 11)"
version: "0.1"
status: "Draft (living document)"
---

# Glossary

This glossary collects the engineering terms introduced in the chapters written so far.

It is a living document. New terms should be added as later chapters are written.

Terms are listed alphabetically.

---

## A

### Acceleration

A change in speed or direction.

A buggy accelerates when it speeds up, slows down, or turns.

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

### Baseline Dimensioning

A way of locating several features from one common reference, or datum.

This can reduce accumulated positional error.

---

### Bearing

A component that supports a rotating shaft while reducing friction.

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

## C

### CAD

Computer-Aided Design.

Software used to create precise 2D drawings and 3D models.

---

### Calibration

Comparing a measuring tool with a trusted reference.

Calibration helps identify or correct measurement bias.

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

### Compensation

A deliberate CAD or slicer adjustment used to achieve the desired real printed size.

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

### Constraint

A limit within which a design must work.

Examples:

- budget
- printer size
- available tools
- chosen battery
- build time

---

### Control Variable

A factor kept the same during a fair test.

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

### Critical Dimension

A dimension that strongly affects fit, function, or safety.

---

### Cross-Check

Checking a result using a second method.

---

## D

### Datum

A chosen reference point, line, or surface used for measurement or dimensioning.

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

### Dimension

A numerical description of a feature's size or location.

---

### Divergent Thinking

Producing many possible ideas before judging them.

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

### Driveshaft

A shaft that carries rotation and torque from one place to another.

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

### Elephant's Foot

Outward spreading of the first printed layer.

It can make printed parts wider at the bottom.

---

### Energy

The ability to do work or cause change.

A battery stores electrical energy.

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

### Engineer

Someone who designs, tests, improves, and understands how things work.

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

## F

### Fatigue

Failure caused by repeated loading.

A part may fail from many small load cycles even if one cycle does not break it.

---

### FDM (Fused Deposition Modelling)

A 3D printing method that melts plastic filament and lays it down in fused layers.

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

### Fit

The relationship between two connected parts.

---

### Fit Library

A record of tested dimensions and the real fits they produced.

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

### Isometric View

A 3D-looking drawing view showing several faces at once.

---

### Iteration

One pass through the design-build-test-improve cycle.

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

### Mass

The amount of matter in an object.

Usually measured in grams or kilograms.

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

## O

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

### Part Number

A unique identifier assigned to a part.

---

### Peer Review

A review performed by another person.

---

### Performance Requirement

A requirement describing how well a function must be performed.

---

### Permanent Deformation

A shape change that remains after the load is removed.

---

### Pinion Gear

The small gear attached to the motor shaft.

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

### Random Error

Unpredictable variation between repeated measurements.

---

### Range

The difference between the largest and smallest values in a set.

---

### Reaction Force

A force produced in response to another force.

---

### Reference Dimension

A trusted known dimension used to help interpret other dimensions.

---

### Repeatability

Getting similar results when the same person measures the same thing with the same method and tool.

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

### Section View

A drawing view showing internal features using an imaginary cut.

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

### Significant Figures

Digits that meaningfully describe a measurement.

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

### Speed

How quickly something moves.

---

### Spur Gear

The larger gear driven by the pinion.

---

### Static Load

A load that changes slowly or remains mostly steady.

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

### Threaded Fit

A connection involving screw threads.

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

### Top View

An orthographic view looking down on an object.

---

### Torque

Twisting force around a centre.

---

### Torsion

A twisting load along the length of a part.

---

### Traceability

The ability to follow a measurement or design decision back to:

- tool
- method
- date
- revision
- person
- original data

---

### Trade-Off

A benefit gained while accepting a cost somewhere else.

---

### Transition Fit

A fit near the boundary between clearance and interference.

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

### Warping

Corners of a print curling upward as the plastic cools and shrinks unevenly.

It is worst on large flat parts.

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

### Wheelspin

A condition where a driven tyre rotates faster than the vehicle moves.

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
5. Add cross-links only after the chapter filenames are stable.
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
