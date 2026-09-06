# Contributing to TTRPG History Vault

Thank you for your interest in contributing! This guide will help you add content while maintaining vault quality and consistency.

## Getting Started

1. **Fork the Repository** (if using GitHub)
2. **Clone Your Fork**
   ```bash
   git clone https://github.com/YOUR-USERNAME/TTRPG-History-Vault.git
   cd TTRPG-History-Vault
   ```
3. **Create a Branch**
   ```bash
   git checkout -b feature/new-game-shadowrun
   ```

## Content Standards

### Required Quality Levels

- **Word Count**: 2,000+ words per entry
- **Links**: Minimum 8 WikiLinks to related content
- **Citations**: All historical claims must have sources
- **Property Schema**: 100% compliance with schemas
- **Datacore Queries**: All queries must execute without errors

### Property Schema Compliance

Each entry type has strict required properties. See [[Property-Schema]] for complete reference.

**Games** must have:
- title, type, publisher, designer, year-published, system, genre (list), complexity (1-5), historical-significance (1-5), innovation-score (1-5), tags (list), status

**Publishers** must have:
- title, type, founded, headquarters, significance (1-5), era-active, tags, status

**Designers** must have:
- title, type, nationality, active-years, tags, status

[Continue for all types]

### Writing Style

- **Encyclopedic but Engaging**: Factual tone with narrative flow
- **Third Person**: Avoid "I" and "you"
- **Present/Past Tense**: Present for current facts, past for historical events
- **Citations**: Include in "Notes and References" section

### Sections Structure

**Game Entries**:
1. Historical Context (background, market position, development)
2. Mechanical Innovations (bullet list of key systems)
3. Cultural Impact (influence on hobby/culture)
4. Design Philosophy (creator intentions)
5. Setting and Themes (if applicable)
6. Reception and Legacy (reviews, awards, lasting influence)
7. Related Games (Datacore query)
8. Publisher Context (Datacore query)
9. Designer Context (Datacore query)
10. Notes and References (bibliography)

[Continue for other types]

## Adding New Content

### Creating a New Game Entry

1. **Navigate to Folder**
   ```bash
   cd Games/
   ```

2. **Create File**
   ```bash
   # Naming: [Game Title] ([Year]).md
   touch "Blades in the Dark (2017).md"
   ```

3. **Use Template**
   - Copy [[Game Entry Template]]
   - Fill in all prompts (or use Templater if in Obsidian)
   - Replace `<% tp.* %>` syntax with actual values

4. **Write Content**
   - Research using [[Research Archive]] sources
   - Aim for 2,500+ words (exceeding minimum shows quality)
   - Include 10+ WikiLinks
   - Cite all sources

5. **Add Datacore Queries**
   ```datacore
   TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher"
   FROM "Games"
   WHERE contains(influenced-by, this.file.link) OR contains(influence-on, this.file.link)
   SORT year-published ASC
   ```

6. **Update Relationships**
   - If game influenced by [[Apocalypse World]], add this game to AW's influence-on list
   - Update designer's notable-works
   - Update publisher's key-releases

### Validation Before Committing

**Run All Validators**:
```bash
python Scripts/link_validator.py --report link-check.md
python Scripts/schema_validator.py --report schema-check.md
python Scripts/reciprocal_link_checker.py --report reciprocal-check.md
```

**Review Reports**:
- Fix all errors (❌)
- Address warnings (⚠️) if possible
- Aim for 90%+ property completeness

**Test Queries**:
- Open entry in Obsidian
- Verify all Datacore queries display results
- Check WikiLinks resolve (no broken links)

## Committing Changes

### Commit Message Format

Use conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**:
- `feat`: New entry (game, publisher, designer)
- `fix`: Correction to existing content
- `docs`: Documentation changes
- `style`: Formatting, typo fixes
- `refactor`: Restructuring without content change
- `test`: Adding validation tests
- `chore`: Maintenance tasks

**Examples**:
```bash
git commit -m "feat(games): Add Blades in the Dark (2017) entry

- 3,200 word comprehensive entry
- Covers FitD system creation
- 12 WikiLinks to related content
- All queries tested and functional"
```

```bash
git commit -m "fix(publishers): Correct TSR founding date to 1973

- Was incorrectly listed as 1974
- Updated based on Jon Peterson's 'Game Wizards'
- Added citation to Research Archive"
```

### Push and Create PR

```bash
git push origin feature/new-game-shadowrun
```

Then create Pull Request on GitHub with:
- Descriptive title
- Summary of changes
- Validation results (attach reports)
- Screenshots (if visual changes)

## Review Process

1. **Automated Checks**: GitHub Actions runs validators
2. **Peer Review**: Maintainer reviews content quality
3. **Revisions**: Address any requested changes
4. **Approval**: Once approved, merged to main branch

## Licensing of Contributions

By submitting a pull request you agree that:

- Content contributions (Markdown notes, templates, views, documentation, CSS) are licensed under
  [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) (see `LICENSE`).
- Code contributions (anything under `Scripts/`) are licensed under the MIT licence
  (see `Scripts/LICENSE`).
- You have the right to license the material you contribute. Do not paste in copyrighted rules
  text, and quote sources only briefly with attribution.

### A note on provenance

Much of this vault was AI-drafted in October 2025 and is still being verified. When you touch an
entry, prefer replacing unsupported claims with sourced ones over adding more unsourced prose.
Never invent quotations; if you cannot cite where a quote comes from, paraphrase and attribute
the idea instead.

## Code of Conduct

- **Be Respectful**: Treat all contributors with respect
- **Assume Good Intent**: Mistakes happen; help fix them
- **Cite Sources**: Respect intellectual property
- **No Plagiarism**: Write in own words, cite appropriately
- **Factual Accuracy**: Double-check historical claims

## Questions?

- Open an issue labeled `question`
- Check [[README]] and [[ADVANCED-FEATURES]]
- Review existing entries for examples

---

Thank you for helping build the definitive TTRPG history resource!
