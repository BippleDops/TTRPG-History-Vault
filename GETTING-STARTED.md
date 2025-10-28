# Getting Started with Your TTRPG History Vault

Welcome to your comprehensive TTRPG History Tracking Vault! This document will help you get started exploring and using this extensive database.

---

## What's Been Built

This vault contains a complete, production-ready Obsidian database documenting tabletop roleplaying game history from 1974 to present. Here's what's included:

### 📚 Content Library

**5 Landmark Games**:
- Dungeons & Dragons (1974) - The foundation of all TTRPGs
- Call of Cthulhu (1981) - Horror gaming pioneer
- Vampire: The Masquerade (1991) - Story-focused revolution
- Dungeons & Dragons Third Edition (2000) - The d20 System
- Apocalypse World (2010) - PbtA framework creation

**5 Major Publishers**:
- TSR - Founded the industry
- Chaosium - Horror and percentile systems
- White Wolf Publishing - World of Darkness creator
- Wizards of the Coast - Modern D&D steward
- Lumpley Games - Indie innovation leader

**6 Influential Designers**:
- Gary Gygax - D&D co-creator
- Dave Arneson - D&D co-creator
- Sandy Petersen - Call of Cthulhu designer
- Mark Rein-Hagen - Vampire creator
- Monte Cook - D&D 3rd Edition co-designer
- D. Vincent Baker - PbtA framework architect

**3 Foundational Mechanics**:
- d20 System - The iconic RPG resolution mechanic
- Sanity Mechanic - Horror gaming's signature system
- Powered by the Apocalypse (Moves) - Modern indie framework

**3 Pivotal Historical Events**:
- Founding of TSR (1973) - Birth of the industry
- The Satanic Panic (1980s) - Cultural controversy and moral panic
- Release of Open Gaming License (2000) - Industry transformation

### 🛠️ Infrastructure

**6 Professional Templates**:
- Game Entry Template (with Templater automation)
- Publisher Template
- Designer Template
- Mechanics Documentation Template
- Historical Event Template
- Web Archive Template

**6 Database Views (Bases)**:
- All Games Database
- Publishers Analysis
- Design Innovations Timeline
- Games by Decade
- All Designers
- Historical Events

**Navigation & Documentation**:
- Main Dashboard with statistics and quick links
- Early Era Map of Content (MOC)
- Complete README with usage instructions
- Property Schema Reference
- Comprehensive .gitignore for version control

**Plugin Configuration**:
- Templater fully configured with folder-based auto-templates
- Dataview enabled with JavaScript queries
- Core plugins configured
- All settings optimized for database use

---

## First Steps

### 1. Open in Obsidian

```bash
cd "/Users/jonsussmanstudio/Desktop/Code Demonstrator For Karl"
# Then open "TTRPG-History-Vault" as a vault in Obsidian
```

### 2. Install Required Plugins

Go to **Settings → Community Plugins**:
1. Turn off Restricted Mode
2. Click "Browse" and search for:
   - **Templater** - Install and enable
   - **Dataview** - Install and enable

Both are already configured! Just install them.

### 3. Start Exploring

**Best Entry Points**:
1. Open **`Views/TTRPG-History-Dashboard.md`** for overview
2. Browse **`Views/All-Games.base`** to see the database interface
3. Read **`Games/Dungeons & Dragons (1974).md`** for example content
4. Check **`README.md`** for complete documentation

---

## Key Features to Explore

### 📊 Database Views (Bases)

Open any `.base` file in the Views folder:
- **Filter** by properties (year, publisher, significance, etc.)
- **Sort** by clicking column headers
- **Group** by decade, era, or other properties
- **Edit** entries by clicking to open source notes

### 🔗 Knowledge Graph

- **Graph View** (Ctrl/Cmd + G) shows all connections
- Click any node to navigate
- See how games, publishers, and designers interconnect
- Watch the knowledge network grow as you add content

### 🔍 Dynamic Queries

Every note includes Dataview queries showing:
- Related games
- Publisher catalogs
- Designer portfolios
- Mechanical evolution
- Historical relationships

### ✍️ Smart Templates

Create a new note in any folder:
1. The appropriate template auto-applies
2. Templater prompts for required information
3. Dropdown menus for categorical data
4. Cursor automatically positioned for writing
5. Embedded queries already included

---

## Adding Your First Entry

Let's add a new game together:

1. **Create the Note**:
   - Right-click on `Games` folder
   - Select "New note"
   - Name it: `Your Favorite Game (Year).md`

2. **Apply Template** (if auto-templates not working):
   - Ctrl/Cmd + P → "Templater: Insert Template"
   - Select "Game Entry Template"

3. **Fill In Data**:
   - Answer the prompts (game title, publisher, year, etc.)
   - Use suggesters for system and genre
   - Rate complexity, significance, innovation

4. **Write Content**:
   - Cursor is positioned in "Historical Context" section
   - Write 3-4 paragraphs about the game
   - Fill in other sections (Mechanical Innovations, Cultural Impact, etc.)
   - Create [[WikiLinks]] to publishers, designers, and related games

5. **View in Database**:
   - Open `Views/All-Games.base`
   - Your new entry appears automatically!
   - Filter, sort, and group to see it in context

---

## Understanding the Structure

### Folder System

```
Games/           → Individual TTRPG titles
Publishers/      → Publishing companies
Designers/       → Game creators
Mechanics/       → Game systems and innovations
Historical Context/ → Major events and controversies
Research Archive/  → Web clippings and sources
Templates/       → Template files
Views/          → Database views and MOCs
Attachments/    → Images and PDFs
```

### Property Schema

Every entry type has specific properties:

**Games** need:
- title, type, publisher, designer
- year-published, system, genre
- complexity, historical-significance, innovation-score
- tags, status

**Publishers** need:
- type, publisher-name, founded
- headquarters, era-active, significance
- tags

See **`Views/Property-Schema.md`** for complete reference.

### Linking Strategy

Create rich connections:
- Link games to their publishers: `publisher: [[TSR]]`
- Link to designers: `designer: [[Gary Gygax]]`
- Create relationship lists:
  ```yaml
  influenced-by:
    - "[[Game One]]"
    - "[[Game Two]]"
  ```

---

## Example Workflows

### Research Workflow

1. **Find a game** you want to document
2. **Research** using online sources, books, Wikipedia
3. **Archive sources** using Web Archive Template
4. **Create game entry** using Game Entry Template
5. **Link** to publishers, designers, mechanics
6. **Query** relationships using embedded Dataview

### Exploration Workflow

1. **Open Dashboard** for overview statistics
2. **Browse** an era MOC (Early Era, Golden Age, etc.)
3. **Read** example entries to understand content depth
4. **Follow links** between related entries
5. **Use Graph View** to visualize connections

### Analysis Workflow

1. **Open Bases view** for topic of interest
2. **Filter** by properties (e.g., all horror games)
3. **Sort** by significance or innovation
4. **Group** by decade or publisher
5. **Export** data or create custom reports

---

## Next Steps

### Immediate Actions

1. ✅ Install Templater and Dataview plugins
2. ✅ Open the Dashboard and explore
3. ✅ Browse a Bases view
4. ✅ Read example content
5. ✅ Try creating a new entry

### Growing the Vault

**Add More Games**:
- Classic D&D editions (AD&D, 2nd Edition, 4th Edition, 5th Edition)
- RuneQuest, Traveller, GURPS, Champions
- Pathfinder, Dungeon World, Blades in the Dark
- Modern indie darlings

**Document Publishers**:
- Paizo, Green Ronin, Evil Hat
- Pelgrane Press, Fantasy Flight Games
- Indie publishers

**Profile Designers**:
- Jonathan Tweet, Skip Williams
- Robin D. Laws, Fred Hicks
- Numerous contemporary designers

**Analyze Mechanics**:
- Hit Points, Armor Class
- Classes and Levels
- Advantage/Disadvantage
- Fate Points, Aspect-based systems

**Chronicle Events**:
- D&D 4th Edition Wars
- Pathfinder's rise
- Critical Role phenomenon
- OGL 1.1 controversy (2023)

### Advanced Usage

**Create Custom Views**:
- New .base files for specific analyses
- Filter by personal collection
- Track games you own or have played

**Build Era MOCs**:
- Golden Age (1985-2000)
- d20 Era (2000-2008)
- OSR Revival (2008-2015)
- Modern Era (2015-Present)

**Develop Research Archive**:
- Clip designer interviews
- Save convention reports
- Archive Kickstarter campaigns
- Document industry news

---

## Tips & Tricks

### Efficiency

- **Quick Switcher** (Ctrl/Cmd + O): Jump to any note instantly
- **Command Palette** (Ctrl/Cmd + P): Access all commands
- **Templater Hotkeys**: Assign keyboard shortcuts to templates
- **Starred Notes**: Star frequently-accessed notes

### Quality

- Fill all required properties for database functionality
- Write substantial content (3-4 paragraphs minimum)
- Create multiple links between related entries
- Include citations and sources
- Use consistent formatting and style

### Organization

- Use tags consistently (`ttrpg`, `game`, era tags, genre tags)
- Create MOCs for browsing by theme
- Build custom Bases views for specific interests
- Regular property validation using Dataview queries

---

## Getting Help

### Documentation

- **`README.md`** - Complete vault documentation
- **`Views/Property-Schema.md`** - All property definitions
- **Example entries** - Model content and structure

### External Resources

- [Obsidian Help](https://help.obsidian.md/)
- [Dataview Documentation](https://blacksmithgu.github.io/obsidian-dataview/)
- [Templater Documentation](https://silentvoid13.github.io/Templater/)

### TTRPG Research

- Wikipedia (use thetimetube.com for clean copies)
- RPG.net forums
- Board Game Geek RPG section
- DriveThruRPG for game catalogs
- Academic sources (Playing at the World, Game Wizards, etc.)

---

## Version Control with Git

The vault is Git-ready with proper .gitignore:

```bash
cd "TTRPG-History-Vault"
git init
git add .
git commit -m "Initial commit: TTRPG History Vault"
git remote add origin [your-repo-url]
git push -u origin main
```

Regular commits as you add content!

---

## What Makes This Special

This isn't just a collection of notes—it's a **fully functional database system** that:

✅ Uses Obsidian's native Bases (not community plugins)
✅ Includes comprehensive example content
✅ Has working templates with automation
✅ Provides multiple database views
✅ Enables sophisticated querying
✅ Creates a knowledge graph through linking
✅ Supports research and archiving
✅ Scales to thousands of entries
✅ Ready for Git version control
✅ Fully documented and explained

---

## Your Journey Begins

You now have a professional-grade TTRPG history database. Whether you're:
- **Researching** game design history
- **Cataloging** your personal collection
- **Documenting** industry developments
- **Analyzing** design trends
- **Preserving** gaming knowledge

This vault provides the structure and tools you need.

**Start exploring, start adding content, and watch your knowledge base grow!**

---

*Questions? Check the README.md or explore the example content to see how everything works.*

**Happy gaming history documentation! 🎲**
