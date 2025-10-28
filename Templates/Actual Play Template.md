---
title: <% tp.system.prompt("Show title") %>
type: actual-play
format: <% tp.system.suggester(["Video", "Podcast", "Livestream", "Hybrid"], ["video", "podcast", "livestream", "hybrid"]) %>
system-used: [[<% tp.system.prompt("Primary system used") %>]]
years-active: <% tp.system.prompt("Years active (YYYY-present or YYYY-YYYY)") %>
cast: []
platform: <% tp.system.prompt("Platform (YouTube, Twitch, podcast networks)") %>
cultural-impact: <% tp.system.prompt("Cultural impact (1-5)") %>
audience-size: <% tp.system.prompt("Audience size estimate", "") %>
influence-on: []
tags:
  - ttrpg
  - actual-play
  - modern-era
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## Show Details

### Format and Platform


### Cast and Crew


### Production Quality


## Content and Style

### Campaign Overview


### Storytelling Approach


### Gameplay Style


## Cultural Impact

### Audience Growth


### Industry Influence


### Community Engagement


## Notable Episodes/Moments


## Reception and Legacy

### Critical Reception


### Awards and Recognition


### Impact on TTRPG Culture


---

## Datacore Queries

### Other Actual Plays Using Same System

```datacore
table title as "Show", format as "Format", years-active as "Years Active", cultural-impact as "Impact"
from #actual-play
where system-used = this.system-used
   AND file.name != this.file.name
sort cultural-impact desc
```

### Games Influenced By This Show

```datacore
table title as "Game", designer as "Designer", year-published as "Year"
from #ttrpg
where contains(influence-on, this.file.link)
   OR contains(this.influence-on, file.link)
sort year-published desc
```

### Contemporary Actual Plays

```datacore
table title as "Show", system-used as "System", format as "Format", cultural-impact as "Impact"
from #actual-play
where file.name != this.file.name
sort cultural-impact desc
limit 15
```

---

## Notes

### Episode Guide


### External Links

