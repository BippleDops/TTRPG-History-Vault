---
tags:
  - reference
  - documentation
  - schema
---

# Property Schema Reference

Complete documentation of all properties used across the TTRPG History Vault. This reference ensures consistency when creating new entries and serves as the definitive guide for metadata structure.

---

## Overview

Properties (also called frontmatter or metadata) provide structured data enabling:
- Database views through Bases
- Dynamic queries through Dataview
- Relationships between notes
- Filtering and sorting
- Statistical analysis

**Key Principles**:
- Use consistent property names across all notes of the same type
- Use appropriate data types (text, number, date, list, link)
- Maintain list format for tags, aliases, and other arrays (introduced v1.9.0)
- Link to other notes using `[[WikiLinks]]` format
- Use ISO dates (YYYY-MM-DD) for date properties

---

## Game Entry Properties

Used for notes in the `Games/` folder documenting individual TTRPG titles.

### Required Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `title` | text | Full game title | `Dungeons & Dragons` |
| `type` | text | Note type identifier | `game` |
| `publisher` | link | Publisher as WikiLink | `[[TSR]]` |
| `designer` | link | Primary designer as WikiLink | `[[Gary Gygax]]` |
| `year-published` | number | Publication year | `1974` |
| `system` | text | Mechanical system | `d20`, `percentile`, `pbta` |
| `genre` | list | Genre categories | `fantasy`, `horror`, `sci-fi` |
| `complexity` | number | Complexity rating 1-5 | `3` |
| `historical-significance` | number | Historical impact 1-5 | `5` |
| `innovation-score` | number | Mechanical innovation 1-5 | `4` |
| `tags` | list | Classification tags | `ttrpg`, `game`, `early-era` |
| `status` | text | Current availability | `in-print`, `out-of-print` |

### Optional Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `edition` | text | Edition or version | `Third Edition`, `Revised` |
| `player-count` | text | Player range | `3-6`, `2-5` |
| `setting` | text | Campaign setting | `Forgotten Realms`, `Generic Fantasy` |
| `influence-on` | list | Games it influenced | List of game links |
| `influenced-by` | list | Games that influenced it | List of game links |
| `purchase-date` | date | Personal acquisition date | `2024-12-15` |
| `personal-rating` | number | Optional personal rating 1-5 | `4` |
| `play-experience` | checkbox | Have you played this? | `true`, `false` |

### Example Frontmatter

```yaml
---
title: Call of Cthulhu
type: game
publisher: [[Chaosium]]
designer: [[Sandy Petersen]]
year-published: 1981
edition: First Edition
system: percentile
genre:
  - horror
complexity: 2
historical-significance: 5
innovation-score: 4
player-count: 2-7
setting: Lovecraftian Horror
influence-on:
  - "[[Trail of Cthulhu (2008)]]"
  - "[[Delta Green (1997)]]"
influenced-by: []
tags:
  - ttrpg
  - game
  - golden-age
  - horror
status: in-print
play-experience: true
---
```

---

## Publisher Properties

Used for notes in the `Publishers/` folder documenting publishing companies.

### Required Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `type` | text | Note type identifier | `publisher` |
| `publisher-name` | text | Company name | `TSR, Inc.` |
| `founded` | number | Year founded | `1973` |
| `headquarters` | text | Location | `Lake Geneva, Wisconsin` |
| `era-active` | text | Historical era | `early-era`, `golden-age` |
| `significance` | number | Historical significance 1-5 | `5` |
| `tags` | list | Classification tags | `publisher`, `early-era` |

### Optional Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `defunct` | number | Year ceased operations | `1997` |
| `key-releases` | list | Major games published | List of game links |
| `notable-designers` | list | Significant designers employed | List of designer links |

### Example Frontmatter

```yaml
---
type: publisher
publisher-name: Chaosium
founded: 1975
defunct:
headquarters: Ann Arbor, Michigan
key-releases:
  - "[[Call of Cthulhu (1981)]]"
  - "[[RuneQuest (1978)]]"
notable-designers:
  - "[[Sandy Petersen]]"
  - "[[Greg Stafford]]"
era-active: early-era
significance: 4
tags:
  - publisher
  - early-era
  - horror
---
```

---

## Designer Properties

Used for notes in the `Designers/` folder documenting game creators.

### Required Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `type` | text | Note type identifier | `designer` |
| `designer-name` | text | Full name | `Gary Gygax` |
| `active-years` | text | Career span | `1971-2008` |
| `tags` | list | Classification tags | `designer`, `foundational` |

### Optional Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `birth-year` | number | Year born | `1938` |
| `notable-works` | list | Major games designed | List of game links |
| `publishers-worked-with` | list | Companies worked for | List of publisher links |
| `innovations` | list | Contributions to design | Text list |
| `awards` | list | Recognition received | Text list |

### Example Frontmatter

```yaml
---
type: designer
designer-name: Sandy Petersen
birth-year: 1955
notable-works:
  - "[[Call of Cthulhu (1981)]]"
publishers-worked-with:
  - "[[Chaosium]]"
innovations:
  - Created the Sanity mechanic
  - Pioneered investigation-focused RPG design
awards:
  - Origins Award Best Roleplaying Rules (1981)
active-years: 1980-present
tags:
  - designer
  - horror
---
```

---

## Mechanics Properties

Used for notes in the `Mechanics/` folder documenting game systems and design patterns.

### Required Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `type` | text | Note type identifier | `mechanic` |
| `mechanic-name` | text | Mechanic name | `Sanity Mechanic` |
| `first-appearance` | link | Game where it debuted | `[[Call of Cthulhu (1981)]]` |
| `year-introduced` | number | Year first published | `1981` |
| `complexity` | number | Complexity rating 1-5 | `3` |
| `popularity` | number | Adoption level 1-5 | `4` |
| `tags` | list | Classification tags | `mechanic`, `game-design` |

### Optional Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `games-using` | list | Games that use this mechanic | List of game links |
| `description` | text | Brief description | Short explanation |

### Example Frontmatter

```yaml
---
type: mechanic
mechanic-name: Sanity Mechanic
first-appearance: "[[Call of Cthulhu (1981)]]"
year-introduced: 1981
games-using:
  - "[[Call of Cthulhu (1981)]]"
  - "[[Trail of Cthulhu (2008)]]"
complexity: 3
popularity: 4
tags:
  - mechanic
  - game-design
  - horror
---
```

---

## Historical Event Properties

Used for notes in the `Historical Context/` folder documenting pivotal moments.

### Required Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `type` | text | Note type identifier | `historical-event` |
| `event-name` | text | Event name | `Founding of TSR` |
| `date` | text/date | Specific date or year | `1973-10-01` or `1973` |
| `year` | number | Year for grouping/sorting | `1973` |
| `significance` | number | Historical significance 1-5 | `5` |
| `tags` | list | Classification tags | `historical-event`, `ttrpg-history` |

### Optional Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `games-affected` | list | Games impacted | List of game links |
| `publishers-affected` | list | Publishers impacted | List of publisher links |

### Example Frontmatter

```yaml
---
type: historical-event
event-name: Founding of TSR
date: 1973-10-01
year: 1973
games-affected: []
publishers-affected:
  - "[[TSR]]"
significance: 5
tags:
  - historical-event
  - ttrpg-history
  - foundational
---
```

---

## Web Archive Properties

Used for notes in the `Research Archive/` folder documenting web sources.

### Required Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `source` | text | Source URL | Full URL |
| `title` | text | Article title | Article or page title |
| `archived` | date | Archive date | `2024-12-15` |
| `type` | text | Note type | `web-archive` |
| `category` | text | Content category | `review`, `interview`, `news` |
| `tags` | list | Classification tags | `web-clip`, `research` |

### Optional Properties

| Property | Type | Description | Example |
|----------|------|-------------|---------|
| `author` | text | Content author | Author name |
| `related-games` | list | Relevant games | List of game links |
| `related-publishers` | list | Relevant publishers | List of publisher links |
| `related-designers` | list | Relevant designers | List of designer links |

---

## Common Tags

Standard tags used across the vault for categorization:

### Entry Type Tags
- `game` - Game entries
- `publisher` - Publisher profiles
- `designer` - Designer biographies
- `mechanic` - Mechanical systems
- `historical-event` - Pivotal moments
- `web-archive` - Research sources

### Era Tags
- `early-era` (1974-1985)
- `golden-age` (1985-2000)
- `d20-era` (2000-2008)
- `osr-revival` (2008-2015)
- `modern-era` (2015-Present)

### Genre Tags
- `fantasy`
- `horror`
- `sci-fi`
- `modern`
- `historical`
- `superhero`
- `universal`

### System Tags
- `d20`
- `percentile`
- `pbta`
- `fitd`
- `osr`
- `story-game`

### Significance Tags
- `foundational` - Created the medium or genre
- `influential` - Major impact on design
- `innovative` - Introduced new mechanics
- `landmark` - Cultural touchstone

---

## Data Type Guidelines

### Text
Plain text without formatting. Use for names, titles, descriptions.

### Number
Numeric values without quotes. Use for years, ratings, counts.

```yaml
year-published: 1974  # Correct
year-published: "1974"  # Incorrect
```

### Date
ISO format YYYY-MM-DD. Use for specific dates.

```yaml
archived: 2024-12-15  # Correct
archived: "12/15/2024"  # Incorrect
```

### List
YAML list format (v1.9.0+). Use for tags, links, arrays.

```yaml
tags:
  - ttrpg
  - game
  - horror
```

### Link
WikiLink format to other notes.

```yaml
publisher: [[Chaosium]]
designer: [[Sandy Petersen]]
```

### Checkbox
Boolean true/false value.

```yaml
play-experience: true
play-experience: false
```

---

## Validation Queries

Use these Dataview queries to check for missing or incorrect properties:

### Games Missing Required Properties

```dataview
TABLE file.link AS "Game"
FROM "Games"
WHERE !title OR !type OR !publisher OR !designer OR !year-published
```

### Publishers Without Key Releases

```dataview
TABLE file.link AS "Publisher"
FROM "Publishers"
WHERE !key-releases OR length(key-releases) = 0
```

### Designers Without Notable Works

```dataview
TABLE file.link AS "Designer"
FROM "Designers"
WHERE !notable-works OR length(notable-works) = 0
```

---

## Best Practices

1. **Fill Required Properties**: Always complete all required properties for entry type
2. **Use Consistent Types**: Match data types exactly as specified
3. **Link Generously**: Create [[WikiLinks]] to related entries
4. **Tag Appropriately**: Use standard tags for discoverability
5. **Maintain Lists**: Keep list properties updated as relationships change
6. **Validate Regularly**: Run validation queries to check for missing data
7. **Document Sources**: For historical claims, archive sources

---

*This schema ensures consistency and enables powerful querying across the entire vault. When in doubt, refer to example entries or the [[README]].*
