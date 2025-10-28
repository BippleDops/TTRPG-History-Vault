# Changelog

All notable changes to the TTRPG History Vault will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- GitHub Actions CI/CD validation workflow
- Issue templates for new entries and content expansion
- Pull request template with validation checklist
- .gitattributes for consistent line endings

---

## [2.0.0] - 2024-12-15

### Major Enhancements

This release significantly expands the vault with advanced features, new content types, automation scripts, and comprehensive documentation.

### Added

**New Content Types** (8 templates):
- Actual Play template for documenting streaming shows and podcasts
- Supplement template for adventures, sourcebooks, and expansions
- Retroclone template for OSR and emulation games
- VTT Platform template for Roll20, Foundry, etc.
- Digital Adaptation template for video game adaptations
- Convention template for Gen Con, Origins, regional cons
- Award template for Origins Awards, ENnies, etc.
- Controversy template for industry disputes and scandals

**Documentation** (4 comprehensive guides):
- ADVANCED-FEATURES.md - Deep dive into vault capabilities
- QUERY-COOKBOOK.md - 50+ copy-paste Datacore query examples
- PLUGIN-INTEGRATION-GUIDE.md - Plugin configuration instructions
- WORKFLOW-GUIDE.md - Step-by-step workflows for common tasks

**Automation Scripts** (3 Python validators):
- schema_validator.py - Validates entry property schemas, calculates completeness
- link_validator.py - Checks WikiLinks, suggests fixes for broken links
- reciprocal_link_checker.py - Validates bidirectional relationships

**Quality Documentation**:
- QUALITY-STANDARDS.md - 3-tier quality system (Minimal/Standard/Exemplary)
- CONTRIBUTING.md - Contributor guidelines and Git workflow
- TESTING-GUIDE.md - Pre-commit testing procedures
- VALIDATION-CHECKLIST.md - Quick reference validation checklist

**CSS Enhancements** (5 snippets):
- entry-type-colors.css - Color-coded type properties
- era-themes.css - Era-specific MOC themes
- property-display-formatting.css - Enhanced property visualization
- mobile-optimized.css - Responsive design for mobile devices
- print-ready.css - PDF export optimization

**Query Library**:
- Query-Library.md with 30+ advanced Datacore patterns
- Temporal analysis queries
- Relationship mapping queries
- Statistical analysis queries
- Cross-type queries
- Validation queries

**Git Infrastructure**:
- .github/PULL_REQUEST_TEMPLATE.md
- .github/ISSUE_TEMPLATE/new-entry.md
- .github/ISSUE_TEMPLATE/content-expansion.md
- .github/workflows/validate.yml (CI/CD pipeline)
- CHANGELOG.md (this file)
- .gitattributes

### Changed

- Updated README.md with references to new features
- Expanded template examples in all MOC files
- Enhanced property schema documentation
- Improved navigation structure in dashboard

### Technical

- All Python scripts use Python 3.7+
- Scripts require PyYAML dependency
- GitHub Actions workflow validates all PRs automatically
- CSS snippets compatible with Obsidian v1.9.10+

---

## [1.0.0] - 2024-12-01

### Initial Release

**Core Infrastructure**:
- Vault structure with 7 primary folders
- Obsidian Bases integration for database views
- Datacore query system (migrated from Dataview)
- Templater-powered dynamic templates

**Content Types** (5 original):
- Game entries with comprehensive property schema
- Publisher profiles
- Designer biographies
- Mechanic documentation
- Historical event timeline

**Initial Content** (97 entries):
- 20 landmark game entries
- 15 publisher profiles
- 16 designer biographies
- 10 mechanic documentation entries
- 13 historical event entries
- 18 research archive entries

**Core Files**:
- TTRPG-History-Dashboard.md - Central navigation hub
- Property-Schema.md - Complete property reference
- VAULT-NAVIGATION.md - Comprehensive browse interface
- README.md - Complete vault documentation

**Era MOCs** (5 files):
- Early Era MOC (1974-1985)
- Golden Age MOC (1985-2000)
- d20 Era MOC (2000-2008)
- OSR Revival MOC (2008-2015)
- Modern Era MOC (2015-Present)

**Templates** (5 original):
- Game Entry Template.md
- Publisher Template.md
- Designer Template.md
- Mechanics Documentation Template.md
- Historical Event Template.md
- Web Archive Template.md

**Database Views**:
- All-Games.base
- Publishers.base
- Designers.base
- Innovations.base (mechanics timeline)
- By-Decade.base
- Historical-Events.base

**Statistics**:
- 266,000+ total words
- 250+ embedded Datacore queries
- 600+ bidirectional WikiLinks
- <2 second vault load time

---

## Version Numbering

**Major version (X.0.0)**: Breaking changes to property schemas, vault structure, or required plugins

**Minor version (0.X.0)**: New features, content types, or significant enhancements

**Patch version (0.0.X)**: Bug fixes, small improvements, content additions

---

## Contributing to Changelog

When making changes, add entries under `[Unreleased]` section using these categories:

### Categories

- **Added** - New features, templates, content types
- **Changed** - Changes to existing functionality
- **Deprecated** - Features to be removed in future versions
- **Removed** - Removed features
- **Fixed** - Bug fixes
- **Security** - Security fixes

### Entry Format

```markdown
- Brief description of change (closes #123)
```

### Example

```markdown
## [Unreleased]

### Added
- New mechanic documentation template for advanced systems
- Support for campaign setting entries

### Changed
- Improved schema_validator.py performance for large vaults

### Fixed
- Reciprocal link checker now handles list properties correctly (closes #45)
```

---

## Release Process

1. **Prepare Release**
   - Move `[Unreleased]` items to new version section
   - Add release date
   - Update version number in README

2. **Tag Release**
   ```bash
   git tag -a v2.0.0 -m "Release version 2.0.0"
   git push origin v2.0.0
   ```

3. **GitHub Release**
   - Create GitHub release from tag
   - Copy changelog section to release notes
   - Attach any release artifacts

---

## Links

- [Keep a Changelog](https://keepachangelog.com/)
- [Semantic Versioning](https://semver.org/)
- [GitHub Releases](https://github.com/your-username/ttrpg-history-vault/releases)

---

*This changelog helps users and contributors understand what has changed between versions and plan upgrades accordingly.*
