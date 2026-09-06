# 🎲 TTRPG History Vault - Master Index

**The Complete A-Z Reference Guide**

---

## Purpose

This master index provides alphabetical access to all content in the TTRPG History Vault. Use this when you know what you're looking for and want direct access.

---

## Navigation

- **[[README]]** - Overview, setup and orientation (read this first)
- **[[TTRPG-History-Dashboard]]** - In-vault dashboard: era navigation, database views, highlights
- **[[Games-by-Year]]** - Chronological index
- **[[Games-by-Designer]]** - Creator index
- **[[Games-by-System]]** - Mechanical index
- **Era MOCs**: [[Early Era MOC]] · [[Golden Age MOC]] · [[d20 Era MOC]] · [[OSR Revival MOC]] · [[Modern Era MOC]]

---

## Complete Alphabetical Index

### Games (A-Z)

```dataview
TABLE year-published AS "Year", designer AS "Designer", publisher AS "Publisher", system AS "System"
FROM "Games"
SORT file.name ASC
```

---

### Designers (A-Z)

```dataview
TABLE birth-year AS "Born", nationality AS "From", LIST(notable-works, 3) AS "Notable Works", active-years AS "Years Active"
FROM "Designers"
SORT file.name ASC
```

---

### Publishers (A-Z)

```dataview
TABLE founded AS "Founded", headquarters AS "HQ", status AS "Status", LIST(key-releases, 3) AS "Key Releases"
FROM "Publishers"
SORT file.name ASC
```

---

### Mechanics (A-Z)

```dataview
TABLE introduced-in AS "First Used", popularized-by AS "Made Famous By", complexity AS "Complexity", innovation-score AS "Innovation"
FROM "Mechanics"
SORT file.name ASC
```

---

### Historical Eras (Chronological)

```dataview
TABLE date-range AS "Years", LIST(defining-games, 5) AS "Defining Games", LIST(key-designers, 5) AS "Key Designers"
FROM "Historical Context"
SORT file.name ASC
```

---

### Controversies (Chronological)

```dataview
TABLE year AS "Year", involved-parties AS "Parties Involved", impact AS "Impact"
FROM "Controversies"
SORT year ASC
```

---

### Supplements (A-Z)

```dataview
TABLE year-published AS "Year", game-line AS "Game Line", publisher AS "Publisher"
FROM "Supplements"
SORT file.name ASC
```

---

### Campaign Settings (A-Z)

```dataview
TABLE year-published AS "Year", game-system AS "System", publisher AS "Publisher", genre AS "Genre"
FROM "Settings"
SORT file.name ASC
```

---

### Retroclones / OSR (A-Z)

```dataview
TABLE year-published AS "Year", retro-clone-of AS "Clones", designer AS "Designer", osr-generation AS "Generation"
FROM "Retroclones"
SORT file.name ASC
```

---

### VTT Platforms (A-Z)

```dataview
TABLE launched AS "Launched", type AS "Type", status AS "Status", pricing-model AS "Pricing"
FROM "VTT Platforms"
SORT file.name ASC
```

---

### Actual Play Shows (A-Z)

```dataview
TABLE start-year AS "Started", network AS "Network", game-system AS "System", status AS "Status"
FROM "Actual Play"
SORT file.name ASC
```

---

## Cross-Reference by Tags

### Most Common Tags

```dataview
TABLE
  tag AS "Tag",
  length(rows) AS "# Entries"
FROM "Games" OR FROM "Designers" OR FROM "Publishers"
FLATTEN file.tags AS tag
WHERE tag != null
GROUP BY tag
SORT length(rows) DESC
LIMIT 50
```

---

## By Historical Significance

### Highly Significant (5/5)

```dataview
TABLE file.link AS "Entry", type AS "Type", year-published AS "Year", innovation-score AS "Innovation"
FROM "Games" OR FROM "Mechanics"
WHERE historical-significance = 5 OR innovation-score = 5
SORT year-published ASC
```

### Significant (4/5)

```dataview
TABLE file.link AS "Entry", type AS "Type", year-published AS "Year", innovation-score AS "Innovation"
FROM "Games" OR FROM "Mechanics"
WHERE historical-significance = 4 OR innovation-score = 4
SORT year-published ASC
```

---

## By Status

### Active / In-Print

```dataview
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE status = "active" OR status = "in-print"
SORT year-published DESC
```

### Out of Print

```dataview
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher", system AS "System"
FROM "Games"
WHERE status = "out-of-print"
SORT year-published ASC
```

---

## By Complexity

### Beginner-Friendly (1-2)

```dataview
TABLE file.link AS "Game", complexity AS "Level", year-published AS "Year", system AS "System"
FROM "Games"
WHERE complexity <= 2 AND complexity != null
SORT complexity ASC, file.name ASC
```

### Intermediate (3)

```dataview
TABLE file.link AS "Game", complexity AS "Level", year-published AS "Year", system AS "System"
FROM "Games"
WHERE complexity = 3
SORT file.name ASC
```

### Advanced (4-5)

```dataview
TABLE file.link AS "Game", complexity AS "Level", year-published AS "Year", system AS "System"
FROM "Games"
WHERE complexity >= 4 AND complexity != null
SORT complexity DESC, file.name ASC
```

---

## By Genre

### Fantasy

```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System", complexity AS "Complexity"
FROM "Games"
WHERE contains(string(genre), "fantasy")
SORT year-published ASC
LIMIT 30
```

### Science Fiction

```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System", complexity AS "Complexity"
FROM "Games"
WHERE contains(string(genre), "science fiction") OR contains(string(genre), "sci-fi")
SORT year-published ASC
LIMIT 30
```

### Horror

```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System", complexity AS "Complexity"
FROM "Games"
WHERE contains(string(genre), "horror")
SORT year-published ASC
LIMIT 30
```

### Superhero

```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System", complexity AS "Complexity"
FROM "Games"
WHERE contains(string(genre), "superhero")
SORT year-published ASC
```

---

## By Movement

### OSR (Old School Renaissance)

```dataview
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer"
FROM "Games" OR "Retroclones"
WHERE contains(string(tags), "OSR") OR type = "retroclone"
SORT year-published ASC
```

### Story Games and Narrative Design

```dataview
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", game-structure AS "Structure"
FROM "Games"
WHERE contains(string(tags), "story-game") OR contains(string(tags), "narrative") OR contains(string(tags), "GM-less")
SORT year-published ASC
```

### Powered by the Apocalypse

```dataview
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", genre AS "Genre"
FROM "Games"
WHERE contains(string(system), "PbtA") OR contains(string(influenced-by), "Apocalypse World")
SORT year-published ASC
```

### Forged in the Dark

```dataview
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", setting AS "Setting"
FROM "Games"
WHERE contains(string(system), "FitD") OR contains(string(influenced-by), "Blades in the Dark")
SORT year-published ASC
```

---

## By Game System

```dataview
TABLE system AS "System Family", length(rows) AS "# Games"
FROM "Games"
WHERE system != null AND system != ""
GROUP BY system
SORT length(rows) DESC
LIMIT 20
```

---

## Highlights

### Most Influential Designers

```dataview
TABLE file.link AS "Designer", influence-score AS "Influence", notable-works AS "Key Works", active-years AS "Active"
FROM "Designers"
WHERE influence-score >= 4
SORT influence-score DESC, file.name ASC
LIMIT 12
```

### Most Innovative Mechanics (5/5)

```dataview
TABLE file.link AS "Mechanic", introduced-in AS "First Appeared In", popularized-by AS "Popularized By"
FROM "Mechanics"
WHERE innovation-score = 5
SORT file.name ASC
```

### Recent Additions

```dataview
TABLE file.mtime AS "Modified", file.link AS "Entry", type AS "Type"
FROM "Games" OR "Designers" OR "Publishers"
SORT file.mtime DESC
LIMIT 10
```

---

## Quick Statistics

### Total Entries by Type

```dataview
TABLE type AS "Entry Type", COUNT(file.link) AS "Count"
FROM "Games" OR FROM "Designers" OR FROM "Publishers" OR FROM "Mechanics" OR FROM "Historical Context"
WHERE type != null
GROUP BY type
SORT COUNT(file.link) DESC
```

### Coverage by Decade

```dataview
TABLE
  decade + "s" AS "Decade",
  COUNT(file.link) AS "Games"
FROM "Games"
WHERE year-published != null
FLATTEN floor(year-published / 10) * 10 AS decade
GROUP BY decade
SORT decade ASC
```

### Geographic Distribution

```dataview
TABLE nationality AS "Country", COUNT(file.link) AS "# Designers"
FROM "Designers"
WHERE nationality != null AND nationality != ""
GROUP BY nationality
SORT COUNT(file.link) DESC
```

---

## Search Tips

**By Name:** Use Quick Switcher (Cmd/Ctrl + O) to jump directly to any entry

**By Content:** Use Search (Cmd/Ctrl + Shift + F) to find text across all entries

**By Attribute:** Use this index or the specialized indexes (by-year, by-designer, by-system)

**By Relationship:** Follow wikilinks within entries to explore connections

**By Query:** Use Dataview queries to create custom filtered views

---

## Related Resources

### Documentation

- **[[README]]** - Overview, setup, orientation
- **[[CONTRIBUTING]]** - Content guidelines and licensing of contributions
- **[[QUALITY-STANDARDS]]** - Entry requirements
- **[[CHANGELOG]]** - Dated history of the repository
- **[[Property-Schema]]** - Every property, per entry type
- **[[Query-Library]]** and **[[QUERY-COOKBOOK]]** - Dataview query patterns

### Indexes

- **[[Games-by-Year]]** - Chronological timeline
- **[[Games-by-Designer]]** - Creator catalog
- **[[Games-by-System]]** - Mechanical families
- **[[TTRPG-History-Dashboard]]** - Era MOCs and database views

### Tools

- **Scripts/analytics/** - 8 analysis tools
- **Scripts/export/** - 5 export formats
- **Scripts/link_validator.py**, **schema_validator.py**, **reciprocal_link_checker.py** - Validators
- **Scripts/quality_enhancer.py** - Improvement tool
- **Scripts/bibliography_generator.py** - Citation tool

See the README's *Scripts* section for usage.

---

**🎲 Complete A-Z access to 449 entries covering 50 years of TTRPG history 🎲**

*Use Cmd/Ctrl + F to search this index, or use the specialized indexes for attribute-based browsing.*

---

*Last updated: September 2026 (repair release — see [[CHANGELOG]])*
