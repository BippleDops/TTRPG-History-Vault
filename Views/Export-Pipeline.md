---
type: moc
title: Export Pipeline
category: infrastructure
status: active
last-updated: 2025-01-XX
tags:
  - export
  - distribution
  - publishing
  - v3.0
---

# Export Pipeline

**Purpose**: Multi-format distribution system for vault content

The Export Pipeline transforms Obsidian vault content into various formats for wide distribution, enabling the TTRPG History Vault to reach diverse audiences across platforms.

---

## Export Formats

### 1. Hugo Static Site

**Script**: `Scripts/export/hugo_exporter.py`

**What It Does**:
- Converts vault to Hugo-compatible static site
- Transforms wikilinks to HTML links
- Organizes content by type (games, designers, etc.)
- Copies images and diagrams to static assets
- Generates Hugo configuration

**Usage**:
```bash
python Scripts/export/hugo_exporter.py
cd Exports/hugo-site
git clone https://github.com/alex-shpak/hugo-book themes/hugo-book
hugo
hugo server  # Preview locally
```

**Output**:
- `Exports/hugo-site/` - Complete Hugo site structure
- `Exports/hugo-site/public/` - Built static site (after running `hugo`)

**Deployment**:
- Netlify
- GitHub Pages
- Vercel
- Any static hosting

**Use Cases**:
- Public-facing website
- Searchable online reference
- SEO-friendly content
- Easy sharing via URL

---

### 2. PDF Anthology

**Script**: `Scripts/export/pdf_compiler.py`

**What It Does**:
- Compiles vault entries into professional PDF
- Includes table of contents
- Page numbering and cross-references
- Section organization
- Academic formatting

**Usage**:
```bash
# Full anthology
python Scripts/export/pdf_compiler.py

# Single section
python Scripts/export/pdf_compiler.py --section games --output Exports/Games-Only.pdf
```

**Requirements**:
- Pandoc: `brew install pandoc` (macOS) or https://pandoc.org/installing.html
- LaTeX: Install TeX Live, MacTeX, or MiKTeX

**Output**:
- `Exports/TTRPG-History-Vault-Complete.pdf` - Full anthology (500+ pages)
- Section-specific PDFs when using `--section` flag

**Use Cases**:
- Offline reading
- Print-on-demand publishing
- Academic citations
- Archival preservation

---

### 3. EPUB Ebook

**Script**: `Scripts/export/epub_generator.py`

**What It Does**:
- Generates EPUB 3.0 ebook format
- Readable on e-readers (Kindle, Kobo, Nook)
- Reflowable text
- Table of contents navigation
- Embedded metadata

**Usage**:
```bash
# Full ebook
python Scripts/export/epub_generator.py

# Section-specific ebook
python Scripts/export/epub_generator.py --section games --output Exports/Games.epub
```

**Requirements**:
- Pandoc: Same as PDF export

**Output**:
- `Exports/TTRPG-History-Vault-Complete.epub` - Full ebook
- Section EPUBs with `--section` flag

**Compatible Devices**:
- Kindle (convert with Calibre)
- Apple Books
- Google Play Books
- Kobo
- Nook
- Any EPUB reader app

**Use Cases**:
- Mobile reading
- E-reader distribution
- Library lending
- Accessible reading formats

---

### 4. JSON API

**Script**: `Scripts/export/json_api_exporter.py`

**What It Does**:
- Exports vault as structured JSON
- RESTful API structure
- Individual entry endpoints
- Search index
- Programmatic access

**Usage**:
```bash
python Scripts/export/json_api_exporter.py

# Serve locally for testing
cd Exports/json-api
python -m http.server 8000
```

**Output Structure**:
```
Exports/json-api/
├── index.json                    # Master index
├── games.json                    # All games collection
├── designers.json                # All designers
├── API-DOCUMENTATION.md          # Usage docs
└── api/v1/
    ├── games/
    │   ├── dungeons-dragons-fifth-edition-2014.json
    │   └── ... (one file per game)
    ├── designers/
    └── ... (other types)
```

**Endpoints**:
- `GET /index.json` - Vault index and stats
- `GET /games.json` - All game entries
- `GET /api/v1/games/{id}.json` - Single game

**Use Cases**:
- Web applications
- Mobile apps
- Research tools
- Data analysis
- Integration with other systems

---

### 5. Anki Flashcards

**Script**: `Scripts/export/anki_flashcards.py`

**What It Does**:
- Generates flashcards for studying TTRPG history
- Multiple card types (games, designers, timeline)
- Tagged for organization
- Anki-importable format

**Usage**:
```bash
python Scripts/export/anki_flashcards.py
```

**Card Types Generated**:
1. **Game Cards**:
   - "When was [Game] published?" → Year
   - "Who designed [Game]?" → Designer(s)
   - "Who published [Game]?" → Publisher

2. **Designer Cards**:
   - "What are notable works by [Designer]?" → Games list
   - "Who designed [Game]?" → Designer

3. **Timeline Cards**:
   - "Name 3 TTRPGs from the 1980s" → List
   - "What era was [Game] from?" → Era

4. **Mechanic Cards**:
   - "What is [Mechanic]?" → Definition
   - "Where was [Mechanic] introduced?" → Game

**Output**:
- `Exports/ttrpg-history-flashcards.txt` - Anki import file

**Import to Anki**:
1. Open Anki
2. File > Import
3. Select `ttrpg-history-flashcards.txt`
4. Set field mapping: Front, Back, Tags
5. Import

**Use Cases**:
- Study TTRPG history
- Academic exam prep
- Trivia practice
- Educational tools

---

## Running All Exports

To generate all export formats at once:

```bash
#!/bin/bash
cd "/Users/jonsussmanstudio/Desktop/Code Demonstrator For Karl/TTRPG-History-Vault"

echo "Exporting to Hugo..."
python Scripts/export/hugo_exporter.py

echo "Generating PDF..."
python Scripts/export/pdf_compiler.py

echo "Generating EPUB..."
python Scripts/export/epub_generator.py

echo "Exporting JSON API..."
python Scripts/export/json_api_exporter.py

echo "Generating Anki flashcards..."
python Scripts/export/anki_flashcards.py

echo "All exports complete!"
```

---

## Export Workflow

### For Public Release

1. **Update Content**: Ensure vault is current
2. **Run Validation**: `python Scripts/link_validator.py`
3. **Generate Analytics**: Run analytics scripts for latest insights
4. **Export All Formats**: Run export pipeline
5. **Test Outputs**: Verify each format
6. **Deploy**:
   - Hugo site → Netlify/GitHub Pages
   - PDF → Archive.org, print-on-demand
   - EPUB → Ebook platforms
   - JSON API → Static hosting
   - Anki → AnkiWeb shared decks

### For Academic Distribution

1. **PDF Anthology**: Full compilation with citations
2. **JSON API**: For researchers needing structured data
3. **Hugo Site**: Searchable online reference

### For Educational Use

1. **Anki Flashcards**: Study tool
2. **EPUB**: Portable reading
3. **Hugo Site**: Interactive learning

---

## Customization

### Hugo Site

Edit `Exports/hugo-site/config.yaml`:
```yaml
baseURL: 'https://your-domain.com/'
title: 'Your Custom Title'
theme: 'hugo-book'  # or other theme
```

Add custom CSS: `Exports/hugo-site/static/css/custom.css`

### PDF Styling

Modify Pandoc args in `pdf_compiler.py`:
```python
pandoc_args = [
    '--pdf-engine=xelatex',
    '-V', 'geometry:margin=0.75in',  # Adjust margins
    '-V', 'fontsize=12pt',           # Change font size
    '-V', 'mainfont=Times New Roman' # Change font
]
```

### JSON API

Customize data structure in `json_api_exporter.py`:
- Add/remove metadata fields
- Change URL structure
- Filter sensitive data

---

## Automation

### GitHub Actions

Auto-export on push:

```yaml
name: Export Vault
on:
  push:
    branches: [main]

jobs:
  export:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
      - name: Install dependencies
        run: |
          sudo apt-get install pandoc texlive-xetex
          pip install pyyaml
      - name: Run exports
        run: |
          python Scripts/export/hugo_exporter.py
          python Scripts/export/json_api_exporter.py
      - name: Deploy Hugo site
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./Exports/hugo-site/public
```

### Cron Job

Weekly auto-export:
```bash
# Add to crontab: crontab -e
0 2 * * 0 cd /path/to/vault && ./export_all.sh
```

---

## Distribution Channels

### Official Releases

- **GitHub Releases**: PDF, EPUB, JSON API as downloadable assets
- **Archive.org**: Permanent archival hosting
- **Zenodo**: Academic citation DOI

### Community Platforms

- **DriveThruRPG**: PDF marketplace (if commercial)
- **Itch.io**: Pay-what-you-want distribution
- **AnkiWeb**: Shared flashcard decks

### Academic Repositories

- **Open Science Framework (OSF)**
- **figshare**
- **Institutional repositories**

---

## Licensing

All exports include license metadata:
- **Default**: Creative Commons Attribution-ShareAlike 4.0 (CC BY-SA 4.0)
- **Commercial**: Modify scripts to add different license
- **Attribution**: Include in all exported formats

---

## Performance

### Export Times (approximate)

- **Hugo**: 30-60 seconds (100+ entries)
- **PDF**: 2-5 minutes (depends on LaTeX)
- **EPUB**: 1-3 minutes
- **JSON API**: 10-30 seconds
- **Anki**: 5-15 seconds

### Output Sizes (100 entries)

- **Hugo site**: ~50 MB (with images)
- **PDF**: ~10-20 MB
- **EPUB**: ~5-15 MB
- **JSON API**: ~5-10 MB
- **Anki**: <1 MB

---

## Troubleshooting

### Pandoc Not Found

**Error**: `ERROR: Pandoc not found!`

**Solution**:
```bash
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
# Download from https://pandoc.org/installing.html
```

### LaTeX Error in PDF Generation

**Error**: `! LaTeX Error: File not found`

**Solution**: Install complete LaTeX distribution
```bash
# macOS
brew install --cask mactex

# Ubuntu
sudo apt-get install texlive-full

# Windows
# Install MiKTeX from https://miktex.org/
```

### Hugo Theme Missing

**Error**: Theme not found

**Solution**:
```bash
cd Exports/hugo-site
git clone https://github.com/alex-shpak/hugo-book themes/hugo-book
```

---

## Future Enhancements (v3.1+)

- Interactive timeline visualization (vis.js/Timeline.js)
- Obsidian Publish integration
- Markdown to Notion converter
- LaTeX academic paper generator
- Wiki.js import format
- Confluence import format

---

## Related

- [[Analytics Dashboard]] - Data analysis tools
- [[README|Vault Documentation]]
- [[Quality Standards]] - Content requirements
- [[Validation Scripts]] - Quality checks

---

*The Export Pipeline enables the TTRPG History Vault to reach global audiences across formats, from academic researchers to casual readers to students using flashcards.*

**Export Formats**: 5 (Hugo, PDF, EPUB, JSON, Anki)
**Scripts**: 5 export scripts
**Last Updated**: 2025-01-XX
