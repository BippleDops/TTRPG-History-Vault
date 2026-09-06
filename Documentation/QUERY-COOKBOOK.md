---
tags:
  - reference
  - queries
  - dataview
  - examples
---

# Dataview Query Cookbook

Practical, copy-paste-ready Dataview queries for common research tasks in the TTRPG History Vault. All queries use Dataview Query Language (DQL) inside ```` ```dataview ```` fences, with explicit column aliases.

---

## Quick Reference

- [Games Queries](#games-queries)
- [Publisher Queries](#publisher-queries)
- [Designer Queries](#designer-queries)
- [Relationship Queries](#relationship-queries)
- [Historical Analysis](#historical-analysis)
- [Statistical Queries](#statistical-queries)
- [Validation Queries](#validation-queries)
- [Dashboard Queries](#dashboard-queries)

---

## Games Queries

### All Games by Year

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  publisher AS "Publisher",
  system AS "System"
FROM "Games"
SORT year-published ASC
```

### Highly Significant Games

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  historical-significance AS "Significance",
  innovation-score AS "Innovation"
FROM "Games"
WHERE historical-significance >= 4
SORT historical-significance DESC, year-published ASC
```

### Games by Genre

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  publisher AS "Publisher",
  complexity AS "Complexity"
FROM "Games"
WHERE contains(genre, "horror")
SORT year-published ASC
```

**Modify for other genres**: Replace `"horror"` with `"fantasy"`, `"sci-fi"`, `"modern"`, etc.

### Games by System Type

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  complexity AS "Complexity"
FROM "Games"
WHERE system = "d20"
SORT year-published ASC
```

**Other systems**: `"percentile"`, `"pbta"`, `"fitd"`, `"osr"`, `"story-game"`

### Games by Decade

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  publisher AS "Publisher",
  historical-significance AS "Significance"
FROM "Games"
WHERE year-published >= 1980 AND year-published < 1990
SORT year-published ASC
```

**Modify decades**: Change year ranges (1970-1979, 1990-1999, etc.)

### Currently In-Print Games

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  publisher AS "Publisher",
  edition AS "Edition"
FROM "Games"
WHERE status = "in-print"
SORT year-published DESC
```

### Most Innovative Games

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  innovation-score AS "Innovation",
  system AS "System"
FROM "Games"
WHERE innovation-score >= 4
SORT innovation-score DESC, year-published ASC
```

### Low Complexity Games

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  complexity AS "Complexity",
  system AS "System"
FROM "Games"
WHERE complexity <= 2
SORT year-published ASC
```

**Use Case**: Finding beginner-friendly games

### Games I've Played

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  personal-rating AS "My Rating",
  system AS "System"
FROM "Games"
WHERE play-experience = true
SORT personal-rating DESC
```

**Requires**: `personal-rating` and `play-experience` properties filled in

---

## Publisher Queries

### All Publishers by Founding Year

```dataview
TABLE
  file.link AS "Publisher",
  founded AS "Founded",
  headquarters AS "Location",
  significance AS "Significance"
FROM "Publishers"
SORT founded ASC
```

### Active Publishers

```dataview
TABLE
  file.link AS "Publisher",
  founded AS "Founded",
  era-active AS "Era",
  length(key-releases) AS "Games Published"
FROM "Publishers"
WHERE !defunct
SORT founded ASC
```

### Most Significant Publishers

```dataview
TABLE
  file.link AS "Publisher",
  founded AS "Founded",
  significance AS "Significance",
  length(key-releases) AS "Games"
FROM "Publishers"
WHERE significance >= 4
SORT significance DESC, founded ASC
```

### Publishers by Era

```dataview
TABLE
  file.link AS "Publisher",
  founded AS "Founded",
  headquarters AS "Location",
  length(key-releases) AS "Games"
FROM "Publishers"
WHERE era-active = "early-era"
SORT founded ASC
```

**Other eras**: `"golden-age"`, `"d20-era"`, `"osr-revival"`, `"modern-era"`

### Most Prolific Publishers

```dataview
TABLE
  file.link AS "Publisher",
  length(key-releases) AS "Games Published",
  founded AS "Founded",
  significance AS "Significance"
FROM "Publishers"
WHERE key-releases
SORT length(key-releases) DESC
LIMIT 10
```

### Defunct Publishers

```dataview
TABLE
  file.link AS "Publisher",
  founded AS "Founded",
  defunct AS "Closed",
  (defunct - founded) AS "Years Active"
FROM "Publishers"
WHERE defunct
SORT defunct DESC
```

---

## Designer Queries

### All Designers Alphabetically

```dataview
TABLE
  file.link AS "Designer",
  active-years AS "Active",
  length(notable-works) AS "Games"
FROM "Designers"
SORT file.name ASC
```

### Most Prolific Designers

```dataview
TABLE
  file.link AS "Designer",
  length(notable-works) AS "Games Designed",
  active-years AS "Career"
FROM "Designers"
WHERE length(notable-works) >= 3
SORT length(notable-works) DESC
```

### Designers by Era

```dataview
TABLE
  file.link AS "Designer",
  active-years AS "Active",
  length(notable-works) AS "Games"
FROM "Designers"
WHERE contains(active-years, "197")
SORT file.name ASC
```

**Modify for other decades**: Change `"197"` to `"198"`, `"199"`, `"200"`, `"201"`

### Award-Winning Designers

```dataview
TABLE
  file.link AS "Designer",
  length(notable-works) AS "Games",
  length(awards) AS "Awards"
FROM "Designers"
WHERE awards AND length(awards) > 0
SORT length(awards) DESC
```

---

## Relationship Queries

### Games That Influenced This Game

Embed in a game entry to show its influences:

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  system AS "System"
FROM "Games"
WHERE contains(this.file.frontmatter.influenced-by, file.link)
SORT year-published ASC
```

### Games This Game Influenced

Embed in a game entry to show what it influenced:

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  system AS "System"
FROM "Games"
WHERE contains(influenced-by, this.file.link)
SORT year-published ASC
```

### Publisher's Key Releases

Embed in a publisher entry:

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  historical-significance AS "Significance"
FROM "Games"
WHERE publisher = this.file.link
SORT year-published ASC
```

### Designer's Notable Works

Embed in a designer entry:

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  publisher AS "Publisher",
  historical-significance AS "Significance"
FROM "Games"
WHERE designer = this.file.link
SORT year-published ASC
```

### Games Using This Mechanic

Embed in a mechanic entry:

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  system AS "System",
  complexity AS "Complexity"
FROM "Games"
WHERE contains(this.file.frontmatter.games-using, file.link)
SORT year-published ASC
```

### Related Games (Shared Designer & Publisher)

Embed in a game entry to find similar games:

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer"
FROM "Games"
WHERE (designer = this.file.frontmatter.designer OR publisher = this.file.frontmatter.publisher)
  AND file.link != this.file.link
SORT year-published ASC
LIMIT 10
```

---

## Historical Analysis

### Games by Decade with Stats

```dataview
TABLE WITHOUT ID
  floor(year-published / 10) * 10 + "s" AS "Decade",
  length(rows) AS "Games Published",
  round(avg(rows.historical-significance), 1) AS "Avg Significance",
  round(avg(rows.innovation-score), 1) AS "Avg Innovation",
  round(avg(rows.complexity), 1) AS "Avg Complexity"
FROM "Games"
WHERE year-published
GROUP BY floor(year-published / 10) * 10 + "s"
SORT "Decade" ASC
```

### Publishers Founded by Decade

```dataview
TABLE WITHOUT ID
  floor(founded / 10) * 10 + "s" AS "Decade",
  length(rows) AS "Publishers Founded"
FROM "Publishers"
WHERE founded
GROUP BY floor(founded / 10) * 10 + "s"
SORT "Decade" ASC
```

### Most Influential Year

```dataview
TABLE WITHOUT ID
  year-published AS "Year",
  length(rows) AS "Games Released",
  round(avg(rows.historical-significance), 1) AS "Avg Significance"
FROM "Games"
WHERE year-published
GROUP BY year-published
SORT round(avg(rows.historical-significance), 1) DESC
LIMIT 10
```

### Genre Distribution Over Time

```dataview
TABLE
  year-published AS "Year",
  file.link AS "Game",
  genre AS "Genres"
FROM "Games"
WHERE contains(genre, "horror")
SORT year-published ASC
```

**Modify**: Change genre to analyze different category trends

---

## Statistical Queries

### Average Significance by System

```dataview
TABLE WITHOUT ID
  system AS "System",
  length(rows) AS "Games",
  round(avg(rows.historical-significance), 1) AS "Avg Significance",
  round(avg(rows.innovation-score), 1) AS "Avg Innovation"
FROM "Games"
WHERE system
GROUP BY system
SORT "Avg Significance" DESC
```

### Complexity Distribution

```dataview
TABLE WITHOUT ID
  complexity AS "Complexity",
  length(rows) AS "Count"
FROM "Games"
WHERE complexity
GROUP BY complexity
SORT complexity ASC
```

### Publisher Impact Score

```dataview
TABLE
  file.link AS "Publisher",
  length(key-releases) AS "Games",
  significance AS "Significance",
  (length(key-releases) * significance) AS "Impact Score"
FROM "Publishers"
WHERE key-releases AND significance
SORT (length(key-releases) * significance) DESC
LIMIT 10
```

### Designer Impact Score

```dataview
TABLE
  file.link AS "Designer",
  length(notable-works) AS "Games",
  length(awards) AS "Awards"
FROM "Designers"
WHERE notable-works
SORT (length(notable-works) + length(awards) * 2) DESC
LIMIT 10
```

**Formula**: (Games + Awards×2) as proxy for impact

---

## Validation Queries

### Games Missing Required Properties

```dataview
TABLE file.link AS "Game"
FROM "Games"
WHERE !title OR !type OR !publisher OR !designer OR !year-published
```

### Publishers Without Key Releases

```dataview
TABLE
  file.link AS "Publisher",
  founded AS "Founded"
FROM "Publishers"
WHERE !key-releases OR length(key-releases) = 0
```

### Designers Without Notable Works

```dataview
TABLE
  file.link AS "Designer",
  active-years AS "Active"
FROM "Designers"
WHERE !notable-works OR length(notable-works) = 0
```

### Orphan Games (No Influences)

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  historical-significance AS "Significance"
FROM "Games"
WHERE (!influence-on OR length(influence-on) = 0)
  AND (!influenced-by OR length(influenced-by) = 0)
  AND year-published < 2020
SORT year-published ASC
```

**Use Case**: Find significant older games that need relationship documentation

### Incomplete Entries (Low Property Count)

```dataview
TABLE
  file.link AS "Entry",
  type AS "Type",
  length(keys(this.file.frontmatter)) AS "Properties"
FROM "Games" OR "Publishers" OR "Designers"
WHERE length(keys(this.file.frontmatter)) < 8
SORT length(keys(this.file.frontmatter)) ASC
```

---

## Dashboard Queries

### Recent Additions

```dataview
TABLE
  file.link AS "Entry",
  type AS "Type",
  year-published AS "Year",
  file.mtime AS "Added"
FROM "Games" OR "Publishers" OR "Designers"
WHERE file.name != "TTRPG-History-Dashboard"
SORT file.mtime DESC
LIMIT 10
```

### Entry Count by Type

```dataview
TABLE WITHOUT ID
  type AS "Type",
  length(rows) AS "Count"
FROM "Games" OR "Publishers" OR "Designers" OR "Mechanics" OR "Historical Context"
GROUP BY type
SORT "Count" DESC
```

### Vault Statistics Summary

```dataview
TABLE WITHOUT ID
  "Total Entries" AS "Metric",
  length(rows) AS "Value"
FROM "Games" OR "Publishers" OR "Designers" OR "Mechanics" OR "Historical Context"
```

### Top 10 Most-Linked Entries

```dataview
TABLE
  file.link AS "Entry",
  type AS "Type",
  length(file.inlinks) AS "Incoming Links"
FROM "Games" OR "Publishers" OR "Designers"
SORT length(file.inlinks) DESC
LIMIT 10
```

---

## Tips for Using These Queries

### Modifying Queries

1. **Change Folders**: Update `FROM "Games"` to target different folders
2. **Adjust Filters**: Modify `WHERE` clauses for different criteria
3. **Add Columns**: Include more properties in `TABLE` section
4. **Change Sorting**: Update `SORT` to reorder results
5. **Limit Results**: Add `LIMIT 10` to restrict output

### Combining Queries

Use `OR` to query multiple folders:

```dataview
TABLE file.link AS "Entry", type AS "Type"
FROM "Games" OR "Publishers" OR "Designers"
WHERE year-published >= 2000 OR founded >= 2000
SORT file.name ASC
```

### Performance Tips

- Add `LIMIT` to large result sets
- Use specific folder paths (not wildcards)
- Filter with `WHERE` before `SORT`
- Avoid deeply nested calculations

### Embedding Queries

Place queries in:
- **MOC files**: For era or category overviews
- **Dashboard**: For vault-wide statistics
- **Entry notes**: For contextual relationships
- **Dedicated query notes**: For complex analysis

---

## Common Patterns

### Pattern: "Show me X related to current note"

```dataview
TABLE file.link AS "Title"
FROM "Folder"
WHERE contains(property-name, this.file.link)
SORT criteria ASC
```

### Pattern: "Top N by criteria"

```dataview
TABLE file.link AS "Title", property AS "Property"
FROM "Folder"
WHERE condition
SORT property DESC
LIMIT N
```

### Pattern: "Grouped statistics"

```dataview
TABLE WITHOUT ID
  grouping-field AS "Category",
  length(rows) AS "Count",
  round(avg(rows.numeric-property), 1) AS "Average"
FROM "Folder"
WHERE condition
GROUP BY grouping-field
SORT "Count" DESC
```

### Pattern: "Missing or incomplete data"

```dataview
TABLE file.link AS "Entry"
FROM "Folder"
WHERE !required-property OR required-property = ""
```

---

## Troubleshooting

**Query shows "No results"**
- Check folder path matches exactly (case-sensitive)
- Verify property names in WHERE/SORT clauses
- Ensure Dataview plugin is enabled

**Syntax error messages**
- Always use `AS "Alias"` for column names (quotation marks required)
- Check for missing commas between TABLE columns
- Verify `FROM` path uses quotes: `FROM "Games"`

**Properties don't display**
- Check property name spelling (case-sensitive)
- Use frontmatter property names (not display names)
- Some properties require `this.file.frontmatter.property` syntax

**Queries slow down Obsidian**
- Add `LIMIT` to restrict results
- Avoid multiple heavy queries on one page
- Use specific folders instead of vault-wide queries

---

## Further Resources

- **[[Query-Library]]**: 30+ advanced query patterns with explanations
- **[[ADVANCED-FEATURES]]**: Deep dive into Dataview capabilities
- **[[Property-Schema]]**: Complete property reference
- **[Dataview Documentation](https://blacksmithgu.github.io/obsidian-dataview/)**: Official plugin docs

---

*Copy these queries into your notes and modify them for your research needs. Remember to use Dataview (DQL) syntax with explicit column aliases.*
