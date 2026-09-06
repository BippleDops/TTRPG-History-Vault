# TTRPG History Tracking Vault

> [!warning] AI-drafted content under verification
> This vault was drafted with the help of AI tools in October 2025 and is still being verified.
> Entries can contain errors, anachronisms, and unsupported claims. Check facts against the
> cited sources (and the primary literature, e.g. Peterson's *Playing at the World*,
> Appelcline's *Designers & Dragons*) before reusing anything here. The `Research Archive/`
> notes are AI syntheses, not archived web pages, and their "quotes" are illustrative rather
> than real quotations. Corrections are welcome — see [Contributing](#contributing).

> **🚀 NEW USER? Start here:** [[START-HERE|Quick Start Guide]] - Your complete 5-minute introduction

A comprehensive Obsidian vault documenting 50+ years of tabletop roleplaying game history (1974-present). This vault contains **309+ entries** covering games, designers, publishers, mechanics, controversies, and cultural movements, plus **18 Python scripts** for analytics and export.

**Current Statistics:**
- 73 Games | 39 Designers | 33 Publishers | 23 Mechanics
- 15 Actual Play Shows | 11 Controversies | 11 Supplements
- 10 Campaign Settings | 11 Retroclones | 10 VTT Platforms | 8 Historical Eras

---

## Table of Contents

- [Overview](#overview)
- [Vault Structure](#vault-structure)
- [Getting Started](#getting-started)
- [Using the Vault](#using-the-vault)
- [Templates](#templates)
- [Database Views (Bases)](#database-views-bases)
- [Required Plugins](#required-plugins)
- [Contributing](#contributing)
- [Backup and Version Control](#backup-and-version-control)

---

## Overview

This vault implements a comprehensive database system using Obsidian's native **Bases** core plugin, combined with Datacore for advanced querying and Templater for streamlined data entry. All notes use rich property metadata enabling sophisticated cross-referencing and analysis.

### Key Features

✅ **Complete Historical Coverage**: Track games from 1974's original D&D to modern releases (309+ entries)
✅ **Rich Metadata Schema**: Comprehensive property definitions across all entry types
✅ **Multiple Navigation Paths**: Dashboard, Master Index, by-Year, by-Designer, by-System
✅ **RPG-Evocative Theme**: Custom theme with dice, character sheets, and stat block styling
✅ **Database Views**: Multiple Bases views for browsing and analyzing data
✅ **Dynamic Queries**: Datacore queries showing relationships and statistics
✅ **Smart Templates**: Templater-powered templates streamlining data entry
✅ **Knowledge Graph**: Extensive linking creating explorable knowledge network
✅ **Research Archive**: Web clipping and source documentation system
✅ **Git-Ready**: Structured for version control and collaborative development

---

## Vault Structure

```
TTRPG-History-Vault/
├── Games/                    # Individual TTRPG titles
├── Publishers/               # Publishing companies and imprints
├── Designers/                # Game designers and creators
├── Mechanics/                # Game systems and mechanical innovations
├── Historical Context/       # Timeline events, movements, cultural moments
├── Reviews & Analysis/       # Critical reception and retrospectives
├── Research Archive/         # Web clippings, articles, interviews
├── Templates/               # All template files
├── Views/                   # Bases files and Maps of Content
└── Attachments/            # Images, PDFs, cover art
```

### Folder Purposes

- **Games**: Core entries documenting individual TTRPG titles with full metadata
- **Publishers**: Company profiles with founding dates, key releases, and business info
- **Designers**: Creator biographies with notable works and innovations
- **Mechanics**: Documentation of mechanical systems and design patterns
- **Historical Context**: Major events, controversies, and cultural moments
- **Reviews & Analysis**: Critical reception documentation
- **Research Archive**: Captured web content, articles, and primary sources
- **Templates**: Templater templates for creating new entries
- **Views**: Bases database views and Maps of Content (MOCs) for navigation
- **Attachments**: Images, PDFs, and other media files

---

## Getting Started

> **👉 For a complete quick start guide, see [[START-HERE|START-HERE.md]]**

### Prerequisites

1. **Obsidian v1.9.10+** (any recent version)
2. **Required Core Plugins** (enable in Settings → Core Plugins):
   - Properties
   - Backlinks
   - Graph View
   - Outline
   - Search

3. **Required Community Plugins** (install from Settings → Community Plugins):
   - **Datacore** (NOT Dataview - critical distinction!)
   - **Templater** (optional, for templates)
   - Advanced Tables (optional but recommended)

### Initial Setup

1. **Open the vault** in Obsidian
2. **Enable core plugins** listed above
3. **Install community plugins**:
   - Go to Settings → Community Plugins
   - Turn off Restricted Mode
   - Browse and install Templater and Datacore
4. **Configure Templater**:
   - Settings → Templater → Template folder location: `Templates`
   - Enable "Trigger Templater on new file creation"
   - Configure folder-based templates (see Templates section)
5. **Enable Datacore**:
   - Settings → Datacore → Enable codeblock dataviews: ON
   - Enable inline dataviews: ON

### First Steps

1. **Open the Dashboard**: Navigate to `Views/TTRPG-History-Dashboard.md`
2. **Explore the Database Views**: Click the `.base` files in Views folder
3. **Browse Example Content**: Read through Games, Publishers, Designers
4. **Review Property Schema**: Check `Views/Property-Schema.md`
5. **Try Creating an Entry**: Use templates to add a new game or publisher

---

## Using the Vault

### Navigation

**Start Here**:
- **[[TTRPG-History-Dashboard]]**: Main navigation hub with stats and quick links
- **[[MASTER-INDEX]]**: Complete A-Z reference guide
- **[[Games-by-Year]]**: Chronological timeline (1974-present)
- **[[Games-by-Designer]]**: Browse by creator
- **[[Games-by-System]]**: Browse by mechanical family
- **[[Historical Context]]**: Browse 8 comprehensive historical eras
- **Database Views**: Use .base files for browsing and filtering

**Finding Content**:
- Use **Quick Switcher** (Ctrl/Cmd + O) to jump to specific notes
- Use **Search** (Ctrl/Cmd + Shift + F) for full-text search
- Use **Graph View** to explore connections visually
- Use **Backlinks** panel to see what links to current note

### Adding New Entries

**Using Templates**:
1. Create new note in appropriate folder (Games, Publishers, etc.)
2. Select or auto-apply relevant template
3. Fill in prompted information
4. Replace cursor placeholders with detailed content
5. Link to related entries using [[wikilinks]]

**Manual Creation**:
1. Create new note in appropriate folder
2. Copy frontmatter from similar entry
3. Fill in all required properties
4. Add content sections
5. Create links to related notes

### Linking Strategy

**Create bidirectional links**:
- Link games to publishers and designers
- Link publishers to their games and designers
- Link designers to games and publishers
- Link mechanics to games that use them
- Link historical events to affected games/publishers

**Use lists for multi-links**:
```yaml
influenced-by:
  - "[[Game One]]"
  - "[[Game Two]]"
```

### Querying Data

**Datacore Queries**:
Use datacore code blocks in any note:

```datacore
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher"
FROM "Games"
WHERE historical-significance >= 4
SORT year-published ASC
```

**Bases Views**:
Open .base files in Views folder to:
- Filter by multiple properties
- Sort by columns
- Group by decades, publishers, etc.
- Calculate statistics
- Export data

---

## Templates

All templates use Templater syntax for dynamic prompts and automation.

### Available Templates

| Template | Purpose | Location |
|----------|---------|----------|
| Game Entry Template | Document TTRPG titles | `Templates/Game Entry Template.md` |
| Publisher Template | Profile publishing companies | `Templates/Publisher Template.md` |
| Designer Template | Chronicle game creators | `Templates/Designer Template.md` |
| Mechanics Documentation Template | Analyze game mechanics | `Templates/Mechanics Documentation Template.md` |
| Historical Event Template | Record pivotal moments | `Templates/Historical Event Template.md` |
| Web Archive Template | Save research sources | `Templates/Web Archive Template.md` |

### Template Features

- **Dynamic Prompts**: Templater asks for required information
- **Suggesters**: Dropdown menus for categorical data (system type, genre, etc.)
- **Auto-dates**: Automatically populate current date
- **Cursor Positioning**: Places cursor at main content section
- **Embedded Queries**: Include relevant Datacore queries automatically

### Folder-Based Auto-Templates

Configure Templater to automatically apply templates when creating notes in specific folders:

1. Settings → Templater → Folder Templates
2. Add mappings:
   - `Games` → `Templates/Game Entry Template.md`
   - `Publishers` → `Templates/Publisher Template.md`
   - `Designers` → `Templates/Designer Template.md`
   - `Mechanics` → `Templates/Mechanics Documentation Template.md`
   - `Historical Context` → `Templates/Historical Event Template.md`

---

## Database Views (Bases)

The vault includes pre-configured Bases views for browsing and analyzing data.

### Available Views

| View | Purpose | File |
|------|---------|------|
| All Games Database | Complete game catalog with filtering | `Views/All-Games.base` |
| Publishers Analysis | Publishing companies by era and significance | `Views/Publishers.base` |
| Design Innovations Timeline | Mechanical innovations chronologically | `Views/Innovations.base` |
| Games by Decade | Historical progression view | `Views/By-Decade.base` |
| All Designers | Game creators and contributors | `Views/Designers.base` |
| Historical Events | Major moments in TTRPG history | `Views/Historical-Events.base` |

### Using Bases Views

1. **Open** a .base file from Views folder
2. **Filter** using column headers to narrow results
3. **Sort** by clicking column headers
4. **Group** using the Group By option
5. **Edit** entries by clicking to open the source note
6. **Export** data using Bases export functions

### Creating Custom Views

1. Create new .base file in Views folder
2. Configure source folder
3. Define columns mapping to properties
4. Set default sort, filters, and grouping
5. Save and use like built-in views

---

## Required Plugins

### Core Plugins

These are built into Obsidian and must be enabled:

- **Bases**: Native database system (v1.9.10+)
- **Properties**: Manage metadata across vault
- **Templates**: Basic template functionality
- **Daily Notes**: Optional, for research logging
- **Backlinks**: View incoming links
- **Graph View**: Visualize knowledge graph
- **Outline**: Document structure navigation
- **Search**: Full-text search
- **Quick Switcher**: Fast note navigation

### Community Plugins

Install from Settings → Community Plugins → Browse:

**Required**:
- **Templater** (v2.8.3+): Dynamic templates with prompts and automation
- **Datacore** (latest version): Advanced querying and data display

**Recommended**:
- **Advanced Tables**: Improved table editing
- **Tracker**: Visualize trends over time
- **QuickAdd**: Rapid entry macros
- **DB Folder**: Alternative spreadsheet-style editing

**Optional**:
- **Obsidian Web Clipper**: Browser extension for research archiving
- **Calendar**: Daily notes visualization
- **Kanban**: Task management boards

### Plugin Configuration

**Templater**:
```
Template folder location: Templates
Trigger Templater on new file creation: ON
Enable folder templates: ON
Syntax highlighting: ON
```

**Datacore**:
```
Enable codeblock dataviews: ON
Enable inline dataviews: ON
Inline dataview prefix: =
```

---

## Contributing

### Adding Content

The vault is designed for ongoing expansion:

**Add Games**:
- Use the Game Entry Template
- Include full metadata (publisher, designer, year, etc.)
- Write detailed content sections
- Link to related entries

**Add Publishers**:
- Document founding date, headquarters, era
- Link to key releases
- Note significant designers
- Include business model and history

**Add Designers**:
- Chronicle career and active years
- Link to notable works
- Document innovations and contributions
- Include biographical information

**Add Mechanics**:
- Explain how the mechanic works
- Identify first appearance
- List games using the mechanic
- Analyze impact on game design

### Content Standards

**Required**:
- All required properties filled in
- Minimum 3-4 paragraphs of content
- Links to at least 2 related entries
- Proper tags applied

**Recommended**:
- Citations for factual claims
- Multiple content sections developed
- Embedded queries showing relationships
- Historical context provided

**Quality**:
- Clear, informative writing
- Accurate information
- Consistent formatting
- Comprehensive coverage

---

## Backup and Version Control

### Git Integration

The vault is structured for Git version control:

**Setup**:
```bash
cd TTRPG-History-Vault
git init
git add .
git commit -m "Initial commit"
git remote add origin [your-repo-url]
git push -u origin main
```

**Recommended .gitignore**:
```
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache/
.trash/
```

### Commit Strategy

**Individual Entries**:
```bash
git add "Games/New Game Title.md"
git commit -m "Add: New Game Title (year)"
git push
```

**Batch Updates**:
```bash
git add Publishers/
git commit -m "Update: Publisher entries with new metadata"
git push
```

**Template Changes**:
```bash
git add Templates/
git commit -m "Refine: Game Entry Template with additional fields"
git push
```

### Backup Recommendations

1. **Git Remote**: Push to GitHub/GitLab regularly
2. **Cloud Sync**: Use Obsidian Sync or cloud storage
3. **Local Backup**: Periodic full vault backups
4. **Export Important Queries**: Save key Datacore queries separately

---

## Support and Resources

### Obsidian Documentation
- [Obsidian Help](https://help.obsidian.md/)
- [Datacore Plugin](https://github.com/blacksmithgu/datacore)
- [Templater Documentation](https://silentvoid13.github.io/Templater/)

### TTRPG Research Resources
- RPG.net
- Board Game Geek (RPG section)
- DriveThruRPG
- The Alexandrian
- Wikipedia TTRPG entries (use thetimetube.com for clean copies)

### Related Projects
- Designers & Dragons (Shannon Applecline)
- Playing at the World (Jon Peterson)
- Game Wizards (Jon Peterson)
- Various TTRPG history podcasts and YouTube channels

---

## License and Attribution

- **Vault content** (all Markdown notes, templates, views, documentation, theme and CSS snippets) is
  licensed under the [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/)
  licence. See [`LICENSE`](LICENSE). Attribute as "TTRPG History Vault contributors" and share
  adaptations under the same licence.
- **Scripts** (everything under `Scripts/`) are licensed under the MIT licence. See
  [`Scripts/LICENSE`](Scripts/LICENSE).
- Game titles, logos, and rules text belong to their respective publishers and designers. This vault
  documents and analyses them under fair-use / fair-dealing principles and does not reproduce rules text.

When documenting games, publishers, and designers, always:
- Respect copyright and trademarks
- Provide citations for factual claims
- Credit original sources
- Follow fair use principles for analysis and commentary

---

## Additional Documentation

**Essential:**
- **[[START-HERE]]** - Quick start guide (read this first!)
- **[[TTRPG-History-Dashboard]]** - Main navigation hub
- **[[MASTER-INDEX]]** - Complete A-Z reference
- **COMPREHENSIVE-IMPROVEMENT-SUMMARY.md** - Complete v4.0 achievements
- **CONTRIBUTING.md** - How to add content
- **QUALITY-STANDARDS.md** - Content requirements
- **PARALLEL-AGENTS-GUIDE.md** - Using Claude Code for expansion

**Advanced** (in `Documentation/` folder):
- Advanced Features, Customization Guide, Plugin Integration
- Query Cookbook, Workflow Guide, Testing Guide
- Validation Checklist, Vault Navigation

**Development:**
- `Scripts/` - 18 Python scripts for analytics and export
- `Educational/` - Complete 6-week university curriculum
- `Templates/` - Entry templates for creating content

---

## Changelog

### Version 4.0 (October 2025)
- **309+ entries** across 11 content categories (+115% growth from v3.0)
- **18 Python scripts** (8 analytics, 5 export, 3 validation, 2 quality)
- **8 historical era entries** covering 1974-present
- **5 navigation indexes** (Dashboard, Master Index, by-Year, by-Designer, by-System)
- **Custom RPG-evocative theme** (dice, character sheets, stat blocks)
- **3 configured plugins** (Datacore, Templater, Excalidraw)
- Complete educational curriculum (6-week course)
- Parallel agentic expansion (165 new entries in single session)
- Streamlined documentation structure
- Production-ready infrastructure

### Version 1.0 (October 2024)
- Initial vault structure
- All templates created
- Example content for games, publishers, designers, mechanics
- Database views configured
- Dashboard and MOC files implemented
- Complete documentation

---

*This vault is a living document of TTRPG history. Every entry, link, and query contributes to our collective understanding of this transformative medium.*

**Questions or Issues?** See [[START-HERE|START-HERE.md]] for troubleshooting and [[SESSION-COMPLETION-REPORT]] for latest updates.
