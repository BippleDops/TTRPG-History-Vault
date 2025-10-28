---
type: mechanic
mechanic-name: <% tp.system.prompt("Mechanic name") %>
first-appearance: [[<% tp.system.prompt("Game where it first appeared") %>]]
year-introduced: <% tp.system.prompt("Year introduced (YYYY)") %>
games-using: []
complexity: <% tp.system.prompt("Complexity 1-5") %>
popularity: <% tp.system.prompt("Popularity 1-5 (1=niche, 5=ubiquitous)") %>
tags:
  - mechanic
  - game-design
---

# <% tp.frontmatter["mechanic-name"] %>

**First Appeared In**: <% tp.frontmatter["first-appearance"] %>
**Year**: <% tp.frontmatter["year-introduced"] %>
**Complexity**: <% tp.frontmatter.complexity %>/5
**Popularity**: <% tp.frontmatter.popularity %>/5

## Description

<% tp.file.cursor(1) %>

## How It Works

### Core Mechanics


### Resolution Process


### Edge Cases and Variations


## Games Using This Mechanic

```datacore
TABLE file.link AS "Game", year-published AS "Year", designer AS "Designer", system AS "System"
FROM "Games"
WHERE contains(string(this.file.link), mechanic-name) OR contains(games-using, this.file.link)
SORT year-published ASC
```

## Variations and Iterations

## Design Intent and Purpose

## Strengths and Weaknesses

### Strengths
-

### Weaknesses
-

## Impact on Game Design

## Evolution Over Time

## Related Mechanics

## Designer Commentary

## References and Analysis
