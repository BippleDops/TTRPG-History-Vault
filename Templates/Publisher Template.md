---
type: publisher
publisher-name: <% tp.system.prompt("Publisher name") %>
founded: <% tp.system.prompt("Year founded (YYYY)") %>
defunct: <% tp.system.prompt("Year defunct (YYYY) - leave blank if still active", "") %>
headquarters: <% tp.system.prompt("Headquarters location (optional)", "") %>
key-releases: []
notable-designers: []
era-active: <% tp.system.suggester(["Early Era (1974-1985)", "Golden Age (1985-2000)", "d20 Era (2000-2008)", "OSR Revival (2008-2015)", "Modern Era (2015-Present)"], ["early-era", "golden-age", "d20-era", "osr-revival", "modern-era"]) %>
significance: <% tp.system.prompt("Historical significance 1-5") %>
tags:
  - publisher
  - <% tp.frontmatter["era-active"] %>
---

# <% tp.frontmatter["publisher-name"] %>

**Founded**: <% tp.frontmatter.founded %>
**Active Era**: <% tp.frontmatter["era-active"] %>
**Historical Significance**: ⭐ <% tp.frontmatter.significance %>/5
**Headquarters**: <% tp.frontmatter.headquarters %>

## History

<% tp.file.cursor(1) %>

## Key Releases

```datacore
TABLE file.link AS "Game", year-published AS "Year", genre AS "Genre", historical-significance AS "Impact"
FROM "Games"
WHERE contains(publisher, this.file.link)
SORT year-published ASC
```

## Notable Designers

```datacore
TABLE file.link AS "Designer", active-years AS "Active Years"
FROM "Designers"
WHERE contains(publishers-worked-with, this.file.link)
```

## Business Model and Distribution

## Innovation and Design Philosophy

## Legacy and Influence

## Timeline of Major Releases

## Cultural Impact

## References and Resources
