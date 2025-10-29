# Complete TTRPG Timeline - All Games

## Interactive Timeline Visualization

```datacore
TABLE WITHOUT ID
  "🎲 " + file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre",
  "⭐".repeat(historical-significance) AS "Significance"
FROM "Games"
WHERE year-published != null
SORT year-published ASC, title ASC
```

## Games by Decade

### 1970s - The Dawn (1974-1979)

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  system AS "System"
FROM "Games"
WHERE year-published >= 1974 AND year-published <= 1979
SORT year-published ASC
```

### 1980s - The Golden Age (1980-1989)

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  system AS "System"
FROM "Games"
WHERE year-published >= 1980 AND year-published <= 1989
SORT year-published ASC
```

### 1990s - The Storyteller Revolution (1990-1999)

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  system AS "System"
FROM "Games"
WHERE year-published >= 1990 AND year-published <= 1999
SORT year-published ASC
```

### 2000s - The d20 Boom & Indie Explosion (2000-2009)

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  system AS "System",
  innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 2000 AND year-published <= 2009
SORT year-published ASC
```

### 2010s - The PbtA Era & OSR Renaissance (2010-2019)

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  system AS "System",
  innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 2010 AND year-published <= 2019
SORT year-published ASC
```

### 2020s - The Modern Landscape (2020-Present)

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  designer AS "Designer",
  system AS "System",
  innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 2020
SORT year-published ASC
```

## Innovation Leaders by Era

```datacore
TABLE WITHOUT ID
  file.link AS "Highly Innovative Games",
  year-published AS "Year",
  innovation-score AS "Innovation",
  designer AS "Designer"
FROM "Games"
WHERE innovation-score >= 4
SORT innovation-score DESC, year-published DESC
LIMIT 50
```

## Historical Significance Rankings

```datacore
TABLE WITHOUT ID
  file.link AS "Most Historically Significant",
  year-published AS "Year",
  historical-significance AS "Significance",
  designer AS "Designer"
FROM "Games"
WHERE historical-significance >= 4
SORT historical-significance DESC, year-published ASC
LIMIT 50
```

## By System Family

### Powered by the Apocalypse

```datacore
TABLE WITHOUT ID
  file.link AS "PbtA Game",
  year-published AS "Year",
  designer AS "Designer"
FROM "Games"
WHERE contains(system, "Apocalypse") OR contains(tags, "PbtA")
SORT year-published ASC
```

### Forged in the Dark

```datacore
TABLE WITHOUT ID
  file.link AS "FitD Game",
  year-published AS "Year",
  designer AS "Designer"
FROM "Games"
WHERE contains(system, "Forged in the Dark") OR contains(tags, "FitD") OR contains(tags, "Forged-in-the-Dark")
SORT year-published ASC
```

### OSR and Retroclones

```datacore
TABLE WITHOUT ID
  file.link AS "OSR Game",
  year-published AS "Year",
  designer AS "Designer"
FROM "Games" OR FROM "Retroclones"
WHERE contains(tags, "OSR") OR file.folder = "Retroclones"
SORT year-published ASC
```

## Visualization Notes

This timeline provides multiple views of TTRPG history:
- Chronological complete listing
- Decade-based historical context
- Innovation and significance rankings
- System family groupings

The interactive Datacore queries allow sorting, filtering, and exploration of the complete game history represented in this vault.


## Comprehensive Game Release Timeline (1974-Present)

```datacore
TABLE WITHOUT ID
  year-published AS "Year",
  file.link AS "Game",
  designer AS "Designer",
  publisher AS "Publisher",
  genre AS "Genre"
FROM "Games"
WHERE year-published != null
SORT year-published ASC, title ASC
```

## Visualization: Games by Decade

```datacore
TABLE WITHOUT ID
  "📅 " + string(floor(year-published/10)*10) + "s" AS "Decade",
  length(rows) AS "Games Released",
  join(list(slice(rows.file.link, 0, 5)), ", ") + "..." AS "Sample Games"
FROM "Games"
WHERE year-published != null
GROUP BY floor(year-published/10)*10
SORT floor(year-published/10)*10 ASC
```

## Games by Era

### The Dawn Era (1974-1979)

```datacore
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", significance AS "Impact"
FROM "Games"
WHERE year-published >= 1974 AND year-published <= 1979
SORT year-published ASC
```

### The Golden Age (1980-1989)

```datacore
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", historical-significance AS "Impact"
FROM "Games"
WHERE year-published >= 1980 AND year-published <= 1989
SORT year-published ASC
```

### The Storyteller Revolution (1990-1999)

```datacore
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 1990 AND year-published <= 1999
SORT year-published ASC
```

### The d20 Boom (2000-2007)

```datacore
TABLE file.link AS "Game", year-published AS "Year", system AS "System"
FROM "Games"
WHERE year-published >= 2000 AND year-published <= 2007
SORT year-published ASC
```

### The Indie Explosion (2008-2015)

```datacore
TABLE file.link AS "Game", year-published AS "Year", tags AS "Tags"
FROM "Games"
WHERE year-published >= 2008 AND year-published <= 2015
SORT year-published ASC
```

### The Fifth Edition Era (2014-2020)

```datacore
TABLE file.link AS "Game", year-published AS "Year", genre AS "Genre"
FROM "Games"
WHERE year-published >= 2014 AND year-published <= 2020
SORT year-published ASC
```

### The Modern Landscape (2020-Present)

```datacore
TABLE file.link AS "Game", year-published AS "Year", innovation-score AS "Innovation"
FROM "Games"
WHERE year-published >= 2020
SORT year-published DESC
```

## Most Influential Games by Innovation Score

```datacore
TABLE file.link AS "Game", year-published AS "Year", innovation-score AS "Innovation", historical-significance AS "Historical Impact"
FROM "Games"
WHERE innovation-score >= 4
SORT innovation-score DESC, historical-significance DESC
LIMIT 50
```

## Games by Complexity

```datacore
TABLE WITHOUT ID
  "⚙️ Complexity " + string(complexity) AS "Level",
  length(rows) AS "Count",
  join(list(slice(rows.file.link, 0, 3)), ", ") + "..." AS "Examples"
FROM "Games"
WHERE complexity != null
GROUP BY complexity
SORT complexity ASC
```

---

*This timeline provides comprehensive chronological view of TTRPG development across 50 years, showing how gaming evolved from D&D's origins through multiple revolutions to contemporary diversity.*

