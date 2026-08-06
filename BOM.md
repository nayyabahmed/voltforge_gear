---
title: "Bill of Materials (BOM)"
project: "VoltForge Gear — The Young Engineer's Handbook"
version: "0.2"
status: "Reviewed (stages populated from Topics 4.1-4.10; quantities and prices are yours to fill in)"
feeds_from: "Topics 3.1-3.10, 4.1-4.10"
---

# Bill of Materials

Every part the buggy project uses, in one place. Topic 4.1 teaches you to keep
this; this file is where you keep it. See the matching
[COST-LEDGER.md](COST-LEDGER.md) for what was actually spent.

> **This is a template, not a shopping list.** The rows below are what each
> stage *needs*, taken from the Part 4 topics. The exact model, quantity and
> price depend on your donor, your printer and what you already own - which is
> the whole point of Topic 4.6. Fill in the blanks as you go, and never let a
> blank quietly become a guess.

Per our guiding principles, every item is categorised so the trade-offs stay
visible:

| Category | Meaning |
|---|---|
| required-now | Needed for the current build stage |
| required-later | Known future need - do not buy yet |
| optional | Nice to have, not needed to progress |
| reusable | Carries over between versions and stages |
| donor | Comes from a donor platform |
| printable | We make this part ourselves |
| consumable | Gets used up (filament, solder, tape) |

**The stage gate rule (Topic 4.1):** nothing in a later stage is bought until
the current stage's evidence passes. A row marked `required-later` is a
decision already made and deliberately not yet acted on.

---

## Stage 1 - Layout and Rolling Mock-Up (Topics 4.2-4.3)

Target spend: **£0.** If this stage costs money, something has gone wrong.

| Item | Qty | Category | Est. cost | Status | Notes |
|---|---|---|---|---|---|
| Corrugated cardboard | - | consumable | free | | Packaging boxes work fine |
| Large paper or lining paper | - | consumable | free/low | | For the full-size packaging board |
| Wooden skewers or straight rods | 1 pack | consumable | low | | Axles. Trim and cover the points |
| Straws or paper tubes | few | consumable | free | | Simple bushes |
| Bottle tops or similar wheels | 4+ | reusable | free | | Matched diameters matter more than looks |
| Tape, glue, string | - | consumable | free/low | | |
| Coins or washers | - | reusable | free | | Temporary mass for load tests |
| Ruler, square, pencil | - | reusable | owned | | From Topic 1.5 |

## Stage 2 - Low-Power Wire-Frame Car (Topic 4.4)

The first stage that costs anything. Buy only what you do not already have.

| Item | Qty | Category | Est. cost | Status | Notes |
|---|---|---|---|---|---|
| Low-voltage motor, known specification | 1 | required-now | low | | Stated voltage range required - see Topic 3.7 |
| Switched battery holder | 1 | required-now | low | | Switch must be immediately reachable |
| Cells, matched set | 1 set | consumable | low | | **Never mix old and new, or mix chemistries** |
| Prewired lead set or safe connectors | 1 | required-now | low | | |
| Pulleys, elastic bands or friction wheel | - | consumable | free/low | | Drive method per Topic 4.4 |
| Stage 1 chassis and wheels | 1 | reusable | £0 | | Carried forward |

**Not yet:** the final brushless system. That decision belongs to Topic 4.7
onwards and is locked until this stage passes.

## Stage 3 - Radio-Controlled Prototype (Topic 4.5)

Buy only the missing parts of **one approved complete control path**. Mixing
parts of two paths needs a new compatibility review first (Topic 3.1's eight
checks).

| Item | Qty | Category | Est. cost | Status | Notes |
|---|---|---|---|---|---|
| Surface radio set (transmitter + receiver) | 1 | required-now | medium | | Topic 3.4. Protocol compatibility, not just band |
| Steering servo | 1 | required-now | low/medium | | Topic 3.5. Compare torque and speed at the SAME voltage |
| ESC suited to the motor type | 1 | required-now | low/medium | | Topic 3.6. Brushed and brushless are not interchangeable |
| Battery suited to the ESC | 1 | required-now | medium | | Topic 3.3. Chemistry, cell count and connector all checked |
| Compatible charger | 1 | required-now | medium | | Balance charging if LiPo |
| LiPo safety bag or approved container | 1 | required-now | low | | **Not optional if the pack is LiPo** |
| Stage 2 chassis and drive | 1 | reusable | £0 | | Where compatible |

## Stage 4 - Donor Parts (Topic 4.6)

Buy precision, build structure. The donor supplies what you cannot make.

| Item | Qty | Category | Est. cost | Status | Notes |
|---|---|---|---|---|---|
| Donor model or module | 1 | required-now | varies | | Only one that passes the written gate |
| Drivetrain, differential, gearbox | - | donor | included | | |
| Hubs, shafts, bearings, wheel hexes | - | donor | included | | The parts a printer cannot make well |
| Steering knuckles, arms, hinge pins | - | donor | included | | |
| Shocks and springs | - | donor | included | | |
| Wheels and tyres | - | donor | included | | Where suitable |
| Service parts | - | required-later | varies | | **Only after inspection confirms the need** |

Record the **whole cost** (Topic 4.6): purchase, delivery, missing items,
service parts and adapters. A cheap donor needing two adapters was not cheap.

## Stage 5 - Modular Printed Chassis (Topic 4.7)

| Item | Qty | Category | Est. cost | Status | Notes |
|---|---|---|---|---|---|
| Filament, known brand and type | 1 kg | consumable | medium | | Enough for coupons AND modules. Topic 2.6 |
| Standard fasteners, washers, nuts | - | required-now | low | | M3 mostly. See TOOLS.md |
| Heat-set inserts | - | optional | low | | Only where a joint is opened repeatedly |
| Chassis core, adapters, trays | - | printable | filament | | |
| Coupon ladders | - | printable | filament | | Printed BEFORE the chassis, always |

**Not yet:** exotic filament. Topic 4.7 is explicit that unusual material
never compensates for untested geometry.

## Stage 6 - Assembly and Installation (Topics 4.8-4.9)

| Item | Qty | Category | Est. cost | Status | Notes |
|---|---|---|---|---|---|
| Correct standard fasteners | - | required-now | low | | Length checked against the whole stack |
| Washers, lock nuts | - | required-now | low | | |
| Specified bearings or service parts | - | required-now | low/medium | | Only those the manual confirms |
| Approved lubricant | - | optional | low | | Only where the manual specifies |
| Thread-locking product | 1 | optional | low | | **Adult handles it.** Only where specified |
| Battery strap or retainer | 1 | required-now | low | | Two independent retention ideas |
| Wire sleeve, grommets, cable guides | - | required-now | low | | Abrasion protection, Topic 4.9 |
| Connectors, if the approved system lacks them | - | required-now | low | | |

## Stage 7 - Version 1 Testing (Topic 4.10)

| Item | Qty | Category | Est. cost | Status | Notes |
|---|---|---|---|---|---|
| Spare fasteners | - | consumable | low | | Things vibrate loose. They always do |
| Tape measure or marked test lane | 1 | reusable | owned | | Stopping-distance measurement |
| Timer or stopwatch | 1 | reusable | owned | | A phone is fine |
| Result sheets | - | printable | free | | |

**Not yet:** upgrades. Topic 4.10 tests what you built; Part 5 is where the
evidence decides what is worth changing.

---

## Maintenance Rules

1. Add items when their topic is written, even before buying.
2. Never delete a row - mark it "replaced" or "not purchased" instead.
3. Each purchase gets a matching entry in [COST-LEDGER.md](COST-LEDGER.md).
4. Keep the "buy precision, build structure" rule in mind before adding a
   printable alternative to a precision part (see
   [the guiding principles](style-guides-principles/GUIDING-PRINCIPLES.md)).
   Topic 4.7 names the parts never to print merely to save money: battery
   components, gears, high-speed shafts and wheel hubs.
5. A blank in the cost column is honest. A guessed number written as if
   measured is not - mark estimates as estimates.
