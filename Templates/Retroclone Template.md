---
title: <% tp.system.prompt("Retroclone title") %>
type: retroclone
emulates: [[<% tp.system.prompt("Game being emulated") %>]]
publisher: [[<% tp.system.prompt("Publisher") %>]]
designer: [[<% tp.system.prompt("Designer") %>]]
year-published: <% tp.system.prompt("Year published (YYYY)") %>
license: <% tp.system.suggester(["OGL", "CC-BY-SA", "Proprietary", "Other"], ["ogl", "cc-by-sa", "proprietary", "other"]) %>
design-goals: <% tp.system.prompt("Design goals (optional)", "") %>
complexity: <% tp.system.prompt("Complexity (1-5)") %>
tags:
  - ttrpg
  - retroclone
  - osr
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## Design Philosophy

### Goals and Intentions


### Target Audience


### Relationship to Source Material


## Mechanical Details

### Core System


### Differences from Original


### Improvements and Modernizations


## Legal Framework

### Licensing


### Rights and Permissions


### Open Gaming Content


## Content and Presentation

### Rules Coverage


### Production Quality


### Additional Material


## Reception and Impact

### Community Response


### Market Success


### Influence on OSR Movement


## Supplements and Support

### Published Supplements


### Third-Party Support


### Community Content


---

## Datacore Queries

### Original Game Being Emulated

```datacore
table title as "Game", year-published as "Year", designer as "Designer", publisher as "Publisher"
from #ttrpg
where file.link = this.emulates
   OR file.name = this.emulates
```

### Other Retroclones of Same Source

```datacore
table title as "Retroclone", year-published as "Year", designer as "Designer", license as "License", complexity as "Complexity"
from #retroclone
where emulates = this.emulates
   AND file.name != this.file.name
sort year-published asc
```

### OSR Games from Same Period

```datacore
table title as "Game", year-published as "Year", designer as "Designer", game-system as "System"
from #ttrpg OR #retroclone
where contains(tags, "osr")
   AND year-published >= (this.year-published - 3)
   AND year-published <= (this.year-published + 3)
   AND file.name != this.file.name
sort year-published asc
limit 15
```

---

## Notes

### Design Notes


### Community Resources


### External Links

