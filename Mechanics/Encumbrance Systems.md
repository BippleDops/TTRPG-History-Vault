---
mechanic-name: Encumbrance Systems
type: mechanic
introduced-in: "[[Dungeons & Dragons|Dungeons & Dragons (1974)]]"
popularized-by: "[[Torchbearer|Torchbearer (2013)]]"
used-in:
  - "[[Dungeons & Dragons]]"
  - "[[Pathfinder]]"
  - "[[GURPS]]"
  - "[[Torchbearer]]"
  - "[[Forbidden Lands]]"
  - "[[Blades in the Dark]]"
  - "[[The One Ring]]"
  - "[[Knave]]"
  - "[[Into the Odd]]"
  - "[[Mausritter]]"
design-purpose: "Limits carrying capacity to create resource management decisions, encourage strategic equipment choices, and model physical constraints"
complexity: 2
innovation-score: 3
mechanic-category: "resource-management"
tags:
  - encumbrance
  - carrying-capacity
  - inventory-management
  - weight-limits
  - slot-based-inventory
  - resource-constraints
  - equipment-tracking
  - burden-mechanics
  - inventory-slots
  - gear-management
aliases:
  - Carrying Capacity
  - Inventory Systems
  - Weight Limits
  - Slot-Based Inventory
  - Burden
---

# Encumbrance Systems

## Overview

Encumbrance systems govern how much characters can carry, creating constraints on equipment acquisition and inventory management. These mechanics transform "what gear do I bring?" from trivial question into strategic decision: every item carried has opportunity cost, forcing choices between offensive capability, defensive protection, utility tools, treasure acquisition, and consumable resources. Well-designed encumbrance creates meaningful equipment decisions; poorly designed encumbrance creates tedious bookkeeping that players ignore.

The fundamental purpose of encumbrance is introducing scarcity and consequence to equipment choices. Without carrying limits, optimal play becomes "carry everything possibly useful plus all treasure found." Encumbrance forces trade-offs: heavy armor improves defense but reduces carrying capacity for treasure; bringing ten days' rations ensures survival but limits combat equipment; taking specialized tools enables specific solutions but crowds out general utility.

The design challenge is balancing meaningful constraint with playability. Overly detailed weight tracking (recording 0.1-pound items, calculating encumbrance to the ounce) creates realistic simulation but tedious arithmetic. Overly generous limits eliminate meaningful choices—if everyone can carry everything, why track it? The sweet spot provides enough constraint to create decisions without overwhelming play with bookkeeping.

Modern encumbrance systems span from detailed weight-based calculations to abstract slot-based inventories to complete narrative abstraction. Weight-based systems model realistic physical constraints through pounds or kilograms, rewarding strong characters and creating granular optimization. Slot-based systems abstract items into inventory slots, reducing arithmetic while maintaining capacity constraints. Narrative systems ignore mechanical tracking entirely, relying on fictional plausibility and GM adjudication.

The evolution of encumbrance reflects broader TTRPG design trends: from simulation toward accessibility, from punishment toward interesting choice, and from universal rules toward systems tailored to specific gameplay priorities. Games emphasizing exploration and resource management feature robust encumbrance; games prioritizing combat and story often minimize or eliminate it.

## Historical Development

Encumbrance mechanics evolved from wargaming's transport logistics through increasingly sophisticated attempts to balance realism with playability, eventually diversifying into specialized systems serving different design goals.

**Original D&D (1974)** included weight-based encumbrance inherited from wargaming logistics. Characters had carrying capacity based on Strength, with equipment weight in coin (gold piece) weights. Carrying different weight loads affected movement speed: lightly encumbered moved 12", heavily encumbered moved 6". The system existed but many groups ignored it, finding the arithmetic tedious compared to its gameplay impact.

The coin-weight standard (10 coins = 1 pound) simplified calculations slightly but still required tracking weights of all equipment, weapons, armor, and treasure. Players accumulated hundreds of coins' worth of gear, necessitating constant recalculation as equipment changed. Many tables houseruled simplified or ignored encumbrance entirely.

**AD&D (1st Edition, 1977)** refined weight-based encumbrance with more detailed weight categories and movement rate reductions. The system distinguished between various encumbrance levels (unencumbered, light, moderate, heavy, severe), each reducing movement progressively. Armor weight significantly affected encumbrance, creating trade-off between protection and mobility. However, the system's complexity meant many groups continued ignoring it.

**GURPS (1986)** embraced detailed encumbrance simulation with multiple encumbrance levels based on Strength: No Encumbrance (under ST×2 lbs), Light (ST×4), Medium (ST×6), Heavy (ST×12), Extra-Heavy (ST×20). Each level imposed increasing penalties to movement, dodge, and physical actions. The granular system supported realistic simulation but required careful tracking and frequent recalculation.

**AD&D 2nd Edition (1989)** simplified weight tracking slightly but maintained fundamentally similar system. The persistence of weight-based encumbrance reflected D&D's wargaming heritage and simulationist roots, even as practical play often ignored the rules due to tedium.

**D&D 3rd Edition (2000)** streamlined encumbrance with clearer Strength-based capacity categories (Light load: up to Strength×10 lbs, Medium: ×10-20, Heavy: ×20-30) and explicit penalties for each category (Medium: ×2/3 speed, max Dex +3; Heavy: ×1/2 speed, max Dex +1). The systematization improved clarity but didn't solve tedium. Most groups still ignored encumbrance except when obviously violated (can't carry 1000 pounds of treasure).

The 3rd Edition period saw increasing player focus on character optimization. When tables did track encumbrance, optimizers found ways to maximize carrying capacity (Bags of Holding, Strength buffs, pack animals, Shrink Item spells), turning encumbrance into solvable problem rather than meaningful constraint.

**Torchbearer (2013)** by [[Luke Crane]] and [[Thor Olavsrud]] revolutionized encumbrance with slot-based inventory. Characters had limited inventory slots (determined by class and Strength), with each significant item consuming one slot. Small items bundled into slots (quiver of arrows, bag of coins). The system was simple enough to track constantly while creating meaningful capacity constraints. Every item decision mattered: bringing rope meant leaving something else behind.

Torchbearer made encumbrance central gameplay pillar rather than annoying bookkeeping. The inventory system integrated with resource management, equipment degradation, and the grind mechanic, creating strategic gameplay around gear management. This demonstrated that encumbrance could be engaging when designed as feature rather than simulation obligation.

**Blades in the Dark (2017)** introduced elegant load abstraction. Before scores, players chose load level (Light, Normal, Heavy) affecting mobility without itemizing equipment. During play, players declared what they brought when needed (within reason for chosen load). This retroactive inventory eliminated pre-mission packing tedium while maintaining carrying constraints—heavy load meant capable of bringing anything reasonable but suffering stealth and mobility penalties.

**OSR Revival Games (2010s+)** embraced slot-based encumbrance. Games like **Knave (2018)**, **Into the Odd**, and **Mausritter (2020)** used inventory slots equal to Constitution or similar stat, with meaningful items consuming slots. This simple system was easily understood and consistently tracked, making encumbrance actually functional rather than nominally present but practically ignored.

The OSR slot-based approach recognized that encumbrance works when it's: simple enough to track without tedium, restrictive enough to force meaningful choices, and well-integrated with gameplay (dungeon-crawling, treasure-hauling, resource management).

**Forbidden Lands (2018)** combined slot inventory with degradation mechanics. Characters had limited carry slots with items taking 1-4 slots based on size. Equipment also degraded through use and damage, creating ongoing resource management. The system supported survival-exploration gameplay where equipment decisions mattered constantly.

Contemporary design treats encumbrance as tunable parameter: games prioritizing resource management use robust systems (slot-based for playability), while games prioritizing other pillars minimize or eliminate it. The recognition that encumbrance should serve specific gameplay goals rather than simulate physical reality represents maturation of design thinking.

## How It Works

Encumbrance systems function through several key mechanisms determining carrying capacity, tracking methods, and consequences of overloading:

### Capacity Determination

**Strength-Based Weight Capacity**: Carrying capacity calculated from Strength score, with items having specific weights.

Example: **D&D 5e** - Carrying capacity = Strength score × 15 pounds. Strength 16 = 240 lbs capacity. Encumbered (over Strength × 5) suffers speed reduction. Heavily encumbered (over Strength × 10) suffers speed reduction and disadvantage on physical checks. Exceed capacity = can't move.

**Slot-Based Capacity**: Characters have fixed number of inventory slots, with items consuming slots.

Example: **Knave** - Inventory slots = Constitution score (typically 9-12). Most significant items take 1 slot. Small items bundle (100 coins = 1 slot). Simple, intuitive system creating immediate trade-offs.

Example: **Torchbearer** - Inventory slots based on class and Strength. Items sized as "pack 1," "pack 2," etc. indicating slots consumed. Worn items (armor, clothing) don't take inventory space. Clear, gamified inventory management.

**Attribute-Modified Slots**: Slot capacity determined by physical attributes.

Example: **Mausritter** - Inventory slots = 10 (plus some conditional slots). Tiny mouse characters have appropriately limited capacity. Items drawn on inventory card showing exactly what you're carrying and where.

**Abstract Load Categories**: Players choose general load level rather than itemizing.

Example: **Blades in the Dark** - Choose Light (1 load), Normal (3-5 load), or Heavy (6-8 load) before score. Light gives mobility; Heavy allows bringing more but impairs stealth and movement. Declare what you brought when needed (within load limits).

### Item Sizing

**Precise Weights**: Every item has specific weight in pounds/kilograms.

Example: **D&D 5e** - Longsword 3 lbs, Chain Mail 55 lbs, Rope 10 lbs, Rations 2 lbs per day. Sum all item weights for total carry weight. Requires addition and tracking.

**Slot Consumption**: Items categorized by slot size (1 slot, 2 slots, etc.).

Example: **Torchbearer** - Sword 1 slot, Two-handed weapon 2 slots, Waterskin 1 slot, Sack of Items 1 slot (containing multiple small items). Armor worn doesn't count against inventory. Simple abstraction.

**Bundling**: Small items group into single slot.

Example: **Knave** - 100 coins = 1 slot. Quiver of arrows = 1 slot. Bag of small items = 1 slot. Prevents tedious tracking of minor items while maintaining capacity constraints.

**Worn vs. Carried**: Equipment worn on body (armor, clothing, belt items) may not count or count less than packed items.

Example: **Torchbearer** - Armor, clothing, belt items don't consume pack slots. Encourages wearing useful items rather than packing everything.

### Encumbrance Effects

**Movement Reduction**: Carrying too much reduces movement speed.

Example: **D&D 5e** - Normal speed 30 feet. Encumbered (over Strength × 5 lbs): speed reduced by 10 feet (20 feet). Heavily encumbered (over Strength × 10 lbs): speed reduced by 20 feet (10 feet).

**Action Penalties**: Encumbrance impairs physical actions.

Example: **GURPS Encumbrance** - Medium encumbrance: -1 to Dodge, Move reduced to 0.8×Basic. Heavy encumbrance: -2 Dodge, -2 ST and DX, Move reduced to 0.6×Basic. Severe penalties making encumbrance tactically significant.

Example: **D&D 5e Heavy Encumbrance** - Disadvantage on Strength, Dexterity, Constitution ability checks, attack rolls, and saving throws. Significant combat impairment.

**Binary Limits**: Exceed capacity = can't carry more.

Example: **Slot-based systems** - 10 slots filled = can't carry additional significant items. Must drop something to pick up new item. Clean, clear limitation.

**Push/Drag Rules**: May be able to push/drag more than carrying capacity.

Example: **D&D 5e** - Can push/drag/lift Strength × 30 lbs (double carrying capacity). Allows moving heavy objects short distances without permanent carry.

### Looting and Treasure

**Treasure Has Weight/Slots**: Found wealth consumes carry capacity.

Example: **OSR dungeon-crawling** - 100 coins = 1 slot or 1 lb. Finding 5,000 gold pieces = 50 slots or 50 lbs. Creates meaningful choice: leave treasure or drop equipment to carry more gold.

**Conversion and Transport**: Systems for converting loot to portable form or using transport.

Example: **Gems and jewelry** - Treasure in compact high-value form. 1,000 gp value gem weighs negligible amount. Encourages converting coin hoards to gems.

Example: **Pack animals, carts, hirelings** - External carrying capacity. Mule carries 420 lbs (D&D). Cart holds more but needs roads. Hirelings each carry their own capacity. Creates resource management gameplay around treasure extraction.

## Design Philosophy

Encumbrance system design reflects priorities around realism, resource management gameplay, accessibility, and integration with other systems.

**Simulation vs. Playability**: Weight-based encumbrance models physical reality: objects have mass, humans have finite strength, carrying heavy loads impairs capability. This simulation appeals to realism-focused players and supports grounded gameplay. However, realistic simulation requires arithmetic (summing weights, comparing to capacity, calculating penalties) that many players find tedious.

Slot-based and abstract systems sacrifice realism for playability. A longsword and a crowbar both taking "1 slot" ignores weight differences but creates simple, trackable system. The design question is whether realistic simulation serves gameplay goals enough to justify bookkeeping burden.

**Meaningful Choice vs. Nominal Presence**: Encumbrance only matters when it creates actual decisions. If capacity is so generous that characters rarely approach limits, why track it? Conversely, if limits are so restrictive that characters constantly juggle items, it becomes frustrating busywork.

Good encumbrance design creates meaningful equipment decisions without constant micromanagement: characters must choose between meaningful alternatives (more combat gear or more treasure capacity?), but can carry baseline adventuring gear without agonizing over each piece.

**Resource Management as Gameplay**: Games centered on exploration, dungeon-crawling, and survival benefit from robust encumbrance creating resource management gameplay. Torchbearer makes inventory management central strategic layer: what to bring, what to leave, what to discard when finding treasure. The constraint creates interesting choices supporting the game's dungeon-crawling focus.

Games emphasizing other pillars (combat tactics, social intrigue, story development) may deemphasize or eliminate encumbrance to focus attention elsewhere. D&D 5e's light touch reflects that encumbrance isn't central to heroic fantasy combat gameplay.

**Integration with Other Systems**: Encumbrance works best when integrated with other mechanics rather than isolated. Torchbearer integrates inventory with equipment degradation, resource depletion, and the grind mechanic. Forbidden Lands connects inventory to survival, crafting, and degradation. This integration makes encumbrance feel essential rather than arbitrary.

Isolated encumbrance feels like punishment—you have to track this tedious thing and it only restricts you. Integrated encumbrance feels like gameplay—managing inventory is part of the game's strategic challenge.

**Class and Build Differentiation**: Encumbrance can differentiate character types. Strong characters carry more, creating mechanical incentive for Strength beyond combat effectiveness. Light-armored characters sacrifice protection for mobility and carrying capacity. These trade-offs create character variety and meaningful build choices.

However, encumbrance-based differentiation must balance meaningfully without punishing: low-Strength characters shouldn't be completely gimped, just carrying less than high-Strength equivalents.

**Treasure and Economy**: Dungeon-crawling games use encumbrance to limit treasure extraction, creating "how much gold can we carry out?" strategic questions. Coin weight forces choices: maximize treasure value per weight (convert to gems), bring pack animals, make multiple trips, or leave wealth behind. This supports treasure-focused gameplay where successful adventure means returning rich, not just victorious.

Games without treasure-as-goal often ignore coin weight because it's irrelevant constraint. Modern D&D characters rarely worry about gold weight because wealth isn't primary progression mechanic.

## Variations Across Systems

**D&D 5e Weight-Based**: Carrying capacity = Strength × 15 lbs. Encumbered (Strength × 5 lbs) reduces speed by 10 feet. Heavily encumbered (Strength × 10 lbs) reduces speed by 20 feet and imposes disadvantage on physical checks. Straightforward weight calculation with gentle penalties. Most tables ignore it unless obviously violated because tracking weights is tedious and limits rarely matter given generous capacity.

**Torchbearer Slot Inventory**: Inventory slots based on class and Strength (typically 9-16 slots). Items sized as "pack 1," "pack 2," etc. Small items bundle (waterskin, rope, sack). Worn items don't consume slots. Simple, consistently tracked, creates meaningful choices. Supports the game's resource-management focus where every inventory decision matters during dungeon crawls.

**Blades in the Dark Load**: Players choose load level before scores: Light (1-3 items), Normal (3-5 items), Heavy (6-8 items). Load affects mobility and stealth but doesn't itemize. During score, declare what you brought when needed (within load limits). Elegant abstraction eliminating pre-planning tedium while maintaining carrying constraints. Supports the game's heist focus on action over preparation.

**Knave Slot-Based**: Inventory slots = Constitution score (typically 9-12). Each significant item takes 1 slot. Small items bundle (100 coins = 1 slot). Simple OSR system making encumbrance actually functional. Armor consumes slots based on type (leather 1 slot, chain 2 slots, plate 3 slots), creating defense vs. capacity trade-off. Works because it's simple enough to actually track.

**GURPS Detailed Weight**: Encumbrance levels based on multiples of Strength: No Encumbrance (0 to ST×2 lbs), Light (ST×4), Medium (ST×6), Heavy (ST×12), Extra-Heavy (ST×20). Each level imposes penalties to Move, Dodge, and actions. Granular simulation supporting realistic gameplay but requires careful tracking and calculation. Serves GURPS's simulationist focus.

**Forbidden Lands Slot and Degradation**: Inventory slots based on Strength (typically 10-14 slots). Items sized by slots (1-4 slots). Equipment also has durability that degrades with use and damage. Combined inventory management and equipment degradation creates ongoing resource management. Supports survival-exploration gameplay.

**Mausritter Visual Inventory**: 10 inventory slots plus conditional spaces drawn on character sheet. Players draw items in inventory slots, creating visual representation of gear. Small-scale mouse adventurers carrying tiny items. The visual inventory makes tracking intuitive and clear—you see what you're carrying.

**Into the Odd**: Inventory slots = Strength (typically 10). Each significant item takes 1 slot. Simple OSR approach. Characters can carry beyond capacity but become deprived (can't recover HP). Creates emergency overload option with clear consequence.

**The One Ring Fatigue**: Encumbrance tracked through Fatigue levels rather than weight. Wearing armor, carrying items, traveling increases Fatigue. High Fatigue impairs actions. Abstract system modeling burden's effect rather than calculating weight. Fits the game's journey-focused gameplay.

**Pathfinder 2e Bulk**: Items have Bulk ratings (typically 0-2 Bulk). Light items are L (10 L = 1 Bulk). Carrying capacity based on Strength. Encumbered (over 5 + Str): -10 feet speed, -1 AC/attacks/checks. Maximum (over 10 + Str): can't move. Simplified from precise weight while maintaining granularity.

**Fate Ignored**: Fate Core doesn't track encumbrance mechanically. Narrative plausibility and aspects determine what characters can carry. "Burdened with Treasure" aspect might be compelled for narrative complication. Abstract approach trusting players and GM for reasonable fiction.

## Impact on Play

Encumbrance systems significantly affect gameplay experience, strategic planning, equipment decisions, and play pacing.

**Strategic Equipment Decisions**: Robust encumbrance creates meaningful pre-adventure choices. Torchbearer players carefully plan loadouts: how much food and water, which tools, combat gear vs. utility items. These decisions matter throughout play, creating satisfying strategic layer. Conversely, ignored encumbrance makes equipment selection trivial—bring everything possibly useful.

**Treasure Management**: Dungeon-crawling with limited carrying capacity creates "treasure run" gameplay. After successful delve, party must decide what treasure to prioritize, whether to make multiple trips, hire carriers, or leave wealth behind. This supports the classic adventure structure of delving for treasure and returning rich.

**Loot Anxiety**: Strict encumbrance can create frustrating "inventory Tetris" where players constantly juggle items, drop and pick up gear, and optimize packing. While some enjoy this puzzle, others find it tedious. Good design provides enough capacity for baseline needs while creating meaningful choices around optional equipment and treasure.

**Play Pacing**: Detailed weight tracking slows play as players calculate sums, reference item weights, and recalculate when gear changes. Slot systems speed tracking through simple counting. Abstract systems eliminate tracking almost entirely. The pacing impact depends on how often encumbrance becomes relevant—constant checking slows more than occasional verification.

**Resource Management Culture**: Games with robust encumbrance foster careful resource management. Players track consumables (rations, arrows, torches), plan supplies, and manage degradation. This creates gameplay culture focused on logistics and preparation. Games without encumbrance focus attention on other concerns (tactics, story, character development).

**Class and Build Impact**: When encumbrance matters, Strength becomes valuable beyond combat. Heavy-armor builds sacrifice mobility and carry capacity. Lightly-armed scouts maximize mobility. These trade-offs create meaningful character differentiation. When encumbrance is ignored, these considerations evaporate.

**Realism vs. Heroism**: Strict encumbrance reinforces grounded, gritty gameplay where characters are constrained by physical reality. Ignored or minimal encumbrance supports heroic fantasy where adventurers aren't bothered by mundane concerns. The system communicates tone: realistic simulation or cinematic heroism?

**Buy-In and Enforcement**: Encumbrance only works with table buy-in. Many groups nominally use weight-based systems but never actually calculate unless obvious abuse occurs. This creates inconsistency and rewards system ignorance over honest tracking. Simple systems (slots) more often see actual enforcement because they're trackable without tedium.

**New Player Accessibility**: Complex encumbrance creates learning curve barrier. New players must learn capacity calculation, item weights, and penalties. Slot systems are more intuitive—count to ten, full slots mean full capacity. Abstract systems require minimal learning but depend on group norms about reasonable carrying.

## References

- Gygax, Gary, and Dave Arneson. *Dungeons & Dragons*. 1974.
- Crane, Luke, and Thor Olavsrud. *Torchbearer*. 2013.
- Harper, John. *Blades in the Dark*. 2017.
- Mearls, Mike, and Jeremy Crawford. *Dungeons & Dragons 5th Edition*. 2014.
- Milton, Ben. *Knave*. 2018.
- Nystul, Chris. *Into the Odd*. 2014.

## Related Mechanics

- [[Resource Management]]
- [[Inventory Systems]]
- [[Equipment Degradation]]
- [[Treasure Systems]]
- [[Strength Attributes]]
- [[Movement Systems]]
- [[Looting Mechanics]]

## Games Using This Mechanic

```dataview
TABLE WITHOUT ID
  file.link as "Game",
  year as "Year",
  designer as "Designer"
FROM "Games"
WHERE contains(mechanics, "encumbrance") OR contains(mechanics, "inventory-slots") OR contains(mechanics, "carrying-capacity")
SORT year ASC
```
