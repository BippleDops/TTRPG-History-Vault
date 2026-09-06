# 🎲 Games by Year - Chronological Timeline

**Browse TTRPG history from 1974 to the present**

---

## Purpose

This index presents all games in the vault in chronological order, allowing you to explore the evolution of tabletop roleplaying games decade by decade and year by year.

---

## Navigation

- **[[TTRPG-History-Dashboard]]** - Main visual dashboard
- **[[START-HERE]]** - Quick start guide
- **[[MASTER-INDEX]]** - Complete A-Z reference
- **[[Games-by-Designer]]** - Creator index
- **[[Games-by-System]]** - Mechanical index

---

## Complete Chronological Timeline

### All Games by Year

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", system AS "System", genre AS "Genre"
FROM "Games"
WHERE year-published != null
SORT year-published ASC, file.name ASC
```

---

## By Decade

### 1970s - The Dawn Era

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", historical-significance AS "Significance"
FROM "Games"
WHERE year-published >= 1970 AND year-published < 1980
SORT year-published ASC
```

**Era Context:** [[Historical Context/The Dawn Era (1974-1979)]]

**Defining Characteristics:**
- Birth of the hobby
- Wargaming roots
- Experimental mechanics
- Small publisher scene

---

### 1980s - The Golden Age

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", historical-significance AS "Significance"
FROM "Games"
WHERE year-published >= 1980 AND year-published < 1990
SORT year-published ASC
```

**Era Context:** [[Historical Context/The Golden Age (1980-1989)]]

**Defining Characteristics:**
- TSR dominance
- Genre explosion (sci-fi, horror, superhero)
- Satanic Panic
- International expansion

---

### 1990s - The Storyteller Revolution

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", historical-significance AS "Significance"
FROM "Games"
WHERE year-published >= 1990 AND year-published < 2000
SORT year-published ASC
```

**Era Context:** [[Historical Context/The Storyteller Revolution (1990-1999)]]

**Defining Characteristics:**
- White Wolf and narrative focus
- Collectible card games emerge
- Live action roleplaying grows
- Alternative game theory

---

### 2000s - The d20 Boom

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", historical-significance AS "Significance"
FROM "Games"
WHERE year-published >= 2000 AND year-published < 2010
SORT year-published ASC
```

**Era Context:** [[Historical Context/The d20 Boom (2000-2007)]]

**Defining Characteristics:**
- Open Gaming License
- D&D 3rd Edition revolution
- d20 System proliferation
- Digital tools emerge

---

### 2010s - The Modern Renaissance

#### Early 2010s - OSR & Indie Explosion (2010-2014)

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 2010 AND year-published < 2015
SORT year-published ASC
```

**Era Context:** [[Historical Context/The OSR Renaissance (2006-2014)]] and [[Historical Context/The Indie Explosion (2008-2015)]]

**Defining Characteristics:**
- Old School Renaissance movement
- Kickstarter revolutionizes funding
- Indie games flourish
- Narrative mechanics innovation

#### Mid-Late 2010s - Fifth Edition Era (2014-2020)

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 2014 AND year-published < 2020
SORT year-published ASC
```

**Era Context:** [[Historical Context/The Fifth Edition Era (2014-2020)]]

**Defining Characteristics:**
- D&D 5E dominates market
- Actual play shows explode (Critical Role)
- PbtA and FitD families grow
- Mainstream acceptance

---

### 2020s - The Modern Landscape

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", publisher AS "Publisher", innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 2020
SORT year-published ASC
```

**Era Context:** [[Historical Context/The Modern Landscape (2020-Present)]]

**Defining Characteristics:**
- Pandemic shifts to online play
- VTT platforms mature
- Diversity and inclusion focus
- Hybrid digital/analog games
- Safety tools standardized

---

## By Publication Volume

### Most Productive Years

```dataview
TABLE
  year-published AS "Year",
  COUNT(file.link) AS "# Games Published",
  LIST(file.link, 8) AS "Games Released"
FROM "Games"
WHERE year-published != null
GROUP BY year-published
SORT COUNT(file.link) DESC
LIMIT 15
```

---

## By Historical Significance

### Landmark Years (5+ significant games)

```dataview
TABLE
  year-published AS "Year",
  COUNT(file.link) AS "Major Releases",
  LIST(file.link, 10) AS "Significant Games"
FROM "Games"
WHERE historical-significance >= 4
GROUP BY year-published
SORT year-published ASC
```

---

## By Innovation

### Most Innovative Years

```dataview
TABLE
  year-published AS "Year",
  COUNT(file.link) AS "# Innovative Games",
  LIST(file.link, 8) AS "Groundbreaking Releases"
FROM "Games"
WHERE innovation-score >= 4
GROUP BY year-published
SORT COUNT(file.link) DESC
LIMIT 12
```

---

## Key Milestones by Year

### Industry-Defining Moments

**1974** - [[Dungeons & Dragons]] launches, creating the TTRPG hobby
**1977** - [[Traveller]] establishes lifepath character creation
**1978** - [[RuneQuest]] introduces percentile skills
**1981** - [[Call of Cthulhu]] brings horror to tabletop
**1983** - [[Ars Magica]] creates troupe play
**1987** - [[GURPS]] unifies universal mechanics
**1989** - [[Shadowrun]] blends cyberpunk and fantasy
**1991** - [[Vampire: The Masquerade]] starts Storyteller System
**1997** - [[Dying Earth]] introduces resource pool mechanics
**2000** - [[D&D 3rd Edition]] and OGL revolutionize industry
**2004** - [[FATE]] creates aspect-based narrative mechanics
**2008** - [[Apocalypse World]] launches PbtA revolution
**2011** - [[Fiasco]] proves GM-less games can succeed
**2012** - [[Dungeon World]] brings PbtA to fantasy
**2014** - [[D&D 5th Edition]] achieves mainstream success
**2017** - [[Blades in the Dark]] creates FitD framework
**2019** - Critical Role reaches 100 million views
**2020** - Pandemic accelerates VTT adoption

---

## Timeline Visualizations

### Generate Timeline Charts

Run analytics to create visual timelines:

```bash
python3 Scripts/analytics/publication_trends.py
python3 Scripts/analytics/innovation_timeline.py
```

**Output:** `Attachments/Diagrams/analytics/`

---

## By Genre Over Time

### Fantasy Games by Decade

```dataview
TABLE
  floor(year-published / 10) * 10 + "s" AS "Decade",
  COUNT(file.link) AS "# Fantasy Games",
  LIST(file.link, 5) AS "Examples"
FROM "Games"
WHERE contains(string(genre), "fantasy") AND year-published != null
GROUP BY floor(year-published / 10) * 10
SORT floor(year-published / 10) * 10 ASC
```

### Science Fiction Games by Decade

```dataview
TABLE
  floor(year-published / 10) * 10 + "s" AS "Decade",
  COUNT(file.link) AS "# Sci-Fi Games",
  LIST(file.link, 5) AS "Examples"
FROM "Games"
WHERE (contains(string(genre), "science fiction") OR contains(string(genre), "sci-fi")) AND year-published != null
GROUP BY floor(year-published / 10) * 10
SORT floor(year-published / 10) * 10 ASC
```

### Horror Games by Decade

```dataview
TABLE
  floor(year-published / 10) * 10 + "s" AS "Decade",
  COUNT(file.link) AS "# Horror Games",
  LIST(file.link, 5) AS "Examples"
FROM "Games"
WHERE contains(string(genre), "horror") AND year-published != null
GROUP BY floor(year-published / 10) * 10
SORT floor(year-published / 10) * 10 ASC
```

---

## Search Tips

**Find games by specific year:** Use Quick Switcher (Cmd/Ctrl + O) or search this page with Cmd/Ctrl + F

**Compare eras:** Use the decade sections above to see trends

**Track innovation:** Check the innovation score columns to identify groundbreaking designs

**Explore influences:** Follow wikilinks to see how games influenced each other chronologically

---

## Related Resources

### Historical Context

- **[[Historical Context]]** - Browse 8 comprehensive era entries
- **[[Designer-Influence-Network]]** - See creative relationships over time
- **[[System-Family-Trees]]** - Track mechanical evolution

### Alternative Views

- **[[Games-by-Designer]]** - Browse by creator
- **[[Games-by-Publisher]]** - Browse by company
- **[[Games-by-System]]** - Browse by mechanical family
- **[[MASTER-INDEX]]** - Complete A-Z reference

---

**🎲 50 years of TTRPG evolution - from 1974 to the present 🎲**

*Use this timeline to explore how game design, themes, and mechanics have evolved over five decades of tabletop roleplaying.*

---

*Last updated: October 2025*
*Version: 4.0*
*Vault Status: Production-Ready*
