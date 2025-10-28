---
title: <% tp.system.prompt("VTT name") %>
type: vtt
founded: <% tp.system.prompt("Year founded (YYYY)") %>
supported-systems: []
features: []
pricing-model: <% tp.system.suggester(["Free", "Freemium", "Subscription", "One-time Purchase"], ["free", "freemium", "subscription", "one-time"]) %>
user-base: <% tp.system.prompt("User base estimate", "") %>
impact-on-industry: <% tp.system.prompt("Impact (1-5)") %>
status: <% tp.system.suggester(["Active Development", "Maintenance Mode", "Defunct"], ["active", "maintenance", "defunct"]) %>
tags:
  - ttrpg
  - vtt
  - digital-tools
  - modern-era
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## Platform History

### Founding and Early Development


### Major Milestones


### Current Development Status


## Technical Details

### Platform and Technology


### System Requirements


### Architecture


## Features and Capabilities

### Core Features


### Advanced Features


### Unique Selling Points


## System Support

### Officially Supported Systems


### Community Support


### Rules Automation Level


## User Experience

### Ease of Use


### Learning Curve


### Accessibility


## Business Model

### Pricing Structure


### Monetization


### Value Proposition


## Community and Ecosystem

### User Community


### Content Marketplace


### Third-Party Integration


## Impact on Industry

### Market Position


### Innovation Contribution


### Influence on Remote Play


## Comparison to Competitors


---

## Datacore Queries

### Games with Official VTT Support

```datacore
table title as "Game", year-published as "Year", designer as "Designer", publisher as "Publisher"
from #ttrpg
where contains(supported-systems, this.file.link)
   OR contains(vtt-support, this.file.link)
sort year-published desc
limit 20
```

### Digital Adaptations on This Platform

```datacore
table title as "Adaptation", source-game as "Source", year-released as "Year", adaptation-quality as "Quality"
from #digital-adaptation
where contains(platform, this.file.name)
   OR platform = "VTT"
sort year-released desc
```

### Other VTT Platforms

```datacore
table title as "Platform", founded as "Founded", pricing-model as "Pricing", impact-on-industry as "Impact", status as "Status"
from #vtt
where file.name != this.file.name
sort impact-on-industry desc, founded desc
```

---

## Notes

### Feature Updates


### Community Resources


### External Links


### Integration Options

