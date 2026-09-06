# TTRPG History Tracking Vault

> [!warning] AI-drafted content under verification
> This vault was drafted with the help of AI tools in October 2025 and is still being verified.
> Entries can contain errors, anachronisms, and unsupported claims. Check facts against the
> cited sources (and the primary literature, e.g. Peterson's *Playing at the World*,
> Appelcline's *Designers & Dragons*) before reusing anything here. The `Research Archive/`
> notes are AI syntheses, not archived web pages, and their "quotes" are illustrative rather
> than real quotations. Corrections are welcome — see [Contributing](#contributing).

An [Obsidian](https://obsidian.md) vault documenting 50+ years of tabletop roleplaying game
history (1974–present): games, designers, publishers, mechanics, eras, controversies, campaign
settings, supplements, retroclones, virtual tabletops and actual-play shows, plus Python scripts
for analytics, validation and export.

**Current contents** (counted from the files, September 2026):

| Folder | Entries | Folder | Entries |
|--------|--------:|--------|--------:|
| `Games/` | 128 | `Retroclones/` | 17 |
| `Designers/` | 94 | `Actual Play/` | 15 |
| `Mechanics/` | 74 | `Controversies/` | 11 |
| `Publishers/` | 46 | `Supplements/` | 11 |
| `Historical Context/` | 24 (8 eras, 16 events) | `Settings/` | 10 |
| `VTT Platforms/` | 19 | | |

449 content entries in total (10 of them short, sourced stubs tagged `stub`), about 1.08 million
words across all notes, plus 19 `Research Archive/` syntheses, a 6-week curriculum and 8
accessibility notes in `Educational/`, and 18 Python scripts in `Scripts/`.

---

## Table of Contents

- [Overview](#overview)
- [Vault Structure](#vault-structure)
- [Opening the Vault in Obsidian](#opening-the-vault-in-obsidian)
- [Finding Your Way Around](#finding-your-way-around)
- [Who Is This For?](#who-is-this-for)
- [Adding and Editing Entries](#adding-and-editing-entries)
- [Templates](#templates)
- [Database Views (Bases)](#database-views-bases)
- [Scripts: Validation, Analytics and Export](#scripts-validation-analytics-and-export)
- [Plugins](#plugins)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Documentation Map](#documentation-map)
- [Backup and Version Control](#backup-and-version-control)
- [Support and Resources](#support-and-resources)
- [License and Attribution](#license-and-attribution)

---

## Overview

Every note carries structured frontmatter (see `Views/Property-Schema.md`) so the vault works as
a database as well as a wiki:

- **Bases views** (`Views/*.base`) — Obsidian's native database views for filtering, sorting and
  grouping entries.
- **Dataview queries** — 800+ embedded ```` ```dataview ```` blocks show related games, publisher
  catalogues, designer portfolios and era statistics.
- **Templater templates** — guided creation of new entries with the right properties.
- **WikiLinks and aliases** — entries are named `Title (Year).md` and declare a year-less
  `aliases:` entry, so `[[Blades in the Dark]]` and `[[Blades in the Dark (2017)]]` both resolve.
- **Maps of Content** — era MOCs in `Views/` and the indexes at the vault root.

---

## Vault Structure

```
TTRPG-History-Vault/
├── Games/                 # Individual TTRPG titles (`Title (Year).md`)
├── Designers/             # Game designers and creators
├── Publishers/            # Publishing companies and imprints
├── Mechanics/             # Game systems and mechanical innovations
├── Historical Context/    # Eras and pivotal events
├── Controversies/         # Industry disputes and cultural moments
├── Supplements/           # Adventures, sourcebooks, expansions
├── Settings/              # Campaign settings
├── Retroclones/           # OSR and emulation games
├── VTT Platforms/         # Virtual tabletops and digital tools
├── Actual Play/           # Streaming shows and podcasts
├── Research Archive/      # AI-synthesised topic overviews (see banner above)
├── Educational/           # Curriculum and accessibility notes
├── Views/                 # Bases files, MOCs, dashboard, Property-Schema, Query-Library
├── Visualizations/        # Timeline and network notes
├── Templates/             # Templater templates for every entry type
├── Documentation/         # Guides (plugins, queries, workflow, testing, theme)
│   └── _meta/             # October 2025 generation logs — provenance only
├── Scripts/               # Python validation, analytics and export tools
├── Attachments/           # Images and generated diagrams
└── .github/               # CI workflow, issue and PR templates
```

Root-level navigation notes: `MASTER-INDEX.md` (A–Z, by attribute), `Games-by-Year.md`,
`Games-by-Designer.md`, `Games-by-System.md`. Policy documents: `CONTRIBUTING.md`,
`QUALITY-STANDARDS.md`, `CHANGELOG.md`, `LICENSE`.

---

## Opening the Vault in Obsidian

1. **Get the files**: `git clone https://github.com/BippleDops/TTRPG-History-Vault.git` (or
   download the ZIP from GitHub).
2. **Open as a vault**: in Obsidian choose *Open folder as vault* and select the
   `TTRPG-History-Vault` folder. Use Obsidian 1.9.10 or newer so the Bases core plugin is available.
3. **Enable core plugins** (Settings → Core plugins): Bases, Properties, Backlinks, Graph view,
   Outline, Search, Quick switcher.
4. **Install community plugins** (Settings → Community plugins → turn off Restricted mode → Browse):
   - **Dataview** — required; every embedded query is Dataview DQL.
   - **Templater** — optional, needed only to create entries from the templates.
   - **Excalidraw** — optional, for the hand-drawn diagrams.

   The plugin *settings* are already committed in `.obsidian/plugins/*/data.json`; only the plugin
   code needs downloading.
5. **Configure Dataview**: Settings → Dataview → *Enable codeblock dataviews* ON,
   *Enable inline dataviews* ON.
6. **Configure Templater** (if installed): Settings → Templater → *Template folder location* =
   `Templates`, *Trigger Templater on new file creation* ON, and add folder templates
   (`Games` → `Templates/Game Entry Template.md`, `Publishers` → `Templates/Publisher Template.md`,
   `Designers` → `Templates/Designer Template.md`,
   `Mechanics` → `Templates/Mechanics Documentation Template.md`,
   `Historical Context` → `Templates/Historical Event Template.md`).

### First steps

1. Open `Views/TTRPG-History-Dashboard.md` — era navigation, database views, highlights.
2. Open `MASTER-INDEX.md` — every entry type as a sortable table, plus browse-by-attribute views.
3. Open `Views/All-Games.base` to see the Bases interface.
4. Read `Games/Dungeons & Dragons (1974).md` for a representative entry.
5. Open the Graph view (Ctrl/Cmd + G) to see how entries connect.

---

## Finding Your Way Around

- **Quick Switcher** (Ctrl/Cmd + O): type any game, designer or publisher name.
- **Search** (Ctrl/Cmd + Shift + F): full-text search across all entries.
- **Indexes**: `MASTER-INDEX.md` (A–Z, by significance, status, complexity, genre, movement),
  `Games-by-Year.md`, `Games-by-Designer.md`, `Games-by-System.md`.
- **Eras**: `Historical Context/` and the era MOCs in `Views/` (Early Era, Golden Age, d20 Era,
  OSR Revival, Modern Era).
- **Follow links**: every entry links to related games, people and companies; the Backlinks pane
  shows what links here.
- **Bases views**: `.base` files in `Views/` filter, sort and group by property.

### Entry structure

Every entry has frontmatter (metadata) followed by prose sections and one or more embedded
queries:

```yaml
---
title: Dungeons & Dragons
type: game
year-published: 1974
designer:
  - "[[Gary Gygax]]"
  - "[[Dave Arneson]]"
publisher: "[[TSR]]"
aliases:
  - Dungeons & Dragons
---
```

Typical sections: overview and history; mechanics and design analysis; cultural impact; legacy and
influence; notes and references; Dataview queries showing related entries.

---

## Who Is This For?

- **Researchers** — export the vault as JSON (`Scripts/export/json_api_exporter.py`), run the
  analytics scripts for CSV datasets and network data, and generate bibliographies
  (`Scripts/bibliography_generator.py --style chicago|mla|apa`). Verify claims against primary
  sources first (see the banner).
- **Educators** — a 6-week syllabus lives in `Educational/Curricula/History-of-RPGs-101/`;
  `Scripts/export/anki_flashcards.py` builds study decks and `hugo_exporter.py` builds a static
  site.
- **Game designers** — `Mechanics/` catalogues mechanical innovations, `Designers/` profiles
  design philosophies, and `Scripts/analytics/system_family_tree.py` draws system lineages.
- **Players** — browse `Games/`, follow the influence links, read `Actual Play/` for the shows
  that brought the hobby to a wider audience.

---

## Adding and Editing Entries

### Your first entry (with Templater)

1. Right-click the target folder (for example `Games`) → *New note* and name it
   `Title (Year).md`.
2. If folder templates are configured the Game Entry Template applies automatically; otherwise
   Ctrl/Cmd + P → *Templater: Insert Template* → choose the template.
3. Answer the prompts (title, publisher, year, system, genre, ratings). Suggesters offer the
   schema-valid values.
4. Write the body — at least the sections and word count in `QUALITY-STANDARDS.md` — and link to
   publishers, designers, mechanics and related games with `[[WikiLinks]]`.
5. Add `aliases:` with the year-less title so prose links resolve.
6. Check the entry appears in `Views/All-Games.base`, then run the validators (below).

### Manual creation

Copy the frontmatter of a similar entry, fill in every required property from
`Views/Property-Schema.md`, write the sections, and link to at least two related notes.

### Linking

Link games to publishers and designers, publishers to their games, designers to their works,
mechanics to the games that use them, and events to the games and companies they affected. Use
lists for multi-valued links:

```yaml
influenced-by:
  - "[[Game One]]"
  - "[[Game Two]]"
```

### Querying

Use ```` ```dataview ```` blocks anywhere:

```dataview
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher"
FROM "Games"
WHERE historical-significance >= 4
SORT year-published ASC
```

`Views/Query-Library.md` and `Documentation/QUERY-COOKBOOK.md` collect ready-made patterns.

---

## Templates

All templates in `Templates/` use Templater prompts, suggesters for categorical values, cursor
positioning and embedded queries. One template exists per entry type: Game Entry, Publisher,
Designer, Mechanics Documentation, Historical Event, Web Archive, Actual Play, Supplement,
Retroclone, VTT Platform, Digital Adaptation, Convention, Award and Controversy.

---

## Database Views (Bases)

| View | Purpose | File |
|------|---------|------|
| All Games Database | Complete game catalogue with filtering | `Views/All-Games.base` |
| Publishers Analysis | Publishing companies by era and significance | `Views/Publishers.base` |
| Design Innovations Timeline | Mechanical innovations chronologically | `Views/Innovations.base` |
| Games by Decade | Historical progression view | `Views/By-Decade.base` |
| All Designers | Game creators and contributors | `Views/Designers.base` |
| Historical Events | Major moments in TTRPG history | `Views/Historical-Events.base` |

Open a `.base` file, filter with the column headers, sort by clicking a column, group with
*Group by*, and click a row to open the source note. Create your own by adding a `.base` file that
points at a source folder and maps columns to properties.

---

## Scripts: Validation, Analytics and Export

All scripts are Python 3 and live in `Scripts/` (MIT licence). Install the dependencies once:

```bash
python3 -m pip install -r requirements.txt
```

### Validation (run before committing)

```bash
python3 Scripts/link_validator.py --report link-report.md      # broken [[WikiLinks]]
python3 Scripts/schema_validator.py                             # required properties per type
python3 Scripts/reciprocal_link_checker.py                      # bidirectional relationships
python3 Scripts/quality_enhancer.py                             # word counts, missing sections
```

`link_validator.py` exits non-zero when broken links exceed `--max-broken N`; the CI workflow in
`.github/workflows/validate.yml` runs it with a budget that is lowered as links are fixed.

### Analytics

```bash
./Scripts/run_all_analytics.sh          # everything below, output in Attachments/Diagrams/analytics/
python3 Scripts/analytics/publication_trends.py
python3 Scripts/analytics/influence_network.py
python3 Scripts/analytics/innovation_timeline.py
python3 Scripts/analytics/coverage_gaps.py
python3 Scripts/analytics/system_family_tree.py
python3 Scripts/analytics/era_comparison.py
python3 Scripts/analytics/complexity_popularity.py
python3 Scripts/analytics/designer_matrix.py
```

### Export

```bash
./Scripts/run_all_exports.sh            # everything below, output in Exports/
python3 Scripts/export/hugo_exporter.py       # static website (Hugo)
python3 Scripts/export/pdf_compiler.py        # PDF anthology (needs Pandoc + LaTeX)
python3 Scripts/export/epub_generator.py      # EPUB (needs Pandoc)
python3 Scripts/export/json_api_exporter.py   # JSON API
python3 Scripts/export/anki_flashcards.py     # Anki deck
python3 Scripts/bibliography_generator.py --style chicago   # or mla / apa
```

---

## Plugins

**Core** (built in): Bases, Properties, Templates, Backlinks, Graph view, Outline, Search, Quick
switcher; Daily notes optional.

**Community — required**: Dataview. **Optional**: Templater (entry creation), Excalidraw
(diagrams), Advanced Tables, Tracker, QuickAdd, DB Folder, Obsidian Web Clipper, Calendar, Kanban.

Settings for Dataview, Templater and Excalidraw are versioned in `.obsidian/plugins/*/data.json`;
the plugin bundles themselves are not committed. See `Documentation/PLUGIN-INTEGRATION-GUIDE.md`
for details and `Documentation/THEME-GUIDE.md` for the CSS snippets.

---

## Troubleshooting

- **Queries show as raw code blocks** — install and enable the Dataview community plugin, then
  reload the vault. Every query is Dataview DQL; the Datacore plugin does not render them.
- **Python scripts fail on import** — `python3 -m pip install -r requirements.txt`.
- **Broken links reported** — expected while the vault is being repaired; run
  `python3 Scripts/link_validator.py --report link-report.md` and fix or alias the targets
  listed under *Most Common Broken Targets*. Do not create empty notes to silence the checker.
- **Analytics output folder missing** — the scripts create `Attachments/Diagrams/analytics/` and
  `Exports/` themselves; check write permissions.
- **Templates do not apply** — set the Templater template folder to `Templates` and enable
  *Trigger Templater on new file creation*.

---

## Contributing

Corrections are the most valuable contribution right now: the content is AI-drafted and under
verification. Read `CONTRIBUTING.md` (workflow, licensing of contributions, provenance rules) and
`QUALITY-STANDARDS.md` (tiers, required sections). In short:

- Cite sources for factual claims and never present paraphrase as quotation.
- Fill every required property (`Views/Property-Schema.md`) and add `aliases:`.
- Link to at least two related entries and update the reciprocal links.
- Run the validators before opening a pull request; CI runs them too.

---

## Documentation Map

| Document | Purpose |
|----------|---------|
| `README.md` (this file) | Overview, setup, orientation |
| `MASTER-INDEX.md` | Navigation: A–Z tables and browse-by-attribute views |
| `Games-by-Year.md`, `Games-by-Designer.md`, `Games-by-System.md` | Specialised indexes |
| `Views/TTRPG-History-Dashboard.md` | In-vault dashboard with era navigation and highlights |
| `CONTRIBUTING.md`, `QUALITY-STANDARDS.md` | How to contribute and what "done" means |
| `CHANGELOG.md` | Real, dated history of the repository |
| `Views/Property-Schema.md` | Every property, per entry type |
| `Views/Query-Library.md`, `Documentation/QUERY-COOKBOOK.md` | Dataview query patterns |
| `Documentation/PLUGIN-INTEGRATION-GUIDE.md` | Plugin setup |
| `Documentation/WORKFLOW-GUIDE.md`, `Documentation/TESTING-GUIDE.md`, `Documentation/VALIDATION-CHECKLIST.md` | Content workflow and checks |
| `Documentation/ADVANCED-FEATURES.md`, `Documentation/CUSTOMIZATION-GUIDE.md`, `Documentation/THEME-GUIDE.md`, `Documentation/VAULT-NAVIGATION.md` | Power-user guides |
| `Documentation/_meta/` | Logs written by the October 2025 generation sessions — provenance only, not documentation |

---

## Backup and Version Control

The repository is the backup. Commit individual entries with descriptive messages
(`git add "Games/New Game (Year).md" && git commit -m "Add Games/New Game (Year)"`), push regularly,
and keep `.obsidian/workspace*.json` out of Git (already in `.gitignore`). Obsidian Sync or any
cloud folder works alongside Git for personal copies.

---

## Support and Resources

**Obsidian**: [Obsidian Help](https://help.obsidian.md/) ·
[Dataview](https://blacksmithgu.github.io/obsidian-dataview/) ·
[Templater](https://silentvoid13.github.io/Templater/)

**TTRPG history (primary and secondary literature)**: Jon Peterson, *Playing at the World* (2012)
and *Game Wizards* (2021); Shannon Appelcline, *Designers & Dragons* (4 vols., 2014);
RPG.net; BoardGameGeek RPG section; DriveThruRPG catalogue; The Alexandrian; Wikipedia TTRPG
entries (as a starting point, not a citation).

Questions and corrections: open an issue or pull request on GitHub.

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
