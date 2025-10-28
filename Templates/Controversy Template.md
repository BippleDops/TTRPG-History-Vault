---
title: <% tp.system.prompt("Controversy name") %>
type: controversy
year: <% tp.system.prompt("Year (YYYY)") %>
parties-involved: []
impact-areas: []
resolution: <% tp.system.suggester(["Resolved", "Ongoing", "Unresolved"], ["resolved", "ongoing", "unresolved"]) %>
significance: <% tp.system.prompt("Significance (1-5)") %>
related-games: []
related-publishers: []
tags:
  - ttrpg
  - controversy
  - historical-event
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## Background

### Historical Context


### Parties Involved


## Timeline of Events

### Initial Incident


### Escalation


### Peak Controversy


### Resolution/Current Status


## Impact Analysis

### Impact on Industry


### Impact on Community


### Impact on Design Practices


### Legal/Policy Changes


## Different Perspectives

### Perspective 1


### Perspective 2


### Contemporary Analysis


## Long-term Consequences

### Changes to Industry Practices


### Influence on Future Games


### Cultural Legacy


---

## Datacore Queries

### Related Games

```datacore
table title as "Game", designer as "Designer", year-published as "Year", publisher as "Publisher"
from #ttrpg
where contains(this.related-games, file.link)
   OR file.link IN this.related-games
sort year-published asc
```

### Related Publishers

```datacore
table title as "Publisher", founded as "Founded", status as "Status"
from #publisher
where contains(this.related-publishers, file.link)
   OR file.link IN this.related-publishers
sort founded asc
```

### Other Controversies in Same Period

```datacore
table title as "Controversy", year as "Year", significance as "Significance", resolution as "Status"
from #controversy
where year >= (this.year - 3)
   AND year <= (this.year + 3)
   AND file.name != this.file.name
sort year asc
```

---

## Notes

### Primary Sources


### Analysis and Commentary


### External Links

