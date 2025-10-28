---
tags:
  - dashboard
  - moc
  - index
---

# TTRPG History Vault: Main Dashboard

Welcome to the comprehensive TTRPG History Tracking Vault. This dashboard serves as your central navigation hub for exploring the complete history of tabletop roleplaying games from 1974 to present.

## Vault Statistics

```datacore
TABLE WITHOUT ID
  length(rows) AS "Count"
FROM "Games" OR "Publishers" OR "Designers" OR "Mechanics" OR "Historical Context"
GROUP BY type AS "Category"
SORT Category ASC
```

**Current Vault Contents**:
- **Games**: 20 landmark titles documented
- **Publishers**: 15 major publishers profiled
- **Designers**: 16 influential creators detailed
- **Mechanics**: 3 foundational systems analyzed
- **Historical Events**: 3 pivotal moments chronicled

---

## Era Navigation

Explore TTRPG history by historical period:

### [[Early Era MOC|📜 Early Era (1974-1985)]]
The birth of roleplaying games, from D&D's creation through TSR's dominance.

### [[Golden Age MOC|⭐ Golden Age (1985-2000)]]
Genre expansion, White Wolf's rise, and the diversification of the RPG market.

### [[d20 Era MOC|🎲 d20 Era (2000-2008)]]
The Open Gaming License explosion and D&D's reinvention.

### [[OSR Revival MOC|🔄 OSR Revival (2008-2015)]]
Old School Renaissance and indie game innovation.

### [[Modern Era MOC|🌟 Modern Era (2015-Present)]]
D&D's mainstream breakthrough and the contemporary RPG renaissance.

---

## Quick Access: Database Views

### Core Databases
- **[[All-Games.base|📚 All Games Database]]** - Complete game catalog with filtering
- **[[Publishers.base|🏢 Publishers View]]** - Publishing companies and imprints
- **[[Designers.base|👤 Designers View]]** - Game creators and contributors
- **[[Innovations.base|💡 Mechanics Timeline]]** - Design innovations over time
- **[[By-Decade.base|📅 Games by Decade]]** - Historical progression view
- **[[Historical-Events.base|📰 Historical Events]]** - Major moments in TTRPG history

---

## Recent Additions

```datacore
TABLE
  file.link AS "Entry",
  type AS "Type",
  year-published AS "Year",
  file.mtime AS "Added"
FROM "Games" OR "Publishers" OR "Designers" OR "Mechanics" OR "Historical Context"
WHERE file.name != "TTRPG-History-Dashboard"
SORT file.mtime DESC
LIMIT 10
```

---

## Highest Significance Games

Games rated 5/5 for historical significance:

```datacore
TABLE
  file.link AS "Game",
  year-published AS "Year",
  publisher AS "Publisher",
  designer AS "Designer",
  innovation-score AS "Innovation"
FROM "Games"
WHERE historical-significance = 5
SORT year-published ASC
```

---

## Most Influential Publishers

Publishers by significance rating:

```datacore
TABLE
  file.link AS "Publisher",
  founded AS "Founded",
  era-active AS "Era",
  headquarters AS "Location"
FROM "Publishers"
WHERE significance >= 4
SORT significance DESC, founded ASC
```

---

## Key Mechanical Innovations

Foundational mechanics that shaped the industry:

```datacore
TABLE
  file.link AS "Mechanic",
  year-introduced AS "Year",
  first-appearance AS "Debuted In",
  popularity AS "Adoption"
FROM "Mechanics"
SORT year-introduced ASC
```

---

## Pivotal Historical Events

Major moments that transformed the industry:

```datacore
TABLE
  file.link AS "Event",
  year AS "Year",
  date AS "Date",
  significance AS "Impact"
FROM "Historical Context"
SORT year ASC
```

---

## Browse by Category

### Games
- **[[All-Games.base|All Games]]** - Complete catalog
- **By Genre**: Fantasy • Horror • Sci-Fi • Modern
- **By System**: d20 • Percentile • PBTA • Story Games
- **By Era**: 1970s • 1980s • 1990s • 2000s • 2010s • 2020s

### People & Organizations
- **[[Designers.base|Designers]]** - Game creators and their legacies
- **[[Publishers.base|Publishers]]** - Companies that shaped the industry
- **Historical Figures**: Gygax • Petersen • Rein-Hagen • Baker

### Systems & Mechanics
- **[[Innovations.base|Innovations Timeline]]** - When mechanics were introduced
- **Core Systems**: d20 • Percentile • Dice Pools • PBTA
- **Design Movements**: OSR • Story Games • Trad Games

### Historical Context
- **[[Historical-Events.base|Major Events]]** - Industry-changing moments
- **Eras**: Early • Golden Age • d20 Boom • OSR • Modern
- **Controversies**: Satanic Panic • OGL Drama • Industry Shifts

---

## Research & Documentation

### Templates
Access templates for adding new entries:
- **[[Game Entry Template]]** - Document new games
- **[[Publisher Template]]** - Profile publishers
- **[[Designer Template]]** - Chronicle designers
- **[[Mechanics Documentation Template]]** - Analyze mechanics
- **[[Historical Event Template]]** - Record pivotal moments
- **[[Web Archive Template]]** - Save research sources

### Reference Materials
- **[[Property-Schema|📋 Property Schema Reference]]** - Complete metadata guide
- **[[Query-Library|🔍 Query Library]]** - Datacore query examples
- **[[README]]** - Vault documentation and usage guide

---

## Validation & Maintenance

### Data Quality Checks

**Games Missing Core Properties**:
```datacore
TABLE file.link AS "Game"
FROM "Games"
WHERE !publisher OR !designer OR !year-published
```

**Publishers Without Key Releases**:
```datacore
TABLE file.link AS "Publisher"
FROM "Publishers"
WHERE !key-releases OR length(key-releases) = 0
```

---

## Statistics & Insights

### Games by Decade

```datacore
TABLE
  length(rows) AS "Count",
  round(avg(rows.historical-significance), 1) AS "Avg Significance",
  round(avg(rows.innovation-score), 1) AS "Avg Innovation"
FROM "Games"
WHERE year-published
GROUP BY floor(year-published / 10) * 10 + "s" AS "Decade"
SORT Decade ASC
```

### Most Prolific Publishers

```datacore
TABLE
  file.link AS "Publisher",
  length(key-releases) AS "Games Published",
  founded AS "Founded",
  era-active AS "Era"
FROM "Publishers"
WHERE key-releases
SORT length(key-releases) DESC
LIMIT 10
```

---

## Getting Started

### New to the Vault?
1. **Explore** the [[All-Games.base|All Games Database]] to see what's documented
2. **Browse** by [[Early Era MOC|historical era]] to understand TTRPG evolution
3. **Read** the [[README]] for detailed vault documentation
4. **Use** the templates to add your own entries
5. **Query** the database using the [[Query-Library|Query Library]] examples

### Adding Content
- Use Ctrl/Cmd + N to create a new note
- Navigate to the appropriate folder (Games, Publishers, etc.)
- Select the relevant template (if auto-templates are configured)
- Fill in the metadata and content sections
- Link to related entries using [[wikilinks]]

### Research Workflow
1. **Research** games, publishers, designers using web sources
2. **Archive** sources using the [[Web Archive Template]]
3. **Document** findings in appropriate entry types
4. **Link** entries together to build knowledge graph
5. **Query** connections using Datacore and Bases

---

## Quick Links

**Most Referenced Games**:
- [[Dungeons & Dragons (1974)]] - The foundation of all TTRPGs
- [[Call of Cthulhu (1981)]] - Horror gaming pioneer
- [[Vampire - The Masquerade (1991)]] - Story-focused revolution
- [[Dungeons & Dragons Third Edition (2000)]] - The d20 System
- [[Apocalypse World (2010)]] - PbtA framework creation

**Essential Publishers**:
- [[TSR]] - Founded the industry
- [[Wizards of the Coast]] - Modern D&D steward
- [[Chaosium]] - Horror and percentile systems
- [[White Wolf Publishing]] - World of Darkness creator
- [[Lumpley Games]] - Indie innovation leader

**Legendary Designers**:
- [[Gary Gygax]] - D&D co-creator
- [[Sandy Petersen]] - Call of Cthulhu designer
- [[Mark Rein-Hagen]] - Vampire creator
- [[D. Vincent Baker]] - PbtA framework architect

---

*This vault documents the rich history of tabletop roleplaying games. Every entry, link, and query helps build a comprehensive knowledge base of this transformative entertainment medium.*

**Last Updated**: December 2024
