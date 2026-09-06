# 🎲 Games by System - Mechanical Families

**Explore TTRPG history through mechanical evolution and system families**

---

## Purpose

This index organizes games by their core mechanical systems, allowing you to trace the evolution of game mechanics and explore how different games implement similar resolution systems.

---

## Navigation

- **[[TTRPG-History-Dashboard]]** - Main visual dashboard
- **[[README]]** - Overview and setup
- **[[MASTER-INDEX]]** - Complete A-Z reference
- **[[Games-by-Year]]** - Chronological index
- **[[Games-by-Designer]]** - Creator index

---

## Major System Families

### All Games by System

```dataview
TABLE
  system AS "System Family",
  COUNT(file.link) AS "# Games",
  LIST(file.link, 10) AS "Games Using This System"
FROM "Games"
WHERE system != null AND system != ""
GROUP BY system
SORT COUNT(file.link) DESC
```

---

## The d20 Family

### Core d20 System Games

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  complexity AS "Complexity"
FROM "Games"
WHERE contains(string(system), "d20") OR contains(string(system), "D20")
SORT year-published ASC
```

**Family Origin:** [[D&D 3rd Edition]] (2000) by [[Monte Cook]], [[Jonathan Tweet]], [[Skip Williams]]

**Defining Characteristics:**
- d20 + modifiers vs target number
- Six ability scores (Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma)
- Class and level progression
- Armor Class defense rating
- Open Gaming License enabled proliferation

**Major Descendants:**
- [[Pathfinder]] - Enhanced 3.5E evolution
- [[Mutants & Masterminds]] - Superhero adaptation
- [[Star Wars d20]] - Space opera implementation
- Dozens of OGL derivatives

---

## Basic D&D / OSR Lineage

### B/X and OSR Games

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  retro-clone-of AS "Clones",
  complexity AS "Complexity"
FROM "Games" OR FROM "Retroclones"
WHERE contains(string(system), "B/X") OR contains(string(system), "OSR") OR contains(string(system), "Basic D&D") OR type = "retroclone"
SORT year-published ASC
```

**Family Origin:** [[Basic D&D]] (1977-1983) by various TSR designers

**Defining Characteristics:**
- Class-based with race-as-class or separate races
- d20 attack rolls vs Armor Class or THAC0
- Six ability scores with modifiers
- Descending or ascending AC
- Simple, lethal combat
- Gold = XP philosophy

**Major Descendants:**
- [[Labyrinth Lord]] - B/X clone
- [[Swords & Wizardry]] - OD&D clone
- [[Lamentations of the Flame Princess]] - Weird horror B/X
- [[Old-School Essentials]] - Modernized B/X
- [[Dungeon Crawl Classics]] - Gonzo OSR evolution

---

## Storyteller / Storytelling System

### White Wolf and Chronicles of Darkness

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "Storyteller") OR contains(string(system), "Storytelling")
SORT year-published ASC
```

**Family Origin:** [[Vampire: The Masquerade]] (1991) by [[Mark Rein-Hagen]]

**Defining Characteristics:**
- d10 dice pools (attribute + skill)
- Success counting (target number 6-8)
- Botch on multiple 1s
- Dots rating system (1-5)
- Character-driven narrative focus
- Gothic-punk aesthetic

**Major Descendants:**
- [[Werewolf: The Apocalypse]]
- [[Mage: The Ascension]]
- [[Changeling: The Dreaming]]
- [[Exalted]] (evolved mechanics)
- Chronicles of Darkness line

---

## Powered by the Apocalypse (PbtA)

### The Apocalypse Engine Games

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "PbtA") OR contains(string(influenced-by), "Apocalypse World")
SORT year-published ASC
```

**Family Origin:** [[Apocalypse World]] (2010) by [[Vincent Baker]]

**Defining Characteristics:**
- 2d6 + modifier vs 7/10
- Playbooks (character archetypes)
- Moves (fictional triggers → mechanics)
- MC Principles and Agenda
- Fail forward philosophy
- Conversation-based play

**Major Descendants:**
- [[Dungeon World]] - D&D meets PbtA
- [[Monsterhearts]] - Teen supernatural drama
- [[Monster of the Week]] - X-Files style investigation
- [[The Sprawl]] - Cyberpunk heists
- [[Urban Shadows]] - Political urban fantasy
- 100+ published hacks

---

## Forged in the Dark (FitD)

### Blades in the Dark Engine

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  setting AS "Setting"
FROM "Games"
WHERE contains(string(system), "FitD") OR contains(string(influenced-by), "Blades in the Dark")
SORT year-published ASC
```

**Family Origin:** [[Blades in the Dark]] (2017) by [[John Harper]]

**Defining Characteristics:**
- d6 dice pools, take highest
- Position (controlled/risky/desperate) and Effect
- Flashbacks and planning abstraction
- Crew mechanics and shared resources
- Stress and trauma
- Devil's bargains
- Clock-based progress

**Major Descendants:**
- [[Scum and Villainy]] - Space opera
- [[Band of Blades]] - Military dark fantasy
- [[Beam Saber]] - Mecha warfare
- [[A Fistful of Darkness]] - Weird West

---

## FATE System

### FATE Core and Derivatives

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "FATE") OR contains(string(system), "Fate")
SORT year-published ASC
```

**Family Origin:** [[FATE]] (2003) by [[Fred Hicks]] and [[Rob Donoghue]], evolved from FUDGE

**Defining Characteristics:**
- Fudge dice (4dF: -1, 0, +1)
- Aspects (descriptive tags with mechanical weight)
- Fate Points economy
- Create Advantage, Overcome, Attack, Defend actions
- Bronze Rule: Everything is a character
- Fractal structure

**Major Descendants:**
- [[FATE Core]] (2013)
- [[FATE Accelerated]]
- [[Dresden Files RPG]]
- Countless custom implementations

---

## Percentile / d100 Systems

### Roll Under Skill Percentile

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "d100") OR contains(string(system), "percentile") OR contains(string(system), "BRP")
SORT year-published ASC
```

**Family Origins:**
- [[RuneQuest]] (1978) - Skill-based percentiles
- [[Call of Cthulhu]] (1981) - Sanity and investigation

**Defining Characteristics:**
- Roll d100 under skill rating
- Skills start at base % plus modifiers
- Granular probability
- Critical success on 01-05, critical fail on 96-00
- Deadly combat
- Reality-based skill progression

**Major Descendants:**
- Basic Roleplaying (BRP) family
- [[Stormbringer]]
- [[Pendragon]] (d20 variant)
- [[Unknown Armies]]
- [[Delta Green]]
- [[Mothership]] (OSR-influenced d100)

---

## GUMSHOE System

### Investigative Games

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "GUMSHOE")
SORT year-published ASC
```

**Family Origin:** [[Trail of Cthulhu]] (2008) by [[Robin D. Laws]]

**Defining Characteristics:**
- Investigative abilities (spend for clues)
- General abilities (roll d6 for challenges)
- Clues always found if ability present
- Resource management focus
- Pacing through information
- Spend for benefits

**Major Descendants:**
- [[Night's Black Agents]]
- [[Ashen Stars]]
- [[Esoterrorists]]
- [[Mutant City Blues]]
- [[TimeWatch]]

---

## Cypher System

### Monte Cook's Universal Engine

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  setting AS "Setting"
FROM "Games"
WHERE contains(string(system), "Cypher")
SORT year-published ASC
```

**Family Origin:** [[Numenera]] (2013) by [[Monte Cook]]

**Defining Characteristics:**
- Roll d20, modified by difficulty (target numbers in multiples of 3)
- GM never rolls
- Stat pools (Might, Speed, Intellect)
- Spend pool points to enhance actions
- Cyphers (one-use magical items/tech)
- GM Intrusions for complications

**Major Descendants:**
- [[The Strange]]
- [[Cypher System Rulebook]] (generic)
- Various licensed implementations

---

## Year Zero Engine

### Free League's Modular System

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  setting AS "Setting"
FROM "Games"
WHERE contains(string(system), "Year Zero") OR publisher = "Free League"
SORT year-published ASC
```

**Family Origin:** [[Mutant: Year Zero]] (2014) by [[Tomas Härenstam]]

**Defining Characteristics:**
- d6 dice pools (skill + attribute)
- Success on 6s, push for rerolls
- Stress/trauma mechanics
- Modular subsystems
- Metaplot integration
- Initiative cards

**Major Descendants:**
- [[Tales from the Loop]]
- [[Forbidden Lands]]
- [[Alien RPG]]
- [[Blade Runner RPG]]
- [[The One Ring]] (adapted)

---

## GURPS (Generic Universal RolePlaying System)

### Universal Simulation

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  setting AS "Setting"
FROM "Games"
WHERE contains(string(system), "GURPS")
SORT year-published ASC
```

**Family Origin:** [[GURPS]] (1986) by [[Steve Jackson]]

**Defining Characteristics:**
- 3d6 roll under skill/attribute
- Point-buy character creation
- Advantages, disadvantages, skills
- Highly detailed simulation
- Modular supplements
- Bell curve probability

---

## Savage Worlds

### Fast, Furious, Fun

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "Savage Worlds")
SORT year-published ASC
```

**Family Origin:** [[Savage Worlds]] (2003) by [[Shane Lacy Hensley]]

**Defining Characteristics:**
- Polyhedral dice by skill level (d4 to d12)
- Exploding dice (Aces)
- Bennies (meta currency)
- Fast combat with initiative cards
- Wild Cards vs Extras
- Genre-agnostic

---

## Cortex System

### Marvel Heroic & Variants

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "Cortex")
SORT year-published ASC
```

**Defining Characteristics:**
- Dice pool of different sizes (d4-d12)
- Sum two dice, use highest as effect
- Complications and assets
- Highly flexible traits
- Narrative-focused

---

## Unique/Experimental Systems

### Games with Novel Mechanics

#### GM-less and Diceless Games

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  game-structure AS "Structure",
  system AS "System"
FROM "Games"
WHERE contains(string(tags), "GM-less") OR contains(string(tags), "diceless") OR contains(string(game-structure), "GM-less")
SORT year-published ASC
```

#### Card-Based Games

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  resolution-mechanic AS "Mechanic"
FROM "Games"
WHERE contains(string(resolution-mechanic), "card") OR contains(string(tags), "card-based")
SORT year-published ASC
```

#### Jenga and Dread-likes

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  resolution-mechanic AS "Mechanic"
FROM "Games"
WHERE contains(string(resolution-mechanic), "Jenga") OR contains(string(influenced-by), "Dread")
SORT year-published ASC
```

---

## Mechanics Innovation Timeline

### Groundbreaking Mechanical Innovations

**1974** - Class & Level (D&D)
**1978** - Percentile Skills ([[RuneQuest]])
**1983** - Troupe Play ([[Ars Magica]])
**1985** - Lifepath Generation ([[Traveller]])
**1987** - Universal Point-Buy ([[GURPS]])
**1991** - Dice Pools ([[Vampire: The Masquerade]])
**1993** - Diceless Resolution ([[Amber Diceless RPG]])
**1997** - Resource Pools ([[Dying Earth]])
**2001** - Aspects ([[FATE]])
**2005** - Jenga Tower Tension ([[Dread]])
**2008** - Auto-Success Clues ([[Trail of Cthulhu]])
**2010** - Playbooks & Moves ([[Apocalypse World]])
**2013** - GM Never Rolls ([[Numenera]])
**2017** - Position & Effect ([[Blades in the Dark]])

---

## By Complexity

### Simple Systems (Complexity 1-2)

```dataview
TABLE
  complexity AS "Level",
  file.link AS "Game",
  system AS "System",
  year-published AS "Year"
FROM "Games"
WHERE complexity <= 2 AND complexity != null
SORT complexity ASC, year-published ASC
```

### Intermediate Systems (Complexity 3)

```dataview
TABLE
  complexity AS "Level",
  file.link AS "Game",
  system AS "System",
  year-published AS "Year"
FROM "Games"
WHERE complexity = 3
SORT year-published ASC
```

### Complex Systems (Complexity 4-5)

```dataview
TABLE
  complexity AS "Level",
  file.link AS "Game",
  system AS "System",
  year-published AS "Year"
FROM "Games"
WHERE complexity >= 4 AND complexity != null
SORT complexity DESC, year-published ASC
```

---

## System Family Trees

### Generate Visual Family Trees

Run analytics to create system evolution diagrams:

```bash
python3 Scripts/analytics/system_family_tree.py
```

**Output:** `Attachments/Diagrams/analytics/system_family_tree.png`

---

## System Philosophy Comparison

### Simulationist Systems
Focus on modeling reality and detailed mechanics

```dataview
TABLE
  file.link AS "Game",
  system AS "System",
  complexity AS "Complexity",
  year-published AS "Year"
FROM "Games"
WHERE contains(string(tags), "simulation") OR complexity >= 4
SORT complexity DESC, year-published ASC
LIMIT 15
```

### Narrativist Systems
Focus on story and dramatic tension

```dataview
TABLE
  file.link AS "Game",
  system AS "System",
  complexity AS "Complexity",
  year-published AS "Year"
FROM "Games"
WHERE contains(string(tags), "narrative") OR contains(string(tags), "story-game")
SORT year-published ASC
LIMIT 20
```

### Gamist Systems
Focus on tactical challenge and player skill

```dataview
TABLE
  file.link AS "Game",
  system AS "System",
  complexity AS "Complexity",
  year-published AS "Year"
FROM "Games"
WHERE contains(string(tags), "tactical") OR contains(string(tags), "combat-focused")
SORT year-published ASC
```

---

## Cross-Genre Systems

### Universal/Generic Systems

```dataview
TABLE
  file.link AS "Game",
  system AS "System",
  year-published AS "Year",
  designer AS "Designer"
FROM "Games"
WHERE contains(string(genre), "universal") OR contains(string(tags), "generic")
SORT year-published ASC
```

**Major Universal Systems:**
- [[GURPS]] - Ultimate simulation
- [[Savage Worlds]] - Fast pulp action
- [[FATE]] - Aspect-driven narrative
- [[Cypher System]] - GM-less rolling
- [[Genesys]] - Narrative dice
- [[BRP]] - Percentile skills

---

## Random System Discovery

### Discover a Random System Family

```dataview
TABLE
  system AS "System Family",
  COUNT(file.link) AS "# Games",
  LIST(file.link, 5) AS "Example Games"
FROM "Games"
WHERE system != null AND system != ""
GROUP BY system
SORT random()
LIMIT 1
```

---

## Search Tips

**Find games by system:** Use the family sections above or search this page

**Compare mechanics:** Read [[Mechanics]] entries for detailed breakdowns

**Track evolution:** Use [[Games-by-Year]] to see mechanical innovation over time

**Explore philosophies:** Follow wikilinks to designer philosophies

---

## Related Resources

### Deep Dive Mechanics

- **[[Mechanics]]** - Browse 23+ detailed mechanic entries
- **[[Resolution-Systems]]** - Core task resolution comparison
- **[[Character-Advancement]]** - Progression mechanics
- **[[Action-Economy]]** - Turn structure and initiative

### Alternative Views

- **[[Games-by-Year]]** - Chronological timeline
- **[[Games-by-Designer]]** - Creator catalog
- **[[Games-by-Publisher]]** - Company catalog
- **[[MASTER-INDEX]]** - Complete A-Z reference

### Analytics

- **System Family Trees** - Visual evolution diagrams
- **Complexity vs Popularity** - Correlation analysis
- **Innovation Timeline** - Mechanical breakthroughs

---

**🎲 The mechanical DNA of 50 years of tabletop roleplaying 🎲**

*Explore how core systems evolved, branched, and cross-pollinated to create the diverse ecosystem of modern TTRPGs.*

---

*Last updated: October 2025*
*Version: 4.0*
*Vault Status: Production-Ready*
