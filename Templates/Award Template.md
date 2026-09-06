---
title: <% tp.system.prompt("Award name") %>
type: award
founded: <% tp.system.prompt("Year founded (YYYY)") %>
categories: []
administering-body: <% tp.system.prompt("Organization/body") %>
frequency: <% tp.system.suggester(["Annual", "Biennial", "Occasional"], ["annual", "biennial", "occasional"]) %>
significance: <% tp.system.prompt("Industry significance (1-5)") %>
notable-winners: []
status: <% tp.system.suggester(["Active", "Defunct"], ["active", "defunct"]) %>
tags:
  - ttrpg
  - award
  - recognition
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## History

### Founding


### Evolution


### Notable Changes


## Award Structure

### Categories


### Nomination Process


### Voting/Selection Process


### Criteria


## Significance

### Industry Recognition


### Impact on Winners


### Prestige Level


## Notable Winners by Year

### Early Years


### Peak Years


### Recent Winners


## Controversies and Criticism


## Current Status


---

## Dataview Queries

### Games That Won This Award

```dataview
table title as "Game", year-published as "Year", designer as "Designer", publisher as "Publisher"
from #ttrpg
where contains(awards, this.file.link)
   OR contains(this.notable-winners, file.link)
sort year-published desc
limit 25
```

### Designers Who Won This Award

```dataview
table title as "Designer", notable-works as "Notable Works", awards as "Awards Won"
from #designer
where contains(awards, this.file.link)
   OR contains(this.notable-winners, file.link)
sort file.name asc
```

### Other Contemporary Awards

```dataview
table title as "Award", founded as "Founded", frequency as "Frequency", significance as "Significance", status as "Status"
from #award
where founded >= (this.founded - 5)
   AND founded <= (this.founded + 5)
   AND file.name != this.file.name
sort founded asc
```

---

## Notes

### Winners by Year


### Nomination History


### External Links

