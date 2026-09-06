---
tags:
  - documentation
  - plugins
  - configuration
  - reference
---

# Plugin Integration Guide

Complete configuration guide for community plugins that enhance the TTRPG History Vault. This guide covers required, recommended, and optional plugins with step-by-step setup instructions.

---

## Table of Contents

- [Required Plugins](#required-plugins)
- [Recommended Plugins](#recommended-plugins)
- [Optional Plugins](#optional-plugins)
- [Plugin Configurations](#plugin-configurations)
- [Troubleshooting](#troubleshooting)

---

## Required Plugins

These plugins are essential for vault functionality. The vault will not work correctly without them.

### Dataview

**Purpose**: Embedded queries for dynamic data views and relationships

**Installation**:
1. Settings → Community Plugins → Browse
2. Search "Dataview"
3. Click Install → Enable

**Configuration**:
```
Settings → Dataview

✓ Enable codeblock dataviews: ON
✓ Enable inline dataviews: ON
✓ Inline dataview prefix: =
✓ Enable JavaScript: ON
✓ Maximum concurrent queries: 10
```

**Why Essential**: Every embedded query in the vault is written in Dataview Query Language (DQL: `TABLE … FROM … WHERE …`) inside ```` ```dataview ```` fences. The vault has 800+ embedded queries across MOCs, the dashboard, and entry notes. (Until the 2026-09 repair the fences were labelled `datacore`; Datacore does not parse DQL, so none of them rendered.)

**Verification**:
- Open [[TTRPG-History-Dashboard]]
- Scroll to "Vault Statistics" section
- If you see a table with entry counts, Dataview is working
- If you see raw code blocks, check plugin is enabled

### Templater

**Purpose**: Dynamic templates with prompts for guided entry creation

**Installation**:
1. Settings → Community Plugins → Browse
2. Search "Templater"
3. Click Install → Enable

**Configuration**:
```
Settings → Templater

Template folder location: Templates
✓ Trigger Templater on new file creation: ON
✓ Enable Folder Templates: ON
✓ Syntax highlighting: ON

Folder Templates:
  Games → Templates/Game Entry Template.md
  Publishers → Templates/Publisher Template.md
  Designers → Templates/Designer Template.md
  Mechanics → Templates/Mechanics Documentation Template.md
  Historical Context → Templates/Historical Event Template.md
  Actual Play → Templates/Actual Play Template.md
  Supplements → Templates/Supplement Template.md
  Retroclones → Templates/Retroclone Template.md
  VTT Platforms → Templates/VTT Platform Template.md
  Digital Adaptations → Templates/Digital Adaptation Template.md
  Conventions → Templates/Convention Template.md
  Awards → Templates/Award Template.md
  Controversies → Templates/Controversy Template.md
```

**Why Essential**: All entry templates use Templater prompts for property population. Without it, templates will show raw code.

**Verification**:
- Create new note in Games/ folder
- Template should auto-apply
- You should see prompts asking for game details
- If you see `<% %>` code, check configuration

---

## Recommended Plugins

These plugins significantly enhance usability but aren't strictly required.

### Advanced Tables

**Purpose**: Spreadsheet-like table editing with formulas and formatting

**Installation**:
1. Settings → Community Plugins → Browse
2. Search "Advanced Tables"
3. Click Install → Enable

**Configuration**:
```
Settings → Advanced Tables

✓ Enable table editor: ON
✓ Format on enter: ON
✓ Format on tab: ON
✓ Alignment: Auto
✓ Column formulas: ON
```

**Use Cases**:
- Edit property comparison tables in MOCs
- Create custom data tables in notes
- Format query results for export

**Keyboard Shortcuts**:
- `Tab` - Next cell
- `Shift+Tab` - Previous cell
- `Enter` - New row
- `Ctrl/Cmd+Shift+D` - Format table

### Tracker

**Purpose**: Visualize trends and statistics over time

**Installation**:
1. Settings → Community Plugins → Browse
2. Search "Tracker"
3. Click Install → Enable

**Configuration**:
```
Settings → Tracker

✓ Auto-complete suggestions: ON
Chart type: Line
Default date format: YYYY-MM-DD
```

**Example Use Cases**:

**Track Personal Play Statistics**:
```tracker
searchType: tag
searchTarget: game, played
folder: Games
line:
    title: Games Played Per Year
    xAxisLabel: Year
    yAxisLabel: Count
```

**Visualize Significance Trends**:
```tracker
searchType: frontmatter
searchTarget: historical-significance
folder: Games
bar:
    title: Game Significance Distribution
    xAxisLabel: Significance (1-5)
    yAxisLabel: Count
```

### QuickAdd

**Purpose**: Rapid entry creation with macros and capture templates

**Installation**:
1. Settings → Community Plugins → Browse
2. Search "QuickAdd"
3. Click Install → Enable

**Configuration**:

**Create Macro: "Quick Game Entry"**
1. Settings → QuickAdd → Manage Macros
2. Add Macro: "Quick Game Entry"
3. Configure:
   - Prompt: Game Title
   - Create Note: `Games/{{VALUE}}.md`
   - Template: `Templates/Game Entry Template.md`
4. Add to Choice: Assign hotkey (e.g., Ctrl/Cmd+Shift+G)

**Create Capture: "Research Note"**
1. Add Choice: "Research Note"
2. Configure:
   - Type: Capture
   - Template: `Templates/Web Archive Template.md`
   - Folder: Research Archive
3. Assign hotkey (e.g., Ctrl/Cmd+Shift+R)

**Use Cases**:
- Rapid game entry during research sessions
- Capture web sources with one keystroke
- Batch entry creation with CSV import

---

## Optional Plugins

These plugins add specialized functionality for power users.

### Excalidraw

**Purpose**: Embedded diagrams, mind maps, and visual design

**Installation**: Community Plugins → Browse → "Excalidraw"

**Configuration**:
```
Settings → Excalidraw

Folder: Attachments/Diagrams
✓ Compatibility mode: ON
Default template: None
```

**Use Cases**:
- **Influence Network Diagrams**: Visualize game→game influence relationships
- **Publisher Timelines**: Timeline infographics showing publisher history
- **System Evolution Trees**: Branching diagrams of system lineages

**Example Integration**:

Create `Attachments/Diagrams/D&D-Influence-Network.excalidraw.md`, then embed:
```markdown
![[D&D-Influence-Network.excalidraw]]
```

### MetaEdit

**Purpose**: Quick property editing without opening notes

**Installation**: Community Plugins → Browse → "MetaEdit"

**Configuration**:
```
Settings → MetaEdit

✓ Auto-update: ON
✓ Suggest existing values: ON
Property selector: Dropdown
```

**Use Cases**:
- Bulk update `status` property across multiple games
- Quick-edit significance ratings during review
- Mass-assign tags to categories

**Keyboard Shortcuts**:
- `Ctrl/Cmd+Alt+E` - Edit frontmatter
- `Ctrl/Cmd+Alt+P` - Edit specific property

### DB Folder

**Purpose**: Alternative spreadsheet-style editing interface

**Installation**: Community Plugins → Browse → "DB Folder"

**Configuration**:
```
Settings → DB Folder

Default view: Table
✓ Enable YAML frontmatter: ON
✓ Auto-save: ON
```

**Use Cases**:
- Spreadsheet-style editing of game properties
- Bulk data entry for multiple entries
- Quick comparison across entries

**Setup**:
1. Right-click on Games/ folder
2. Select "Open as DB Folder"
3. Configure columns to match property schema
4. Edit like a spreadsheet

### Buttons

**Purpose**: Create clickable buttons for common actions

**Installation**: Community Plugins → Browse → "Buttons"

**Example Buttons**:

**Validate Vault Button**:
```button
name Validate Vault
type command
action Shell commands: Run schema_validator.py
```

**Create Game Entry**:
```button
name New Game
type note
action Games/
template Templates/Game Entry Template.md
```

**Run Link Checker**:
```button
name Check Links
type command
action Shell commands: Run link_validator.py
```

### Kanban

**Purpose**: Task management boards for vault development

**Installation**: Community Plugins → Browse → "Kanban"

**Configuration**:
```
Settings → Kanban

Date format: YYYY-MM-DD
✓ Link dates to daily notes: OFF
✓ Archive completed items: ON
```

**Use Cases**:

**Research Pipeline Board**:
Create `Views/Research-Pipeline.md`:
```markdown
---
kanban-plugin: basic
---

## To Research
- [ ] Pendragon (1985)
- [ ] Ars Magica (1987)

## In Progress
- [ ] GURPS (1986) @research

## Complete
- [x] Call of Cthulhu (1981)
```

**Content Quality Board**:
Columns: Minimal Quality | Standard Quality | Exemplary Quality

Move entries between columns as you improve them.

---

## Plugin Configurations

### Templater Advanced Setup

**Custom Scripts Folder**:

Create `.obsidian/scripts/templater/` with helper functions:

**`get_related_games.js`**:
```javascript
function getRelatedGames(tp) {
    // Query games by same designer or publisher
    return tp.frontmatter.designer;
}
module.exports = getRelatedGames;
```

**Use in Templates**:
```markdown
Related games: <% tp.user.get_related_games(tp) %>
```

### Dataview Performance Tuning

**For Vaults with 500+ Entries**:

```
Settings → Dataview

Maximum concurrent queries: 5
✓ Enable query caching: ON
Cache expiration: 300 seconds
✓ Index optimization: ON
```

**For Slower Devices**:
- Reduce concurrent queries to 3
- Increase cache expiration to 600s
- Disable inline queries (use only codeblock)

### QuickAdd Capture Templates

**Game Discovery Capture**:

Create template capturing:
- Source URL
- Game title
- Publisher (if known)
- Year (if known)
- Quick notes

Hotkey: `Ctrl/Cmd+Shift+D`

Saves to: `Research Archive/To Process/`

**Interview Capture**:

Template for designer/publisher interviews:
- Interview subject
- Publication/source
- Date published
- Key quotes
- Related games mentioned

---

## Integration Workflows

### Research Workflow with Multiple Plugins

1. **Discovery** (Browser → Obsidian Web Clipper):
   - Clip article to Research Archive
   - Auto-apply Web Archive Template

2. **Quick Entry** (QuickAdd):
   - Ctrl/Cmd+Shift+G to create game entry
   - Template prompts for required properties

3. **Property Refinement** (MetaEdit):
   - Quick-edit significance ratings
   - Mass-update tags across entries

4. **Relationship Mapping** (Excalidraw):
   - Create influence network diagram
   - Link diagram to game entries

5. **Validation** (Buttons + Shell Commands):
   - Click "Validate Vault" button
   - Review generated report
   - Fix identified issues

### Batch Entry Workflow

1. **Prepare Data** (External spreadsheet):
   - CSV with game data
   - Columns match property schema

2. **Import** (QuickAdd CSV Import):
   - Import via QuickAdd macro
   - Auto-apply templates

3. **Refine in Spreadsheet View** (DB Folder):
   - Open Games/ as DB Folder
   - Edit properties like spreadsheet

4. **Add Relationships** (Normal Obsidian):
   - Open individual notes
   - Add influence-on/influenced-by links

5. **Verify** (Python Scripts):
   - Run schema_validator.py
   - Run reciprocal_link_checker.py

### Visualization Workflow

1. **Create Diagram** (Excalidraw):
   - Design influence network
   - Color-code by era/system

2. **Add Timeline** (Tracker):
   - Visualize publication trends
   - Show significance over time

3. **Embed in MOC** (Markdown):
   - Link diagram and charts
   - Add explanatory text

4. **Export** (Print CSS):
   - Enable print-ready.css
   - Export to PDF

---

## Plugin Compatibility

### Tested Combinations

**Fully Compatible**:
- Dataview + Templater + Advanced Tables ✓
- Dataview + Tracker + Excalidraw ✓
- Templater + QuickAdd + MetaEdit ✓

**Potential Conflicts**:
- **DB Folder + Dataview**: Can cause property sync issues if editing simultaneously
  - **Solution**: Close DB Folder view before running Dataview queries
- **MetaEdit + Templater**: Hotkey conflicts possible
  - **Solution**: Assign unique hotkeys in Settings

**Performance Impact**:
- **Many plugins enabled**: Slower vault load times
  - **Solution**: Enable only plugins you actively use
- **Heavy Dataview + Tracker**: Can slow editing on older hardware
  - **Solution**: Reduce concurrent queries, increase cache time

---

## Troubleshooting

### Common Issues

**"Dataview queries don't update"**
- Clear cache: Settings → Dataview → Clear Cache
- Reload Obsidian: Ctrl/Cmd+R
- Check query syntax (requires explicit aliases)

**"Templater prompts appear as code"**
- Verify plugin enabled: Settings → Community Plugins
- Check template folder path: Settings → Templater
- Ensure file extension is `.md` not `.txt`

**"QuickAdd creates notes in wrong folder"**
- Check macro configuration: Settings → QuickAdd → Edit Macro
- Verify folder path uses forward slashes: `Games/`
- Ensure folder exists before running macro

**"MetaEdit doesn't show properties"**
- Property must exist in at least one note
- Check property name spelling (case-sensitive)
- Verify YAML formatting in frontmatter

**"DB Folder breaks property formatting"**
- Always close DB Folder view before running Dataview queries
- Use DB Folder for editing only, not viewing
- Keep backup before bulk editing

**"Buttons don't execute commands"**
- Verify command name exactly matches: Settings → Hotkeys
- Check Shell Commands plugin if using Python scripts
- Ensure scripts have execute permissions: `chmod +x script.py`

### Plugin Update Issues

**After updating plugins**:
1. Clear all caches: Settings → Obsidian → Reload without saving
2. Re-enable plugins: Settings → Community Plugins
3. Verify configurations: Check each plugin's settings
4. Test core workflows: Run validation scripts, create test note

**If queries stop working after Dataview update**:
- Check [Dataview release notes](https://github.com/blacksmithgu/obsidian-dataview/releases)
- Syntax changes may require query updates
- Use [[Query-Library]] as reference for current syntax

---

## Advanced Integration: Shell Commands

**Plugin**: Shell Commands (optional but powerful)

**Setup**:
1. Install Shell Commands plugin
2. Add commands for Python scripts:

**Command 1: Validate Schema**
```
Command: python Scripts/schema_validator.py
Working directory: {{vault_path}}
Output: Modal
```

**Command 2: Check Links**
```
Command: python Scripts/link_validator.py
Working directory: {{vault_path}}
Output: New Note (validation-report.md)
```

**Command 3: Reciprocal Links**
```
Command: python Scripts/reciprocal_link_checker.py
Working directory: {{vault_path}}
Output: New Note (reciprocal-links-report.md)
```

**Assign Hotkeys**:
- Ctrl/Cmd+Alt+V: Validate Schema
- Ctrl/Cmd+Alt+L: Check Links
- Ctrl/Cmd+Alt+R: Check Reciprocal Links

**Create Buttons** (using Buttons plugin):
```button
name 🔍 Validate All
type command
action Shell commands: Validate Schema
```

---

## Recommended Plugin Combinations by Use Case

### For Researchers
- **Required**: Dataview, Templater
- **Recommended**: QuickAdd, Advanced Tables
- **Optional**: Obsidian Web Clipper (browser extension)

### For Data Managers
- **Required**: Dataview, Templater
- **Recommended**: MetaEdit, DB Folder, Advanced Tables
- **Optional**: Shell Commands

### For Visual Learners
- **Required**: Dataview, Templater
- **Recommended**: Excalidraw, Tracker
- **Optional**: Kanban

### For Collaborators
- **Required**: Dataview, Templater
- **Recommended**: Git, Shell Commands
- **Optional**: Kanban (for task tracking)

---

## Plugin Resources

### Documentation Links

- **Dataview**: https://blacksmithgu.github.io/obsidian-dataview/
- **Templater**: https://silentvoid13.github.io/Templater/
- **Advanced Tables**: https://github.com/tgrosinger/advanced-tables-obsidian
- **Tracker**: https://github.com/pyrochlore/obsidian-tracker
- **QuickAdd**: https://github.com/chhoumann/quickadd

### Community Resources

- Obsidian Forum: https://forum.obsidian.md/
- Obsidian Discord: https://discord.gg/obsidianmd
- Plugin-specific GitHub issues

---

## Next Steps

- **[[ADVANCED-FEATURES]]**: Deep dive into vault capabilities
- **[[QUERY-COOKBOOK]]**: Copy-paste query examples
- **[[WORKFLOW-GUIDE]]**: Step-by-step common workflows
- **[[README]]**: Complete vault documentation

---

*This guide covers the most useful plugin integrations for the TTRPG History Vault. Experiment with different combinations to find what works best for your research style.*
