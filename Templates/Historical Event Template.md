---
type: historical-event
event-name: <% tp.system.prompt("Event name") %>
date: <% tp.system.prompt("Date (YYYY-MM-DD) or year (YYYY)") %>
year: <% tp.system.prompt("Year (YYYY)") %>
games-affected: []
publishers-affected: []
significance: <% tp.system.prompt("Significance 1-5") %>
tags:
  - historical-event
  - ttrpg-history
---

# <% tp.frontmatter["event-name"] %>

**Date**: <% tp.frontmatter.date %>
**Historical Significance**: ⭐ <% tp.frontmatter.significance %>/5

## Overview

<% tp.file.cursor(1) %>

## Context and Background

## Key Players

## Games Affected

```datacore
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher"
FROM "Games"
WHERE year-published = number(<% tp.frontmatter.year %>) OR contains(games-affected, this.file.link)
SORT title ASC
```

## Publishers Affected

```datacore
TABLE file.link AS "Publisher", founded AS "Founded"
FROM "Publishers"
WHERE contains(publishers-affected, this.file.link)
```

## Immediate Impact

## Long-term Consequences

## Industry Response

## Cultural Ripple Effects

## Contemporary Commentary

## Historical Analysis

## Timeline

## Primary Sources and References
