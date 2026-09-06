# 🎲 TTRPG History Vault - Main Dashboard

**Welcome to your comprehensive TTRPG historical research system!**

---

## 📊 Vault Statistics

```dataview
TABLE WITHOUT ID
  "**Category**" AS "",
  "**Count**" AS "Entries"
FROM ""
WHERE file.folder != null
FLATTEN COUNT(file.link) AS count
```

### Quick Stats

**Total Content:** 309+ comprehensive entries
**Coverage:** 1974-Present (50+ years)
**Scripts:** 18 Python analytics & export tools
**Documentation:** Complete research infrastructure

---

## 🎮 Browse by Category

### Core Content

```dataview
TABLE
  "📁 " + file.folder AS "Category",
  length(rows.file.link) AS "# Entries",
  "[[" + file.folder + "|Browse →]]" AS "View All"
FROM "Games" OR FROM "Designers" OR FROM "Publishers" OR FROM "Mechanics"
GROUP BY file.folder
SORT length(rows.file.link) DESC
```

### Historical & Cultural

```dataview
TABLE
  "📁 " + file.folder AS "Category",
  length(rows.file.link) AS "# Entries",
  "[[" + file.folder + "|Browse →]]" AS "View All"
FROM "Historical Context" OR FROM "Controversies" OR FROM "Actual Play"
GROUP BY file.folder
SORT length(rows.file.link) DESC
```

### Products & Systems

```dataview
TABLE
  "📁 " + file.folder AS "Category",
  length(rows.file.link) AS "# Entries",
  "[[" + file.folder + "|Browse →]]" AS "View All"
FROM "Supplements" OR FROM "Settings" OR FROM "Retroclones" OR FROM "VTT Platforms"
GROUP BY file.folder
SORT length(rows.file.link) DESC
```

---

## 🗺️ Navigation Indexes

### Browse by Attribute

- **[[Games-by-Year]]** - Chronological timeline (1974-present)
- **[[Games-by-Designer]]** - Browse by creator
- **[[Games-by-Publisher]]** - Browse by company
- **[[Games-by-System]]** - Browse by mechanical family

### Curated Views

- **[[Historical Context]]** - Browse 8 eras of TTRPG history
- **[[Designer-Influence-Network]]** - See creative relationships
- **[[System-Family-Trees]]** - Mechanical evolution
- **[[Genre-Guide]]** - Games by genre and theme

---

## 🔥 Highlights & Featured Content

### Most Historically Significant Games (5/5 rating)

```dataview
TABLE year-published AS "Year", file.link AS "Game", designer AS "Designer", innovation-score AS "Innovation"
FROM "Games"
WHERE historical-significance = 5
SORT year-published ASC
LIMIT 15
```

### Most Innovative Mechanics (5/5 rating)

```dataview
TABLE file.link AS "Mechanic", introduced-in AS "First Appeared In", popularized-by AS "Popularized By"
FROM "Mechanics"
WHERE innovation-score = 5
SORT file.name ASC
```

### Most Influential Designers

```dataview
TABLE file.link AS "Designer", influence-score AS "Influence", LIST(notable-works, 3) AS "Key Works", active-years AS "Active"
FROM "Designers"
WHERE influence-score >= 4
SORT influence-score DESC, file.name ASC
LIMIT 12
```

---

## 📅 Timeline View

### Games by Decade

```dataview
TABLE
  "**" + decade + "s**" AS "Decade",
  length(rows.file.link) AS "Games Published",
  LIST(rows.file.link, 5) AS "Notable Releases"
FROM "Games"
WHERE year-published != null
FLATTEN floor(year-published / 10) * 10 AS decade
GROUP BY decade
SORT decade ASC
```

---

## 🎯 Quick Access

### Recent Additions

```dataview
TABLE file.mtime AS "Added", file.link AS "Entry", type AS "Type"
FROM "Games" OR FROM "Designers" OR FROM "Publishers"
SORT file.mtime DESC
LIMIT 10
```

### By Game System

```dataview
TABLE system AS "System Family", COUNT(file.link) AS "# Games"
FROM "Games"
WHERE system != null AND system != ""
GROUP BY system
SORT COUNT(file.link) DESC
LIMIT 12
```

---

## 📚 Research Tools

### Analytics & Visualization

Run Python scripts to generate insights:
- `./Scripts/run_all_analytics.sh` - Generate all visualizations
- `publication_trends.py` - Publication patterns over time
- `influence_network.py` - Designer influence graphs
- `system_family_tree.py` - Mechanical evolution trees
- `coverage_gaps.py` - Identify missing content

**Output:** `Attachments/Diagrams/analytics/`

### Export Formats

Generate distribution-ready formats:
- `./Scripts/run_all_exports.sh` - Generate all formats
- Hugo static website
- PDF anthology (500+ pages)
- EPUB ebook
- JSON API
- Anki flashcards

**Output:** `Exports/`

### Quality Tools

- `quality_enhancer.py` - Find improvement opportunities
- `bibliography_generator.py` - Generate citations (Chicago/MLA/APA)
- `link_validator.py` - Check for broken wikilinks

---

## 🎓 Educational Resources

### Complete Curriculum

**[[Educational/Curricula/History-of-RPGs-101/00-Syllabus]]**
- 6-week university course
- Readings, assignments, assessments
- Integrated with vault content

### Study Aids

- Anki flashcards (generate with `anki_flashcards.py`)
- Dataview queries for filtered study lists
- Timeline visualizations

---

## 🔍 Search Strategies

### By Historical Significance

```dataview
TABLE historical-significance AS "Significance", file.link AS "Game", year-published AS "Year"
FROM "Games"
WHERE historical-significance >= 4
SORT historical-significance DESC, year-published ASC
LIMIT 20
```

### By Innovation Score

```dataview
TABLE innovation-score AS "Innovation", file.link AS "Game/Mechanic", year-published AS "Year", designer AS "Designer"
FROM "Games" OR FROM "Mechanics"
WHERE innovation-score >= 4
SORT innovation-score DESC, year-published ASC
LIMIT 20
```

### By Complexity

**Simple Games (1-2):**
```dataview
TABLE complexity AS "Complexity", file.link AS "Game", system AS "System", year-published AS "Year"
FROM "Games"
WHERE complexity <= 2 AND complexity != null
SORT complexity ASC, year-published ASC
LIMIT 15
```

**Complex Games (4-5):**
```dataview
TABLE complexity AS "Complexity", file.link AS "Game", system AS "System", year-published AS "Year"
FROM "Games"
WHERE complexity >= 4 AND complexity != null
SORT complexity DESC, year-published ASC
LIMIT 15
```

---

## 🌟 Explore by Movement

### OSR (Old School Renaissance)

```dataview
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer"
FROM "Games" OR FROM "Retroclones"
WHERE contains(string(tags), "OSR") OR type = "retroclone"
SORT year-published ASC
LIMIT 20
```

### Story Games & Narrative Design

```dataview
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", game-structure AS "Structure"
FROM "Games"
WHERE contains(string(tags), "story-game") OR contains(string(tags), "narrative") OR contains(string(tags), "GM-less")
SORT year-published ASC
LIMIT 20
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

## 📖 Documentation

### Getting Started

- **[[START-HERE]]** - Complete quick start guide (read this first!)
- **[[README]]** - Technical overview and setup
- **[[CONTRIBUTING]]** - How to add content
- **[[QUALITY-STANDARDS]]** - Content requirements

### Advanced Guides

- **[[Documentation/THEME-GUIDE]]** - Customize the RPG theme
- **[[Documentation/QUERY-COOKBOOK]]** - Dataview query examples
- **[[Documentation/WORKFLOW-GUIDE]]** - Content creation workflows
- **[[Documentation/ADVANCED-FEATURES]]** - Power user features

### Development

- **[[PARALLEL-AGENTS-GUIDE]]** - Expand vault with Claude Code
- **[[SESSION-COMPLETION-REPORT]]** - Latest achievements
- **Scripts/** - All analytics and export code

---

## 🎲 Random Discoveries

### Random Game

```dataview
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", system AS "System"
FROM "Games"
WHERE year-published != null
SORT random()
LIMIT 1
```

### Random Designer

```dataview
TABLE file.link AS "Designer", LIST(notable-works, 3) AS "Notable Works", active-years AS "Active"
FROM "Designers"
SORT random()
LIMIT 1
```

### Random Historical Era

```dataview
TABLE file.link AS "Era", date-range AS "Years", LIST(defining-games, 5) AS "Key Games"
FROM "Historical Context"
SORT random()
LIMIT 1
```

---

## 🛠️ Maintenance

### Health Check

**Last analytics run:** Check `Attachments/Diagrams/analytics/` for timestamps
**Broken links:** Run `python3 Scripts/link_validator.py`
**Quality issues:** Run `python3 Scripts/quality_enhancer.py`
**Coverage gaps:** Run `python3 Scripts/analytics/coverage_gaps.py`

### Content Needs

Check [[Coverage-Gaps-Report]] for systematic improvement priorities.

---

## 📊 Current Focus Areas

Based on latest analysis, prioritize:
1. **Missing Major Games:** See coverage gaps analysis
2. **Underrepresented Eras:** Pre-1980 and 2020-present
3. **International Coverage:** Non-English games
4. **Mechanical Documentation:** Advanced systems
5. **Publisher Histories:** Independent publishers

---

**🎲 Your comprehensive TTRPG research database - 50 years of gaming history! 🎲**

*Navigate, explore, analyze, and discover the rich tapestry of tabletop roleplaying games.*

---

*Last updated: October 2025 | Version 4.0 | 309+ Entries*
