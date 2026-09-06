# Changelog

All notable changes to the TTRPG History Vault are documented in this file.
The format loosely follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Dates are the real Git commit dates of this repository
(`https://github.com/BippleDops/TTRPG-History-Vault`).

---

## 2026-09-06 — Repair release

A clean-up pass driven by an external review of the public repository. No new
history content was written; the goal was to make the vault open correctly,
make the tooling honest, and label the content's provenance.

### Added
- `LICENSE` (Creative Commons Attribution-ShareAlike 4.0) for vault content and
  `Scripts/LICENSE` (MIT) for the Python tooling; licensing stated in `README.md`
  and `CONTRIBUTING.md`.
- A provenance banner at the top of `README.md`: the vault was AI-drafted in
  October 2025 and is under verification.
- `aliases:` frontmatter on every `Title (Year).md` entry (year-less title, plus
  the colon form for titles whose `:` had been replaced by ` - `), so prose
  links such as `[[Blades in the Dark]]` resolve to
  `Games/Blades in the Dark (2017).md`.
- Ten short, sourced stub entries for heavily linked hubs that did not exist
  (for example `Games/Chainmail (1971).md`), tagged `stub`.
- `Scripts/link_validator.py --max-broken N` so the link check can act as a CI
  gate with a ratcheting budget.
- `requirements.txt` for the analytics and export scripts.
- `Documentation/_meta/` holding the October 2025 generation logs, with a README
  explaining what they are.
- A `> [!warning] Synthesis` callout on every `Research Archive/` note.

### Changed
- All embedded queries are now in ```` ```dataview ```` fences (they were
  Dataview DQL labelled `datacore`, which never rendered); Dataview is enabled
  in `.obsidian/community-plugins.json`.
- `.github/workflows/validate.yml`: actions pinned to current major versions,
  the link check is blocking (with a documented broken-link budget), the schema
  and reciprocal-link checks report as artifacts without blocking, the quality
  step can actually fail, and the PR comment reflects the real result.
- Duplicate entries merged: *Advanced Dungeons & Dragons (1977)*,
  *Dungeons & Dragons Third Edition (2000)*, and *Curse of Strahd* each have a
  single canonical note; the removed names survive as aliases.
- `Research Archive/` notes are typed `synthesis` (not `web-archive`), list
  `sources:` instead of a fake `source-url`, and no longer present invented
  quotations as real ones.
- Factual corrections: *Dungeons & Dragons (1974)* credits Dave Arneson and no
  longer claims "tens of thousands" of early sales; *Traveller (1977)* notes the
  1998–2008 publication gap and that the Third Imperium arrived in later
  supplements; *Call of Cthulhu (1981)* no longer attributes Delta Green to
  Chaosium; *Gary Gygax* lists the Origins/Adventure Gaming Hall of Fame once;
  *Shadowrun (1989)* has a valid YAML designer list.
- `README.md` and `MASTER-INDEX.md` are the two entry documents;
  `START-HERE.md`, `GETTING-STARTED.md`, and the root
  `TTRPG-History-Dashboard.md` were folded into them and removed
  (`Views/TTRPG-History-Dashboard.md` remains the in-vault dashboard).
- Shell scripts locate the vault relative to themselves instead of a hard-coded
  personal path.

### Fixed
- `.gitattributes` no longer marks every file `export-ignore` (GitHub's
  "Download ZIP" was empty) and no longer applies `merge=union` to prose.
- Vendored plugin bundles (`.obsidian/plugins/*/main.js`, `styles.css`,
  ~10 MB) are untracked and ignored; Obsidian re-downloads them.

### Removed
- Root-level AI session artifacts (moved to `Documentation/_meta/`).
- The recommendation to use "thetimetube.com" for Wikipedia copies.

---

## 2025-10-29 — Expansion import

Commit `0f389d6` "Autonomous expansion: Added 175+ entries (Games, Designers,
Mechanics, Publishers, VTT, Accessibility, Visualizations) - 388K words".

- Added roughly 175 AI-drafted entries across `Games/`, `Designers/`,
  `Mechanics/`, `Publishers/`, `VTT Platforms/`, `Educational/Accessibility/`
  and `Visualizations/`.
- Added the root session summaries now kept in `Documentation/_meta/`.

## 2025-10-28 — Initial import

Commit `09e27e7` "Initial commit: TTRPG History Vault complete structure with
games, designers, publishers, mechanics, and comprehensive documentation".

- First public version of the vault: folder structure, templates, Bases views,
  MOCs, documentation, the `Scripts/` tooling, and the initial AI-drafted
  entries.

---

## Pre-repository generation notes (dates unverifiable)

Earlier versions of this changelog described a "1.0.0" release dated
2024-12-01 and a "2.0.0" release dated 2024-12-15, and `README.md` described a
"Version 1.0 (October 2024)" and "Version 4.0 (October 2025)". Those entries
were written by the generation sessions themselves; they predate the repository
and cannot be checked against any commit. They are summarised here only so the
information is not lost:

- **"1.0.0"** — vault structure with seven primary folders; Bases views
  (`All-Games`, `Publishers`, `Designers`, `Innovations`, `By-Decade`,
  `Historical-Events`); Templater templates; five era MOCs; dashboard,
  `Property-Schema.md`, `VAULT-NAVIGATION.md`, `README.md`; about 97 initial
  entries.
- **"2.0.0"** — eight additional entry templates (Actual Play, Supplement,
  Retroclone, VTT Platform, Digital Adaptation, Convention, Award,
  Controversy); the `Documentation/` guides; `schema_validator.py`,
  `link_validator.py`, `reciprocal_link_checker.py`; `QUALITY-STANDARDS.md`,
  `CONTRIBUTING.md`; CSS snippets; `Views/Query-Library.md`; GitHub templates
  and the first `validate.yml`.
- **"3.0" / "4.0"** — the content expansion that became the 2025-10-29 commit.

---

## Contributing to this changelog

Add entries under a dated heading (`YYYY-MM-DD — short title`) using the
Keep-a-Changelog categories *Added / Changed / Fixed / Removed*. Reference the
commit or pull request where useful. Content additions do not need individual
entries; batches of entries or schema changes do.
