---
title: <% tp.system.prompt("Supplement title") %>
type: supplement
parent-game: [[<% tp.system.prompt("Parent game") %>]]
publisher: [[<% tp.system.prompt("Publisher") %>]]
year-published: <% tp.system.prompt("Year published (YYYY)") %>
supplement-type: <% tp.system.suggester(["Adventure", "Sourcebook", "Rules Expansion", "Campaign Setting"], ["adventure", "sourcebook", "rules-expansion", "campaign-setting"]) %>
page-count: <% tp.system.prompt("Page count") %>
setting: <% tp.system.prompt("Setting (optional)", "") %>
notable-content: []
tags:
  - ttrpg
  - supplement
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## Content Summary

### Major Sections


### Key Features


## Mechanical Additions

### New Rules


### Character Options


### Game Systems


## Setting Details

### Locations


### NPCs and Factions


### Plot Hooks


## Reception

### Critical Response


### Community Impact


### Legacy


## Related Materials

### Prerequisites


### Follow-up Publications


---

## Datacore Queries

### Games in Same Product Line

```datacore
table title as "Game", year-published as "Year", game-system as "System"
from #ttrpg
where contains(product-line, this.parent-game)
   OR file.name = this.parent-game
sort year-published asc
```

### Other Supplements for Parent Game

```datacore
table title as "Supplement", year-published as "Year", supplement-type as "Type", page-count as "Pages"
from #supplement
where parent-game = this.parent-game
   AND file.name != this.file.name
sort year-published asc
```

### Related Supplements by Setting

```datacore
table title as "Title", parent-game as "Game", year-published as "Year"
from #supplement
where setting = this.setting
   AND setting != ""
   AND file.name != this.file.name
sort year-published asc
limit 10
```

---

## Notes

