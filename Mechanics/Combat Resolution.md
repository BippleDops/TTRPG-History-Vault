---
type: mechanic
mechanic-name: Combat Resolution
first-appearance: "[[Dungeons & Dragons (1974)]]"
year-introduced: 1974
introduced-in: "[[Dungeons & Dragons (1974)]]"
games-using:
  - "[[Dungeons & Dragons (1974)]]"
  - "[[Advanced Dungeons & Dragons (1977)]]"
  - "[[Dungeons & Dragons Third Edition (2000)]]"
  - "[[Dungeons & Dragons Fifth Edition (2014)]]"
complexity: 3
popularity: 5
purpose: "Determine whether attacks hit and damage dealt in combat situations"
historical-significance:
  - "Evolved from wargaming combat tables"
  - "THAC0 became infamous for counterintuitive complexity"
  - "Ascending AC revolutionized attack resolution clarity"
  - "Advantage/disadvantage simplified modifier mathematics"
  - "Core mechanic defining tactical combat experience"
innovation-score: 4
tags:
  - mechanic
  - game-design
  - combat
  - resolution
  - probability
category: combat
---

# Combat Resolution

**First Appeared In**: [[Dungeons & Dragons (1974)]]
**Year**: 1974
**Complexity**: 3/5
**Popularity**: 5/5
**Innovation Score**: 4/4

## Definition

Combat resolution systems are mechanical frameworks determining whether attacks succeed and what damage they inflict during conflicts. These systems transform narrative descriptions of combat into discrete mechanical outcomes through dice rolls, modifiers, and mathematical comparisons. Combat resolution answers three fundamental questions: Does the attack hit the target? How much damage does it deal? What mechanical effects result? This framework converts chaotic violence into structured gameplay where players can make meaningful tactical decisions based on probability, character capabilities, and situational factors.

The combat resolution system forms the mechanical heart of most traditional RPGs. Since combat consumes significant play time and presents life-or-death stakes, the resolution mechanic must balance competing concerns: realism versus playability, speed versus depth, randomness versus skill, accessibility versus tactical complexity. Different games prioritize these factors differently—quick skirmish games favor speed and simplicity, while tactical combat games favor depth and complexity, while narrative games may abstract combat entirely to maintain story focus.

## Historical Development

### Attack Matrices and Tables: Original D&D (1974)

Original D&D inherited combat resolution from *Chainmail* wargaming rules using attack matrices—large tables cross-referencing attacker type with defender Armor Class to determine required d20 roll. Each character class and level had table row; each AC value had column; intersection showed target number needed on d20 to hit.

**Example Attack Matrix**:
```
Fighter Level | AC 2 | AC 4 | AC 6 | AC 8
Level 1       |  19  |  17  |  15  |  13
Level 4       |  16  |  14  |  12  |  10
Level 7       |  13  |  11  |   9  |   7
```

To resolve attack: Find your class and level row, find target's AC column, cross-reference for target number, roll d20 and meet or exceed that number. This system had several notable features:

**Descending Armor Class**: AC 9 (unarmored) was worst; AC 2 (plate armor) was excellent; AC -3 (magical plate + shield + bonuses) was superhuman. Lower AC meant better armor—counterintuitive but inherited from wargaming conventions.

**Level-Based Attack Progression**: Higher-level fighters needed lower rolls to hit same AC, representing improved combat skill. This created satisfying advancement—hitting reliably felt like mastery.

**Class Differentiation**: Fighters improved attack rates fastest; clerics improved moderately; magic-users barely improved. This reinforced class roles and combat specializations.

The system worked but had problems. Tables required constant reference—players couldn't internalize cross-referenced values. Looking up values every attack slowed play significantly. The descending AC confused new players expecting "higher is better" convention. These issues became increasingly frustrating as D&D grew beyond wargaming enthusiasts.

### THAC0: AD&D's Infamous Innovation (1977-1989)

Advanced D&D 1st Edition introduced infamous THAC0 (To Hit Armor Class 0, pronounced "THACK-oh")—mathematical formula replacing attack matrix lookups. Instead of tables, each character had single THAC0 number representing d20 roll needed to hit AC 0. To resolve attacks:

**THAC0 Formula**: Roll 1d20, add modifiers, compare to (THAC0 - Target AC)

**Example**: Fighter with THAC0 15 attacking AC 2 enemy:
- Target number = 15 - 2 = 13
- Roll d20, add modifiers
- If total ≥ 13, attack hits

THAC0 eliminated table lookups through single calculation. However, the counterintuitive mathematics confused players:
- Lower THAC0 was better (needed lower rolls)
- Lower AC was better (made enemies' THAC0 less effective)
- Subtracting AC from THAC0 meant better armor (lower AC) made target number higher
- Negative ACs created double-negative confusion (THAC0 15 vs AC -3 = target 18)

The system became notorious for requiring explanation to every new player and causing persistent confusion even among veterans. "THAC0" entered gaming vocabulary as shorthand for unnecessarily complex mechanics. Despite mathematical efficiency, the counterintuitive nature made THAC0 one of AD&D's most criticized features.

AD&D 2nd Edition (1989) kept THAC0 but attempted better explanation. The community developed alternative THAC0 explanations, house rules converting to ascending AC, and simplified calculation methods. The design community increasingly recognized that mathematical elegance didn't guarantee usability.

### Ascending AC Revolution: D&D 3rd Edition (2000)

D&D 3rd Edition revolutionized combat resolution by inverting Armor Class to ascending values and creating unified d20 resolution:

**Ascending AC Mechanics**:
- AC 10 = unarmored (baseline)
- AC 15 = leather armor + Dex
- AC 20 = plate armor + shield
- AC 25+ = magical armor + bonuses
- Higher AC is better (intuitive)

**Unified Attack Resolution**:
1. Roll 1d20
2. Add attack bonus (Base Attack Bonus + Strength/Dexterity + magic + situational)
3. Compare total to target AC
4. If total ≥ AC, attack hits

This elegant inversion solved THAC0's problems:
- **Intuitive Comparison**: Higher roll beats higher AC—straightforward
- **Unified Mechanic**: Same roll+modifier≥target structure as skill checks and saves
- **No Subtraction**: Pure addition—faster mental math
- **Positive Bonuses**: All modifiers add rather than subtract
- **Scales Clearly**: Bigger numbers obviously better

The 3rd Edition innovation was so successful that it became permanent baseline. Fourth Edition and Fifth Edition retained ascending AC with minimal changes. The elegance of "roll high, add bonuses, beat target" proved ideal balance of simplicity and functionality.

### Advantage/Disadvantage: 5th Edition Streamlining (2014)

D&D 5th Edition introduced advantage/disadvantage replacing most numerical modifiers:

**Traditional System** (3E): Roll 1d20 + 2 (flanking) + 1 (high ground) + 2 (Bless) + 1 (magic weapon) = 1d20+6

**Advantage System** (5E): Roll 2d20, take higher result—done

Instead of calculating cumulative bonuses, favorable circumstances granted advantage (roll two d20s, take higher). Unfavorable circumstances granted disadvantage (roll two d20s, take lower). This dramatically simplified combat:

- No modifier arithmetic during combat
- DM simply determines: advantage, disadvantage, or neither
- Multiple sources don't stack—binary state
- Advantage and disadvantage cancel regardless of quantities

The system sacrificed granularity (all bonuses become equivalent "advantage") for speed and elegance. Mathematical analysis showed advantage roughly equals +4-5 bonus, making it comparable to previous editions' typical modifiers while eliminating calculation overhead.

### Opposed Rolls: Contested Actions

Many games moved from roll-vs-static-target to opposed rolls where both sides roll and compare:

**Static Target** (D&D): Attacker rolls vs defender's AC (static number)

**Opposed Roll** (many systems): Attacker rolls vs defender's roll, highest wins

**Example** (*Burning Wheel*): Attacker rolls attack skill vs defender's defense skill, comparing successes

Opposed rolls create dramatic tension—both sides roll, both sides affect outcome, neither is passive. However, they double rolling overhead and increase randomness. Modern games carefully choose when opposed rolls create better experience than static targets.

### Success Counting: Dice Pools

Many non-D&D systems use dice pool success counting:

**World of Darkness**: Roll pool of d10s equal to (Attribute + Skill), count dice meeting target number (typically 8+). Compare success count to difficulty.

**Shadowrun**: Roll d6 pool, count 5s and 6s as successes. Opposed rolls compare success totals.

**Genesys/FFG Star Wars**: Roll custom dice with success/failure/advantage/threat symbols, cancel opposites, interpret net results.

These systems create different probability curves and narrative outcomes than single d20 roll, supporting different play experiences. Success counting allows partial success and narrative complications impossible with binary hit/miss.

## Mechanical Implementation

### Core Resolution Frameworks

**Roll vs Static Target** (D&D 3E/5E):
1. Roll die/dice
2. Add relevant modifiers
3. Compare total to static target (AC, DC)
4. Meet or exceed = success

**Roll vs Opposed Roll**:
1. Both parties roll
2. Add relevant modifiers
3. Compare totals
4. Highest wins (ties favor defender usually)

**Dice Pool Success Counting**:
1. Assemble dice pool based on attributes/skills
2. Roll pool
3. Count successes (dice meeting threshold)
4. Compare success count to difficulty or opposed successes

**Roll Under Target**:
1. Roll die/dice
2. Compare to static attribute/skill rating
3. Roll equal-to or under = success
4. Used in BRP, GURPS, others

### Attack Bonus Construction

**D&D 3E/5E Formula**:
Attack Bonus = Base Attack Bonus + Ability Modifier + Proficiency + Magic + Situational

**Example 5E 5th-level Fighter**:
- Proficiency: +3
- Strength: +3
- Magic weapon: +1
- Total: +7 attack bonus

**Factors**:
- **Base/Proficiency**: Increases with level
- **Ability Modifier**: Str for melee, Dex for ranged
- **Proficiency**: Trained vs untrained weapons
- **Magic**: Weapon enchantments
- **Situational**: Cover, flanking, advantage/disadvantage

### Armor Class Construction

**5E Formula**:
AC = 10 + Armor Bonus + Dexterity Modifier + Shield + Magic + Situational

**Example** (Fighter in Plate + Shield):
- Base: 10
- Plate armor: +8
- Shield: +2
- Magic: +1
- Total: AC 21

**Factors**:
- **Armor**: Type determines bonus (leather +1, chain +4, plate +8)
- **Dexterity**: Natural agility (some armor limits Dex bonus)
- **Shield**: +2 typically
- **Magic**: Enchanted armor/shields
- **Situational**: Cover, spells, conditions

### Damage Resolution

**Basic Process**:
1. Attack hits
2. Roll weapon damage dice
3. Add relevant modifiers (Str/Dex, magic, features)
4. Subtract from target HP
5. Apply any special effects

**Critical Hits**:
- Natural 20 on d20 = critical hit
- Roll damage dice twice (5E) or multiply by factor (3E)
- Automatic hit regardless of AC
- Creates dramatic moments

**Damage Types**:
- Physical: Slashing, piercing, bludgeoning
- Energy: Fire, cold, lightning, acid, thunder
- Special: Force, psychic, radiant, necrotic, poison
- Resistance/immunity/vulnerability modify damage taken

## Design Philosophy

### Binary Success vs Degrees

Traditional D&D uses binary hit/miss—attacks succeed completely or fail completely. Alternative systems use success degrees:

**Margin of Success** (many systems): Amount by which you exceed target determines effect quality. Beat by 5+ means better outcome.

**Success Levels** (FATE, Genesys): Multiple success thresholds create gradual outcomes from failure to critical success.

Binary is faster and clearer. Degrees create narrative richness and reduce all-or-nothing randomness. Design choice depends on desired complexity and narrative style.

### Whiff Factor: Missing Every Attack

D&D's binary hit/miss creates "whiff factor"—combat rounds where nothing happens because all attacks miss. This frustrates players feeling ineffective. Solutions include:

**4E Approach**: Ensure every power does something (damage on miss, conditions on hit)
**13th Age Escalation**: Cumulative attack bonus each round reducing miss chances
**PbtA Approach**: Partial success on mixed results—never total failure
**Narrative Reframing**: Misses aren't incompetence but effective defense

### Bounded Accuracy: 5E Innovation

5th Edition introduced "bounded accuracy"—limiting AC and attack bonus progression so d20 roll always matters. Compare to 3E where high-level characters had +30 bonuses vs AC 40, making rolls nearly irrelevant.

**5E Bounded Numbers**:
- Attack bonuses rarely exceed +11-13
- ACs rarely exceed 19-21
- Low-level threats remain somewhat dangerous
- High-level characters can still miss
- Lucky goblins can hit legendary heroes

This flattens power curve, keeps d20 relevant, and prevents mathematical escalation requiring increasingly complex bonuses. Critics argue it reduces advancement satisfaction; proponents argue it maintains tension and simplifies math.

### Hit Points as Abstraction

Combat resolution interacts with hit point philosophy. Are HP meat points (physical damage) or abstract competency/luck/fighting spirit? This affects how combat resolution is narrated:

**Meat Points**: Every hit draws blood, combat is brutal
**Abstract**: Hits are close calls and fatigue until final blow kills
**Hybrid**: Minor damage is fatigue, major damage is wounds

Resolution mechanics don't dictate interpretation, but system design can encourage particular understandings through narrative guidance.

## Evolution Across Games

### D&D Combat Evolution

**OD&D (1974)**: Attack matrices, descending AC, table lookups
**AD&D 1E (1977)**: THAC0 introduction, descending AC, complex modifiers
**AD&D 2E (1989)**: THAC0 retained, attempted clarification
**D&D 3E (2000)**: Ascending AC, unified d20 mechanic, clear bonuses
**D&D 4E (2008)**: Maintained 3E system, added guaranteed damage
**D&D 5E (2014)**: Advantage/disadvantage, bounded accuracy, streamlined

Progression shows increasing simplification and intuitive design while maintaining tactical depth.

### Alternative Resolution Systems

**Storyteller/World of Darkness**: Dice pools of d10s, count successes (8+), degrees of success

**FATE**: Roll 4dF (Fudge dice: -1, 0, +1), add skill, compare to opposition, margin = quality

**Powered by the Apocalypse**: Roll 2d6+stat, 10+ success, 7-9 mixed success, 6- failure with consequences

**Year Zero Engine** (Mutant, Alien): Roll d6 pools, count 6s as successes, 1s on stress dice cause problems

**Genesys**: Custom dice with symbols, cancel opposites, interpret narrative results

## Cultural Impact

### "Roll for Initiative!" Iconography

Combat resolution's cultural impact centers on iconic phrases. "Roll for initiative!" became universal RPG reference, appearing in popular culture, memes, and non-gaming contexts. The ritualistic nature of combat resolution—declaring attacks, rolling dice, announcing results—became definitional RPG experience.

### THAC0 Infamy

THAC0 achieved lasting infamy as example of poor usability design. It became shorthand for unnecessarily complex mechanics, with "It's like THAC0" as criticism meaning "confusing despite mathematical elegance." The term persists decades after THAC0's retirement, demonstrating impact of confusing core mechanics.

### Critical Hit Excitement

Natural 20 critical hits became cultural phenomenon. The moment of rolling 20, the table's excitement, the doubled damage—this created memorable experiences transcending mechanical function. "Nat 20" entered common gaming vocabulary, referenced in popular media and celebrated in gaming culture.

### "Roll for Attack" Ritual

The combat resolution sequence became ritualized social performance: declaring target, rolling attack, announcing result, rolling damage, GM narrating outcome. This call-and-response pattern created shared experience and community bonding through repeated structure.

## Modern Usage

### Best Practices

**Pre-Calculate Totals**: Have players calculate attack bonuses and ACs before combat, writing them prominently on character sheets. This eliminates mid-combat calculation.

**Declare Then Roll**: Players declare targets and actions before rolling. This maintains narrative flow and prevents retconning based on roll results.

**Narrate Results**: GMs should narrate hit/miss results descriptively rather than simply announcing numbers. "Your sword glances off the dragon's scales" vs "You miss."

**Roll Damage with Attack**: Roll attack and damage dice simultaneously where possible. If attack hits, damage is ready. This saves time.

**Use Digital Tools**: Virtual tabletops auto-calculate modifiers, roll dice, and apply damage. This dramatically speeds combat resolution.

### Contemporary Variants

**Advantage on Crits** (5E): Some groups grant advantage on damage rolls for critical hits, creating bigger impact.

**Crit Confirms** (3E): Natural 20 requires confirmation roll vs AC to actually critical. Reduces crit frequency.

**Max Damage Crits**: Instead of rolling damage twice, maximize one set of damage dice then roll second. Creates consistent significant crits.

**Brutal Criticals**: Add additional dice to critical hits based on weapon/features. Increases crit impact variety.

**Degrees of Success**: Import margin-of-success rules where beating AC by 5/10 grants additional effects. Adds complexity but reduces whiff factor.

### House Rules

**Flanking Advantage**: Grant advantage for flanking rather than +2 bonus (5E optional rule)
**Critical Success/Failure**: Nat 20/1 on ability checks cause special outcomes
**Confirmation Rolls**: Require confirmation on natural 20s
**Wound Thresholds**: Massive damage causes wounds beyond HP loss
**Called Shots**: Target specific body parts at penalty for special effects

## Related Mechanics

```datacore
TABLE file.link AS "Mechanic", year-introduced AS "Year", first-appearance AS "First Appearance"
FROM "Mechanics"
WHERE contains(file.name, "Armor Class") OR contains(file.name, "Initiative") OR contains(file.name, "Advantage") OR contains(file.name, "Hit Points")
SORT year-introduced ASC
```

**[[Armor Class]]**: The target number for attack resolution, core to combat math

**[[Initiative Systems]]**: Determines order of combat resolution, affecting tactical decisions

**[[Advantage and Disadvantage]]**: Modern D&D's elegant modifier replacement system

**[[Hit Points]]**: The resource depleted by successful attacks, defining character survival

**[[d20 System]]**: Unified resolution mechanic underlying D&D 3E+ combat resolution

**[[Saving Throws]]**: Complementary resolution for avoiding effects rather than attacks

## References and Analysis

- Gygax, Gary and Dave Arneson. *Dungeons & Dragons* (Original Edition). TSR, 1974.
  - Attack matrices and descending AC establishing baseline
- Gygax, Gary and Dave Arneson. *Chainmail*. TSR, 1971.
  - Wargaming rules that influenced D&D combat resolution
- Gygax, Gary. *Advanced Dungeons & Dragons Dungeon Master's Guide*. TSR, 1979.
  - THAC0 system introduction and complex combat modifiers
- Cook, Monte, Jonathan Tweet, and Skip Williams. *D&D Player's Handbook, 3rd Edition*. Wizards of the Coast, 2000.
  - Ascending AC and unified d20 resolution revolution
- Mearls, Mike and Jeremy Crawford. *D&D Player's Handbook, 5th Edition*. Wizards of the Coast, 2014.
  - Advantage/disadvantage and bounded accuracy innovations
- Rein-Hagen, Mark. *Vampire: The Masquerade*. White Wolf, 1991.
  - Alternative dice pool success-counting resolution
- Baker, D. Vincent. *Apocalypse World*. Lumpley Games, 2010.
  - 2d6 resolution with partial success mechanics
- Various. "Bounded Accuracy in D&D 5E" design articles and analysis
  - Discussion of mathematical progression limitations

## Games Using This Mechanic

```datacore
TABLE file.link AS "Game", year-published AS "Year", system AS "System", designer AS "Designer"
FROM "Games"
WHERE type = "game" AND (contains(lower(file.content), "combat") OR contains(lower(file.content), "attack"))
SORT year-published ASC
LIMIT 30
```
