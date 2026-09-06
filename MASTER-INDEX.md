# 🎲 TTRPG History Vault - Master Index

**The Complete A-Z Reference Guide**

---

## Purpose

This master index provides alphabetical access to all content in the TTRPG History Vault. Use this when you know what you're looking for and want direct access.

---

## Navigation

- **[[TTRPG-History-Dashboard]]** - Main visual dashboard
- **[[START-HERE]]** - Quick start guide
- **[[Games-by-Year]]** - Chronological index
- **[[Games-by-Designer]]** - Creator index
- **[[Games-by-System]]** - Mechanical index

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

- **START-HERE.md** - New user orientation
- **README.md** - Technical overview
- **CONTRIBUTING.md** - Content guidelines
- **QUALITY-STANDARDS.md** - Entry requirements

### Indexes

- **Games-by-Year.md** - Chronological timeline
- **Games-by-Designer.md** - Creator catalog
- **Games-by-Publisher.md** - Company catalog
- **Games-by-System.md** - Mechanical families

### Tools

- **Scripts/analytics/** - 8 analysis tools
- **Scripts/export/** - 5 export formats
- **Scripts/quality_enhancer.py** - Improvement tool
- **Scripts/bibliography_generator.py** - Citation tool

---

**🎲 Complete A-Z access to 309+ entries covering 50 years of TTRPG history 🎲**

*Use Cmd/Ctrl + F to search this index, or use the specialized indexes for attribute-based browsing.*

---

*Last updated: October 2025*
*Version: 4.0*
*Vault Status: Production-Ready*
