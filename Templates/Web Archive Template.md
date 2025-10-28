---
source: <% tp.system.prompt("Source URL") %>
title: <% tp.system.prompt("Article title") %>
author: <% tp.system.prompt("Author name (optional)", "") %>
archived: <% tp.date.now("YYYY-MM-DD") %>
type: web-archive
category: <% tp.system.suggester(["Publisher Info", "Game Review", "Designer Interview", "Industry News", "Analysis", "Historical Documentation"], ["publisher-info", "review", "interview", "news", "analysis", "historical"]) %>
related-games: []
related-publishers: []
related-designers: []
tags:
  - web-clip
  - research
---

# <% tp.frontmatter.title %>

**Author**: <% tp.frontmatter.author %>
**Source**: <% tp.frontmatter.source %>
**Archived**: <% tp.frontmatter.archived %>
**Category**: <% tp.frontmatter.category %>

## Content

<% tp.file.cursor(1) %>

## Key Insights

## Related Entries

### Games
```datacore
TABLE file.link AS "Game", year-published AS "Year"
FROM "Games"
WHERE contains(related-games, this.file.link)
```

### Publishers
```datacore
TABLE file.link AS "Publisher", founded AS "Founded"
FROM "Publishers"
WHERE contains(related-publishers, this.file.link)
```

### Designers
```datacore
TABLE file.link AS "Designer", active-years AS "Active Years"
FROM "Designers"
WHERE contains(related-designers, this.file.link)
```

## Notes and Commentary

## Citation
