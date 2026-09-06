---
title: <% tp.system.prompt("Digital adaptation title") %>
type: digital-adaptation
source-game: [[<% tp.system.prompt("Source TTRPG") %>]]
platform: <% tp.system.suggester(["PC", "Console", "Mobile", "VTT", "Multi-platform"], ["pc", "console", "mobile", "vtt", "multi-platform"]) %>
developer: <% tp.system.prompt("Developer/studio") %>
year-released: <% tp.system.prompt("Year released (YYYY)") %>
adaptation-type: <% tp.system.suggester(["Video Game", "VTT", "Mobile App", "Online Platform"], ["video-game", "vtt", "mobile-app", "online-platform"]) %>
adaptation-quality: <% tp.system.prompt("Adaptation quality (1-5)") %>
tags:
  - ttrpg
  - digital-adaptation
  - cross-media
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## Development History

### Development Team


### Development Timeline


### Licensing and Rights


## Adaptation Details

### Platform and Technology


### Core Gameplay


### Rules Implementation


## Faithfulness to Source

### Mechanical Fidelity


### Thematic Fidelity


### Content Coverage


## Features and Innovations

### Unique Features


### Technical Achievements


### User Experience


## Reception

### Critical Reception


### Player Response


### Commercial Success


## Impact

### Impact on Source Game


### Impact on Digital TTRPG Space


### Legacy and Influence


---

## Dataview Queries

### Source Game Details

```dataview
table title as "Game", year-published as "Year", designer as "Designer", game-system as "System"
from #ttrpg
where file.link = this.source-game
   OR file.name = this.source-game
```

### Other Adaptations of Same Game

```dataview
table title as "Adaptation", adaptation-type as "Type", year-released as "Year", platform as "Platform", adaptation-quality as "Quality"
from #digital-adaptation
where source-game = this.source-game
   AND file.name != this.file.name
sort year-released asc
```

### Digital Adaptations from Same Era

```dataview
table title as "Adaptation", source-game as "Source", year-released as "Year", adaptation-type as "Type", adaptation-quality as "Quality"
from #digital-adaptation
where year-released >= (this.year-released - 3)
   AND year-released <= (this.year-released + 3)
   AND file.name != this.file.name
sort year-released asc
```

---

## Notes

### Version History


### External Links


### Screenshots/Media

