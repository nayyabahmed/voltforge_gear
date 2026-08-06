---
title: "Part 1 Review Quiz"
part: "Part 1 - Engineering Mindset"
topic: quiz
version: "0.1"
status: "Draft"
difficulty: Beginner
estimated_time: "45-60 minutes, or split across two sittings"
prerequisites:
  - Topic 1.1 - What Are We Building?
  - Topic 1.2 - Systems Thinking
  - Topic 1.3 - How Machines Move
  - Topic 1.4 - Forces and Why Parts Break
  - Topic 1.5 - Measurement
  - Topic 1.6 - Accuracy, Precision and Error
  - Topic 1.7 - Tolerances and Fits
  - Topic 1.8 - Engineering Drawings
  - Topic 1.9 - The Engineering Design Process
  - Part 1 Capstone - First Engineering Challenge
learning_objectives:
  - Check which Part 1 ideas are solid and which need another look.
  - Use wrong answers as a map back to the right topic.
  - Apply several Part 1 ideas together to one realistic problem.
---

# Part 1 Review Quiz

> **"This is not a test you can fail.
> It is a map of what to read again."**

---

# How to Use This Quiz 🧭

Nine topics and a capstone is a lot of engineering. Some of it will have stuck firmly. Some of it will have faded. The only problem would be not knowing which is which - because Part 2 builds directly on all of it.

So this quiz has one job: **tell you where to look again.**

Some rules, and they matter:

- **Nobody is timing you.** Engineering is not a speed sport.
- **Write your answers down** in your notebook rather than thinking them. A thought that felt clear often turns out to be vague when it has to become a sentence.
- **Do not look anything up while answering.** Look everything up afterwards.
- **Every answer carries a topic number.** When you get one wrong, that number is where to go.
- **Getting things wrong here is the cheapest possible place to get them wrong.** Better now than halfway through a build.

There are five parts, and they get harder:

| Part | What it asks | Questions |
| --- | --- | --- |
| A | Do you know the words? | 15 |
| B | Can you explain it? | 10 |
| C | Can you use it? | 8 |
| D | Can you read a failure? | 5 |
| E | Can you put it all together? | 1 |

Mark yourself honestly. "Nearly right" is not right, and spotting that is itself an engineering skill.

---

# Part A - Do You Know the Words? 📖

One sentence each, in your own words. Do not just recite the glossary - if you can only repeat it word for word, you may not have it yet.

1. What is a **system**?
2. What is a **load path**?
3. What is the difference between **strength** and **stiffness**?
4. What is **anisotropy**?
5. What is a **stress concentration**?
6. What is the difference between **accuracy** and **precision**?
7. What is **zero error**?
8. What is a **tolerance**?
9. What is the difference between **nominal size** and **actual size**?
10. What is a **datum**?
11. What is **swept volume**?
12. What is a **packaging envelope**?
13. What is a **constraint**, and how is it different from a requirement?
14. What is an **iteration**?
15. What is **design intent**?

---

# Part B - Can You Explain It? 💬

Two or three sentences each. These are the ideas Part 2 will assume you already have.

16. Why is a pile of correct parts not automatically a working machine?
17. Why does pushing a door near the handle turn it more easily than pushing near the hinge, even with the same force?
18. Why is a folded sheet of card stiffer than a flat one, when it contains exactly the same material?
19. Why does repeating a measurement several times help with random error but not with systematic error?
20. Why can a display showing `0.01 mm` still give you an inaccurate measurement?
21. Why does a hole designed as `5.00 mm` often not fit a 5 mm pin once it is printed?
22. Why should every dimension on a drawing be measured from a datum rather than from the previous feature?
23. Why should the same feature never be dimensioned twice on one drawing?
24. Why should you change only one thing at a time between tests?
25. Why is there no "Finish" box in the engineering design cycle?

---

# Part C - Can You Use It? 🔧

These give you a situation. Say what you would do, and why.

26. You are designing a suspension arm. It will be bent up and down every time the buggy hits a bump. Which way should the printed layers run, and how would you decide?

27. A friend hands you a battery and says "it's 34 mm wide, so make the tray 34 mm". What is wrong with that instruction, and what would you actually measure?

28. You measure the same shaft five times and get 5.02, 5.01, 5.02, 5.44 and 5.01 mm. What do you do about the 5.44, and what would be wrong with simply deleting it?

29. You need a bearing to spin freely in a printed hole. Would you choose a clearance fit, a transition fit or an interference fit - and what would happen if you chose one of the others?

30. You have three ideas for a battery tray and no way to decide between them. Describe how you would choose, without simply picking your favourite.

31. Your cardboard prototype fits perfectly. Name two things this proves, and two things it does not prove at all.

> **[F3 right-versus-wrong array - Figure Q.1: two printed suspension arms shown side by side under the same bending load, layer lines drawn as fine parallel lines in both. In one, the layers run along the length of the arm; in the other they run across it. Both are drawn at the moment the load is applied, with one intact and one cracked along a layer line. The two are deliberately not labelled - the reader has to decide which is which]**
>
> *Figure Q.1 - One of these will survive the bump and one will not. Question 32 asks you which, and why.*
>
> *Alt text: Two printed suspension arms under the same load, one with layers running along its length and one across, one cracked.*

32. Look at Figure Q.1. Which arm was printed in the better orientation, how can you tell, and what does the crack tell you about how the part failed?

33. A drawing says `4 × Ø3.2 THRU`. What does that tell the person making the part, and what does it *not* tell them?

---

# Part D - Can You Read a Failure? 🔍

Reading a failure is the most useful skill in Part 1. Each of these describes something that went wrong. Say what you think happened and what you would check first.

34. A printed bracket snapped cleanly across a flat face, and the break looks smooth and slightly shiny with visible lines running across it. What kind of failure is this, and what would you change?

35. A bracket did not snap. Instead it slowly sagged over three weeks in a sunny window, until the part it was holding no longer lined up. What happened, and why did testing it on the day it was made not catch this?

36. Three spacers are each within `±0.2 mm` of their drawing, and every one passed inspection. Stacked together, the assembly is 0.6 mm too tall. Who is at fault, and what should have been done differently?

37. A part cracked at an inside corner after a few dozen uses, not on the first one. Name the two ideas from Topic 1.4 that together explain this, and one change to the shape that would help.

38. Your buggy switches on and the motor runs, but the wheels do not turn. Using the idea of a motion path, describe how you would find the fault instead of guessing.

---

# Part E - Put It All Together 🏆

39. **The one-question challenge.**

A friend asks you to design a printed mount that holds a small camera on the front of their buggy. They tell you: "It just needs to hold the camera. Make it strong."

Write half a page explaining how you would take that from a sentence to a design you could actually make. You do not have to design the mount - you have to describe the *process*.

A good answer will touch on at least six of these, and will say *why* each one matters rather than just naming it:

- what you would ask them before designing anything
- what you would measure, and how carefully
- what the packaging envelope would have to include beyond the camera itself
- what the interfaces are
- how you would turn "make it strong" into something testable
- which loads the mount will actually see
- how you would decide the print orientation
- what you would prototype first, and what question that prototype would answer
- how you would know when it was finished

---

# Your Revision Map 🗺️

Mark your answers against the key below. Then, instead of adding up a score, do this:

**Write down the topic number beside every question you got wrong or felt unsure about.** Count how many times each topic appears.

| What you find | What it means | What to do |
| --- | --- | --- |
| A topic appears three or more times | That idea has not settled yet | Reread the topic before starting Part 2 |
| A topic appears once or twice | Small gaps, not a problem | Reread just that section |
| Part A wrong but Parts B-D right | You know the ideas, not the labels | Reread the New Words tables only |
| Part A right but Parts C-D wrong | You know the words, not the ideas | Reread the worked examples and activities |
| Part E felt impossible to start | Normal - it is the hardest thing here | Reread Topic 1.9 and the capstone together |

That last row is worth saying plainly. Question 39 asks you to do what an engineer does on the first day of a real project, and finding it hard is not a sign that Part 1 failed. It is a sign that you have found the thing Part 4 exists to teach.

> **☕ Good place to pause.**
> Mark the quiz in one sitting, then leave the revision until tomorrow.
> Reading a topic again straight after getting it wrong tends to feel like
> punishment. Reading it the next day feels like filling a gap.

---

# When You Are Ready for Part 2 ✅

- [ ] I answered every question, in writing, without looking anything up.
- [ ] I marked myself honestly, including the "nearly right" ones.
- [ ] I built my revision map.
- [ ] I reread every topic that appeared three or more times.
- [ ] I attempted Question 39 even though it was hard.
- [ ] I know which single Part 1 idea I am least sure about.

That last box matters most. Knowing where you are weakest is more useful than being strong everywhere, because it tells you what to watch when things go wrong later.

---

# Looking Ahead 🔭

Part 1 taught you how engineers *think*. Part 2 teaches you what engineers *do* with their hands.

**Topic 2.1 - Workshop Safety and Setup** comes first, and it is not a formality. From here on you will be using tools that are hot, sharp or spinning, and the habits you build in that topic are the ones that let everything afterwards be enjoyable rather than frightening.

Everything you have just been quizzed on will turn up again - but next time it will be attached to a real part, on a real bench, in your hands.

---

# Answers 🔑

Each answer carries the topic to revisit if you got it wrong.

## Part A

1. **(1.1)** A group of parts that work together to do one job that none of them could do alone.
2. **(1.4)** The route a force follows through a part or assembly, from where it enters to where it leaves.
3. **(1.4)** Strength is how much load a part takes before it fails. Stiffness is how much it bends before that. A part can be strong but floppy, or stiff but brittle.
4. **(1.4)** A material behaving differently in different directions - like a printed part being weaker between its layers than along them.
5. **(1.4)** A place where stress crowds into a small area, usually a sharp internal corner or a sudden change of section. Cracks start there.
6. **(1.6)** Accuracy is how close a measurement is to the true value. Precision is how closely repeated measurements agree with each other. They are independent.
7. **(1.6)** A tool reading something other than zero when it should - calipers showing 0.03 mm when fully closed. It adds the same error to every reading.
8. **(1.7)** The amount a dimension is allowed to vary and still be acceptable.
9. **(1.7)** Nominal is the name we give the size - a "5 mm" shaft. Actual is what it really measures, which is always slightly different.
10. **(1.7, 1.8)** A reference surface, edge or line that other dimensions are measured from.
11. **(1.5)** The whole space a part passes through as it moves, not just the space it occupies when still.
12. **(1.5)** The component plus all the space around it that the design must leave free - wires and their bends, connectors, fingers, movement, fasteners, tool access and cooling.
13. **(1.2, 1.9)** A constraint is a limit you must work within, such as budget or build volume. A requirement is what the design must achieve. Requirements say what to reach for; constraints say how far you may go.
14. **(1.9)** One trip round the design cycle - a version built, tested and learned from, feeding the next version.
15. **(1.8, 1.9)** The reason the geometry is the way it is: what must stay true when something changes. "This hole stays centred", not "this hole is 30 mm from the left edge".

## Part B

16. **(1.2)** Because a machine is defined by how its parts are connected, not just by which parts exist. The same parts assembled differently do nothing. The connections are part of the design.
17. **(1.3)** Because turning effect depends on distance from the pivot as well as force. The handle gives a long lever arm, so the same push produces far more torque than the same push near the hinge.
18. **(1.4)** Because bending is resisted mostly by material furthest from the centre. Folding moves material away from the middle, so the same amount of material in a better shape is much stiffer.
19. **(1.6)** Random error is as likely to be high as low, so averaging lets it partly cancel. Systematic error shifts every reading the same way, so averaging just gives a reliable average of the same wrong value.
20. **(1.6)** Because resolution is only what the display can show. Accuracy depends on calibration, technique, temperature and the tool's real quality - a badly zeroed caliper displays four decimal places of a wrong number.
21. **(1.7)** Because printed holes come out undersized. The nozzle compresses each perimeter layer, squashing the extruded circle inward, so the finished hole is typically 0.1 to 0.3 mm smaller than drawn.
22. **(1.7, 1.8)** Because measuring each feature from the previous one lets errors accumulate along the chain. From a single datum, each error stays local instead of adding to the next.
23. **(1.8)** Because two dimensions for the same feature can disagree, especially after a revision, and then nobody knows which is correct. Each feature gets one controlling dimension.
24. **(1.9)** Because if two things change and the result improves, you cannot tell which one did it - or whether one helped while the other made things worse.
25. **(0.0, 1.9)** Because every improvement suggests the next question. Testing produces evidence, evidence suggests changes, changes need testing. Engineering produces versions, not finished designs.

## Part C

26. **(1.4)** The layers should run along the arm, so the bending force has to break through solid plastic rather than pull the layers apart. Decide by asking which way the main force acts, then orienting so the layers run along it.
27. **(1.5)** The instruction confuses the component with its envelope, and takes a number on trust. Measure the real battery yourself, in several places, including its wrapper - then add room for the wires and their bend, the connector and fingers, the strap, and clearance to lift it out.
28. **(1.6)** Investigate it - it is an outlier. It may be a slip, a misread or a badly placed tool, or it may be real and tell you the shaft is damaged or tapered at that point. Deleting it without looking throws away the most interesting reading in the set.
29. **(1.7)** A clearance fit, so the bearing can turn freely. A transition fit might grip or might not, so the result would be unpredictable. An interference fit would need forcing in, would probably split the printed part, and would stop the bearing rotating - which is the one thing it exists to do.
30. **(1.9)** Write the requirements first, then score each concept against weighted criteria in a decision matrix, then check the winner against the risks and assumptions. The matrix does not make the decision, but it makes the reasoning visible enough to argue with.
31. **(Capstone)** It proves layout and geometry: sizes, envelope, access, whether interfaces line up and whether a hand can reach. It does not prove anything about strength, stiffness, layer direction, heat resistance or how printed plastic will fail.
32. **(1.4)** The arm with layers running *along* its length is the better orientation. You can tell because the crack in the other one follows a single straight layer line rather than tearing through material. That clean flat break is the signature of layers being pulled apart - a failure caused by orientation, not by the plastic being too weak.
33. **(1.8)** It tells them: four holes, 3.2 mm diameter, passing all the way through. It does not tell them where the holes are, what tolerance applies, what material the part is, which face to measure from, or whether the edges need a chamfer.

## Part D

34. **(1.4)** A brittle failure along a layer line - the smooth face with lines running across it is the giveaway. The part was almost certainly printed in the wrong orientation for its load. Change the orientation so the layers run along the force, and consider a fillet if the break started at a corner.
35. **(1.4)** Creep: slow permanent deformation under a steady load, made much worse by warmth. Testing on day one only shows the immediate response, and creep needs time and temperature. This is why the part brief has to state how long a load is carried and how hot it will get.
36. **(1.6, 1.7)** Nobody is at fault - each part is within tolerance. This is tolerance stack-up, where several small errors point the same way and add. It should have been caught by a worst-case analysis before the parts were made, and the fix is either a tighter tolerance on the parts that matter or a design that does not stack three of them in a row.
37. **(1.4)** Stress concentration and fatigue. The sharp corner crowds the stress into a small area, and repeated loading grows a crack from it a little at a time until the remaining material cannot hold. Add a fillet to that corner so the stress spreads.
38. **(1.3)** Follow the motion path from motor to ground - motor, pinion, spur gear, differential, driveshafts, axles, wheels - and find the first point where movement stops being passed on. Turn things by hand with the power off. That locates the break instead of guessing, and it is faster than replacing parts hopefully.

## Part E

39. **(All of Part 1)** There is no single correct answer, but a strong one moves from vague to testable and explains why at each step. It should include most of:

    - **Ask first:** which camera, how heavy, where exactly on the buggy, does it need to be removable, does it need to aim, what happens in a crash. "Make it strong" is not yet a requirement.
    - **Measure:** the real camera, several times, including its lens housing and cable - not a number from a website.
    - **Envelope:** the camera plus its cable and bend radius, the connector and fingers, any adjustment movement, fasteners, and room for a hand and tool to fit and remove it.
    - **Interfaces:** the chassis it bolts to, the fasteners, the cable route, the camera's own mounting points, and tool access.
    - **Turn "strong" into a test:** for example, "holds the camera with no visible movement when the buggy lands from 200 mm" - a load, a method and a pass condition.
    - **Loads:** mostly vibration and sudden impact from landings and crashes, not steady weight. That points at toughness and fatigue rather than raw stiffness.
    - **Orientation:** layers running along the main bending load, with the mounting face flat on the plate.
    - **Prototype:** cardboard first, to answer "does it fit and can I reach the screws?" - the cheapest question first.
    - **Definition of done:** written before starting, so "finished" is not decided by how tired you are.

    If your answer named the steps but not the reasons, reread Topic 1.9. If it jumped straight to a shape, reread the capstone - that is exactly the habit it exists to break.
