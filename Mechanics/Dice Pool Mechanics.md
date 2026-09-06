---
title: Dice Pool Mechanics
type: mechanic
year-introduced: 1987
first-appearance: "[[Shadowrun (1989)]]"
complexity: 3
popularity: 4
games-using:
  - "[[Shadowrun (1989)]]"
  - "[[Vampire - The Masquerade (1991)]]"
  - "[[Call of Cthulhu (1981)]]"
influenced-by: ["Dice probability theory", "Multiple dice systems"]
influence-on:
  - "Modern narrative dice systems"
  - "Success-counting mechanics"
  - "Opposed roll systems"
tags:
  - mechanic
  - game-design
  - resolution
  - probability
  - dice
category: resolution
---

# Dice Pool Mechanics

**First Appeared In**: [[Shadowrun (1989)]] (popularized), with earlier precedents
**Year**: Late 1980s
**Complexity**: 3/5
**Popularity**: 4/5

## Overview

Dice Pool Mechanics resolve actions by rolling multiple dice simultaneously and counting how many meet or exceed a target number, with the quantity of successful dice determining outcome quality. Unlike single-die systems (roll d20, add modifiers, compare to DC) where one roll produces one binary result, dice pools create graduated success—rolling 8 dice might produce 0, 3, or 7 successes, each representing different outcome degrees. This fundamental shift from binary (success/failure) to graduated (marginal success, solid success, exceptional success) resolution creates nuanced outcomes, natural critical/fumble mechanics through extreme results, and bell curve probability distributions favoring average results over extreme outliers.

The psychological appeal of dice pools is visceral and immediate. Rolling handfuls of dice feels powerful and dramatic—the physical sensation of gathering 10+ dice, the sound of them clattering across the table, the anticipation of counting successes creates tactile engagement that single-die rolls cannot match. This kinesthetic satisfaction partially explains dice pool systems' enduring popularity despite increased mathematical complexity and handling time. Players enjoy rolling dice pools even when statistically equivalent single-die mechanics would resolve faster.

Dice pools solve specific design problems elegantly. They create natural difficulty scaling (more dice = higher skill, higher target number = harder task) without arithmetic—instead of calculating "+5 skill +2 circumstance -3 difficulty," you simply roll your skill dice against task difficulty. They produce bell curve distributions where average results occur most frequently, extreme results rarely, matching intuitive probability expectations better than linear single-die distributions. They enable opposed rolls where both sides roll pools and compare successes, creating symmetrical competitive resolution. And they allow marginal success/failure gradations—barely succeeding feels different than succeeding spectacularly, mechanically not just narratively.

## Historical Context

Single-die mechanics dominated early RPG design. D&D's d20, RuneQuest's d100, and similar systems rolled one die, modified the result, and compared to target numbers. These systems were mathematically simple (linear probability distributions, straightforward calculations) but created binary outcomes and relied on modifiers for difficulty scaling.

The late 1980s saw experimentation with alternative resolution mechanics. Designers recognized limitations in binary success/failure—real-world tasks aren't purely succeed/fail but exist on gradients. A mediocre performance differs meaningfully from exceptional execution, yet single-die systems struggled representing these gradations without complex subsystems.

Shadowrun (1989) popularized dice pool mechanics for mainstream audiences. The cyberpunk-fantasy game needed to represent cyber-enhanced characters whose enhanced reflexes, strength, and perception granted overwhelming advantages over unaugmented humans. Traditional "+2 bonus" modifiers felt insufficient—a character with wired reflexes should feel dramatically faster, not marginally quicker. Dice pools solved this by scaling dice rolled rather than static modifiers. A character with Quickness 3 rolled 3 dice; augmented to Quickness 8, they rolled 8 dice. The difference felt substantial both mechanically (dramatically better success rates) and physically (8 dice feels like much more than 3).

Vampire: The Masquerade (1991) refined dice pools for narrative play. White Wolf's Storyteller System used d10 pools with successes on 7+, creating accessible probability calculations and elegant opposed rolls (both sides roll pools, higher successes wins). The system emphasized character competence through larger dice pools—ancient vampires rolled massive pools representing centuries of experience, mechanically demonstrating their superiority over younger vampires. This power-through-dice-quantity approach influenced supernatural horror and urban fantasy games throughout the 1990s.

The 1990s became "dice pool decade" with numerous systems exploring variations: different die types (d6, d8, d10), varied success thresholds (5+, 6+, 7+), opposed vs. static difficulty, and success/failure gradations. This experimentation established dice pools as a viable alternative to single-die mechanics, with distinct design trade-offs and aesthetic appeals.

The 2000s-2010s saw sophisticated dice pool evolution. Games like Burning Wheel (2002) combined dice pools with complex conflict resolution systems. The One Roll Engine (2001) identified matching dice within pools, creating speed-vs-power trade-offs. Cortex Plus (2010s) used dice pools with multiple die types representing different traits. Genesys/FFG Star Wars (2012) used custom dice with narrative symbols rather than numbers, generating success/failure and advantage/threat simultaneously. These innovations demonstrated dice pools' flexibility and design potential beyond simple success counting.

## Mechanical Function

### Basic Dice Pool Resolution

Standard dice pool resolution follows this pattern:

1. **Determine Pool Size**: Add attribute + skill + modifiers = number of dice
2. **Roll Dice**: Roll all dice simultaneously
3. **Count Successes**: Each die meeting or exceeding target number = 1 success
4. **Compare to Difficulty**: Successes needed vary by task difficulty
5. **Determine Outcome**: Successes determine result quality

**Example (Storyteller System)**:
- Character has Dexterity 3, Firearms 2 = 5 dice
- Shooting at medium range, target number 7
- Roll 5d10: results are 3, 5, 8, 9, 10
- Three dice (8, 9, 10) meet or exceed 7 = 3 successes
- Task required 2 successes = success with 1 extra (potentially better result)

### Difficulty Scaling

Dice pools scale difficulty through two primary methods:

**Target Number Variation**:
- Easy tasks: Successes on 4+ (d10 system) or 2+ (d6 system)
- Average tasks: Successes on 7+ (d10) or 4+ (d6)
- Hard tasks: Successes on 9+ (d10) or 5+ (d6)
- Very hard: Only 10s succeed (d10) or only 6s (d6)

**Success Threshold Variation**:
- Simple tasks: 1 success required
- Standard tasks: 2-3 successes required
- Complex tasks: 5+ successes required
- Extended actions: Accumulate 10+ successes across multiple rolls

**Example**: Hacking a corporate mainframe (hard task) might require target number 8 with 5 successes needed. A skilled hacker with 8 dice averages 2-3 successes per roll, requiring 2-3 rolls to accumulate 5 successes.

### Opposed Rolls

Many dice pool systems use opposed rolls where both parties roll pools and compare:

**Simple Opposition**: Higher success total wins
- Attacker rolls 6 dice, gets 4 successes
- Defender rolls 4 dice, gets 2 successes
- Attacker wins by 2 (margin of success determines effect degree)

**Success Cancellation**: Some systems cancel opposing successes
- Attacker gets 5 successes
- Defender gets 3 successes
- Net result: 2 successes for attacker

**Margin Effects**: Victory margin often determines outcome severity
- Win by 1: Marginal success
- Win by 3+: Solid success
- Win by 5+: Exceptional success

### Critical Success and Failure

Dice pools create natural criticals through extreme results:

**Critical Success**: Rolling maximum values on multiple dice
- Shadowrun: Multiple 6s allow "exploding dice"—re-roll and add
- Storyteller: Rolling multiple 10s grants exceptional success
- Some systems: All dice succeeding = critical success

**Critical Failure**: Rolling minimum values
- Storyteller (classic): More 1s than successes = botch (critical failure)
- Some systems: No successes + multiple 1s = fumble
- Modern variants: Often soften brutal critical failure rules

**Example**: Rolling 8d10 for critical shot
- Results: 10, 10, 10, 9, 8, 6, 3, 2
- Three 10s (maximum) suggests exceptional shot—headshot, vital organ hit, etc.

### Exploding/Open-Ended Dice

Some systems allow re-rolling maximum results:

**Exploding Dice**: Maximum result allows re-roll, adding to original
- Roll d6, get 6 = re-roll and add
- Second roll gets 4 = total of 10 for that die
- Creates unlimited success potential (theoretically)

**Shadowrun Style**: 6s on d6s allow re-rolls
- Roll 6 dice: 6, 6, 5, 4, 3, 2
- Two 6s (target number 5) = 2 successes, plus re-roll 2 dice
- Re-roll: 6, 4 = 1 additional success + 1 more re-roll
- Re-roll: 3 = no additional success
- Total: 3 successes (two original 6s, one re-roll 6, original 5)

This creates exciting "lucky streak" moments where multiple 6s chain into exceptional results.

### Extended Contests

Some challenges require accumulating successes across multiple rolls:

**Extended Actions**: Accumulate X successes over several rolls
- Researching ancient text: Need 15 successes total
- Each roll adds successes toward total
- Failure rolls might add complications or reduce accumulated successes

**Countdowns**: Time limits on extended actions
- Must accumulate successes before time expires
- Creates tension through resource management

**Deteriorating Pools**: Dice pool reduces each roll (fatigue, damage, resource depletion)

### Dice Pool Variations

**Matched Numbers** (One Roll Engine):
- Instead of counting successes, identify matching die results
- Rolling 2d10 and getting 7, 7 = "pair of 7s"
- Width (how many match) = speed/effectiveness
- Height (number matched) = power/quality
- Allows simultaneous resolution of speed and impact

**Mixed Die Sizes** (Cortex):
- Pool contains d4, d6, d8, d10, d12 based on different traits
- Attribute = d8, Skill = d6, Circumstance = d4
- Roll all, take highest two and add
- Creates interesting probability curves and trait significance

**Custom Symbol Dice** (Genesys/FFG Star Wars):
- Dice show success/failure, advantage/threat, triumph/despair symbols
- Count net successes for task outcome
- Count net advantage for additional effects
- Generates two-axis results: "succeed with complications" or "fail with benefits"

## Design Philosophy

### Bell Curve Probability

Unlike d20's linear distribution (each result equally likely), dice pools create bell curves where average results occur most frequently:

**Single d20**: Each number 1-20 has 5% probability (flat distribution)

**Dice Pool (5d10, target 7+)**:
- 0 successes: ~16% probability
- 1 success: ~31% probability
- 2 successes: ~29% probability (most likely)
- 3 successes: ~17% probability
- 4+ successes: ~7% probability combined

This bell curve matches intuitive expectations—competent characters usually achieve moderate success, rarely fail completely, and occasionally perform exceptionally. Extreme results (total failure or incredible success) occur naturally through dice statistics without requiring special critical hit rules.

### Competence Representation

Larger dice pools represent greater competence viscerally:

**3 dice** feels weak, uncertain, risky
**8 dice** feels capable, confident, reliable
**15 dice** feels overwhelming, expert, nearly certain

This physical representation of capability creates psychological satisfaction. Advancing from 4-dice novice to 10-dice master feels significant both mechanically (dramatically better success rates) and physically (visually impressive pile of dice).

### Gradated Success

Dice pools naturally generate success gradations:

- **0 successes**: Failure
- **1 success**: Bare minimum success
- **2-3 successes**: Solid success
- **4-5 successes**: Excellent success
- **6+ successes**: Exceptional success

This allows nuanced outcome narration without complex subsystems. The same roll determines both "did I succeed?" and "how well?" simultaneously.

**Example**: Picking a lock
- 1 success: Lock opens but makes noise, takes time
- 3 successes: Clean, quiet opening
- 5 successes: Opened instantly, without tools, while blindfolded

### Opposed Roll Symmetry

Dice pools excel at opposed contests because both sides use identical mechanics:

**Traditional**: Attacker rolls d20+bonus vs. target's AC
**Dice Pool**: Both sides roll pools, compare successes

This symmetry creates dynamic, interactive resolution where both participants actively roll rather than passive defense values. The psychological engagement of rolling dice (rather than being targeted by someone else's roll) increases player engagement.

### Transparency Through Physical Dice

With single-die systems, probability calculations require mental math. With dice pools, approximate probability is visible:

**Rolling 10 dice against target 7+**: Looking at the pile of 10 dice, players intuitively understand "some will succeed, some won't, probably get 4-5 successes." The physical dice create tangible probability representation.

This transparency demystifies game mathematics, making success likelihood intuitively graspable rather than requiring calculation.

## Evolution Over Time

### Early Dice Pools (1980s)

Early implementations were mechanically crude but conceptually revolutionary:

**Shadowrun (1989)**: d6 pools, exploding 6s, target numbers varying by task difficulty. Often required rolling 10-20+ dice with complex modifiers, creating handling time issues but visceral satisfaction.

**Problems**: Slow resolution with large pools, unclear guidelines for setting difficulties, explosions could chain indefinitely creating outlier results.

### Storyteller System Era (1990s)

White Wolf refined dice pools for mainstream adoption:

**Vampire: The Masquerade (1991)**: d10 pools, standard target number 6 or 7, success counting. Simpler than Shadowrun, more accessible to new players.

**Improvements**: Consistent target numbers, clearer difficulty guidelines, elegant opposed roll mechanics.

**Problems**: Brutal botch mechanics (1s cancel successes; more 1s than successes = botch), creating disproportionate failure rates for large pools.

### New World of Darkness (2004)

Second-generation Storyteller System addressed first edition's problems:

**Refinements**:
- Removed automatic success cancellation from 1s
- Standardized all rolls to target number 8
- Simplified critical success (5+ successes on single roll = exceptional success)
- Created "9-again" and "10-again" mechanics where certain dice re-roll on high results

**Philosophy Shift**: Moved from "rolling large pools is dangerous (more 1s possible)" to "rolling large pools represents competence."

### Burning Wheel (2002) and Complex Interactions

Burning Wheel used d6 pools but integrated with complex conflict resolution systems:

**Innovations**:
- Successes from pools determined "disposition" in extended conflicts
- Opposed pools with complex scripted actions
- Integrated advancement (skills improve through failed rolls)

Demonstrated dice pools could support sophisticated narrative systems beyond simple resolution.

### One Roll Engine (2001)

Wild Talents/Godlike introduced matched-numbers approach:

**Revolutionary Concept**: Instead of counting dice meeting threshold, identify matching numbers
- Roll 5d10: 7, 7, 7, 3, 2
- "Three 7s" = width 3 (speed), height 7 (power)

**Implications**: Single roll generates multiple data points (speed, effectiveness, hit location). Created simultaneous initiative and damage resolution.

### Custom Symbol Dice (2010s)

FFG Star Wars/Genesys introduced narrative symbol dice:

**Innovation**: Dice show symbols (success/failure, advantage/threat, triumph/despair) rather than numbers
- Generate orthogonal results: success with complications, failure with benefits
- Create built-in narrative prompts

**Criticism**: Custom dice requirement limits accessibility, proprietary system prevents easy adaptation.

### Modern Refinements

Contemporary dice pools emphasize:
- Smaller pools (5-8 dice typical, not 20+)
- Clearer difficulty guidelines
- Streamlined opposed rolls
- Reduced handling time through simplified counting
- Integration with narrative mechanics

## Cultural Impact

### Physical Satisfaction

Dice pools created "fistful of dice" aesthetic that defines certain RPG styles. Throwing handfuls of dice became iconic imagery for World of Darkness, Shadowrun, and similar games. This physical satisfaction contributed to these games' popularity despite mechanical complexity.

### Dice Hoarding Culture

Dice pool games encouraged dice collection—players needed dozens or hundreds of dice for optimal play. This created markets for specialty dice, dice bags, and dice accessories, influencing RPG industry economics.

### Mathematical Complexity Acceptance

Dice pools demonstrated players would accept increased mathematical complexity for satisfying gameplay. Counting 8-10 dice requires more effort than reading a single d20, but players embraced this trade-off for graduated success and tactile engagement.

### "Roll All the Dice!"

The phrase and imagery of rolling massive dice pools became celebration of excessive abundance in gaming. Internet memes, actual play shows, and gaming culture celebrated moments where characters rolled 20+ dice, regardless of mechanical necessity.

### Design Space Exploration

Dice pools proved resolution mechanics needn't be binary (succeed/fail) or use single dice, opening design space for innovative systems like symbol dice, matched numbers, and hybrid approaches.

## Strengths and Weaknesses

### Strengths

**Graduated Success**: Natural generation of success degrees without complex subsystems. One roll determines both "did I succeed?" and "how well?"

**Bell Curve Probability**: Average results most likely, extreme results rare, matching intuitive expectations better than linear single-die distributions.

**Physical Satisfaction**: Rolling handfuls of dice feels dramatic, powerful, and engaging. Tactile and auditory feedback creates psychological satisfaction.

**Competence Representation**: Larger pools visually and physically represent greater skill. Advancement from 3-dice novice to 10-dice master feels meaningful.

**Opposed Roll Elegance**: Symmetrical mechanics for opposition where both sides roll rather than passive defense values.

**Natural Criticals**: Extreme results (all successes or all failures) emerge naturally from statistics without requiring special rules.

**Transparent Probability**: Looking at dice pile provides intuitive sense of success likelihood without calculation.

**Scaling Without Modifiers**: Increase capability by adding dice rather than calculating numerical bonuses, reducing arithmetic.

**Margin of Success Built-In**: Success quantity automatically determines effect degree, eliminating separate margin calculations.

### Weaknesses

**Handling Time**: Gathering, rolling, and counting large dice pools slows resolution compared to single-die systems, especially with 10+ dice.

**Mathematical Complexity**: Probability calculations more difficult than single dice. Players struggle estimating success likelihood for specific pool/difficulty combinations.

**Dice Requirements**: Players need dozens to hundreds of dice for games with large pools. Entry barrier for new players; logistical challenge.

**Physical Space**: Large pools require significant table space for rolling, counting, and organizing dice.

**Accessibility**: Counting 12+ dice can challenge players with dyscalculia, vision difficulties, or attention issues.

**Optimal Pool Size Ambiguity**: Unclear when pool becomes "too large"—diminishing returns, handling time issues, balance problems.

**Difficulty Setting Challenges**: GMs struggle calibrating difficulties. "Is this 3 successes or 5 successes?" harder to judge than "DC 15 or DC 20?"

**System Mastery Barriers**: Understanding probability curves requires experience. New players misjudge task difficulties, overestimate or underestimate success chances.

**Variable Swing**: Small pools (3-4 dice) extremely swingy; large pools (15+ dice) extremely consistent. Creates uneven play experience across character power levels.

**Counting Errors**: More dice = more counting mistakes. Players miscounting successes or missing dice frustrates accurate resolution.

## Modern Usage

### Best Practices

Contemporary dice pool implementation wisdom:

**Optimal Pool Size**: Design for 5-10 dice typical pools. Smaller creates excessive randomness; larger creates handling time issues.

**Clear Success Thresholds**: Provide explicit guidelines for success requirements (Simple = 1-2, Standard = 3-4, Hard = 5-6, Very Hard = 7+).

**Limit Maximum Pools**: Cap pools at 12-15 dice through diminishing returns, automatic successes above threshold, or mechanical limits.

**Exploding Dice Carefully**: Unlimited explosions create unpredictable outliers. Consider limiting re-rolls or capping maximum successes.

**Streamline Counting**: Use consistent target numbers (always 5+ on d6, always 8+ on d10) rather than varying thresholds.

**Physical Tools**: Provide dice sorting tools, rolling trays, or counting aids to reduce handling time.

**Alternative Counting**: Consider "success AND" systems where pairs/triplets grant bonuses rather than counting all dice individually.

**Opposed Roll Guidelines**: Clarify margin effects—what does winning by 1 vs. 5 successes mean?

**Difficulty Calibration**: Playtest extensively to establish appropriate success thresholds for various task difficulties.

**Accessibility Options**: Offer alternative resolution for players struggling with large dice pools (roll fewer dice multiple times, use averages, etc.).

### When to Use Dice Pools

Dice pools work best for:

- Games emphasizing competence and mastery (larger pools = clearly better)
- Systems wanting graduated success without subsystems
- Opposed roll-heavy games (competitive contests)
- Settings where tactile dice rolling enhances theme (cyberpunk, gothic horror)
- Groups enjoying physical dice rolling experience
- Games with moderate complexity tolerance

Dice pools may not suit:

- Fast-paced systems prioritizing speed (single die resolves faster)
- Games targeting absolute beginners (single die more intuitive)
- Systems emphasizing random swing over competence
- Groups with accessibility concerns (vision, dyscalculia, motor control)
- Games with limited physical space for rolling/counting
- Systems wanting simple probability calculations

### Hybrid Approaches

Modern games sometimes combine dice pools with other mechanics:

**Mixed Systems**: Pool determines success, separate dice determine other factors (damage, effects, duration)

**Threshold Pools**: Roll pool; if total exceeds threshold, succeed (combines pool bell curve with simple comparison)

**Best-of-Pool**: Roll pool, take highest single die result (combines pool variance reduction with single-die simplicity)

**Step Die Pools**: Pools use increasing die sizes (d4→d6→d8→d10) rather than increasing quantity

## Related Mechanics

**Target Number Systems**: Combined with dice pools to determine success thresholds.

**Opposed Rolls**: Dice pools excel at opposed contests where both sides roll pools.

**Success Counting**: Core mechanic of tallying how many dice meet threshold.

**Exploding Dice**: Re-rolling maximum results for potential unlimited success.

**Critical Success/Failure**: Extreme results triggering special outcomes.

**Extended Contests**: Accumulating successes across multiple rolls for complex tasks.

**One Roll Engine**: Matched numbers variant creating speed/power trade-offs.

**Margin of Success**: Built-in graduated outcomes based on success quantity.

**Bell Curve Distribution**: Statistical probability pattern creating predictable average results.

## References and Analysis

- Dowd, Tom, et al. *Shadowrun* (1st Edition). FASA Corporation, 1989.
  - Popularized dice pool mechanics for mainstream RPGs
- Rein-Hagen, Mark. *Vampire: The Masquerade*. White Wolf Publishing, 1991.
  - Storyteller System refinement of dice pools
- Crane, Luke. *Burning Wheel* (Gold Edition). Burning Wheel Publishing, 2005.
  - Complex dice pool integration with narrative mechanics
- Stolze, Greg and Kenneth Hite. *Unknown Armies* (2nd Edition). Atlas Games, 2002.
  - One Roll Engine matched-numbers innovation
- Watson, Sam, et al. *World of Darkness* (New World of Darkness). White Wolf, 2004.
  - Second-generation Storyteller System refinements
- FFG Star Wars RPG design team. *Star Wars: Edge of the Empire*. Fantasy Flight Games, 2012.
  - Custom narrative symbol dice pools
- Various probability analysis articles on dice pool mathematics
- Gaming community discussions on optimal pool sizes and counting methods

## Games Using This Mechanic

```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System"
FROM "Games"
WHERE contains(file.content, "dice pool") OR contains(file.content, "Dice Pool") OR contains(system, "Storyteller") OR contains(system, "d6 pool") OR contains(system, "d10 pool")
SORT year-published ASC
```
