# Designer Collaboration Network

## Designer Relationships and Collaborations

```datacore
TABLE WITHOUT ID
  file.link AS "Designer",
  length(notable-works) AS "Games Designed",
  active-years AS "Active Period",
  publishers-worked-with AS "Publishers"
FROM "Designers"
WHERE file.folder = "Designers"
SORT length(notable-works) DESC
```

## Most Prolific Designers

```datacore
TABLE WITHOUT ID
  "🎨 " + file.link AS "Designer",
  length(notable-works) AS "# Games",
  active-years AS "Years Active",
  "⭐".repeat(length(notable-works)) AS "Output"
FROM "Designers"
WHERE length(notable-works) >= 3
SORT length(notable-works) DESC
LIMIT 20
```

## Designer Awards and Recognition

```datacore
TABLE WITHOUT ID
  file.link AS "Award-Winning Designer",
  awards AS "Awards Won",
  notable-works AS "Major Works"
FROM "Designers"
WHERE awards != null AND awards != ""
SORT length(awards) DESC
```

## Designers by Era

### The Forge Era (2000-2010)

```datacore
TABLE file.link AS "Forge Designer", notable-works AS "Games", design-philosophy AS "Philosophy"
FROM "Designers"
WHERE contains(tags, "narrativist") OR contains(tags, "The-Forge")
SORT file.name ASC
```

### PbtA Designers

```datacore
TABLE file.link AS "PbtA Designer", notable-works AS "PbtA Games", active-years AS "Active"
FROM "Designers"
WHERE contains(tags, "PbtA") OR contains(notable-works, "Apocalypse World")
SORT length(notable-works) DESC
```

### OSR Designers

```datacore
TABLE file.link AS "OSR Designer", notable-works AS "OSR Games", active-years AS "Active"
FROM "Designers"
WHERE contains(tags, "OSR")
SORT file.name ASC
```

### Contemporary Indie Leaders (2015-Present)

```datacore
TABLE file.link AS "Contemporary Designer", notable-works AS "Recent Games", status AS "Status"
FROM "Designers"
WHERE contains(active-years, "present") OR contains(active-years, "2020")
SORT length(notable-works) DESC
LIMIT 30
```

## Design Philosophy Groupings

### Narrativist Designers

```datacore
TABLE file.link AS "Narrativist", design-philosophy AS "Philosophy", notable-works AS "Games"
FROM "Designers"
WHERE contains(tags, "narrativist") OR contains(design-philosophy, "narrativist")
SORT file.name ASC
```

### GMless Specialists

```datacore
TABLE file.link AS "GMless Designer", notable-works AS "GMless Games", design-philosophy AS "Approach"
FROM "Designers"
WHERE contains(tags, "GMless") OR contains(tags, "GMless-games")
SORT file.name ASC
```

### Horror Game Designers

```datacore
TABLE file.link AS "Horror Designer", notable-works AS "Horror Games", design-philosophy AS "Approach"
FROM "Designers"
WHERE contains(tags, "horror") OR contains(design-philosophy, "horror")
SORT file.name ASC
```

## Publisher-Designer Relationships

### Evil Hat Designers

```datacore
TABLE file.link AS "Evil Hat Designer", notable-works AS "Published by Evil Hat"
FROM "Designers"
WHERE contains(publishers-worked-with, "Evil Hat")
SORT file.name ASC
```

### Self-Published Designers

```datacore
TABLE file.link AS "Self-Published Designer", notable-works AS "Self-Published Games"
FROM "Designers"
WHERE contains(publishers-worked-with, "Self-published") OR contains(publishers-worked-with, "self-published")
SORT length(notable-works) DESC
```

## Geographic Distribution

### United States Designers

```datacore
TABLE file.link AS "US Designer", notable-works AS "Games", active-years AS "Active"
FROM "Designers"
WHERE nationality = "United States"
SORT length(notable-works) DESC
```

### United Kingdom Designers

```datacore
TABLE file.link AS "UK Designer", notable-works AS "Games", active-years AS "Active"
FROM "Designers"
WHERE nationality = "United Kingdom"
SORT file.name ASC
```

### International Designers

```datacore
TABLE file.link AS "Designer", nationality AS "Country", notable-works AS "Games"
FROM "Designers"
WHERE nationality != "United States" AND nationality != "United Kingdom" AND nationality != ""
SORT nationality ASC, file.name ASC
```

## Active vs Historical Designers

### Currently Active

```datacore
TABLE file.link AS "Active Designer", status AS "Status", notable-works AS "Games"
FROM "Designers"
WHERE status = "active"
SORT length(notable-works) DESC
```

### Historical/Deceased

```datacore
TABLE file.link AS "Historical Designer", death-year AS "Died", notable-works AS "Legacy Games"
FROM "Designers"
WHERE status = "deceased" OR death-year != ""
SORT death-year ASC
```

## Collaboration Patterns

### Co-Designers and Partners

```datacore
TABLE file.link AS "Designer", notable-works AS "Collaborative Works"
FROM "Designers"
WHERE contains(notable-works, "co-designer") OR contains(notable-works, "with")
SORT file.name ASC
```

---

*This network view shows the web of designers, their collaborations, movements, and relationships that shaped 50 years of TTRPG history.*
