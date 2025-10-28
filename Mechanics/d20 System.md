---
type: mechanic
mechanic-name: d20 System
first-appearance: "[[Dungeons & Dragons (1974)]]"
year-introduced: 1974
games-using:
  - "[[Dungeons & Dragons (1974)]]"
  - "[[Dungeons & Dragons Third Edition (2000)]]"
complexity: 2
popularity: 5
tags:
  - mechanic
  - game-design
  - foundational
  - d20
---

# d20 System

**First Appeared In**: [[Dungeons & Dragons (1974)]]
**Year**: 1974
**Complexity**: 2/5
**Popularity**: 5/5

## Description

The d20 System refers to the use of a twenty-sided die (d20) as the primary resolution mechanic in roleplaying games. The player rolls a d20, adds relevant modifiers (attributes, skills, situational bonuses), and compares the result to a target number. Meeting or exceeding the target number indicates success.

While the original D&D used multiple dice types, the d20 became central to resolution mechanics, particularly for attack rolls and saving throws. Dungeons & Dragons Third Edition (2000) formalized and unified the d20 System, using it for nearly all resolution mechanics and establishing it as an industry standard.

## How It Works

### Core Mechanics

**Basic Resolution**:
1. Player declares action
2. Roll 1d20
3. Add relevant modifiers (ability scores, skill ranks, circumstantial bonuses)
4. Compare total to target number (Difficulty Class/DC, Armor Class/AC, etc.)
5. Equal to or greater than target = success

**Example**: A character attempting to climb a wall (DC 15) with +5 Climb skill rolls d20, gets 11, adds +5 for total of 16, succeeding.

### Resolution Process

**Attack Rolls**: Roll 1d20 + attack bonus vs. target's Armor Class. Success means the attack hits, then roll weapon damage.

**Saving Throws**: Roll 1d20 + save bonus vs. Difficulty Class. Success means avoiding or reducing harmful effect.

**Skill Checks**: Roll 1d20 + skill modifier vs. DC set by difficulty. Success means completing the task.

**Ability Checks**: Roll 1d20 + ability modifier vs. DC. Used for raw attribute tests.

### Edge Cases and Variations

**Natural 20 (Critical Success)**: Rolling 20 on the die (before modifiers) typically means automatic success and often special effects (double damage on attacks in D&D).

**Natural 1 (Critical Failure)**: Rolling 1 on the die typically means automatic failure, though implementations vary.

**Advantage/Disadvantage** (5th Edition): Roll 2d20, take higher (advantage) or lower (disadvantage) result. Elegant modifier replacement.

**Bounded Accuracy** (5th Edition): Target numbers and bonuses stay relatively low (typically +0 to +11), keeping dice roll mattering at all levels.

**Take 10/Take 20** (3rd Edition): Under certain circumstances, assume roll of 10 or 20 rather than rolling, trading time for certainty.

## Games Using This Mechanic

```datacore
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", system AS "System"
FROM "Games"
WHERE contains(string(this.file.link), "d20") OR contains(string(system), "d20")
SORT year-published ASC
```

## Variations and Iterations

**Original D&D (1974)**: Used d20 for attacks and saves alongside other dice for specific tasks.

**AD&D (1977-1999)**: Standardized d20 for combat and saves, but used various resolution methods for different tasks.

**D&D Third Edition (2000)**: Unified nearly all resolution around d20 + modifier vs. DC, creating "the d20 System."

**d20 Modern (2002)**: Adapted the system for modern-day settings with different skill lists and classes.

**Pathfinder (2009)**: Refined 3rd Edition d20 mechanics with additional options and clarifications.

**D&D Fifth Edition (2014)**: Streamlined d20 System with advantage/disadvantage replacing numeric modifiers, bounded accuracy keeping bonuses low.

**d20 System SRD**: The Open Gaming License allowed third-party publishers to create d20-compatible games, spawning hundreds of variations.

## Design Intent and Purpose

The d20 System serves several design goals:

**Intuitive Probability**: The linear distribution of d20 (each number equally likely) makes probability assessment relatively intuitive.

**Heroic Variance**: The wide range (1-20) creates drama—even skilled characters can fail, unskilled characters can succeed.

**Unified Mechanics**: Using the same core mechanic for all resolutions simplifies learning and play.

**Modifier Significance**: The wide die range makes modifiers (+1 to +15) meaningful without overwhelming the randomness.

**Transparency**: Simple math allows players to calculate success probability quickly.

**Tension Creation**: The moment of the die roll creates dramatic tension in outcomes.

## Strengths and Weaknesses

### Strengths

- **Universal Recognition**: The d20 is instantly recognized as the RPG die
- **Simplicity**: Easy to teach and learn—roll high, add modifiers
- **Balanced Randomness**: Neither too swingy nor too predictable
- **Scalability**: Works from level 1 to level 20+ with appropriate target number adjustment
- **Drama**: Creates exciting moments when high or low rolls occur at critical times
- **Quick Resolution**: Fast calculation enables smooth play flow

### Weaknesses

- **Linear Probability**: Unlike dice pools, doesn't create bell curves favoring average results
- **Modifier Inflation**: Higher levels require increasingly high target numbers, creating "treadmill" effect
- **Binary Outcomes**: Success/failure is typically all-or-nothing without gradations (though 5e partially addresses this)
- **Critical Hit Controversy**: Natural 20s create situations where impossible tasks sometimes succeed due to mechanics
- **Analysis Paralysis**: Players may spend time calculating optimal bonuses rather than playing

## Impact on Game Design

The d20 System profoundly shaped RPG design:

**Industry Standard**: Became the default resolution mechanic for fantasy RPGs, similar to how QWERTY became the default keyboard.

**Design Baseline**: Designers either adopt d20 mechanics or explicitly position against them, making it the reference point.

**Open Gaming License**: The d20 System SRD enabled hundreds of compatible games, creating a shared mechanical ecosystem.

**Accessibility**: New players often encounter d20 mechanics first, making them the "standard" RPG experience.

**Video Game Translation**: The straightforward math translates well to digital implementation, influencing CRPGs.

**Tactical Depth**: Grid-based combat with d20 resolution creates rich tactical possibilities.

## Evolution Over Time

**1974-2000**: The d20 coexisted with other resolution mechanics within D&D, gradually becoming more central.

**2000-2008**: Third Edition unified D&D around d20, and the OGL spawned the "d20 boom" of compatible products.

**2008-2014**: Fourth Edition maintained d20 core while adding story elements; Pathfinder kept 3.5 d20 mechanics alive.

**2014-Present**: Fifth Edition streamlined d20 with advantage/disadvantage and bounded accuracy, creating the most elegant d20 implementation yet.

**Future**: The d20 System continues evolving, with new editions refining rather than replacing the core mechanic.

## Related Mechanics

**Dice Pools**: Alternative resolution using multiple dice (like White Wolf's d10 pools) creating different probability curves.

**Percentile Systems**: d100 systems (like Call of Cthulhu) offering finer granularity than d20.

**Target Number Systems**: Various games use different dice but similar "roll + modifier vs. target" structures.

**Advantage/Disadvantage**: 5th Edition's innovation now influencing other games' modifier mechanics.

## Designer Commentary

Gary Gygax originally chose the d20 for attack rolls because it provided good granularity without excessive complexity. The wide range allowed meaningful differentiation between novice and expert characters while maintaining drama.

Jonathan Tweet, Monte Cook, and Skip Williams unified D&D around the d20 in Third Edition because consistent mechanics reduced cognitive load—players learned one resolution method rather than multiple disparate systems.

Mike Mearls and Jeremy Crawford introduced advantage/disadvantage in Fifth Edition to reduce math and streamline play while maintaining the d20's dramatic variance.

## References and Analysis

- Gygax, Gary. Advanced Dungeons & Dragons Dungeon Master's Guide. TSR, 1979.
- Tweet, Jonathan, et al. Dungeons & Dragons Player's Handbook, 3rd Edition. Wizards of the Coast, 2000.
- Mearls, Mike and Jeremy Crawford. Dungeons & Dragons Player's Handbook, 5th Edition. Wizards of the Coast, 2014.
- Cook, Monte. "The d20 System: A Retrospective." Various gaming articles.
