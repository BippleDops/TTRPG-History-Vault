---
type: designer
designer-name: <% tp.system.prompt("Designer full name") %>
birth-year: <% tp.system.prompt("Birth year (YYYY) - optional", "") %>
notable-works: []
publishers-worked-with: []
innovations: []
awards: []
active-years: <% tp.system.prompt("Active years (e.g., 1975-1990)", "") %>
tags:
  - designer
---

# <% tp.frontmatter["designer-name"] %>

**Active Years**: <% tp.frontmatter["active-years"] %>
**Birth Year**: <% tp.frontmatter["birth-year"] %>

## Biography

<% tp.file.cursor(1) %>

## Design Philosophy

## Notable Works

```datacore
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher", historical-significance AS "Impact"
FROM "Games"
WHERE contains(designer, this.file.link)
SORT year-published ASC
```

## Innovations and Contributions

### Mechanical Innovations
-

### Conceptual Contributions
-

### Industry Impact
-

## Awards and Recognition

## Collaborations

```datacore
TABLE file.link AS "Designer", active-years AS "Active Years"
FROM "Designers"
WHERE this.file.link != file.link AND
  (any(map(notable-works, (w) => contains(notable-works, w))))
```

## Publishers Worked With

```datacore
TABLE file.link AS "Publisher", founded AS "Founded", significance AS "Significance"
FROM "Publishers"
WHERE contains(notable-designers, this.file.link)
```

## Influence on Later Designers

## Quotes and Interviews

## Bibliography and References
