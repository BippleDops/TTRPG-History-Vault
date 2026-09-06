# 🎲 Games by Designer - Creator Catalog

**Explore TTRPG history through its creative minds**

---

## Purpose

This index organizes games by their designers, allowing you to explore creative visions, design philosophies, and the evolution of individual creators' work over time.

---

## Navigation

- **[[TTRPG-History-Dashboard]]** - Main visual dashboard
- **[[README]]** - Overview and setup
- **[[MASTER-INDEX]]** - Complete A-Z reference
- **[[Games-by-Year]]** - Chronological index
- **[[Games-by-System]]** - Mechanical index

---

## All Designers A-Z

### Designer Directory

```dataview
TABLE
  file.link AS "Designer",
  birth-year AS "Born",
  nationality AS "From",
  LIST(notable-works, 4) AS "Notable Games",
  influence-score AS "Influence",
  active-years AS "Active"
FROM "Designers"
SORT file.name ASC
```

---

## Most Influential Designers

### Legendary Creators (Influence 5/5)

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 5) AS "Key Works",
  design-philosophy AS "Philosophy",
  active-years AS "Years Active"
FROM "Designers"
WHERE influence-score = 5
SORT file.name ASC
```

### Highly Influential (Influence 4/5)

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 4) AS "Key Works",
  design-philosophy AS "Philosophy",
  active-years AS "Years Active"
FROM "Designers"
WHERE influence-score = 4
SORT file.name ASC
```

---

## Games by Each Designer

### Browse Complete Catalogs

Use the queries below to see all games by specific designers:

#### Gary Gygax

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Gary Gygax")
SORT year-published ASC
```

[[Gary Gygax]] - Co-creator of Dungeons & Dragons, father of the TTRPG hobby

---

#### Dave Arneson

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Dave Arneson")
SORT year-published ASC
```

[[Dave Arneson]] - Co-creator of D&D, pioneer of collaborative storytelling

---

#### Mark Rein-Hagen

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Mark Rein-Hagen") OR contains(string(designer), "Mark Rein·Hagen")
SORT year-published ASC
```

[[Mark Rein-Hagen]] - Creator of Vampire: The Masquerade and Storyteller System

---

#### Vincent Baker

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Vincent Baker") OR contains(string(designer), "D. Vincent Baker")
SORT year-published ASC
```

[[Vincent Baker]] - Creator of Apocalypse World and PbtA framework

---

#### John Harper

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "John Harper")
SORT year-published ASC
```

[[John Harper]] - Creator of Blades in the Dark and FitD framework

---

#### Monte Cook

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Monte Cook")
SORT year-published ASC
```

[[Monte Cook]] - D&D 3E designer, Numenera creator, Cypher System architect

---

#### Jonathan Tweet

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Jonathan Tweet")
SORT year-published ASC
```

[[Jonathan Tweet]] - D&D 3E co-designer, Over the Edge, Ars Magica

---

#### Robin D. Laws

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Robin") AND contains(string(designer), "Laws")
SORT year-published ASC
```

[[Robin D. Laws]] - GUMSHOE System creator, Feng Shui, HeroQuest

---

#### Ken Hite

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Ken Hite") OR contains(string(designer), "Kenneth Hite")
SORT year-published ASC
```

[[Ken Hite]] - Night's Black Agents, Trail of Cthulhu, GURPS Infinite Worlds

---

#### Sandy Petersen

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Sandy Petersen")
SORT year-published ASC
```

[[Sandy Petersen]] - Creator of Call of Cthulhu, Lovecraftian gaming pioneer

---

#### Greg Stafford

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Greg Stafford")
SORT year-published ASC
```

[[Greg Stafford]] - Creator of Glorantha, RuneQuest, Pendragon, King Arthur Pendragon

---

#### Steve Jackson

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Steve Jackson")
SORT year-published ASC
```

[[Steve Jackson]] - GURPS creator, Munchkin, Car Wars

---

#### Mike Pondsmith

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Mike Pondsmith")
SORT year-published ASC
```

[[Mike Pondsmith]] - Creator of Cyberpunk 2020, Castle Falkenstein

---

#### Luke Crane

```dataview
TABLE year-published AS "Year", file.link AS "Game", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE contains(string(designer), "Luke Crane")
SORT year-published ASC
```

[[Luke Crane]] - Creator of Burning Wheel, Mouse Guard, Torchbearer

---

## Design Philosophies

### Narrative-Focused Designers

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Games",
  active-years AS "Active"
FROM "Designers"
WHERE contains(string(design-philosophy), "narrative") OR contains(string(design-philosophy), "story")
SORT file.name ASC
```

### Simulation-Focused Designers

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Games",
  active-years AS "Active"
FROM "Designers"
WHERE contains(string(design-philosophy), "simulation") OR contains(string(design-philosophy), "realism")
SORT file.name ASC
```

### Mechanics-Focused Designers

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Games",
  active-years AS "Active"
FROM "Designers"
WHERE contains(string(design-philosophy), "mechanics") OR contains(string(design-philosophy), "system")
SORT file.name ASC
```

### OSR Movement Designers

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Games",
  active-years AS "Active"
FROM "Designers"
WHERE contains(string(tags), "OSR") OR contains(string(design-philosophy), "old-school")
SORT file.name ASC
```

---

## Collaborative Partnerships

### Famous Design Duos

**Gygax & Arneson** - Created D&D together
- [[Gary Gygax]] + [[Dave Arneson]] = [[Dungeons & Dragons]]

**Cook & Tweet** - D&D 3rd Edition architects
- [[Monte Cook]] + [[Jonathan Tweet]] = [[D&D 3rd Edition]]

**Laws & Tweet** - Over the Edge innovators
- [[Robin D. Laws]] + [[Jonathan Tweet]] = [[Over the Edge]]

**Baker & Baker** - Apocalypse World creative team
- [[Vincent Baker]] + [[Meguey Baker]] = [[Apocalypse World]]

---

## By Generation

### First Generation (1970s Origins)

```dataview
TABLE
  file.link AS "Designer",
  birth-year AS "Born",
  LIST(notable-works, 3) AS "Pioneering Works"
FROM "Designers"
WHERE active-years != null AND contains(string(active-years), "197")
SORT birth-year ASC
```

**Characteristics:** Wargaming roots, experimental, foundational mechanics

---

### Second Generation (1980s Expansion)

```dataview
TABLE
  file.link AS "Designer",
  birth-year AS "Born",
  LIST(notable-works, 3) AS "Key Works"
FROM "Designers"
WHERE active-years != null AND contains(string(active-years), "198")
SORT birth-year ASC
```

**Characteristics:** Genre diversification, professional approach, alternative systems

---

### Third Generation (1990s Innovation)

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Works"
FROM "Designers"
WHERE active-years != null AND contains(string(active-years), "199")
SORT file.name ASC
```

**Characteristics:** Narrative focus, indie movement begins, diceless and experimental mechanics

---

### Fourth Generation (2000s Renaissance)

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Works"
FROM "Designers"
WHERE active-years != null AND contains(string(active-years), "200")
SORT file.name ASC
```

**Characteristics:** The Forge theory, PbtA revolution, OSR movement, Kickstarter era

---

### Fifth Generation (2010s-Present Modern Era)

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Works"
FROM "Designers"
WHERE active-years != null AND (contains(string(active-years), "201") OR contains(string(active-years), "202"))
SORT file.name ASC
```

**Characteristics:** Diverse voices, safety tools, hybrid play, mainstream acceptance

---

## By Geographic Origin

### American Designers

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Works",
  influence-score AS "Influence"
FROM "Designers"
WHERE nationality = "American" OR nationality = "USA"
SORT influence-score DESC, file.name ASC
```

### British Designers

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Key Works",
  influence-score AS "Influence"
FROM "Designers"
WHERE nationality = "British" OR nationality = "UK" OR nationality = "English"
SORT file.name ASC
```

### European Designers

```dataview
TABLE
  file.link AS "Designer",
  nationality AS "Country",
  LIST(notable-works, 3) AS "Key Works"
FROM "Designers"
WHERE nationality != null AND nationality != "American" AND nationality != "USA" AND nationality != "British" AND nationality != "UK"
SORT nationality ASC, file.name ASC
```

---

## Most Prolific Designers

### By Number of Notable Works

```dataview
TABLE
  file.link AS "Designer",
  length(notable-works) AS "# Games",
  LIST(notable-works, 6) AS "Notable Works",
  active-years AS "Career Span"
FROM "Designers"
WHERE notable-works != null
SORT length(notable-works) DESC
LIMIT 20
```

---

## Career Longevity

### Still Active (40+ Years)

```dataview
TABLE
  file.link AS "Designer",
  active-years AS "Career Span",
  LIST(notable-works, 4) AS "Key Works Across Decades"
FROM "Designers"
WHERE contains(string(active-years), "197") AND contains(string(active-years), "20")
SORT file.name ASC
```

---

## Design Influence Networks

### Who Influenced Whom

View the complete influence network:
- **[[Designer-Influence-Network]]** - Interactive relationship map

Generate influence visualizations:
```bash
python3 Scripts/analytics/influence_network.py
```

**Output:** `Attachments/Diagrams/analytics/influence_network.png`

---

## By Awards and Recognition

### ENnie Award Winners

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Award-Winning Works",
  influence-score AS "Industry Impact"
FROM "Designers"
WHERE contains(string(tags), "award") OR contains(string(tags), "ENnie")
SORT file.name ASC
```

### Origins Award Winners

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 3) AS "Award-Winning Works",
  influence-score AS "Industry Impact"
FROM "Designers"
WHERE contains(string(tags), "Origins")
SORT file.name ASC
```

---

## System Innovators

### Creators of Major Systems

**d20 Family:**
- [[Monte Cook]], [[Jonathan Tweet]], [[Skip Williams]] - D&D 3E/d20 System

**Storyteller System:**
- [[Mark Rein-Hagen]] - Vampire, World of Darkness

**PbtA (Powered by the Apocalypse):**
- [[Vincent Baker]], [[Meguey Baker]] - Apocalypse World

**FitD (Forged in the Dark):**
- [[John Harper]] - Blades in the Dark

**FATE:**
- [[Fred Hicks]], [[Rob Donoghue]] - FATE System

**GUMSHOE:**
- [[Robin D. Laws]] - GUMSHOE investigative system

**Cypher System:**
- [[Monte Cook]] - Numenera, The Strange

**Year Zero Engine:**
- [[Tomas Härenstam]] - Mutant: Year Zero, Tales from the Loop

---

## Random Designer Discovery

### Discover a Random Creator

```dataview
TABLE
  file.link AS "Designer",
  LIST(notable-works, 4) AS "Notable Works",
  design-philosophy AS "Philosophy",
  influence-score AS "Influence"
FROM "Designers"
SORT random()
LIMIT 1
```

---

## Search Tips

**Find specific designer:** Use Quick Switcher (Cmd/Ctrl + O) or search this page

**Explore design lineages:** Follow wikilinks to see influences and collaborations

**Compare philosophies:** Use the philosophy sections to find like-minded creators

**Track evolution:** Use Games-by-Year to see how designers evolved over time

---

## Related Resources

### Alternative Views

- **[[Games-by-Year]]** - Chronological timeline
- **[[Games-by-Publisher]]** - Company catalog
- **[[Games-by-System]]** - Mechanical families
- **[[MASTER-INDEX]]** - Complete A-Z reference

### Deep Dives

- **[[Designer-Influence-Network]]** - Creative relationship mapping
- **[[Design-Philosophy-Guide]]** - Schools of thought in TTRPG design
- **[[Historical Context]]** - Era-by-era designer movements

---

**🎲 The creative minds behind 50 years of roleplaying games 🎲**

*Explore how individual designers shaped the evolution of tabletop roleplaying through their visions, philosophies, and innovations.*

---

*Last updated: October 2025*
*Version: 4.0*
*Vault Status: Production-Ready*
