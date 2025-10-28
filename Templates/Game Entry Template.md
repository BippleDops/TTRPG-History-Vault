---
title: <% tp.system.prompt("Game title") %>
type: game
publisher: [[<% tp.system.prompt("Publisher name") %>]]
designer: [[<% tp.system.prompt("Primary designer name") %>]]
year-published: <% tp.system.prompt("Year published (YYYY)") %>
edition: <% tp.system.prompt("Edition or version (optional)", "") %>
system: <% tp.system.suggester(["d20", "Percentile", "d6 Pool", "PBTA", "FITD", "Story Game", "OSR", "Custom"], ["d20", "percentile", "d6-pool", "pbta", "fitd", "story-game", "osr", "custom"]) %>
genre:
  - <% tp.system.suggester(["Fantasy", "Science Fiction", "Horror", "Modern", "Historical", "Superhero", "Universal"], ["fantasy", "sci-fi", "horror", "modern", "historical", "superhero", "universal"]) %>
complexity: <% tp.system.prompt("Complexity rating 1-5") %>
historical-significance: <% tp.system.prompt("Historical significance 1-5") %>
innovation-score: <% tp.system.prompt("Innovation score 1-5") %>
player-count: <% tp.system.prompt("Player count (e.g., 2-6)", "") %>
setting: <% tp.system.prompt("Campaign setting or world (optional)", "") %>
influence-on: []
influenced-by: []
tags:
  - ttrpg
  - game
status: <% tp.system.suggester(["In Print", "Out of Print", "Revised Edition", "Living Game"], ["in-print", "out-of-print", "revised", "living"]) %>
play-experience: false
---

# <% tp.frontmatter.title %>

**Publisher**: <% tp.frontmatter.publisher %>
**Designer**: <% tp.frontmatter.designer %>
**Year**: <% tp.frontmatter["year-published"] %>
**System**: <% tp.frontmatter.system %>
**Genre**: <% tp.frontmatter.genre %>
**Status**: <% tp.frontmatter.status %>

## Historical Context

<% tp.file.cursor(1) %>

## Mechanical Innovations

## Cultural Impact

## Design Philosophy

## Setting and Themes

## Reception and Legacy

## Related Games

```datacore
TABLE file.link AS "Game", year-published AS "Year"
FROM "Games"
WHERE contains(influenced-by, this.file.link) OR contains(influence-on, this.file.link)
SORT year-published ASC
```

## Publisher Context

```datacore
TABLE file.link AS "Publisher", founded AS "Founded"
FROM "Publishers"
WHERE contains(key-releases, this.file.link)
```

## Designer Context

```datacore
TABLE file.link AS "Designer", active-years AS "Active Years"
FROM "Designers"
WHERE contains(notable-works, this.file.link)
```

## Notes and References
