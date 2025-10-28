# 🎲 START HERE - TTRPG History Vault

**Your Complete Quick Start Guide**

---

## 📊 What You Have

The **TTRPG History Vault** is a comprehensive Obsidian knowledge base documenting 50+ years of tabletop roleplaying game history (1974-present). This vault serves researchers, educators, game designers, publishers, and players.

### Current Statistics

**Content Entries: 309+ total**
- **Games**: 73 entries (D&D, Pathfinder, World of Darkness, PbtA games, OSR, indie, international)
- **Designers**: 39 profiles (Gygax, Baker, Crane, Harper, Cook, Stafford, Petersen, Hite, Laws, and more)
- **Publishers**: 33 companies (TSR, WotC, Paizo, White Wolf, Evil Hat, Chaosium, Free League, and more)
- **Mechanics**: 23 innovations (dice systems, initiative, character creation, magic systems)
- **Historical Eras**: 8 comprehensive era entries (Dawn Era 1974-1979 through Modern Landscape 2020-Present)
- **Controversies**: 11 historical moments (Satanic Panic, edition wars, industry disputes)
- **Supplements**: 11 major releases (Greyhawk, Blackmoor, Unearthed Arcana, etc.)
- **Campaign Settings**: 10 worlds (Forgotten Realms, Dragonlance, Eberron, Glorantha, etc.)
- **Retroclones**: 11 OSR games (OSRIC, Labyrinth Lord, Old School Essentials, etc.)
- **VTT Platforms**: 10 platforms (Roll20, Foundry VTT, Fantasy Grounds, etc.)
- **Actual Play Shows**: 15 shows (Critical Role, NADDPOD, Dimension 20, TAZ, and more)

**Infrastructure: 18 Python scripts**
- 8 analytics scripts (trends, networks, timelines, coverage gaps)
- 5 export scripts (Hugo website, PDF, EPUB, JSON API, Anki flashcards)
- 2 quality tools (quality enhancer, bibliography generator)
- 3 validation scripts (link validator, schema validator, reciprocal checker)

---

## 🚀 Quick Start (5 Minutes)

### 1. Open in Obsidian

1. Launch Obsidian
2. Open this folder as a vault: `File → Open vault → Open folder as vault`
3. Select: `/Users/jonsussmanstudio/Desktop/Code Demonstrator For Karl/TTRPG-History-Vault`

### 2. Required Plugins

**Core Plugins** (Settings → Core Plugins):
- ✅ Properties
- ✅ Backlinks
- ✅ Graph View
- ✅ Outline
- ✅ Tags

**Community Plugins** (Settings → Community Plugins → Browse):
- ✅ **Datacore** (NOT Dataview - critical distinction!)
  - For embedded database queries
  - Shows relationships between entries
- ✅ **Templater** (optional)
  - For creating new entries from templates
- ✅ **Excalidraw** (optional)
  - For viewing hand-drawn diagrams

### 3. Explore the Vault

**Start with navigation hubs:**
- **[[TTRPG-History-Dashboard]]** - Main navigation hub with stats, queries, and quick links
- **[[MASTER-INDEX]]** - Complete A-Z reference to all 309+ entries
- **[[Games-by-Year]]** - Chronological timeline from 1974 to present
- **[[Games-by-Designer]]** - Browse by creator and explore design philosophies
- **[[Games-by-System]]** - Browse by mechanical family (d20, PbtA, FitD, etc.)
- **[[Historical Context]]** - Explore 8 comprehensive historical eras

**Or browse folders directly:**
- `Games/` - Browse 73 comprehensive game entries
- `Designers/` - Read 39 designer profiles and philosophies
- `Publishers/` - Understand 33 company histories
- `Historical Context/` - Read 8 era entries covering 50 years
- `Actual Play/` - Explore 15 streaming show cultural impacts

**Try the Graph View:**
- Click the graph icon in the left sidebar
- See the knowledge network of interconnected entries
- Click any node to open that entry

---

## 🔍 Using the Vault

### Finding Content

**Method 1: Quick Switcher** (Cmd/Ctrl + O)
- Type any game, designer, or publisher name
- Instantly jump to that entry

**Method 2: Search** (Cmd/Ctrl + Shift + F)
- Full-text search across all entries
- Search by year, genre, mechanic, or any keyword

**Method 3: Browse Folders**
- Navigate folder tree in left sidebar
- Each folder contains related entries

**Method 4: Follow Links**
- Every entry contains wikilinks to related content
- Click any `[[Link]]` to explore connections

### Understanding Entry Structure

Every entry contains:

**Frontmatter** (metadata at top):
```yaml
---
title: Dungeons & Dragons
type: game
year-published: 1974
designer: [[Gary Gygax]], [[Dave Arneson]]
publisher: [[TSR]]
---
```

**Sections**:
- Overview and history
- Detailed analysis (mechanics, design, impact)
- Cultural significance
- Legacy and influence
- References

**Datacore Queries** (at bottom):
- Dynamic tables showing related entries
- Auto-updates as you add content

### Adding New Entries

1. **Create new note** in appropriate folder
2. **Copy frontmatter** from similar entry
3. **Fill in metadata** and write content
4. **Add wikilinks** to related entries: `[[Game Name]]`
5. **Add tags** for categorization

See `Templates/` folder for entry templates.

---

## 📈 Analytics & Insights

### Running Analytics (Requires Python)

**Prerequisites:**
```bash
pip install pyyaml matplotlib pandas networkx scipy plotly seaborn
```

**Run all analytics:**
```bash
cd "/Users/jonsussmanstudio/Desktop/Code Demonstrator For Karl/TTRPG-History-Vault"
chmod +x Scripts/run_all_analytics.sh
./Scripts/run_all_analytics.sh
```

**Output:** 15+ visualizations and 8 CSV datasets in `Attachments/Diagrams/analytics/`

**Individual scripts:**
```bash
# Publication trends over time
python3 Scripts/analytics/publication_trends.py

# Designer influence network
python3 Scripts/analytics/influence_network.py

# Innovation timeline
python3 Scripts/analytics/innovation_timeline.py

# Coverage gap analysis
python3 Scripts/analytics/coverage_gaps.py

# System family trees
python3 Scripts/analytics/system_family_tree.py

# Era comparison
python3 Scripts/analytics/era_comparison.py

# Complexity vs popularity
python3 Scripts/analytics/complexity_popularity.py

# Designer contribution matrix
python3 Scripts/analytics/designer_matrix.py
```

### Exporting Content (Multiple Formats)

**Run all exports:**
```bash
chmod +x Scripts/run_all_exports.sh
./Scripts/run_all_exports.sh
```

**Individual exports:**
```bash
# Static website (Hugo)
python3 Scripts/export/hugo_exporter.py

# PDF anthology (requires Pandoc + LaTeX)
python3 Scripts/export/pdf_compiler.py

# EPUB ebook (requires Pandoc)
python3 Scripts/export/epub_generator.py

# JSON API
python3 Scripts/export/json_api_exporter.py

# Anki flashcards
python3 Scripts/export/anki_flashcards.py
```

**Output:** `Exports/` folder with all formats

---

## 🎯 Common Use Cases

### For Researchers

**Tools:**
- JSON API for computational analysis
- 8 CSV datasets for statistical analysis
- Bibliography generator (Chicago/MLA/APA)
- Influence network data for network analysis

**Start here:**
1. Run analytics: `./Scripts/run_all_analytics.sh`
2. Export JSON API: `python3 Scripts/export/json_api_exporter.py`
3. Load CSVs in R/Python from `Attachments/Diagrams/analytics/`

### For Educators

**Resources:**
- Complete 6-week curriculum in `Educational/Curricula/History-of-RPGs-101/`
- Anki flashcards for student study
- Hugo website for class portal
- EPUB for assigned reading

**Start here:**
1. Review syllabus: `Educational/Curricula/History-of-RPGs-101/00-Syllabus.md`
2. Generate flashcards: `python3 Scripts/export/anki_flashcards.py`
3. Export website: `python3 Scripts/export/hugo_exporter.py`

### For Game Designers

**Research:**
- System family trees showing mechanical evolution
- Designer profiles documenting philosophies
- Influence networks revealing design lineages
- Comprehensive mechanical innovation catalog

**Start here:**
1. Explore `Mechanics/` folder
2. Read designer profiles in `Designers/`
3. Run system family tree analysis
4. Use Graph View to explore connections

### For Players

**Discovery:**
- 73 comprehensive game histories
- Designer backgrounds and philosophies
- System comparisons and recommendations
- Related games suggestions

**Start here:**
1. Browse `Games/` folder
2. Use Graph View to explore relationships
3. Read `Actual Play/` for streaming shows
4. Follow wikilinks to discover new games

---

## 📚 Additional Documentation

All advanced documentation is now organized in the `Documentation/` folder:

**For Advanced Users:**
- `Documentation/ADVANCED-FEATURES.md` - Advanced Obsidian features
- `Documentation/CUSTOMIZATION-GUIDE.md` - Personalizing the vault
- `Documentation/PLUGIN-INTEGRATION-GUIDE.md` - Plugin setup
- `Documentation/QUERY-COOKBOOK.md` - Datacore query examples
- `Documentation/WORKFLOW-GUIDE.md` - Content creation workflows

**For Contributors:**
- `CONTRIBUTING.md` - How to contribute content
- `QUALITY-STANDARDS.md` - Content quality requirements
- `Documentation/TESTING-GUIDE.md` - Testing procedures
- `Documentation/VALIDATION-CHECKLIST.md` - Quality checklist

**For Developers:**
- `PARALLEL-AGENTS-GUIDE.md` - Using Claude Code for expansion
- `SESSION-COMPLETION-REPORT.md` - Latest session achievements
- `Scripts/` folder - All Python analytics and export code

---

## 🛠️ Quality & Maintenance

### Check Content Quality

```bash
# Analyze all content quality
python3 Scripts/quality_enhancer.py

# Check for broken links
python3 Scripts/link_validator.py

# Find coverage gaps
python3 Scripts/analytics/coverage_gaps.py

# Validate entry schemas
python3 Scripts/schema_validator.py
```

### Generate Citations

```bash
# Chicago style
python3 Scripts/bibliography_generator.py --style chicago

# MLA style
python3 Scripts/bibliography_generator.py --style mla

# APA style
python3 Scripts/bibliography_generator.py --style apa
```

**Output:** `Exports/bibliography-{style}.txt`

---

## 🎓 Learning Path

**Week 1: Explore**
1. Read this guide completely
2. Browse 10-15 entries across different folders
3. Try the Graph View to see connections
4. Run one analytics script to see visualizations

**Week 2: Deepen**
1. Read designer profiles of your favorite designers
2. Explore game entries for systems you know
3. Follow wikilinks to discover new connections
4. Try searching for specific topics

**Week 3: Analyze**
1. Run all analytics scripts
2. Review generated visualizations
3. Export content in different formats
4. Generate a bibliography for a research topic

**Week 4: Contribute**
1. Add a new game entry you know well
2. Link it to existing entries
3. Add tags and complete frontmatter
4. Run quality checks on your addition

---

## 🚨 Troubleshooting

**Problem: Datacore queries not working**
- Solution: Install Datacore plugin (NOT Dataview!)
- Go to: Settings → Community Plugins → Browse → Search "Datacore"

**Problem: Python scripts failing**
- Solution: Install required packages
- Run: `pip install pyyaml matplotlib pandas networkx scipy plotly seaborn`

**Problem: Broken links showing**
- Solution: Normal for growing vault, run link validator
- Run: `python3 Scripts/link_validator.py`

**Problem: Analytics output directory missing**
- Solution: Scripts create directories automatically
- Ensure you have write permissions to vault folder

---

## 🎉 You're Ready!

**Your TTRPG History Vault contains:**
✅ 309+ comprehensive entries spanning 50 years (+115% growth!)
✅ 5 navigation indexes (Dashboard, Master Index, by-Year, by-Designer, by-System)
✅ 8 historical era entries covering complete TTRPG timeline
✅ 18 Python scripts for analysis and export
✅ Custom RPG-evocative theme (dice, character sheets, stat blocks)
✅ Complete infrastructure for research and education
✅ Production-ready for publication, teaching, or personal use

**Next steps:**
1. Start with [[TTRPG-History-Dashboard]] to explore navigation options
2. Browse [[MASTER-INDEX]] for A-Z access to all content
3. Run analytics to see patterns: `./Scripts/run_all_analytics.sh`
4. Add your own entries using templates
5. Share insights with the community

**For questions or issues:**
- Review documentation in `Documentation/` folder
- Check `COMPREHENSIVE-IMPROVEMENT-SUMMARY.md` for complete v4.0 achievements
- Consult `PARALLEL-AGENTS-GUIDE.md` for expansion methodology

---

**🎲 Welcome to the ultimate TTRPG History Vault! 🎲**

*Last Updated: October 27, 2025*
*Version: 4.0*
*Entries: 309+ | Scripts: 18 | Historical Eras: 8 | Navigation Indexes: 5 | Status: Production-Ready*
