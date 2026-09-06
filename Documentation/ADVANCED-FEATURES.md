---
tags:
  - documentation
  - advanced
  - reference
---

# Advanced Features Guide

This guide documents advanced features, enhancements, and power-user techniques for the TTRPG History Vault. These features extend the basic functionality described in the README and enable sophisticated research, visualization, and automation workflows.

---

## Table of Contents

- [Query Library](#query-library)
- [New Content Types](#new-content-types)
- [CSS Customization](#css-customization)
- [Python Automation Scripts](#python-automation-scripts)
- [Plugin Integrations](#plugin-integrations)
- [Advanced Dataview Techniques](#advanced-dataview-techniques)
- [Templater Automation](#templater-automation)
- [Workflow Optimization](#workflow-optimization)

---

## Query Library

The [[Query-Library]] contains 30+ advanced Dataview query patterns for sophisticated data analysis. These queries go beyond basic filtering to provide insights into TTRPG history.

### Quick Access Categories

**Temporal Analysis**
- Games by decade with significance trends
- Publication timelines by publisher
- Designer career trajectories
- Mechanic innovation waves

**Relationship Mapping**
- Influence networks (who influenced whom)
- Publisher-designer connections
- Game lineages and spiritual successors
- Mechanic adoption patterns

**Statistical Queries**
- Average complexity by era
- Genre distribution analysis
- Publisher market share over time
- Innovation hotspots by decade

**Cross-Type Analysis**
- Designer impact scores (weighted by game significance)
- Publisher legacy calculations
- Mechanic popularity trends
- Event impact ripples

### Using Query Patterns

1. **Copy Query from Library**: Navigate to [[Query-Library]], find the pattern you need
2. **Paste into Your Note**: Insert into any markdown file
3. **Customize Parameters**: Adjust WHERE clauses, date ranges, significance thresholds
4. **Embed in MOCs**: Use in Maps of Content for dynamic dashboards

**Example**: Finding all games that influenced modern design:

```dataview
TABLE file.link AS "Game", year-published AS "Year", length(influence-on) AS "Influenced"
FROM "Games"
WHERE year-published >= 2000 AND length(influence-on) > 0
SORT length(influence-on) DESC
```

See [[Query-Library]] for complete documentation and 30+ ready-to-use patterns.

---

## New Content Types

Beyond the original five entry types (Games, Publishers, Designers, Mechanics, Historical Events), the vault now supports eight additional content categories:

### Actual Play Shows

Document actual play series like Critical Role, The Adventure Zone, or Glass Cannon Podcast.

**Template**: `Templates/Actual Play Template.md`
**Properties**: format, system-used, cast, platform, cultural-impact, audience-size
**Example Use Cases**:
- Track how actual play influenced game popularity
- Document the "streaming era" of TTRPGs
- Analyze which systems get most play online

**Creating an Entry**:
1. Create new note in `Actual Play/` folder
2. Apply Actual Play Template
3. Document show details, cultural impact, notable moments
4. Link to games played and systems used

### Supplements & Adventures

Document expansions, sourcebooks, adventure modules, and campaign settings.

**Template**: `Templates/Supplement Template.md`
**Properties**: parent-game, supplement-type, page-count, notable-content
**Example Use Cases**:
- Track evolution of D&D adventures over editions
- Document landmark modules (Tomb of Horrors, Curse of Strahd)
- Analyze publisher supplement strategies

### Retroclones

Document OSR retroclones that emulate older editions.

**Template**: `Templates/Retroclone Template.md`
**Properties**: emulates, license, design-goals
**Example Use Cases**:
- Map the OSR family tree
- Document legal strategies (OGL, Creative Commons)
- Track which editions get most clones

### VTT Platforms

Document virtual tabletop platforms like Roll20, Foundry VTT, Fantasy Grounds.

**Template**: `Templates/VTT Platform Template.md`
**Properties**: supported-systems, features, pricing-model, user-base, impact-on-industry
**Example Use Cases**:
- Track digital transformation of TTRPGs
- Document COVID-19 era shift to online play
- Compare platform features and adoption

### Digital Adaptations

Document video game adaptations, mobile apps, and digital implementations.

**Template**: `Templates/Digital Adaptation Template.md`
**Properties**: source-game, platform, developer, adaptation-type, adaptation-quality
**Example Use Cases**:
- Track crossover between TTRPGs and video games
- Document successful (and failed) adaptations
- Analyze which games work best digitally

### Conventions

Document gaming conventions from Gen Con to local events.

**Template**: `Templates/Convention Template.md`
**Properties**: location, frequency, attendance, notable-events
**Example Use Cases**:
- Track industry gathering points
- Document convention culture evolution
- Link major announcements to conventions

### Awards

Document industry awards like Origins Awards, ENnies, Diana Jones Award.

**Template**: `Templates/Award Template.md`
**Properties**: founded, categories, administering-body, significance
**Example Use Cases**:
- Track what the industry values over time
- Identify consensus "best" games
- Document recognition patterns

### Controversies

Document industry controversies, scandals, and disputes.

**Template**: `Templates/Controversy Template.md`
**Properties**: parties-involved, impact-areas, resolution, significance
**Example Use Cases**:
- Understand industry conflicts
- Track ethical evolution
- Document cautionary tales

---

## CSS Customization

The vault includes five CSS snippets for visual enhancement. Enable them via Settings → Appearance → CSS snippets.

### Entry Type Colors

**File**: `.obsidian/snippets/entry-type-colors.css`

Color-codes the `type` property in metadata panel:
- 🟦 **Games** = Blue (#4A90E2)
- 🟪 **Designers** = Purple (#9B59B6)
- 🟥 **Publishers** = Red (#E74C3C)
- 🟩 **Mechanics** = Green (#2ECC71)
- 🟨 **Events** = Yellow (#F39C12)

**When to Use**: Always enabled for quick visual identification of entry types.

### Era Themes

**File**: `.obsidian/snippets/era-themes.css`

Applies era-specific color themes to MOC files:
- **Early Era** (1974-1985): Brown/beige parchment
- **Golden Age** (1985-2000): Purple/gold royal theme
- **d20 Era** (2000-2008): Blue/silver technical theme
- **OSR Revival** (2008-2015): Dark wood grain
- **Modern Era** (2015+): Clean white/accent colors

**When to Use**: Enable for immersive historical browsing. Creates visual distinction between eras.

### Property Display Formatting

**File**: `.obsidian/snippets/property-display-formatting.css`

Advanced property visualization:
- **Icons for links**: 🎲 games, 👤 designers, 🏢 publishers, ⚙️ mechanics
- **Significance badges**: 5/5 = gold gradient, 4/5 = silver, etc.
- **Date formatting**: Monospace with calendar icons
- **Tag pills**: Rounded, colored by category

**When to Use**: Enable for enhanced readability in reading mode and Bases views.

### Mobile Optimization

**File**: `.obsidian/snippets/mobile-optimized.css`

Responsive design for mobile/tablet:
- Larger touch targets (48px minimum)
- Collapsible sections in reading mode
- Optimized table display (horizontal scroll)
- Simplified property panels

**When to Use**: Enable when using Obsidian Mobile for vault access.

### Print-Ready Styles

**File**: `.obsidian/snippets/print-ready.css`

PDF export optimization:
- Removes UI chrome (sidebars, ribbons)
- Adds page numbers
- Ensures images fit within margins
- Optimized font sizes for print
- Black & white friendly

**When to Use**: Enable before exporting notes to PDF (Settings → Export to PDF).

---

## Python Automation Scripts

Three Python scripts automate validation and maintenance tasks. Run from vault root or Scripts/ folder.

### Link Validator

**Script**: `Scripts/link_validator.py`

Scans all markdown files for broken [[WikiLinks]] and suggests fixes.

**Usage**:
```bash
cd "TTRPG-History-Vault"
python Scripts/link_validator.py
```

**Options**:
- `--folder Games` - Check specific folder only
- `--verbose` - Show all links including valid ones
- `--output report.md` - Write report to file

**Output**:
```
Validating vault at: /Users/you/TTRPG-History-Vault
Found 97 markdown files

✓ Call of Cthulhu (1981).md - All 8 links valid
✗ RuneQuest (1978).md - 1 broken link
  - [[Greg Stafford]] not found (did you mean: Greg Stafford Jr?)

==============================
SUMMARY
Total files: 97
Valid links: 1,247
Broken links: 3
```

**When to Run**:
- Before committing changes
- After bulk renames
- Monthly maintenance check

### Schema Validator

**Script**: `Scripts/schema_validator.py`

Validates all entries conform to property schemas. Calculates completeness scores.

**Usage**:
```bash
python Scripts/schema_validator.py
python Scripts/schema_validator.py --entry-type games
python Scripts/schema_validator.py --verbose
```

**Options**:
- `--entry-type games` - Check specific type only
- `--verbose` - Show valid files too
- `--output validation-report.md` - Write report

**Output**:
```
✗ Shadowrun (1989).md - Missing: complexity, innovation-score (75.0% complete)
✓ Traveller (1977).md - 100.0% complete

==============================
VALIDATION SUMMARY
Total Files: 20
Valid: 18 (90.0%)
Invalid: 2

Average Completeness: 92.5%
```

**When to Run**:
- Before submitting new entries
- During quality audits
- After template updates

### Reciprocal Link Checker

**Script**: `Scripts/reciprocal_link_checker.py`

Validates bidirectional relationships are consistent. Identifies missing reciprocal links.

**Usage**:
```bash
python Scripts/reciprocal_link_checker.py
python Scripts/reciprocal_link_checker.py --verbose
```

**Checks**:
- `influence-on` ↔ `influenced-by`
- `key-releases` ↔ `publisher`
- `notable-works` ↔ `designer`
- `games-using` ↔ mechanic references

**Output**:
```
✓ D&D (1974).influence-on ↔ AD&D (1977).influenced-by
✗ Traveller (1977).influence-on → Coriolis (2016): Missing reciprocal

==============================
SUMMARY
Total Relationships: 342
Valid: 338 (98.8%)
Broken: 4
```

**When to Run**:
- After adding influence relationships
- During link maintenance
- Before major releases

---

## Plugin Integrations

The vault works with additional community plugins for enhanced functionality.

### Recommended Plugins

**Dataview** (Required)
- Embedded queries
- Database views
- Statistical analysis

**Templater** (Required)
- Dynamic templates
- Automated property prompts
- Folder-based templates

**Advanced Tables** (Recommended)
- Spreadsheet-like table editing
- Formula support
- Quick formatting

**Tracker** (Optional)
- Visualize trends over time
- Track personal play statistics
- Graph significance scores

**QuickAdd** (Optional)
- Rapid entry macros
- Capture templates
- Batch operations

See [[PLUGIN-INTEGRATION-GUIDE]] for detailed configuration instructions.

---

## Advanced Dataview Techniques

### Self-Referential Queries

Use `this.file.link` to query relationships to current note:

```dataview
TABLE file.link AS "Game", year-published AS "Year"
FROM "Games"
WHERE contains(influenced-by, this.file.link)
SORT year-published ASC
```

**Use Case**: Embedded in game entries to show "Games This Influenced"

### Calculated Fields

Use inline JavaScript for complex calculations:

```dataview
TABLE
  file.link AS "Game",
  year-published AS "Year",
  (historical-significance + innovation-score) / 2 AS "Impact Score"
FROM "Games"
WHERE historical-significance >= 4
SORT (historical-significance + innovation-score) DESC
```

### Conditional Formatting

Combine WHERE with property checks:

```dataview
TABLE file.link AS "Publisher", founded AS "Founded"
FROM "Publishers"
WHERE defunct AND founded < 2000
SORT founded ASC
```

### List Operations

Work with list properties:

```dataview
TABLE
  file.link AS "Designer",
  length(notable-works) AS "Games Designed",
  active-years AS "Career"
FROM "Designers"
WHERE length(notable-works) >= 3
SORT length(notable-works) DESC
```

### Grouping and Aggregation

Group results by property:

```dataview
TABLE WITHOUT ID
  length(rows) AS "Count",
  round(avg(rows.historical-significance), 1) AS "Avg Significance"
FROM "Games"
WHERE year-published
GROUP BY floor(year-published / 10) * 10 + "s" AS "Decade"
SORT Decade ASC
```

See [[Query-Library]] for 30+ practical examples.

---

## Templater Automation

### Dynamic Prompts

Templates use Templater prompts for guided data entry:

```markdown
year-published: <% tp.system.prompt("Year published (YYYY)") %>
```

**When the template runs**: User is prompted for year, response populates property.

### Suggesters

Dropdown menus for categorical data:

```markdown
system: <% tp.system.suggester(["d20", "Percentile", "PBTA"], ["d20", "percentile", "pbta"]) %>
```

**Result**: User selects from predefined options, ensuring consistency.

### Cursor Positioning

Place cursor after template application:

```markdown
## Historical Context

<% tp.file.cursor(1) %>

## Mechanical Innovations
```

**Result**: Cursor appears in Historical Context section, ready to type.

### Auto-Dates

Automatically insert current date:

```markdown
archived: <% tp.date.now("YYYY-MM-DD") %>
```

### Folder-Based Templates

Configure automatic template application:

Settings → Templater → Folder Templates:
- `Games/` → `Templates/Game Entry Template.md`
- `Publishers/` → `Templates/Publisher Template.md`

**Result**: Creating a note in Games/ automatically applies Game Entry Template.

---

## Workflow Optimization

### Research Workflow

1. **Discover Game/Publisher/Designer** through web research
2. **Archive Sources** using Web Archive Template
3. **Create Entry** using appropriate template
4. **Link Relationships** to related entries
5. **Validate** using Python scripts
6. **Query Connections** using Dataview

### Batch Entry Workflow

1. **Prepare Data** in spreadsheet (CSV)
2. **Import** using QuickAdd plugin
3. **Validate** using schema_validator.py
4. **Check Links** using link_validator.py
5. **Fix Issues** identified by validators
6. **Verify** using reciprocal_link_checker.py

### Quality Improvement Workflow

1. **Run Validators** to identify incomplete entries
2. **Sort by Completeness** (schema_validator.py output)
3. **Research Missing Data** for lowest-scoring entries
4. **Update Properties** and content
5. **Re-validate** to verify improvements

### Collaboration Workflow

1. **Clone Repository** (see Git setup in CONTRIBUTING.md)
2. **Create Branch** for your additions
3. **Add/Edit Entries** following standards
4. **Run All Validators** before committing
5. **Commit with Standards** (see CONTRIBUTING.md)
6. **Push and Create PR** with template
7. **Address Review Feedback**
8. **Merge** once approved

---

## Performance Tips

### Query Optimization

- **Limit Result Sets**: Use `LIMIT 20` for large queries
- **Filter Early**: Put most restrictive WHERE clauses first
- **Avoid Wildcards**: Specific folder paths perform better than `OR`
- **Cache Results**: Heavy queries in dedicated notes rather than embedded everywhere

### Large Vault Management

- **Folder Organization**: Keep related entries in subfolders (e.g., `Games/1970s/`)
- **Archive Old Notes**: Move inactive content to `Archives/` folder
- **External Images**: Link to images rather than embedding huge files
- **Selective Indexing**: Use `.nomedia` in folders you don't want indexed

### Mobile Performance

- **Simplified Views**: Create mobile-specific MOCs with fewer embedded queries
- **Enable Mobile CSS**: Use mobile-optimized.css snippet
- **Sync Selectively**: If using Obsidian Sync, exclude heavy attachments
- **Close Graphs**: Disable graph view on mobile (Settings → Core Plugins)

---

## Troubleshooting

### Common Issues

**"Dataview queries show 'No results'"**
- Check folder path in FROM clause (exact match required)
- Verify property names match schema exactly (case-sensitive)
- Ensure Dataview plugin is enabled and updated

**"Template prompts don't appear"**
- Verify Templater plugin is enabled
- Check Settings → Templater → Template folder location
- Ensure template uses correct syntax: `<% %>` not `{% %}`

**"CSS snippets don't apply"**
- Enable in Settings → Appearance → CSS snippets
- Reload Obsidian (Ctrl/Cmd + R)
- Check for CSS conflicts with theme

**"Python scripts error: Module not found"**
- Install PyYAML: `pip install pyyaml`
- Run from vault root directory
- Use Python 3.7+ (`python --version`)

**"Reciprocal links broken after rename"**
- Run reciprocal_link_checker.py to identify issues
- Use Obsidian's "Update links in vault" when renaming
- Manually fix relationships if bulk rename occurred outside Obsidian

---

## Next Steps

- **[[QUERY-COOKBOOK]]**: Practical copy-paste query examples
- **[[PLUGIN-INTEGRATION-GUIDE]]**: Detailed plugin configurations
- **[[WORKFLOW-GUIDE]]**: Common workflows step-by-step
- **[[CONTRIBUTING]]**: Guidelines for adding content
- **[[QUALITY-STANDARDS]]**: Quality requirements

---

*This guide documents the advanced capabilities of the TTRPG History Vault. Experiment with these features to unlock the full power of your historical research.*
