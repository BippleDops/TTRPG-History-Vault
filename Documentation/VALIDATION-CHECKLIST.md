# Validation Checklist

Quick reference checklist for entry validation.

## For New Game Entries

### Required Properties ✅
- [ ] `title` - Full game title
- [ ] `type: game`
- [ ] `publisher` - [[WikiLink]] to publisher
- [ ] `designer` - [[WikiLink]] to designer
- [ ] `year-published` - YYYY format
- [ ] `system` - System name (d20, pbta, etc.)
- [ ] `genre` - List with at least one genre
- [ ] `complexity` - Number 1-5
- [ ] `historical-significance` - Number 1-5
- [ ] `innovation-score` - Number 1-5
- [ ] `tags` - List including "ttrpg" and "game"
- [ ] `status` - in-print/out-of-print/revised/living

### Optional Properties (Recommended)
- [ ] `edition` - Edition/version name
- [ ] `player-count` - Range like "3-7"
- [ ] `setting` - Campaign world name
- [ ] `influence-on` - List of games influenced
- [ ] `influenced-by` - List of influencing games
- [ ] `play-experience` - true/false checkbox

### Content Requirements
- [ ] 2,000+ words total
- [ ] Historical Context section (2+ paragraphs)
- [ ] Mechanical Innovations section (bullet list)
- [ ] Cultural Impact section (2+ paragraphs)
- [ ] Design Philosophy section
- [ ] Reception and Legacy section
- [ ] 8+ WikiLinks to related content
- [ ] 3 Dataview query blocks (Related Games, Publisher Context, Designer Context)
- [ ] Notes and References section with citations

### Relationship Updates
- [ ] Updated influenced-by games' influence-on lists
- [ ] Updated designer's notable-works list
- [ ] Updated publisher's key-releases list
- [ ] Era MOC updated (if relevant)

## For New Publisher Entries

### Required Properties ✅
- [ ] `title` - Publisher name
- [ ] `type: publisher`
- [ ] `founded` - YYYY
- [ ] `headquarters` - "City, Country"
- [ ] `significance` - Number 1-5
- [ ] `era-active` - Historical period
- [ ] `tags` - Including "publisher"
- [ ] `status` - active/defunct

### Optional Properties (Recommended)
- [ ] `defunct` - YYYY if no longer active
- [ ] `key-releases` - List of major games

### Content Requirements
- [ ] 2,000+ words total
- [ ] Company History section
- [ ] Publishing Philosophy section
- [ ] Major Releases section
- [ ] Cultural Impact section
- [ ] Current Status section
- [ ] Legacy section
- [ ] 2 Dataview queries (Games Published, Designers Employed)

## For New Designer Entries

### Required Properties ✅
- [ ] `title` - Designer full name
- [ ] `type: designer`
- [ ] `nationality` - Country
- [ ] `active-years` - "YYYY-present" or "YYYY-YYYY"
- [ ] `tags` - Including "designer"
- [ ] `status` - active/retired/deceased

### Optional Properties (Recommended)
- [ ] `birth-year` - YYYY
- [ ] `death-year` - YYYY if deceased
- [ ] `notable-works` - List of major games
- [ ] `publishers-worked-with` - List of companies
- [ ] `design-philosophy` - Brief description
- [ ] `awards` - Major awards won

### Content Requirements
- [ ] 2,000+ words total
- [ ] Early Life and Career section
- [ ] Major Works section (detail 3+ games)
- [ ] Design Philosophy section
- [ ] Innovations and Contributions section
- [ ] Awards and Recognition section
- [ ] Legacy and Influence section
- [ ] 2 Dataview queries (Games Designed, Publishers Worked With)

## For New Mechanics Entries

### Required Properties ✅
- [ ] `title` - Mechanic name
- [ ] `type: mechanic`
- [ ] `year-introduced` - YYYY
- [ ] `first-appearance` - [[WikiLink]] to game
- [ ] `complexity` - Number 1-5
- [ ] `popularity` - Number 1-5
- [ ] `tags` - Including "mechanic"
- [ ] `category` - resolution/combat/character-progression/narrative/etc.

### Content Requirements
- [ ] 2,000+ words total
- [ ] Overview section
- [ ] Historical Context section
- [ ] Mechanical Function section (detailed explanation)
- [ ] Design Philosophy section
- [ ] Evolution Over Time section
- [ ] Cultural Impact section
- [ ] Strengths and Weaknesses section
- [ ] Modern Usage section
- [ ] 1+ Dataview query (Games Using This Mechanic)

## For New Historical Event Entries

### Required Properties ✅
- [ ] `title` - Event name
- [ ] `type: historical-event`
- [ ] `year` - YYYY
- [ ] `significance` - Number 1-5
- [ ] `impact-areas` - List (industry/community/design/cultural)
- [ ] `tags` - Including "historical-event"
- [ ] `era` - Era tag (early-era/golden-age/d20-era/osr-revival/modern-era)

### Optional Properties (Recommended)
- [ ] `date` - YYYY-MM-DD if specific date known
- [ ] `key-figures` - List of people involved
- [ ] `related-games` - List of affected games
- [ ] `related-publishers` - List of companies involved

### Content Requirements
- [ ] 2,000+ words total
- [ ] Overview section
- [ ] Background and Context section
- [ ] The Event Itself section (detailed narrative)
- [ ] Immediate Reactions section
- [ ] Short-Term Impact section
- [ ] Long-Term Consequences section
- [ ] Key Figures Involved section
- [ ] Historical Significance section
- [ ] 2+ Dataview queries (Related Games, Related Publishers/Events)

## Universal Validation Steps

### For ALL Entries
- [ ] YAML frontmatter valid (starts/ends with `---`)
- [ ] All WikiLinks use `[[Target]]` format (no markdown links)
- [ ] All lists use proper YAML syntax (dash-space-item on new lines)
- [ ] Dates in YYYY or YYYY-MM-DD format
- [ ] Numbers are actual numbers (not quoted strings)
- [ ] File named correctly: `[Title] ([Year]).md` for dated entries, `[Title].md` for others
- [ ] Saved in correct folder (Games/, Publishers/, Designers/, etc.)

### Testing
- [ ] Ran `link_validator.py` - 0 errors
- [ ] Ran `schema_validator.py` - 0 errors, 90%+ completeness
- [ ] Ran `reciprocal_link_checker.py` - 0 errors
- [ ] Opened in Obsidian - all Dataview queries display
- [ ] Checked graph view - entry connected to related content
- [ ] Verified in Bases view - entry appears with correct properties

---

*Print this checklist and check boxes as you validate!*
