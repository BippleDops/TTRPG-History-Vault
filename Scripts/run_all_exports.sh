#!/bin/bash
# Run All Export Scripts for TTRPG History Vault
# Generates all distribution formats for maximum reach

set -e

VAULT_ROOT="/Users/jonsussmanstudio/Desktop/Code Demonstrator For Karl/TTRPG-History-Vault"
cd "$VAULT_ROOT"

echo "=================================================="
echo "TTRPG HISTORY VAULT - EXPORT PIPELINE"
echo "=================================================="
echo ""
echo "Starting full export pipeline..."
echo "Generated: $(date)"
echo ""

# 1. JSON API
echo "1/5 Exporting JSON API..."
python3 Scripts/export/json_api_exporter.py
echo "✓ Complete"
echo ""

# 2. Anki Flashcards
echo "2/5 Generating Anki flashcards..."
python3 Scripts/export/anki_flashcards.py
echo "✓ Complete"
echo ""

# 3. Hugo Site
echo "3/5 Exporting Hugo static site..."
python3 Scripts/export/hugo_exporter.py
echo "✓ Complete"
echo ""

# 4. EPUB Ebook (requires Pandoc)
echo "4/5 Generating EPUB ebook..."
if command -v pandoc &> /dev/null; then
    python3 Scripts/export/epub_generator.py
    echo "✓ Complete"
else
    echo "⚠ Skipped (Pandoc not installed)"
fi
echo ""

# 5. PDF Anthology (requires Pandoc + LaTeX)
echo "5/5 Compiling PDF anthology..."
if command -v pandoc &> /dev/null; then
    python3 Scripts/export/pdf_compiler.py
    echo "✓ Complete"
else
    echo "⚠ Skipped (Pandoc not installed)"
fi
echo ""

echo "=================================================="
echo "EXPORT COMPLETE"
echo "=================================================="
echo ""
echo "Outputs saved to: Exports/"
echo ""
echo "Distribution formats:"
echo "  • JSON API:    Exports/json-api/"
echo "  • Flashcards:  Exports/ttrpg-history-flashcards.txt"
echo "  • Hugo Site:   Exports/hugo-site/"
echo "  • EPUB:        Exports/TTRPG-History-Vault-Complete.epub"
echo "  • PDF:         Exports/TTRPG-History-Vault-Complete.pdf"
echo ""
echo "View Export Pipeline: open 'Views/Export-Pipeline.md'"
echo ""
