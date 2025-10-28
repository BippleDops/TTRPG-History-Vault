---
tags:
  - reference
  - queries
  - datacore
cssclass: query-library
---

# Query Library

A comprehensive collection of Datacore query patterns for the TTRPG History Vault. All queries use explicit column aliases and Datacore syntax.

## Table of Contents

- [Relationship Queries](#relationship-queries)
- [Timeline & Era Queries](#timeline--era-queries)
- [Analytics & Metrics](#analytics--metrics)
- [Quality Control](#quality-control)
- [Portfolio & Attribution](#portfolio--attribution)
- [Discovery & Exploration](#discovery--exploration)

---

## Relationship Queries

### 1. Multi-Hop Influence Mapping

**Use Case**: Discover second-degree influence relationships - games that influenced games that this game influenced. Useful for understanding indirect lineage and the broader ripple effects of influential titles.

```datacore
table without id
  influenced.file.link AS "First Generation",
  influenced.influence-on AS "Second Generation"
from "Games"
where file.link = this.file.link
flatten influenced-by AS influenced
where influenced.influence-on
```

**Example Output**: Shows how D&D influenced RuneQuest, which then influenced Pendragon - revealing the indirect D&D → Pendragon lineage.

**Usage Notes**: Run from a specific game's note. Returns empty if the game has no influenced-by entries or if those games don't themselves influence others.

---

### 2. Cross-Publisher Designer Connections

**Use Case**: Identify designers who worked with a specific publisher. Maps professional relationships between creative talent and publishing houses.

```datacore
table without id
  file.link AS "Designer",
  publishers-worked-with AS "Publishers",
  notable-works AS "Key Games"
from "Designers"
where contains(publishers-worked-with, [[TSR]])
sort file.name asc
```

**Example Output**: Lists all designers who worked with TSR, showing their publisher relationships and major titles.

**Usage Notes**: Replace `[[TSR]]` with any publisher note link. Use for researching publisher rosters and talent movement.

---

### 3. Mechanics Adoption Network

**Use Case**: Find all games that use a specific mechanic, revealing adoption patterns and showing which designs embraced particular innovations.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  complexity AS "Complexity"
from "Games"
where contains(string(file.inlinks), "Mechanics/")
sort year-published asc
```

**Example Output**: All games using dice pool mechanics chronologically, showing adoption spread from 1990s onward.

**Usage Notes**: Run from a Mechanics note. Shows which games reference this mechanic in their backlinks.

---

### 4. Influence Chain Visualization

**Use Case**: Map the complete influence chain from a seminal game through all its direct descendants.

```datacore
table without id
  file.link AS "Influenced Game",
  year-published AS "Year",
  designer AS "Designer",
  innovation-score AS "Innovation"
from "Games"
where contains(influenced-by, this.file.link)
sort year-published asc
```

**Example Output**: All games directly influenced by D&D, chronologically ordered.

**Usage Notes**: Run from a game note. Pair with query #1 for multi-generational analysis.

---

## Timeline & Era Queries

### 5. Mechanics Adoption Timeline

**Use Case**: Track when and how quickly a mechanic spread through the industry after introduction. Reveals adoption curves and tipping points.

```datacore
table without id
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher"
from "Games"
where contains(string(file.inlinks), "Mechanics/")
sort year-published asc
```

**Example Output**: Shows d20 System adoption from 2000 onward, revealing the rapid uptake during the OGL era.

**Usage Notes**: Run from a Mechanics note. Group by decade to see adoption waves.

---

### 6. Publisher Market Share by Decade

**Use Case**: Analyze publisher dominance and market shifts over time. Shows which publishers led each era.

```datacore
table without id
  publisher AS "Publisher",
  count(file.link) AS "Games Published"
from "Games"
where year-published >= 1970 AND year-published < 1980
group by publisher
sort count(file.link) desc
```

**Example Output**: TSR: 45 games, Chaosium: 12 games, GDW: 8 games (1970s data).

**Usage Notes**: Modify year ranges for different decades. Combine with revenue data if available.

---

### 7. Genre Evolution Tracker

**Use Case**: Monitor how genre popularity changed across decades. Identifies trends like the rise of indie story games or decline of simulation-heavy designs.

```datacore
table without id
  genre AS "Genre",
  count(file.link) AS "Game Count"
from "Games"
where year-published >= 2000 AND year-published < 2010
flatten genre
group by genre
sort count(file.link) desc
```

**Example Output**: Fantasy: 234, Science Fiction: 89, Horror: 67 (2000s data).

**Usage Notes**: Change decade to track shifts. Use `flatten` to handle multi-genre games correctly.

---

### 8. System Family Trees

**Use Case**: Show all games using the same system chronologically, revealing how system families evolved and spawned variants.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  innovation-score AS "Innovation"
from "Games"
where system = [[d20 System]]
sort year-published asc
```

**Example Output**: D&D 3E (2000), Mutants & Masterminds (2002), d20 Modern (2002)...

**Usage Notes**: Replace system link with any system. Shows lineage and derivative works.

---

### 9. Era Transition Games

**Use Case**: Identify boundary-spanning games published during major industry transitions (OSR revival, 5E era, etc.).

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  genre AS "Genre",
  historical-significance AS "Significance"
from "Games"
where year-published IN [1974, 1985, 2000, 2008, 2014]
sort year-published asc
```

**Example Output**: D&D (1974), GURPS (1985), D&D 3E (2000), 4E (2008), D&D 5E (2014).

**Usage Notes**: Modify years for different transition points. Add industry events for context.

---

### 10. Designer Portfolio by Era

**Use Case**: View a designer's complete works organized by historical period, revealing career evolution and era-specific innovations.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  publisher AS "Publisher",
  innovation-score AS "Innovation"
from "Games"
where contains(designer, [[Gary Gygax]])
sort year-published asc
```

**Example Output**: D&D (1974), AD&D (1977), Dangerous Journeys (1992)... showing Gygax's career arc.

**Usage Notes**: Replace designer link. Group manually by decade for era analysis.

---

## Analytics & Metrics

### 11. Innovation Scoring by Era

**Use Case**: Calculate average innovation scores per decade to identify which periods were most creative and groundbreaking.

```datacore
table without id
  floor(year-published / 10) * 10 AS "Decade",
  round(avg(innovation-score), 2) AS "Avg Innovation",
  count(file.link) AS "Game Count"
from "Games"
where innovation-score
group by floor(year-published / 10) * 10
sort floor(year-published / 10) * 10 asc
```

**Example Output**: 1970s: 8.2 avg, 1980s: 6.7 avg, 2010s: 7.1 avg.

**Usage Notes**: Shows whether innovation is increasing, declining, or cyclical. Higher sample sizes (Game Count) yield more reliable averages.

---

### 12. Top Games by Weighted Score

**Use Case**: Rank games using a composite metric that emphasizes historical significance over pure innovation. Identifies the most culturally important titles.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  round((historical-significance * 2 + innovation-score) / 3, 2) AS "Weighted Score",
  historical-significance AS "Significance",
  innovation-score AS "Innovation"
from "Games"
where historical-significance AND innovation-score
sort round((historical-significance * 2 + innovation-score) / 3, 2) desc
limit 20
```

**Example Output**: D&D (9.67), Call of Cthulhu (8.33), Apocalypse World (8.00)...

**Usage Notes**: Adjust weighting formula for different emphases. Use for "greatest games" analysis.

---

### 13. Complexity Distribution Analysis

**Use Case**: Understand the accessibility landscape by counting games at each complexity tier. Reveals market segmentation.

```datacore
table without id
  complexity AS "Complexity Tier",
  count(file.link) AS "Game Count",
  round(count(file.link) * 100.0 / (select count(file.link) from "Games" where complexity), 1) AS "Percentage"
from "Games"
where complexity
group by complexity
sort complexity asc
```

**Example Output**: Low: 89 (22.3%), Medium: 234 (58.5%), High: 77 (19.2%).

**Usage Notes**: Shows whether the vault emphasizes accessible or complex games. Useful for collection balance assessment.

---

### 14. Publisher Productivity Analysis

**Use Case**: Rank publishers by total output and calculate their average game significance. Identifies prolific versus quality-focused publishers.

```datacore
table without id
  publisher AS "Publisher",
  count(file.link) AS "Total Games",
  round(avg(historical-significance), 2) AS "Avg Significance",
  round(avg(innovation-score), 2) AS "Avg Innovation"
from "Games"
where publisher
group by publisher
sort count(file.link) desc
limit 15
```

**Example Output**: TSR: 67 games, 7.2 significance, 6.8 innovation.

**Usage Notes**: Separates quantity from quality. High game count + high scores = industry leader.

---

### 15. Designer Longevity Rankings

**Use Case**: Identify designers with the longest active careers, showing sustained creative output over decades.

```datacore
table without id
  file.link AS "Designer",
  active-years AS "Active Period",
  length(notable-works) AS "Notable Works",
  length(publishers-worked-with) AS "Publishers"
from "Designers"
where active-years
sort active-years desc
limit 20
```

**Example Output**: Ken St. Andre (1975-2024), Steve Jackson (1977-2025), Greg Stafford (1975-2018).

**Usage Notes**: Long careers indicate adaptability and enduring influence. Cross-reference with era-specific innovations.

---

### 16. High-Impact Events

**Use Case**: Surface the most significant historical events in TTRPG history based on significance ratings.

```datacore
table without id
  file.link AS "Event",
  year AS "Year",
  significance AS "Significance",
  impact-areas AS "Impact Areas"
from "Events"
where significance >= 8
sort significance desc, year asc
```

**Example Output**: D&D Publication (1974, 10), OGL Release (2000, 9), TSR Bankruptcy (1997, 8).

**Usage Notes**: Threshold of 8 captures industry-defining moments. Lower for more events.

---

## Quality Control

### 17. Missing Influences Detector

**Use Case**: Identify games that lack influence attribution, helping maintain relationship completeness. Most post-1974 games should acknowledge influences.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  status AS "Status"
from "Games"
where !influenced-by OR length(influenced-by) = 0
where year-published > 1974
sort year-published desc
```

**Example Output**: Shows recent games missing influence data, flagging incomplete entries.

**Usage Notes**: D&D (1974) and Chainmail (1971) are legitimate exceptions. Focus on filling post-1974 gaps.

---

### 18. Orphaned Entries Finder

**Use Case**: Find games that no other game claims as an influence - potential data gaps or truly isolated designs.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  innovation-score AS "Innovation",
  length(file.inlinks) AS "Backlinks"
from "Games"
where !contains(string(file.inlinks), "influenced-by")
sort year-published desc
```

**Example Output**: Identifies games that should be influential but aren't cited, or niche games with no legacy.

**Usage Notes**: High innovation scores with no influence citations suggest missing data. Low scores may be legitimately isolated.

---

### 19. Property Completeness Check

**Use Case**: Audit data quality by finding entries missing important optional properties like genre, complexity, or innovation scores.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  choice(!genre, "Missing", "OK") AS "Genre",
  choice(!complexity, "Missing", "OK") AS "Complexity",
  choice(!innovation-score, "Missing", "OK") AS "Innovation"
from "Games"
where !genre OR !complexity OR !innovation-score
sort year-published desc
```

**Example Output**: Flags incomplete entries for systematic improvement.

**Usage Notes**: Prioritize filling data for high-significance games first. Use for vault maintenance planning.

---

### 20. Recent Additions Tracker

**Use Case**: Monitor vault growth by showing recently created or modified entries. Useful for reviewing recent work.

```datacore
table without id
  file.link AS "Entry",
  type AS "Type",
  file.mtime AS "Last Modified"
from "Games" OR "Designers" OR "Publishers" OR "Mechanics" OR "Events"
sort file.mtime desc
limit 30
```

**Example Output**: Shows last 30 entries added or updated with timestamps.

**Usage Notes**: Increases `limit` for longer history. Use to verify recent batch imports.

---

## Portfolio & Attribution

### 21. Designer Collaboration Network

**Use Case**: Find games with multiple designers, revealing collaborative partnerships and co-creation patterns.

```datacore
table without id
  file.link AS "Game",
  designer AS "Designers",
  year-published AS "Year",
  publisher AS "Publisher"
from "Games"
where length(designer) > 1
sort year-published desc
```

**Example Output**: D&D (Gary Gygax, Dave Arneson), RuneQuest (Steve Perrin, Greg Stafford, Ray Turney).

**Usage Notes**: Shows collaboration trends. Modern indie games often have solo designers; classic games were more collaborative.

---

### 22. Publisher Timeline by Founding Decade

**Use Case**: Group publishers by when they were founded to understand industry growth waves and generation cohorts.

```datacore
table without id
  file.link AS "Publisher",
  founded AS "Founded",
  headquarters AS "Location",
  length(key-releases) AS "Major Releases"
from "Publishers"
where founded >= 1970 AND founded < 1980
sort founded asc
```

**Example Output**: TSR (1973), Chaosium (1975), GDW (1973) - the first generation.

**Usage Notes**: Change decade range to study different eras. Compare with defunct dates to see survival rates.

---

### 23. Mechanics by Category

**Use Case**: Organize mechanics into functional categories (resolution, character creation, conflict, etc.) for systematic study.

```datacore
table without id
  category AS "Category",
  file.link AS "Mechanic",
  year-introduced AS "Introduced",
  popularity AS "Popularity"
from "Mechanics"
where category
group by category
sort category asc, year-introduced asc
```

**Example Output**: Resolution: d20 System, Dice Pools, PBTA; Character Creation: Lifepaths, Point Buy, Random Generation.

**Usage Notes**: Requires `category` property on Mechanics. Add categories for systematic organization.

---

### 24. Publisher Geographic Distribution

**Use Case**: Analyze the geographic origins of TTRPG publishers, revealing regional industry centers.

```datacore
table without id
  headquarters AS "Location",
  count(file.link) AS "Publisher Count",
  sum(length(key-releases)) AS "Total Key Releases"
from "Publishers"
where headquarters
group by headquarters
sort count(file.link) desc
```

**Example Output**: Lake Geneva, WI: 3 publishers, 89 key releases; Seattle, WA: 5 publishers, 34 releases.

**Usage Notes**: Shows industry geographic concentration. Pre-internet era heavily favored US locations.

---

## Discovery & Exploration

### 25. Genre Crossover Games

**Use Case**: Find games that blend multiple genres, identifying innovative hybrid designs.

```datacore
table without id
  file.link AS "Game",
  genre AS "Genres",
  year-published AS "Year",
  innovation-score AS "Innovation"
from "Games"
where length(genre) > 1
sort innovation-score desc
```

**Example Output**: Shadowrun (Fantasy + Cyberpunk), Numenera (Science Fantasy), Deadlands (Western + Horror).

**Usage Notes**: Genre-blending often correlates with innovation. Useful for finding unique designs.

---

### 26. Lost Publishers (Defunct Analysis)

**Use Case**: Study publishers that closed, analyzing industry mortality and historical context.

```datacore
table without id
  file.link AS "Publisher",
  founded AS "Founded",
  defunct AS "Defunct",
  defunct - founded AS "Years Active",
  significance AS "Significance"
from "Publishers"
where defunct
sort defunct desc
```

**Example Output**: TSR (1973-1997, 24 years, significance 10), SJG historical imprints, etc.

**Usage Notes**: Shows industry volatility. Compare active years vs. significance to assess legacy.

---

### 27. Innovation Hotspots by Designer

**Use Case**: Identify designers with highest average innovation scores - the industry's most creative minds.

```datacore
table without id
  designer AS "Designer",
  count(file.link) AS "Games Designed",
  round(avg(innovation-score), 2) AS "Avg Innovation",
  max(innovation-score) AS "Peak Innovation"
from "Games"
where designer AND innovation-score
flatten designer
group by designer
sort round(avg(innovation-score), 2) desc
limit 20
```

**Example Output**: Vincent Baker: 8.7 avg, Greg Stafford: 8.4 avg, Gary Gygax: 9.1 avg.

**Usage Notes**: Requires multiple games per designer for meaningful averages. Shows creative consistency.

---

### 28. System Diversity Index

**Use Case**: Count unique systems used across all games to measure mechanical diversity in the hobby.

```datacore
table without id
  system AS "System",
  count(file.link) AS "Games Using",
  min(year-published) AS "First Appeared"
from "Games"
where system
group by system
sort count(file.link) desc
```

**Example Output**: d20 System: 234 games, BRP: 45 games, PBTA: 89 games.

**Usage Notes**: Shows system dominance vs. diversity. High counts indicate successful systems; many one-off systems show innovation.

---

### 29. Events by Impact Area

**Use Case**: Filter historical events by their impact areas (legal, cultural, economic, creative) to study specific types of industry change.

```datacore
table without id
  file.link AS "Event",
  year AS "Year",
  impact-areas AS "Impact",
  significance AS "Significance"
from "Events"
where contains(impact-areas, "legal")
sort significance desc
```

**Example Output**: OGL Release (2000), D&D Copyright Lawsuit (1979), Satanic Panic (1980s).

**Usage Notes**: Replace "legal" with other impact areas. Shows thematic event clusters.

---

### 30. Era-Defining Games (Peak Significance per Decade)

**Use Case**: Identify the most historically significant game from each decade - the title that defined its era.

```datacore
table without id
  floor(year-published / 10) * 10 AS "Decade",
  file.link AS "Top Game",
  historical-significance AS "Significance",
  innovation-score AS "Innovation"
from "Games"
where historical-significance = max(historical-significance)
group by floor(year-published / 10) * 10
sort floor(year-published / 10) * 10 asc
```

**Example Output**: 1970s: D&D (10), 1980s: Call of Cthulhu (9), 2000s: D&D 3E (9), 2010s: D&D 5E (9).

**Usage Notes**: One representative game per decade. Shows generational milestones.

---

## Advanced Patterns

### 31. Influence Density (Most Referenced Games)

**Use Case**: Calculate which games are most frequently cited as influences by counting backlinks in the influenced-by property.

```datacore
table without id
  file.link AS "Game",
  year-published AS "Year",
  length(influence-on) AS "Direct Influence Count",
  historical-significance AS "Significance"
from "Games"
where length(influence-on) > 0
sort length(influence-on) desc
limit 20
```

**Example Output**: D&D: 234 games influenced, GURPS: 45, Apocalypse World: 89.

**Usage Notes**: Shows quantitative influence reach. Compare with historical-significance for validation.

---

### 32. Designer Influence Score

**Use Case**: Aggregate influence of all games by a designer to identify the most influential creators (not just popular).

```datacore
table without id
  designer AS "Designer",
  count(file.link) AS "Games",
  sum(length(influence-on)) AS "Total Games Influenced",
  round(avg(historical-significance), 2) AS "Avg Significance"
from "Games"
where designer
flatten designer
group by designer
sort sum(length(influence-on)) desc
limit 20
```

**Example Output**: Gary Gygax: 12 games, 456 influenced, 8.9 avg significance.

**Usage Notes**: Separates prolific designers from influential ones. High influence with few games = concentrated impact.

---

### 33. Unrepresented Eras (Gap Analysis)

**Use Case**: Identify decades with low game coverage, revealing gaps in the vault's historical representation.

```datacore
table without id
  floor(year-published / 10) * 10 AS "Decade",
  count(file.link) AS "Game Count"
from "Games"
group by floor(year-published / 10) * 10
sort floor(year-published / 10) * 10 asc
```

**Example Output**: 1940s: 2, 1950s: 1, 1960s: 4, 1970s: 89, 1980s: 234...

**Usage Notes**: Low counts in pre-1970s expected (fewer games existed). Focus on filling 1980s-2000s gaps.

---

### 34. Active Designer Status

**Use Case**: List currently active designers (no death-year listed) for tracking living contributors and potential interview subjects.

```datacore
table without id
  file.link AS "Designer",
  birth-year AS "Born",
  active-years AS "Active Since",
  length(notable-works) AS "Notable Works"
from "Designers"
where !death-year
sort active-years asc
```

**Example Output**: Shows living designers chronologically by when they entered the industry.

**Usage Notes**: Useful for oral history projects and contemporary designer tracking.

---

### 35. System Evolution Chains

**Use Case**: Trace how systems evolved from predecessors by following influenced-by relationships at the system level.

```datacore
table without id
  file.link AS "Game",
  system AS "System",
  influenced-by AS "Influenced By",
  year-published AS "Year"
from "Games"
where system = [[BRP]]
sort year-published asc
```

**Example Output**: Shows BRP lineage from RuneQuest through Call of Cthulhu, Stormbringer, etc.

**Usage Notes**: Replace system to track other families. Reveals mechanical evolution patterns.

---

## Usage Guidelines

### Running Queries

1. **Context Matters**: Some queries use `this.file.link` and must be run from a specific note type
2. **Modify Filters**: Adjust year ranges, limits, and link references for your specific needs
3. **Flatten Lists**: Use `flatten` when querying list properties like genre or designer
4. **Performance**: Large queries may take time; use `limit` for initial testing

### Syntax Reminders

- Always use explicit aliases: `file.link AS "Name"`
- Code fence: ` ```datacore ` (never dataview)
- Self-reference: `this.file.link`
- String searches: `contains(string(file.inlinks), "text")`
- Math functions: `floor()`, `round()`, `avg()`, `sum()`, `count()`

### Customization Tips

- **Combine Queries**: Chain filters for complex analysis
- **Adjust Thresholds**: Modify significance/innovation minimums
- **Change Groupings**: Swap decade for year for finer granularity
- **Add Columns**: Include additional properties for richer context

---

## Contributing

When adding new query patterns:

1. Test thoroughly with actual vault data
2. Include descriptive title and use case
3. Provide example output
4. Note any prerequisites or limitations
5. Use consistent formatting

---

*Last Updated: 2025-10-25*
