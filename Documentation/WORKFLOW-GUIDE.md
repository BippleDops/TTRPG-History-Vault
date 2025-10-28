---
tags:
  - documentation
  - workflows
  - guide
  - tutorials
---

# Workflow Guide

Step-by-step workflows for common tasks in the TTRPG History Vault. Each workflow includes prerequisites, detailed steps, validation checks, and troubleshooting tips.

---

## Table of Contents

- [Basic Workflows](#basic-workflows)
- [Research Workflows](#research-workflows)
- [Quality Improvement Workflows](#quality-improvement-workflows)
- [Collaboration Workflows](#collaboration-workflows)
- [Maintenance Workflows](#maintenance-workflows)
- [Advanced Workflows](#advanced-workflows)

---

## Basic Workflows

### Workflow 1: Adding a New Game

**Time**: 15-30 minutes per game
**Skill Level**: Beginner

**Prerequisites**:
- Basic game information (title, year, publisher, designer)
- Templater plugin enabled
- Property schema understanding

**Steps**:

1. **Create New Note**
   - Navigate to Games/ folder
   - Ctrl/Cmd+N to create new note
   - Name file: `Game Title (Year).md`
   - Example: `Cyberpunk 2020 (1990).md`

2. **Apply Template**
   - If auto-templates configured: Template applies automatically
   - If not: Ctrl/Cmd+P → "Templater: Insert Template" → Select "Game Entry Template"

3. **Fill Required Properties**
   - **Title**: Respond to prompt (e.g., "Cyberpunk 2020")
   - **Publisher**: Enter with brackets (e.g., "[[R. Talsorian Games]]")
   - **Designer**: Enter with brackets (e.g., "[[Mike Pondsmith]]")
   - **Year**: Enter as number (e.g., 1990)
   - **System**: Select from suggester (e.g., "d10 pool")
   - **Genre**: Select from suggester (e.g., "sci-fi")
   - **Complexity**: Rate 1-5 (e.g., 3)
   - **Historical Significance**: Rate 1-5 (e.g., 4)
   - **Innovation Score**: Rate 1-5 (e.g., 4)
   - **Status**: Select from suggester (e.g., "in-print")

4. **Write Content Sections**
   - **Historical Context**: When it was released, market conditions, competition
   - **Mechanical Innovations**: Unique systems or mechanics introduced
   - **Cultural Impact**: How it influenced the hobby
   - **Design Philosophy**: What the designers were trying to achieve
   - **Setting and Themes**: World, tone, narrative focus
   - **Reception and Legacy**: Critical reception, lasting influence

5. **Add Relationships**
   - **influence-on**: List games it influenced
     ```yaml
     influence-on:
       - "[[Shadowrun (1989)]]"
       - "[[Carbon 2185 (2019)]]"
     ```
   - **influenced-by**: List games that influenced it
     ```yaml
     influenced-by:
       - "[[Traveller (1977)]]"
       - "[[Blade Runner RPG]]"
     ```

6. **Link to Related Entries**
   - Link to publisher in content: `Published by [[R. Talsorian Games]]...`
   - Link to designer: `Designed by [[Mike Pondsmith]]...`
   - Link to mechanics: `Uses the [[Interlock System]]...`

7. **Validate Entry**
   - Check all required properties filled
   - Verify WikiLinks use correct syntax `[[Target]]`
   - Ensure content sections have 2-3 paragraphs minimum
   - Run schema_validator.py to confirm compliance

8. **Update Related Entries**
   - Open publisher entry → Add to key-releases
   - Open designer entry → Add to notable-works
   - Update influenced games' influenced-by lists

**Validation Checklist**:
- [ ] All required properties present
- [ ] Publisher and designer links valid
- [ ] Relationships reciprocated (influence-on ↔ influenced-by)
- [ ] 2-3 paragraphs per content section
- [ ] At least 8 total WikiLinks to related entries

**Common Issues**:
- **"WikiLinks show as plain text"**: Missing brackets `[[]]`
- **"Publisher/designer not found"**: Create those entries first
- **"Template shows code"**: Templater plugin not enabled

---

### Workflow 2: Adding a Publisher

**Time**: 10-20 minutes
**Skill Level**: Beginner

**Steps**:

1. **Create Note**: `Publishers/Publisher Name.md`
   - Example: `Publishers/White Wolf Publishing.md`

2. **Apply Template**: Use Publisher Template

3. **Fill Properties**:
   ```yaml
   publisher-name: White Wolf Publishing
   founded: 1991
   defunct: 2006
   headquarters: Stone Mountain, Georgia
   era-active: golden-age
   significance: 5
   key-releases:
     - "[[Vampire - The Masquerade (1991)]]"
     - "[[Werewolf - The Apocalypse (1992)]]"
   notable-designers:
     - "[[Mark Rein-Hagen]]"
   tags:
     - publisher
     - golden-age
     - world-of-darkness
   ```

4. **Write Content**:
   - **History**: Founding story, growth, major milestones
   - **Business Model**: Distribution, pricing, product strategy
   - **Key Releases**: Flagship products and their impact
   - **Legacy**: Long-term influence on industry

5. **Update Related Games**:
   - For each key-release, verify game's `publisher` property points back

**Validation**:
- [ ] Founded year is number (not string)
- [ ] Key releases list games that exist
- [ ] Games' publisher properties reciprocate
- [ ] Significance rating justified in content

---

### Workflow 3: Adding a Designer

**Time**: 15-25 minutes
**Skill Level**: Beginner

**Steps**:

1. **Create Note**: `Designers/Designer Name.md`
   - Example: `Designers/Robin Laws.md`

2. **Apply Template**: Use Designer Template

3. **Fill Properties**:
   ```yaml
   designer-name: Robin Laws
   birth-year: 1964
   active-years: 1990-present
   notable-works:
     - "[[Feng Shui (1996)]]"
     - "[[HeroQuest (2003)]]"
     - "[[Ashen Stars (2011)]]"
   publishers-worked-with:
     - "[[Atlas Games]]"
     - "[[Pelgrane Press]]"
   innovations:
     - Dramatic action sequences system
     - Investigation mechanics
     - Genre-emulation design
   awards:
     - Origins Award Best RPG Rules (1996, Feng Shui)
     - Diana Jones Award (2002)
   tags:
     - designer
     - golden-age
     - modern-era
   ```

4. **Write Biography**: Career progression, design philosophy, major contributions

5. **Update Related Games**: Verify games' `designer` properties point back

---

## Research Workflows

### Workflow 4: Comprehensive Game Research

**Time**: 2-4 hours per game
**Skill Level**: Intermediate

**Goal**: Create exemplary-quality game entry with 2,000+ words and extensive documentation

**Steps**:

1. **Gather Sources** (30 minutes)
   - Search DriveThruRPG for product page
   - Find BoardGameGeek entry for ratings and discussion
   - Search RPG.net for reviews and actual play reports
   - Check Wikipedia for historical context
   - Find designer interviews or postmortems

2. **Archive Sources** (15 minutes)
   - For each source, create Web Archive entry
   - Use Web Archive Template
   - Save URLs, archive dates, key excerpts
   - File in `Research Archive/[Game Name]/`

3. **Create Game Entry** (30 minutes)
   - Follow Workflow 1 (Adding a New Game)
   - Fill all optional properties if available
   - Use archived sources for accuracy

4. **Deep Content Research** (60-90 minutes)
   - **Historical Context** (300+ words):
     - Market conditions at release
     - Competing games
     - Publisher situation
     - Designer's previous work

   - **Mechanical Innovations** (400+ words):
     - Core resolution mechanics
     - Character creation system
     - Unique subsystems
     - Innovation vs. iteration
     - Technical implementation

   - **Cultural Impact** (300+ words):
     - Sales figures (if available)
     - Critical reception
     - Award wins
     - Community adoption
     - Media references

   - **Design Philosophy** (300+ words):
     - Designer intentions
     - Target audience
     - Design goals
     - Influences on design

   - **Setting and Themes** (300+ words):
     - World description
     - Tone and genre
     - Narrative focus
     - Thematic elements

   - **Reception and Legacy** (400+ words):
     - Contemporary reviews
     - Long-term assessment
     - Influence on later games
     - Community status today
     - Reprints and new editions

5. **Build Relationship Network** (30 minutes)
   - Research games it influenced (check designer interviews, retrospectives)
   - Research its influences (check designer credits, bibliography)
   - Document mechanics it introduced or popularized
   - Link to historical events (conventions, controversies)

6. **Add Supplementary Content** (30 minutes)
   - Create supplement entries for major expansions
   - Document award wins
   - Note digital adaptations
   - Link to actual play shows featuring the game

7. **Validate and Polish** (20 minutes)
   - Run schema_validator.py
   - Run link_validator.py
   - Run reciprocal_link_checker.py
   - Proofread for clarity and accuracy
   - Verify all citations

**Quality Targets**:
- [ ] 2,000+ words total content
- [ ] 8+ WikiLinks to related entries
- [ ] 3+ archived research sources
- [ ] All optional properties filled (if available)
- [ ] Influence relationships bidirectional
- [ ] 100% property completeness

---

### Workflow 5: Web Research and Archiving

**Time**: 15-30 minutes per source
**Skill Level**: Beginner

**Tools Needed**:
- Obsidian Web Clipper (browser extension) OR
- Manual copy-paste with Web Archive Template

**Steps**:

1. **Find Source**
   - Navigate to article, review, interview, or resource

2. **Evaluate Relevance**
   - Primary source (designer interview, official announcement)? **High value**
   - Secondary source (review, retrospective)? **Medium value**
   - Tertiary source (wiki, aggregate site)? **Low value, verify elsewhere**

3. **Archive with Web Clipper** (Recommended):
   - Click Web Clipper extension icon
   - Select "Clip to Obsidian"
   - Choose template: Web Archive Template
   - Vault location: `Research Archive/`
   - Confirm clip

4. **Archive Manually** (Alternative):
   - Create note in `Research Archive/`
   - Apply Web Archive Template
   - Fill properties:
     ```yaml
     source: https://url-here.com
     title: Article Title
     archived: 2024-01-15
     author: Author Name
     type: web-archive
     category: interview
     related-games:
       - "[[Game Name]]"
     tags:
       - web-clip
       - research
       - interviews
     ```
   - Copy article content below frontmatter
   - Add your notes in separate section

5. **Link to Related Entries**
   - Open related game/publisher/designer entries
   - Add reference in "Notes and References" section
   - Example: `Source: [[Article Title (Web Archive)]]`

6. **Organize Archive**
   - Create subfolder for major topics: `Research Archive/D&D History/`
   - Use consistent naming: `Source Title (Author, Year).md`
   - Tag appropriately for future discovery

**Best Practices**:
- Archive before the source disappears
- Capture full text (sites go offline)
- Note archive date (content changes)
- Link immediately to related entries

---

## Quality Improvement Workflows

### Workflow 6: Improving Entry Quality

**Time**: 30-60 minutes per entry
**Skill Level**: Intermediate

**Goal**: Elevate entry from "Minimal" to "Standard" or "Standard" to "Exemplary" quality (see [[QUALITY-STANDARDS]])

**Steps**:

1. **Assess Current Quality**
   - Run schema_validator.py to check completeness score
   - Read [[QUALITY-STANDARDS]] for tier definitions
   - Identify which tier entry currently meets

2. **Minimal → Standard** (if entry is minimal):

   **Expand Content** (add 500-1,000 words):
   - Each section should have 2-3 paragraphs minimum
   - Add specific examples and details
   - Cite sources where possible

   **Add Relationships** (add 4+ links):
   - Link to publisher and designer
   - Add influenced-by entries (2-3 minimum)
   - Link to 2-3 related mechanics

   **Fill Optional Properties**:
   - Add edition information if applicable
   - Note player count if available
   - Document setting name

   **Add Embedded Queries**:
   - "Games This Influenced" query
   - "Related Games by Designer" query

3. **Standard → Exemplary** (if entry is standard):

   **Deep Research** (add 1,000+ words):
   - Expand each section with detailed analysis
   - Add historical context with specific dates and events
   - Document reception with specific reviews and quotes

   **Comprehensive Relationships** (add 8+ links):
   - Document full influence chain
   - Link to all supplements and expansions
   - Connect to relevant historical events
   - Link to actual play shows featuring the game

   **Archive Sources**:
   - Create 3+ web archive entries documenting research
   - Link to archives in "Notes and References"

   **Add Visual Elements**:
   - Include cover image in Attachments/
   - Create Excalidraw influence diagram (optional)
   - Embed relevant charts/tables

4. **Validate Improvements**
   - Re-run schema_validator.py
   - Check completeness increased
   - Verify all new links valid
   - Run reciprocal_link_checker.py

5. **Update Related Entries**
   - If you added influences, update target games
   - Add this game to publisher's key-releases
   - Add to designer's notable-works

**Quality Checklist**:

**Standard Quality**:
- [ ] 1,000+ words
- [ ] 2-3 paragraphs per section
- [ ] 4+ WikiLinks
- [ ] All required properties filled
- [ ] Basic relationship documentation

**Exemplary Quality**:
- [ ] 2,000+ words
- [ ] 3-4 paragraphs per section with depth
- [ ] 8+ WikiLinks
- [ ] All optional properties filled
- [ ] Comprehensive influence documentation
- [ ] 3+ archived research sources
- [ ] Custom queries showing relationships

---

### Workflow 7: Batch Quality Audit

**Time**: 2-3 hours
**Skill Level**: Advanced

**Goal**: Identify and prioritize quality improvements across entire vault section

**Steps**:

1. **Run Comprehensive Validation**
   ```bash
   python Scripts/schema_validator.py --entry-type games --output games-validation.md
   ```

2. **Generate Completeness Report**
   - Open validation report
   - Sort by completeness score (lowest first)
   - Export to spreadsheet or table

3. **Prioritize Improvements**
   - **High Priority**: Significant games (significance ≥ 4) with <80% completeness
   - **Medium Priority**: Moderate games (significance 3) with <70% completeness
   - **Low Priority**: Minor games (significance ≤ 2) with any completeness

4. **Create Improvement Plan**
   - Identify top 10 entries needing work
   - Estimate time per entry (30-60 minutes)
   - Schedule improvement sessions

5. **Systematic Improvement**
   - Work through list one entry at a time
   - Use Workflow 6 for each entry
   - Re-validate after each completion

6. **Track Progress**
   - Create Kanban board: `Views/Quality-Improvement.md`
   - Columns: To Improve | In Progress | Standard Quality | Exemplary Quality
   - Move entries as they improve

**Metrics to Track**:
- Average completeness score
- Percentage at Standard quality
- Percentage at Exemplary quality
- Total word count across vault

---

## Collaboration Workflows

### Workflow 8: Contributing New Content

**Time**: Variable
**Skill Level**: Intermediate

**Prerequisites**:
- Git installed and configured
- Vault cloned from repository
- Understanding of Git workflows

**Steps**:

1. **Pull Latest Changes**
   ```bash
   cd TTRPG-History-Vault
   git pull origin main
   ```

2. **Create Feature Branch**
   ```bash
   git checkout -b add-game-shadowrun-1989
   ```

   **Branch naming**:
   - `add-game-[name]` - New game entry
   - `add-publisher-[name]` - New publisher
   - `improve-[entry]` - Quality improvement
   - `fix-links-[section]` - Link corrections

3. **Create Content**
   - Follow appropriate workflow (1-3) for entry type
   - Meet Standard quality minimum (see [[QUALITY-STANDARDS]])
   - Follow property schema exactly

4. **Validate Before Commit**
   ```bash
   python Scripts/schema_validator.py
   python Scripts/link_validator.py
   python Scripts/reciprocal_link_checker.py
   ```

   **All scripts must pass** (exit code 0)

5. **Stage and Commit**
   ```bash
   git add "Games/Shadowrun (1989).md"
   git add "Publishers/FASA Corporation.md"  # If created
   git commit -m "Add: Shadowrun (1989) game entry

   - Complete property schema
   - 1,200 words across all sections
   - Links to FASA, Jordan Weisman, influenced games
   - Passes all validation checks"
   ```

6. **Push Branch**
   ```bash
   git push -u origin add-game-shadowrun-1989
   ```

7. **Create Pull Request**
   - Navigate to repository on GitHub/GitLab
   - Click "New Pull Request"
   - Source: your feature branch
   - Target: main
   - Fill PR template (auto-loads)

8. **Address Review Feedback**
   - Reviewers may request changes
   - Make changes in your branch
   - Commit and push updates
   - PR updates automatically

9. **Merge** (after approval)
   - Maintainer merges PR
   - Delete feature branch locally:
     ```bash
     git checkout main
     git pull origin main
     git branch -d add-game-shadowrun-1989
     ```

**See [[CONTRIBUTING]] for complete guidelines.**

---

### Workflow 9: Reviewing Pull Requests

**Time**: 15-30 minutes per PR
**Skill Level**: Advanced

**Prerequisites**:
- Repository maintainer access
- Understanding of quality standards
- Validation tools installed

**Steps**:

1. **Review PR Description**
   - Check PR template completed
   - Verify validation checkboxes checked
   - Review scope matches branch name

2. **Checkout PR Branch**
   ```bash
   git fetch origin
   git checkout pr-branch-name
   ```

3. **Run Validation Suite**
   ```bash
   python Scripts/schema_validator.py
   python Scripts/link_validator.py
   python Scripts/reciprocal_link_checker.py
   ```

   **If any fail**: Request fixes before approving

4. **Content Quality Review**
   - Open new/modified entries
   - Check against [[QUALITY-STANDARDS]]
   - Verify minimum Standard quality
   - Look for:
     - Complete required properties
     - Adequate content depth (1,000+ words)
     - Proper linking (4+ WikiLinks)
     - Accurate information

5. **Relationship Validation**
   - Check reciprocal links:
     - If game lists influence-on, verify target has influenced-by
     - If publisher lists key-releases, verify game has publisher
   - Verify new links point to existing entries

6. **Style and Formatting**
   - Consistent heading structure
   - Proper WikiLink syntax `[[Target]]`
   - Lists use YAML array format
   - No markdown syntax errors

7. **Leave Review**
   - **Approve**: If all checks pass
   - **Request Changes**: If validation fails or quality below standard
   - **Comment**: Provide specific feedback on issues

8. **Merge** (if approved)
   ```bash
   git checkout main
   git merge pr-branch-name
   git push origin main
   ```

9. **Update Changelog** (for significant additions)
   - Open CHANGELOG.md
   - Add entry under appropriate version
   - Commit: `docs: Update changelog for Shadowrun entry`

---

## Maintenance Workflows

### Workflow 10: Monthly Vault Maintenance

**Time**: 1-2 hours
**Skill Level**: Intermediate

**Frequency**: Monthly

**Checklist**:

**Week 1: Validation**
- [ ] Run schema_validator.py on all folders
- [ ] Run link_validator.py vault-wide
- [ ] Run reciprocal_link_checker.py
- [ ] Review generated reports
- [ ] Create issues for problems found

**Week 2: Link Maintenance**
- [ ] Fix broken WikiLinks identified
- [ ] Update reciprocal relationships
- [ ] Check for renamed files
- [ ] Verify all influence relationships bidirectional

**Week 3: Quality Improvements**
- [ ] Identify 5 entries with <80% completeness
- [ ] Improve each to Standard quality
- [ ] Re-validate after improvements

**Week 4: Documentation**
- [ ] Update CHANGELOG.md with month's additions
- [ ] Review and update MOCs if needed
- [ ] Check Dashboard statistics current
- [ ] Archive completed tasks from Kanban boards

**Performance Check**:
- [ ] Note vault size (MB)
- [ ] Check load time (should be <3s)
- [ ] Review query performance
- [ ] Clear Datacore cache if slow

---

### Workflow 11: Fixing Broken Relationships

**Time**: 30-60 minutes
**Skill Level**: Intermediate

**Goal**: Resolve relationship inconsistencies found by reciprocal_link_checker.py

**Steps**:

1. **Run Reciprocal Link Checker**
   ```bash
   python Scripts/reciprocal_link_checker.py --verbose
   ```

2. **Review Report**
   - Open `reciprocal-links-report.md`
   - Identify issue types:
     - Missing target files
     - Missing reciprocal properties
     - Incomplete reciprocal links

3. **Fix Missing Target Files**
   - **If target was renamed**: Update source link
   - **If target doesn't exist**: Remove link or create entry
   - **If typo**: Correct spelling

4. **Fix Missing Reciprocal Properties**
   - Open target file
   - Add missing property to frontmatter
   - Example:
     ```yaml
     # Add to influenced game:
     influenced-by:
       - "[[Source Game]]"
     ```

5. **Fix Incomplete Reciprocal Links**
   - Target has property but doesn't link back
   - Add source to target's list
   - Example:
     ```yaml
     # Game A says it influenced Game B
     # Game B has influenced-by but doesn't list Game A
     # Add to Game B:
     influenced-by:
       - "[[Game A]]"
       - "[[Previous Entry]]"
     ```

6. **Re-run Checker**
   ```bash
   python Scripts/reciprocal_link_checker.py
   ```

   Should show 0 broken relationships

7. **Commit Fixes**
   ```bash
   git add .
   git commit -m "fix: Resolve reciprocal relationship inconsistencies"
   git push
   ```

---

## Advanced Workflows

### Workflow 12: Bulk Entry Creation from Research List

**Time**: 3-5 hours for 10 entries
**Skill Level**: Advanced

**Scenario**: You have a list of 10 games to add with basic info researched

**Steps**:

1. **Prepare Data Spreadsheet**
   - Create CSV with columns matching property schema:
     - title, publisher, designer, year-published, system, genre, complexity, significance, innovation-score, status
   - Fill in all required data
   - Use exact matches for suggesters (d20, percentile, etc.)

2. **Setup QuickAdd Macro** (one-time)
   - Settings → QuickAdd → Manage Macros
   - Create macro: "Bulk Game Import"
   - Configure CSV import
   - Map CSV columns to properties
   - Set output folder: Games/

3. **Import Batch**
   - Run QuickAdd macro
   - Select prepared CSV
   - Verify file creation in Games/

4. **Quality Check Pass 1: Properties**
   - Run schema_validator.py
   - Open entries flagged as invalid
   - Fix property issues

5. **Quality Check Pass 2: Content**
   - Open each entry
   - Minimum 2 paragraphs per section
   - Add relationships (influenced-by at minimum)
   - Link to publisher and designer

6. **Quality Check Pass 3: Relationships**
   - Update publishers' key-releases
   - Update designers' notable-works
   - Add reciprocal influence links

7. **Final Validation**
   - Run all three validators
   - All must pass
   - Commit batch:
     ```bash
     git add Games/
     git commit -m "bulk: Add 10 OSR retroclone entries

     Games added:
     - OSRIC (2006)
     - Labyrinth Lord (2007)
     - Swords & Wizardry (2008)
     ...

     All entries meet Standard quality minimum."
     ```

---

### Workflow 13: Creating a Custom Era MOC

**Time**: 2-3 hours
**Skill Level**: Advanced

**Goal**: Create a comprehensive Map of Content for a specific era or theme

**Steps**:

1. **Define Scope**
   - Choose era: specific years or thematic period
   - Example: "Indie RPG Renaissance (2002-2010)"
   - Identify 10-20 key games in period

2. **Create MOC File**
   - File: `Views/Indie Renaissance MOC.md`
   - Add frontmatter:
     ```yaml
     tags:
       - moc
       - indie-games
       - 2000s
     ```

3. **Write Overview Section**
   - 2-3 paragraphs introducing era
   - Key characteristics
   - Major developments
   - Significance in TTRPG history

4. **Create Timeline Section**
   - Year-by-year breakdown
   - Major releases by year
   - Significant events
   - Publisher foundings/closures

5. **Add Dynamic Queries**

   **Games of the Era**:
   ```datacore
   TABLE
     file.link AS "Game",
     year-published AS "Year",
     publisher AS "Publisher",
     historical-significance AS "Significance"
   FROM "Games"
   WHERE year-published >= 2002 AND year-published <= 2010
     AND contains(tags, "indie")
   SORT year-published ASC
   ```

   **Publishers Active**:
   ```datacore
   TABLE
     file.link AS "Publisher",
     founded AS "Founded",
     length(key-releases) AS "Games"
   FROM "Publishers"
   WHERE founded >= 2002 AND founded <= 2010
   SORT founded ASC
   ```

   **Designers Emerged**:
   ```datacore
   TABLE
     file.link AS "Designer",
     active-years AS "Active",
     length(notable-works) AS "Games"
   FROM "Designers"
   WHERE contains(active-years, "200")
   SORT file.name ASC
   ```

6. **Write Narrative Sections**
   - **Design Movements**: Story Games, Forge theory, etc.
   - **Key Innovations**: Mechanics introduced this era
   - **Cultural Impact**: How era changed the hobby
   - **Legacy**: Influence on subsequent eras

7. **Link to Entries**
   - Mention specific games in prose with links
   - Link to designer profiles
   - Reference historical events

8. **Add to Navigation**
   - Open [[TTRPG-History-Dashboard]]
   - Add link in Era Navigation section
   - Add brief description

**Exemplar MOCs to Reference**:
- [[Early Era MOC]]
- [[Golden Age MOC]]
- [[Modern Era MOC]]

---

## Workflow Templates

### Quick Reference Card

**Daily Research Session** (1 hour):
1. Discover source (15 min)
2. Archive source (10 min)
3. Create/improve 1 entry (30 min)
4. Validate and link (5 min)

**Weekend Deep Dive** (4 hours):
1. Choose significant game
2. Comprehensive research (90 min)
3. Create exemplary entry (90 min)
4. Build relationship network (30 min)
5. Validate and publish (30 min)

**Monthly Maintenance** (2 hours):
1. Run all validators (15 min)
2. Fix 5 highest-priority issues (60 min)
3. Improve 3 incomplete entries (30 min)
4. Update documentation (15 min)

---

## Troubleshooting Workflows

### Issue: "I can't remember where I left off"

**Solution**: Daily Notes Workflow

1. Enable Daily Notes plugin
2. Create template: `Templates/Daily Research Note.md`
   ```markdown
   # Research Log - {{date}}

   ## Entries Worked On
   - [ ] [[Entry Name]] - Status notes

   ## Sources Archived
   - [ ] Source title - [[Web Archive Link]]

   ## Next Session
   - [ ] Priority task 1
   - [ ] Priority task 2
   ```
3. Use daily note to track progress
4. Review yesterday's note each session

### Issue: "My vault is getting slow"

**Solution**: Performance Optimization Workflow

1. Check vault size: Should be <500MB for <3s load
2. Reduce concurrent Datacore queries: Settings → Datacore → Max 5
3. Clear Datacore cache: Settings → Datacore → Clear Cache
4. Move heavy images to external hosting, link instead of embed
5. Archive inactive content to separate folder
6. Disable unused plugins temporarily

---

## Next Steps

- **[[ADVANCED-FEATURES]]**: Learn advanced capabilities
- **[[QUERY-COOKBOOK]]**: Copy-paste query examples
- **[[PLUGIN-INTEGRATION-GUIDE]]**: Configure helpful plugins
- **[[CONTRIBUTING]]**: Guidelines for collaboration
- **[[QUALITY-STANDARDS]]**: Quality tier definitions

---

*These workflows represent best practices developed through vault usage. Adapt them to your research style and contribute improvements back to the community.*
