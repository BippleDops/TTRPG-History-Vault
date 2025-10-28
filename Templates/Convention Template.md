---
title: <% tp.system.prompt("Convention name") %>
type: convention
founded: <% tp.system.prompt("Year founded (YYYY)") %>
location: <% tp.system.prompt("Location (city, state/country)") %>
frequency: <% tp.system.suggester(["Annual", "Biennial", "Quarterly", "Defunct"], ["annual", "biennial", "quarterly", "defunct"]) %>
attendance: <% tp.system.prompt("Typical attendance", "") %>
significance: <% tp.system.prompt("Significance (1-5)") %>
notable-events: []
status: <% tp.system.suggester(["Active", "Defunct"], ["active", "defunct"]) %>
tags:
  - ttrpg
  - convention
  - community
---

# <% tp.frontmatter.title %>

## Overview

<% tp.file.cursor(1) %>

## History

### Founding


### Growth and Development


### Notable Years


## Convention Details

### Location and Venues


### Typical Schedule


### Size and Scope


## Activities and Programming

### Gaming Events


### Panels and Seminars


### Industry Presence


### Special Events


## Cultural Significance

### Role in Community


### Industry Impact


### Notable Attendees


## Notable Historical Events

### Game Releases


### Announcements


### Controversies or Incidents


## Current Status


---

## Datacore Queries

### Historical Events at This Convention

```datacore
table title as "Event", year as "Year", event-type as "Type", significance as "Significance"
from #historical-event
where contains(location, this.file.name)
   OR contains(notable-events, file.link)
sort year desc
```

### Games Launched at Convention

```datacore
table title as "Game", year-published as "Year", designer as "Designer", publisher as "Publisher"
from #ttrpg
where contains(launch-venue, this.file.link)
   OR contains(this.notable-events, file.link)
sort year-published desc
limit 20
```

### Other Conventions in Same Region

```datacore
table title as "Convention", founded as "Founded", frequency as "Frequency", status as "Status"
from #convention
where contains(location, split(this.location, ",")[0])
   AND file.name != this.file.name
sort founded asc
```

---

## Notes

### Attendance Records


### Programming History


### External Links

