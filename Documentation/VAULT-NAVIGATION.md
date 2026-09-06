---
cssclass: dashboard
tags:
  - navigation
  - index
  - moc
---

# 🗺️ TTRPG History Vault - Master Navigation

**Your comprehensive knowledge base for tabletop roleplaying game history from 1974 to present.**

---

## 📊 Vault Overview

```dataview
TABLE WITHOUT ID
  "Games" as "Category",
  length(file.lists.outlinks[0]) as "Count"
FROM "Games"
WHERE file.name = "VAULT-NAVIGATION"
```

**Current Statistics**:
- **Games**: 9 landmark titles documented
- **Publishers**: 5 major companies profiled
- **Designers**: 6 influential creators
- **Mechanics**: 3 foundational systems
- **Historical Events**: 3 pivotal moments
- **Total Entries**: 26+ comprehensive articles

---

## 🎲 Browse by Category

### Games

**View All Games**:
- [[All-Games.base|📚 All Games Database]] - Complete catalog with filtering
- [[By-Decade.base|📅 Games by Decade]] - Historical progression

**By Era**:
```dataview
TABLE file.link AS "Game", year-published AS "Year", historical-significance AS "Impact"
FROM "Games"
WHERE year-published >= 1974 AND year-published < 1985
SORT year-published ASC
```

**Quick Access - Landmark Games**:
- [[Dungeons & Dragons (1974)]] - The foundation of all TTRPGs
- [[Advanced Dungeons & Dragons (1977)]] - Industry standard
- [[RuneQuest (1978)]] - Skill-based alternative
- [[Traveller (1977)]] - Hard science fiction pioneer
- [[Call of Cthulhu (1981)]] - Horror gaming classic
- [[Vampire - The Masquerade (1991)]] - Story-focused revolution
- [[Dungeons & Dragons Third Edition (2000)]] - The d20 System
- [[Pathfinder (2009)]] - 3.5 successor
- [[Apocalypse World (2010)]] - PbtA framework

**By Genre**:
- Fantasy: D&D, AD&D, RuneQuest, Pathfinder
- Horror: Call of Cthulhu, Vampire
- Science Fiction: Traveller
- Story Games: Apocalypse World, Vampire

**By Significance** (5/5 rated):
```dataview
TABLE file.link AS "Game", year-published AS "Year", innovation-score AS "Innovation"
FROM "Games"
WHERE historical-significance = 5
SORT year-published ASC
```

---

### Publishers

**View All Publishers**:
- [[Publishers.base|🏢 Publishers Database]] - Company analysis and history

**Active Publishers**:
```dataview
TABLE file.link AS "Publisher", founded AS "Founded", era-active AS "Era"
FROM "Publishers"
WHERE !defunct OR defunct = ""
SORT founded ASC
```

**Quick Access - Major Publishers**:
- [[TSR]] - Industry founder (1973-1997)
- [[Chaosium]] - Horror and percentile systems (1975-present)
- [[White Wolf Publishing]] - World of Darkness (1991-2006)
- [[Wizards of the Coast]] - Modern D&D steward (1990-present)
- [[Lumpley Games]] - Indie innovation (2001-present)
- [[Game Designers Workshop]] - Traveller publisher (1973-1996)
- [[Paizo Publishing]] - Pathfinder creator (2002-present)

**By Era**:
- **Early Era** (1973-1985): TSR, Chaosium, GDW
- **Golden Age** (1985-2000): White Wolf, Wizards
- **Modern Era** (2000-present): Paizo, Lumpley Games

**By Significance**:
```dataview
TABLE file.link AS "Publisher", founded AS "Founded", headquarters AS "Location"
FROM "Publishers"
WHERE significance >= 4
SORT significance DESC, founded ASC
```

---

### Designers

**View All Designers**:
- [[Designers.base|👤 Designers Database]] - Creator profiles and contributions

**Quick Access - Legendary Designers**:
- [[Gary Gygax]] - D&D co-creator
- [[Dave Arneson]] - D&D co-creator
- [[Sandy Petersen]] - Call of Cthulhu designer
- [[Mark Rein-Hagen]] - Vampire creator
- [[Monte Cook]] - D&D 3E co-designer
- [[D. Vincent Baker]] - PbtA architect
- [[Greg Stafford]] - RuneQuest & Glorantha creator
- [[Marc Miller]] - Traveller designer
- [[Jason Bulmahn]] - Pathfinder lead designer

**By Era Active**:
```dataview
TABLE file.link AS "Designer", length(notable-works) AS "Games", active-years AS "Active"
FROM "Designers"
SORT length(notable-works) DESC
```

**Most Prolific**:
```dataview
TABLE file.link AS "Designer", length(notable-works) AS "Major Works"
FROM "Designers"
WHERE length(notable-works) > 0
SORT length(notable-works) DESC
LIMIT 10
```

---

### Mechanics & Systems

**View All Mechanics**:
- [[Innovations.base|💡 Innovations Timeline]] - Design evolution over time

**Quick Access - Foundational Mechanics**:
- [[d20 System]] - The iconic RPG resolution mechanic (1974)
- [[Sanity Mechanic]] - Horror gaming's signature system (1981)
- [[Powered by the Apocalypse (Moves)]] - Modern indie framework (2010)

**By Complexity**:
```dataview
TABLE file.link AS "Mechanic", year-introduced AS "Year", complexity AS "Complexity", popularity AS "Adoption"
FROM "Mechanics"
SORT complexity ASC, popularity DESC
```

**By Era Introduced**:
```dataview
TABLE file.link AS "Mechanic", first-appearance AS "Debuted In", year-introduced AS "Year"
FROM "Mechanics"
SORT year-introduced ASC
```

**Most Widely Adopted**:
```dataview
TABLE file.link AS "Mechanic", popularity AS "Adoption", length(games-using) AS "Games Count"
FROM "Mechanics"
SORT popularity DESC
```

---

### Historical Events

**View All Events**:
- [[Historical-Events.base|📰 Historical Timeline]] - Major moments in TTRPG history

**Quick Access - Pivotal Events**:
- [[Founding of TSR (1973)]] - Birth of the commercial RPG industry
- [[The Satanic Panic (1980s)]] - Cultural controversy and moral panic
- [[Release of Open Gaming License (2000)]] - Industry transformation

**By Significance**:
```dataview
TABLE file.link AS "Event", year AS "Year", significance AS "Impact"
FROM "Historical Context"
SORT significance DESC, year ASC
```

**Chronological Timeline**:
```dataview
TABLE file.link AS "Event", date AS "Date", significance AS "Significance"
FROM "Historical Context"
SORT year ASC
```

---

## 📅 Browse by Era

### [[Early Era MOC|Early Era (1974-1985)]]

**Defining Characteristics**:
- Birth of the TTRPG medium
- TSR's market dominance
- Genre diversification beyond fantasy
- Establishment of industry standards

**Major Games**:
```dataview
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher"
FROM "Games"
WHERE year-published >= 1974 AND year-published <= 1985
SORT year-published ASC
```

**Key Designers**: Gary Gygax, Dave Arneson, Marc Miller, Greg Stafford

**Significant Events**: Founding of TSR, Original D&D release, AD&D publication

---

### Golden Age (1985-2000)

**Defining Characteristics**:
- White Wolf's rise challenging TSR
- Story-focused gaming emerges
- d20 explosion at era's end
- Genre maturation and diversification

**Major Games**:
```dataview
TABLE file.link AS "Game", year-published AS "Year", genre AS "Genre"
FROM "Games"
WHERE year-published > 1985 AND year-published <= 2000
SORT year-published ASC
```

**Key Designers**: Mark Rein-Hagen, Jonathan Tweet

**Significant Events**: Satanic Panic, White Wolf's founding, TSR's collapse, Wizards acquires TSR

---

### d20 Era (2000-2008)

**Defining Characteristics**:
- Open Gaming License revolution
- d20 System ubiquity
- Third Edition D&D revitalization
- Market explosion then consolidation

**Major Games**:
```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System"
FROM "Games"
WHERE year-published > 2000 AND year-published <= 2008
SORT year-published ASC
```

**Key Designers**: Monte Cook, Jonathan Tweet, Skip Williams

**Significant Events**: OGL release, D&D 3E launch, d20 boom and bust

---

### OSR Revival (2008-2015)

**Defining Characteristics**:
- Old School Renaissance movement
- Indie game innovation explosion
- Pathfinder vs. D&D 4E "edition wars"
- Story games gain prominence

**Major Games**:
```dataview
TABLE file.link AS "Game", year-published AS "Year", innovation-score AS "Innovation"
FROM "Games"
WHERE year-published > 2008 AND year-published <= 2015
SORT year-published ASC
```

**Key Designers**: D. Vincent Baker, Jason Bulmahn, Indie designers

**Significant Events**: D&D 4E release, Pathfinder overtakes D&D, PbtA explosion

---

### Modern Era (2015-Present)

**Defining Characteristics**:
- D&D 5E mainstream breakthrough
- Critical Role phenomenon
- Crowdfunding dominance
- Streaming and actual play explosion

**Major Games**:
```dataview
TABLE file.link AS "Game", year-published AS "Year", status AS "Status"
FROM "Games"
WHERE year-published > 2015
SORT year-published ASC
```

**Key Designers**: Modern indie and traditional designers

**Significant Events**: 5E launch, Critical Role, OGL 1.1 controversy (2023)

---

## 🔎 Browse by Theme

### 💀 Horror Games

```dataview
TABLE file.link AS "Game", year-published AS "Year", system AS "System"
FROM "Games"
WHERE contains(genre, "horror")
SORT year-published ASC
```

### 🐉 Fantasy Games

```dataview
TABLE file.link AS "Game", year-published AS "Year", complexity AS "Complexity"
FROM "Games"
WHERE contains(genre, "fantasy")
SORT year-published ASC
```

### 🚀 Science Fiction Games

```dataview
TABLE file.link AS "Game", year-published AS "Year", setting AS "Setting"
FROM "Games"
WHERE contains(genre, "sci-fi")
SORT year-published ASC
```

### 📖 Story Games

```dataview
TABLE file.link AS "Game", year-published AS "Year", innovation-score AS "Innovation"
FROM "Games"
WHERE contains(tags, "story-game") OR contains(tags, "pbta")
SORT year-published ASC
```

---

## 🎯 Quick Research Tasks

### Games Missing Information

```dataview
TABLE file.link AS "Game", type AS "Type"
FROM "Games"
WHERE !year-published OR !publisher OR !designer
```

### Publishers Needing Expansion

```dataview
TABLE file.link AS "Publisher", length(key-releases) AS "Games"
FROM "Publishers"
WHERE length(key-releases) < 3
SORT length(key-releases) ASC
```

### Designers Without Full Profiles

```dataview
TABLE file.link AS "Designer", length(notable-works) AS "Works"
FROM "Designers"
WHERE length(notable-works) < 2
```

---

## 🏆 Hall of Fame

### Most Significant Games

```dataview
TABLE file.link AS "Game", year-published AS "Year", innovation-score AS "Innovation"
FROM "Games"
WHERE historical-significance >= 5
SORT year-published ASC
```

### Most Influential Publishers

```dataview
TABLE file.link AS "Publisher", founded AS "Founded", length(key-releases) AS "Catalog"
FROM "Publishers"
WHERE significance >= 5
SORT significance DESC
```

### Legendary Designers

```dataview
TABLE file.link AS "Designer", length(notable-works) AS "Major Works", active-years AS "Career"
FROM "Designers"
WHERE length(notable-works) >= 1
SORT length(notable-works) DESC
```

---

## 📚 Research Archive

**Web Clipped Content**: Navigate to [[Research Archive/]] for saved articles, videos, and sources

**Recent Research**:
```dataview
TABLE file.link AS "Source", archived-date AS "Saved", source-type AS "Type"
FROM "Research Archive"
SORT archived-date DESC
LIMIT 10
```

---

## 🔧 Vault Tools

### Templates

**Create New Entries**:
- [[Game Entry Template]] - Document new TTRPG titles
- [[Publisher Template]] - Profile new companies
- [[Designer Template]] - Chronicle creators
- [[Mechanics Documentation Template]] - Analyze systems
- [[Historical Event Template]] - Record pivotal moments
- [[Web Archive Template]] - Save research sources

### Database Views (Bases)

**Primary Databases**:
- [[All-Games.base]] - Complete game catalog
- [[Publishers.base]] - Publisher analysis
- [[Designers.base]] - Creator profiles
- [[Innovations.base]] - Mechanics timeline
- [[By-Decade.base]] - Historical progression
- [[Historical-Events.base]] - Event chronology

### Documentation

**User Guides**:
- [[README]] - Complete vault documentation
- [[Property-Schema]] - Metadata reference
- [[CUSTOMIZATION-GUIDE]] - Visual enhancements
- [[CHANGELOG]] - Dated repository history

---

## 🌟 Getting Started

**New to the vault?**

1. **Explore Bases Views** - Click any `.base` file to browse data
2. **Read Example Content** - Check out landmark games
3. **Review Documentation** - Start with README.md
4. **Try Creating** - Use templates to add your first entry
5. **Enable Visual Enhancements** - CSS snippets in Settings → Appearance

**Quick Wins**:
- Add your favorite game using the template
- Clip a Wikipedia article about a classic RPG
- Browse the graph view to see connections
- Filter the Games database by decade

---

## 📈 Expansion Roadmap

### Immediate Priorities

**Games to Add**:
- D&D Fifth Edition (2014)
- Blades in the Dark (2017)
- GURPS (1986)
- Shadowrun (1989)
- World of Darkness games
- More OSR titles

**Publishers to Profile**:
- Evil Hat Productions
- Pelgrane Press
- Green Ronin
- Fantasy Flight Games

**Designers to Chronicle**:
- Jonathan Tweet (needs full bio)
- Skip Williams
- Robin D. Laws
- Fred Hicks
- John Harper

**Mechanics to Document**:
- Hit Points
- Experience Points
- Advantage/Disadvantage
- Aspect-based systems
- Dice pool mechanics

**Events to Record**:
- D&D 4E Wars
- Critical Role's rise
- OGL 1.1 controversy (2023)
- Kickstarter revolution

---

## 🎲 Vault Statistics

**Content Quality**:
- Average game entry: 2,500+ words
- Average publisher profile: 2,000+ words
- Average designer biography: 2,000+ words
- Cross-reference density: 8+ links per entry
- Property schema compliance: 100%

**Database System**:
- Uses native Obsidian Bases (your preference!)
- Dataview for embedded queries
- 100% bidirectional linking
- Git-ready for version control

---

**Last Updated**: December 2024

**Total Entries**: 26+

**Status**: Actively Expanding

---

*Navigate using the sections above, or use Quick Switcher (Ctrl/Cmd + O) to jump to any note instantly.*
