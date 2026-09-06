---
title: Armor Class
type: mechanic
year-introduced: 1974
first-appearance: "[[Dungeons & Dragons (1974)]]"
complexity: 2
popularity: 5
games-using:
  - "[[Dungeons & Dragons (1974)]]"
  - "[[Advanced Dungeons & Dragons (1977)]]"
  - "[[Dungeons & Dragons Third Edition (2000)]]"
  - "[[Dungeons & Dragons Fifth Edition (2014)]]"
  - "[[Pathfinder (2009)]]"
  - "[[13th Age (2013)]]"
influenced-by: ["Chainmail wargaming"]
influence-on:
  - "[[Hit Points]]"
  - "Defense Rating systems"
  - "Attack vs. Defense mechanics"
tags:
  - mechanic
  - game-design
  - foundational
  - combat
  - defense
category: combat
---

# Armor Class

**First Appeared In**: [[Dungeons & Dragons (1974)]]
**Year**: 1974
**Complexity**: 2/5
**Popularity**: 5/5

## Overview

Armor Class (AC) represents a character's defensive capability, measuring how difficult they are to hit in combat. Rather than tracking whether armor prevents damage after hits land, AC determines whether attacks successfully strike the target at all. This abstraction combines physical armor protection, natural agility, defensive skill, shield use, magical protection, and sheer size into a single target number that attackers must meet or exceed with their attack rolls. Together with Hit Points, Armor Class forms D&D's fundamental two-axis defense system: AC determines whether you get hit, HP determines how much damage you can sustain.

The elegance of Armor Class lies in resolving both attack accuracy and defense effectiveness with a single roll. Instead of separate rolls for "does the sword swing hit?" and "does the armor block it?", the attack roll against AC answers both questions simultaneously. This streamlined resolution keeps combat flowing quickly while maintaining tactical depth. A heavily armored knight has high AC making them difficult to damage; a nimble rogue has moderate AC from agility; an unarmored wizard has terrible AC making them fragile targets. These defensive profiles create distinct combat identities from a single numerical value.

Armor Class has evolved dramatically across D&D editions while maintaining its core function. The original descending AC system (where lower numbers meant better armor, ranging from AC 9 for unarmored to AC 2 for plate armor) confounded new players for decades before being replaced by ascending AC (higher numbers mean better defense). Despite this mathematical reversal, AC remains one of RPG gaming's most recognizable mechanics, influencing countless games and becoming fundamental vocabulary in gaming culture. When someone says "that enemy has high AC," gamers universally understand: that opponent is difficult to hit.

## Historical Context

Armor Class originated in Chainmail, Gary Gygax and Jeff Perren's medieval miniatures wargame that directly preceded Dungeons & Dragons. Chainmail used armor types as combat modifiers, with different armor providing different defensive capabilities against various weapon types. When Gygax and Dave Arneson developed D&D from Chainmail's framework, they needed to simplify armor mechanics for individual character combat rather than mass miniature battles.

The solution was Armor Class—a unified defense rating that absorbed all defensive factors into one target number. This eliminated the need for complex armor-vs-weapon charts while maintaining the fundamental concept that better armor made you harder to kill. The choice to use descending values (AC 9 to AC 2 for normal armor, extending to AC -10 for incredibly powerful defenses) came from Chainmail's existing framework and mathematical convenience in the original attack tables.

Early D&D presented AC with minimal explanation, simply listing armor types and their AC values. Players equipped armor and noted their AC; attackers consulted attack matrices to determine what roll was needed to hit various ACs. The system worked functionally but created significant cognitive load—remembering that AC 2 was better than AC 5 required learning, and the descending scale defied intuitive understanding.

The abstraction of AC proved both strength and weakness. By combining multiple defensive factors into one number, AC simplified gameplay significantly compared to tracking separate values for armor, dexterity, shields, defensive stance, size, and magical protection. However, this abstraction also created verisimilitude questions: Does high AC mean attacks miss entirely, or do they hit but fail to penetrate armor? The rules left this interpretation deliberately vague, allowing different tables to narrate combat according to their preferences.

Armor Class established the fundamental D&D combat loop: roll d20, add modifiers, compare to target AC, deal damage if you hit. This core resolution method became so ingrained in gaming culture that "d20 vs AC" represents not just a mechanic but an entire design philosophy emphasizing clear probability, fast resolution, and tactical simplicity.

## Mechanical Function

### Determining Armor Class

Characters calculate AC by combining multiple factors:

**Base AC**: Starting value depending on edition (10 in ascending systems, 9-10 in descending systems)

**Armor Value**: Different armor types provide different AC values:
- **Unarmored**: 10 AC (ascending) / AC 9 (descending)
- **Leather Armor**: 11 AC / AC 8
- **Chain Mail**: 16 AC / AC 4
- **Plate Armor**: 18 AC / AC 2

**Dexterity Modifier**: Quick characters dodge better. Dexterity bonuses improve AC (in ascending systems; reduce AC value in descending systems). Heavy armor limits maximum Dexterity bonus—plate armor might allow only +1 Dex bonus maximum, while light armor allows full Dexterity modifier.

**Shield**: Carrying a shield improves AC, typically by +2. Requires dedicating one hand to shield rather than weapons or spellcasting.

**Natural Armor**: Non-humanoid creatures may have tough hides providing AC bonuses. Dragons have scales, elementals have damage-resistant forms, etc.

**Magical Bonuses**: Enchanted armor, magical shields, protection spells, and defensive magic items improve AC. A +1 Chain Mail provides better defense than mundane chain mail.

**Situational Modifiers**: Cover, defensive fighting, dodge actions, and tactical positioning may provide temporary AC improvements.

### Attack Resolution

When attacking a target:

1. **Roll d20**: The attacker rolls a twenty-sided die
2. **Add Attack Modifiers**: Strength (melee), Dexterity (ranged), proficiency bonuses, magical weapon bonuses, situational modifiers
3. **Compare to AC**:
   - **Ascending AC** (modern): If total equals or exceeds target AC, the attack hits
   - **Descending AC** (classic): If total equals or exceeds the required "to-hit" number for that AC (from attack tables), the attack hits
4. **Resolve Damage**: On hit, roll weapon damage dice and subtract from target's Hit Points

**Example (5th Edition ascending AC)**:
- Orc (AC 13) is the target
- Fighter attacks with longsword
- Fighter rolls d20, gets 11
- Fighter has +5 attack bonus (Strength +3, proficiency +2)
- Total: 11 + 5 = 16
- 16 exceeds AC 13, so the attack hits
- Fighter rolls 1d8+3 longsword damage

### AC Variations and Special Cases

**Touch AC** (3rd Edition): Separate AC value ignoring armor and shields, representing only Dexterity and size. Used for spells and attacks targeting reflexes rather than penetrating armor. A heavily armored knight might have AC 22 but Touch AC 10, making them vulnerable to certain spell attacks.

**Flat-Footed AC** (3rd Edition): AC without Dexterity bonus, representing being caught unaware. Used for surprise rounds and situations where defenders can't dodge.

**Different AC Values** (3rd Edition+): Creatures could have different ACs depending on attack type—monks might have high AC against melee but lower AC against ranged attacks due to deflection abilities.

**Situational AC Modifiers**:
- **Cover**: Half-cover grants +2 AC, three-quarters cover grants +5 AC
- **Partial Cover**: Shooting through allies or obstacles increases target AC
- **Prone**: Melee attacks against prone targets gain advantage (easier to hit), ranged attacks have disadvantage (harder to hit)
- **Dodge Action**: Dedicating action to defense grants advantage to attackers (effectively improving AC)

### AC Progression

Unlike Hit Points which grow substantially with level, AC progresses more conservatively:

**Low Level (1-4)**: AC typically ranges from 10-16. Unarmored characters are very vulnerable; armored characters gain significant protection. AC differences feel dramatic—AC 10 vs AC 15 represents twice the hit chance.

**Mid Level (5-10)**: AC ranges 14-19 for most characters. Magical armor appears (+1/+2 enchantments), Dexterity improvements from ability score increases, and class features provide defensive improvements.

**High Level (11-16)**: AC ranges 16-22 for typical characters. Powerful magical armor (+3 enchantments), defensive class features, and protective spells create substantial protection.

**Epic Level (17-20)**: AC can reach 20-25 or higher for specialized defensive builds. Legendary armor, multiple stacked defensive spells, and peak class features provide near-untouchable AC for some characters.

**Bounded Accuracy** (5th Edition): Intentionally limits AC growth to maintain relevance of dice rolls. Even powerful characters rarely exceed AC 20-22, keeping combat uncertain at all levels.

## Design Philosophy

### Abstraction and Interpretation

AC's power lies in deliberate abstraction. The same AC 15 represents different defensive realities for different characters:

**Armored Fighter (AC 15)**: Chain mail armor physically deflecting strikes. Attacks "hit" but glance off metal.

**Unarmored Monk (AC 15)**: Lightning reflexes dodging attacks. Attacks "miss" because the monk isn't where the weapon strikes.

**Mage Armor Wizard (AC 15)**: Magical force field deflecting attacks. Attacks hit invisible barriers surrounding the caster.

This interpretative flexibility allows narrative creativity while maintaining mechanical consistency. Groups can describe combat dramatically while using identical underlying math.

### Probability Management

AC creates predictable probability curves that allow tactical decision-making:

**Attack Bonus +5 vs AC 15**: 11+ on d20 = 50% hit chance
**Attack Bonus +8 vs AC 15**: 8+ on d20 = 65% hit chance
**Attack Bonus +5 vs AC 18**: 14+ on d20 = 35% hit chance

Players can mentally calculate approximate hit chances and make informed tactical decisions: "I have 50% chance to hit the armored knight (AC 18) or 75% chance to hit the unarmored wizard (AC 12)—wizard first!"

This probability transparency creates strategic depth without requiring complex math. Players intuitively learn that +5 attack bonus against AC 15 means "about half my attacks hit."

### Action Economy Interaction

AC's binary hit/miss resolution interacts powerfully with action economy. More attacks per round increase expected damage output against any AC:

**Single Attack (+5) vs AC 15**: 50% chance to hit, expected value = 0.5 × damage
**Two Attacks (+5) vs AC 15**: Two 50% chances, expected damage doubles

This scaling makes multiple attacks extremely valuable and creates tactical considerations around advantage/disadvantage, defensive actions, and positioning. High AC doesn't prevent damage, it reduces damage frequency—but more attacks overcome high AC through statistical volume.

### Gateway to Complexity

Basic AC is simple: higher is better, easy to track, intuitive to use. But AC's framework supports unlimited complexity layering:

**Situational Modifiers**: Cover, concealment, flanking, environmental conditions
**Damage Resistance**: Some AC might represent armor absorbing damage rather than preventing hits entirely
**Called Shots**: Optional rules for targeting specific areas with AC penalties
**Armor Degradation**: AC reduction as armor takes damage
**Mounted Combat**: AC bonuses/penalties while mounted
**Specific Defenses**: AC bonuses against specific attack types (ranged, melee, specific damage types)

This scalability allows groups to use simple baseline AC or add complexity as desired without fundamentally changing the core mechanic.

### Class Balance Through AC Access

Different classes access different AC ranges, creating defensive profiles:

**Heavy Armor Classes** (Fighters, Paladins, Clerics): Access plate armor (AC 18) + shields (AC 20 total). High durability, low mobility (some editions impose speed penalties).

**Medium Armor Classes** (Rangers, Barbarians, some Clerics): Access half-plate (AC 15) + Dex modifier (typically AC 17 total). Balanced defense and mobility.

**Light Armor Classes** (Rogues, Bards): Leather armor (AC 11) + full Dex modifier (potentially AC 16+ with high Dex). Defense through agility.

**Unarmored Classes** (Monks, Barbarians, Druids): Special class features provide AC from Wisdom or Constitution, creating alternative defense scaling.

**Unarmored Casters** (Wizards, Sorcerers): Reliant on Mage Armor spell or Dexterity alone (typically AC 12-15). Extremely vulnerable without magical protection.

This AC access distribution creates class identity through defense mechanics while requiring party balance—pure wizard parties are extremely fragile; pure fighter parties are highly durable.

## Evolution Over Time

### Original D&D (1974-1977)

Original D&D used descending AC inherited from Chainmail, ranging from AC 9 (unarmored) to AC 2 (plate + shield). Attack tables cross-referenced attacker level against target AC to determine required d20 roll. These tables created non-linear progressions where high-level attackers hit low AC easily but struggled against heavy armor.

The system included AC improvements from Dexterity but with crude granularity—only extremely high or low Dexterity affected AC. Most characters' AC came entirely from armor choice. Magical armor provided AC improvements: +1 Chain Mail was AC 4 instead of AC 5.

AC could extend below 2 into negative numbers (AC 0, AC -1, etc.) for extremely powerful defenses—heavily enchanted plate armor and stacked magical protections. This created powerful defensive caps for high-level characters, though reaching very low AC required substantial magical investment.

### Advanced D&D (1977-1989)

AD&D formalized descending AC with comprehensive armor tables, specific armor types, and detailed AC calculation rules. The Player's Handbook explained AC conceptually as "how hard you are to hit" but left narrative interpretation (does armor stop blows or do attacks miss?) deliberately vague.

Dexterity provided AC bonuses based on the Dexterity table, with 18 Dexterity granting -4 AC bonus (four points better). Different armor types allowed different maximum Dexterity bonuses—plate armor allowed no Dexterity bonus; leather armor allowed full bonus.

The edition introduced weapon-vs-armor type modifiers: certain weapons performed better or worse against specific armor types. A two-handed sword was particularly effective against chain mail; a morning star excelled against plate armor. These optional rules added simulation depth but were frequently ignored as excessively complex.

THAC0 ("To Hit Armor Class 0") became shorthand for attack capability: the number you needed on d20 to hit AC 0. A THAC0 of 15 meant you needed 15+ to hit AC 0, 17+ to hit AC -2, 13+ to hit AC 2, etc. While mathematically functional, THAC0 confused countless players and became infamous for counterintuitive arithmetic.

### AD&D 2nd Edition (1989-2000)

Second Edition maintained descending AC and THAC0 with minor refinements. The system remained essentially unchanged from 1st Edition, preserving compatibility with existing adventures and supplements.

The edition's primary AC contribution was clearer presentation and examples attempting to demystify THAC0 calculations. Tables showed THAC0 progression for all classes and pre-calculated "to-hit" numbers for various AC values, reducing arithmetic burden.

Optional rules explored AC variations like deflection bonuses (from magical protection), natural armor bonuses (creature hides), and dodge bonuses (from high Dexterity), previewing 3rd Edition's more granular AC breakdown.

### D&D 3rd Edition (2000-2007)

Third Edition revolutionized AC by inverting to ascending values. The dramatic shift changed AC from "lower is better" (AD&D's AC -3 being superior to AC 5) to "higher is better" (3rd Edition's AC 22 being superior to AC 15). This mathematical reversal aligned with intuitive understanding and streamlined calculation.

The new AC formula: 10 + armor bonus + shield bonus + Dexterity modifier + size modifier + natural armor + deflection bonus + misc modifiers

This granular breakdown allowed precise tracking of different defensive sources:

**Armor Bonus**: From wearing armor (0 for unarmored, +8 for full plate)
**Shield Bonus**: +1-4 depending on shield type
**Dexterity Modifier**: Full modifier for light armor, limited for medium/heavy armor
**Size Modifier**: Large creatures easier to hit (-1 AC), Small creatures harder to hit (+1 AC)
**Natural Armor**: Creature hide/scales bonus
**Deflection Bonus**: Magical force protection
**Misc Modifiers**: Cover, concealment, dodge bonuses, etc.

The edition introduced Touch AC (10 + Dex + size + misc, ignoring armor/shield/natural armor) for attacks targeting reflexes, and Flat-Footed AC (normal AC without Dexterity) for surprise situations. This created tactical depth where heavily armored characters had vulnerabilities to certain attack types.

AC progression remained moderate despite numerous bonus sources. Typical characters ranged from AC 12-20 throughout careers, with specialized defensive builds reaching AC 25-30 at high levels. The system's mathematical precision enabled optimization culture around maximizing AC through item stacking, spell combinations, and build choices.

### D&D 4th Edition (2008-2014)

Fourth Edition maintained ascending AC but simplified calculation significantly. The basic formula: 10 + armor/ability bonus + class bonus + enhancement bonus + misc modifiers.

The edition unified defensive progression across levels through "half-level bonus"—all defenses including AC gained +1 per two character levels automatically. This ensured appropriate scaling against level-appropriate enemies without requiring constant magical equipment upgrades.

Armor became proficiency-based rather than equipment-restricted by class. Characters with heavy armor proficiency could wear plate; those without suffered penalties. This removed "illegal armor" concepts from previous editions.

The edition introduced multiple defense scores (AC, Fortitude, Reflex, Will) with different attacks targeting different defenses. AC specifically defended against physical attacks; some powers targeted Reflex (dodging) or Fortitude (endurance) instead. This created tactical variety where heavily armored characters had high AC but potentially lower Reflex, making them vulnerable to area attacks.

### D&D 5th Edition (2014-Present)

Fifth Edition streamlined AC dramatically while maintaining ascending values. The simplified formula: base AC (from armor) + Dexterity modifier (up to armor's maximum) + shield bonus.

**Light Armor**: Base AC + full Dexterity modifier
**Medium Armor**: Base AC + Dexterity modifier (maximum +2)
**Heavy Armor**: Base AC only (no Dexterity)

The edition introduced "bounded accuracy"—intentionally limiting AC and attack bonus growth to keep d20 rolls relevant at all levels. Even 20th-level characters rarely exceed AC 19-20 without magical items, and bounded attack bonuses mean low-level enemies maintain chances to hit high-level characters. This controversial design maintains tension throughout campaigns rather than creating inevitable hits/misses at extreme level gaps.

Advantage/Disadvantage mechanics replaced many numerical AC modifiers. Instead of +2 AC from cover, attackers have disadvantage. Instead of -2 AC penalty from prone, attackers have advantage. This simplified tracking while maintaining tactical considerations.

The edition provides three unarmored AC calculations for classes without armor:

**Monk**: 10 + Dexterity + Wisdom (while unarmored)
**Barbarian**: 10 + Dexterity + Constitution (while unarmored)
**Draconic Sorcerer**: 13 + Dexterity (permanent natural armor)

These alternatives allow non-armored classes to maintain competitive AC through class features rather than equipment.

### Other Notable Systems

**Pathfinder (2009)**: Maintained 3rd Edition's granular AC system virtually unchanged, preserving Touch AC, Flat-Footed AC, and detailed bonus breakdowns.

**13th Age (2013)**: Simplified ascending AC similar to 5E, with Physical Defense and Mental Defense as separate values. Reduced granularity while maintaining tactical variety.

**Old School Renaissance (OSR) Games**: Many intentionally preserve descending AC and THAC0 for authentic retro experience, celebrating rather than correcting classic D&D's quirks.

## Cultural Impact

### Gaming Vocabulary

"AC" entered universal gaming shorthand. "What's your AC?" is instantly understood across gaming communities. Terms like "AC tank" (high-AC defensive character), "touch attack" (bypassing armor), and "flat-footed" (caught unaware) became standard gaming vocabulary.

The concept influenced countless video games, board games, and other RPGs. "Defense rating," "armor value," and similar mechanics in non-D&D games trace clear lineage to Armor Class. Even games using completely different systems reference AC as the baseline they're diverging from.

### The THAC0 Controversy

THAC0 became legendary for confusing players throughout the AD&D era. The counterintuitive math—subtracting positive numbers to hit worse AC, adding negative numbers to hit better AC—generated endless forum threads, confused new players, and became shorthand for unnecessarily complicated game design. Many players cite THAC0 as primary reason they prefer modern editions.

Conversely, THAC0 nostalgia exists among veteran players who mastered the system. For them, THAC0 represents "real D&D" and ascending AC feels wrong. This generational divide illustrates how core mechanical changes can fracture gaming communities.

### Ascending AC Adoption

Third Edition's switch to ascending AC marked a watershed moment in RPG design. The inversion required retraining millions of players' intuitions but ultimately improved accessibility dramatically. Modern players learn "higher AC is better" instantly, whereas descending AC required explicit teaching and memorization.

The success of ascending AC influenced the entire RPG industry. Most modern games use ascending defense values, making D&D's choice effectively the new standard. Games still using descending values are now oddities rather than norms.

### Bounded Accuracy Debate

Fifth Edition's bounded accuracy philosophy sparked passionate debate. Advocates praise maintaining dice roll relevance at all levels, preserving tension, and preventing mathematical escalation. Critics argue it removes satisfying progression feeling, makes high-level characters feel insufficiently powerful, and contradicts fantasy power scaling.

This debate extends beyond AC to fundamental questions about RPG design: Should advancement make you numerically superior to weak enemies, or should tactical factors always matter regardless of level difference?

## Strengths and Weaknesses

### Strengths

**Simplicity**: Single number representing all defensive capability. Easy to remember, quick to reference, fast to resolve.

**Intuitive Probability**: Players quickly learn approximate hit chances against various ACs, enabling tactical decision-making.

**Fast Resolution**: One roll, one comparison, immediate hit/miss result. Keeps combat flowing.

**Flexible Abstraction**: Accommodates multiple narrative interpretations—armor blocking, attacks missing, magical deflection—without mechanical changes.

**Tactical Depth**: Situational modifiers, cover, positioning, and action choices create tactical richness built on simple foundation.

**Unified Defense Metric**: Different defensive sources (armor, agility, magic, size) combine coherently without separate tracking.

**Clear Progression**: AC improvements provide visible, meaningful advancement rewards that demonstrably improve survivability.

**Class Differentiation**: Armor access creates distinct defensive profiles separating fragile casters from durable warriors.

**Mathematical Predictability**: Designers can precisely calculate hit chances, balance encounters, and tune difficulty curves using AC values.

### Weaknesses

**Loss of Granularity**: Combining all defensive factors into one number loses nuance. A heavily armored but slow character has the same AC as an unarmored but incredibly agile character, despite representing completely different defensive strategies.

**Binary Outcomes**: Hits connect or miss entirely without gradation. Near-misses have identical outcomes to completely wild swings.

**Armor Effectiveness Questions**: Does high AC mean attacks miss or armor absorbs hits? The ambiguity can create narrative confusion when characters survive impossible situations.

**Bounded Progression** (5E): Limited AC growth can feel unrewarding at high levels, with epic characters only marginally harder to hit than novices.

**Dexterity Dominance**: In many editions, Dexterity provides both AC bonus and attack bonus, making it disproportionately valuable compared to other abilities.

**Magic Dependency** (some editions): High-level competitive AC often requires magical items, making non-magical characters progressively vulnerable.

**Swingy Combat**: Heavy reliance on hit/miss binary can create feast-or-famine combat where string of misses against high AC produces frustrating inaction.

**Verisimilitude Issues**: AC abstraction can break immersion when narrative and mechanics conflict—dragon breath "missing" high-AC characters feels wrong.

**Optimization Focus**: AC maximization can become minigame overshadowing other character aspects, especially in optimization-focused editions (3rd/Pathfinder).

**Learning Curve** (descending AC): Historical THAC0 confusion created unnecessary learning barriers that deterred potential players for decades.

## Modern Usage

### Best Practices

Contemporary AC implementation wisdom includes:

**Clear Presentation**: Explicitly state what AC represents in your game's fiction. Is it physical armor, dodge ability, or both? Clear framing prevents interpretation confusion.

**Balance AC Access**: Ensure all character types have viable defensive options. Pure casters need Mage Armor, Shields, or similar mechanics to avoid being glass cannons.

**Limit Inflation**: Prevent AC optimization arms races that make combats swing entirely on AC values. Bounded accuracy or similar caps maintain balanced gameplay.

**Provide Alternatives**: Not all characters should optimize AC identically. Multiple defensive strategies (high AC, high HP, damage resistance, defensive reactions) create build variety.

**Situational Modifiers**: Use cover, concealment, and positioning to create tactical AC variation beyond static character values.

**Normalize Against Attack Bonuses**: Design AC values appropriate for expected attack bonuses at each level. Players should hit roughly 50-65% of attacks against appropriate-level enemies.

**Advantage/Disadvantage**: Use binary states rather than excessive +1/+2 AC modifiers when possible. Simpler tracking, easier adjudication.

**Consider Alternatives**: Evaluate whether static AC suits your game better than active defense rolls, damage reduction systems, or other defensive frameworks.

### Alternative Defensive Mechanics

Many modern games explore alternatives to traditional AC:

**Active Defense** (GURPS, Genesys): Defenders roll to dodge/parry incoming attacks, creating interactive defense rather than passive AC.

**Damage Reduction** (Shadowrun, Warhammer): Armor reduces damage after hits land rather than preventing hits. Creates attrition feel where all attacks hit but armor matters.

**Armor as HP** (some systems): Armor provides additional hit point pools that deplete before health, creating ablative protection feel.

**Split Defenses** (4E, 13th Age): Multiple defense types (AC, Reflex, Fortitude, Will) targeted by different attacks. Adds complexity but prevents single-stat dominance.

**Narrative Defense** (PbtA games): No numerical AC; attack outcomes determined by fiction and roll results. Prioritizes narrative over simulation.

### When to Use AC

Armor Class works best for:

- Fast-paced combat prioritizing speed over detailed simulation
- Tactical combat with grid-based positioning and numerical optimization
- Class-based systems where equipment determines capabilities
- Games emphasizing clear probability and player-facing mathematics
- Traditional fantasy settings with armor progression as advancement reward

AC may not suit:

- Highly narrative games prioritizing description over statistics
- Simulationist games requiring detailed wound tracking and armor realism
- Classless systems where equipment restrictions feel artificial
- Combat-light games where defensive mechanics receive minimal focus
- Settings where armor doesn't meaningfully exist (modern/sci-fi sometimes)

## Related Mechanics

**[[Hit Points]]**: Complementary defensive mechanic—AC determines if you get hit, HP determines how much damage you survive.

**[[d20 System]]**: AC integrates with d20 core mechanics as the primary defense target number.

**[[Saving Throws]]**: Alternative defense mechanic for avoiding effects through resistance rather than preventing hits.

**Attack Bonuses/THAC0**: Offensive counterpart determining likelihood of hitting target AC.

**Damage Resistance/Reduction**: Secondary defensive layer reducing damage after AC fails to prevent hits.

**Dexterity**: Primary ability score affecting AC for most character types.

**Cover and Concealment**: Environmental factors providing AC bonuses or imposing attack penalties.

**Touch AC/Flat-Footed AC**: Variant AC values for specific attack types or situations.

**Advantage/Disadvantage** (5E): Binary modifiers affecting attack rolls against AC rather than modifying AC directly.

## References and Analysis

- Gygax, Gary and Jeff Perren. *Chainmail*. Guidon Games, 1971.
  - Original armor mechanics that evolved into AC
- Gygax, Gary and Dave Arneson. *Dungeons & Dragons* (Original White Box). TSR, 1974.
  - First implementation of descending AC system
- Gygax, Gary. *Advanced Dungeons & Dragons Player's Handbook*. TSR, 1978.
  - Formalized descending AC with detailed armor tables and THAC0
- Tweet, Jonathan, et al. *Dungeons & Dragons Player's Handbook, 3rd Edition*. Wizards of the Coast, 2000.
  - Revolutionary switch to ascending AC
- Mearls, Mike and Jeremy Crawford. *Dungeons & Dragons Player's Handbook, 5th Edition*. Wizards of the Coast, 2014.
  - Simplified AC with bounded accuracy philosophy
- Cook, Monte. "Bounded Accuracy and Defense Mechanics" in various design blogs
  - Analysis of AC progression and mathematical implications
- Peterson, Jon. *Playing at the World*. Unreason Press, 2012.
  - Historical development of AC from wargaming through early RPGs

## Games Using This Mechanic

```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System"
FROM "Games"
WHERE contains(file.content, "Armor Class") OR contains(file.content, "armor class") OR contains(file.content, " AC ")
SORT year-published ASC
```
