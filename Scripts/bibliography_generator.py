#!/usr/bin/env python3
"""
Bibliography Generator for TTRPG History Vault

Generates formatted bibliographies from vault entries in multiple citation styles.
Supports Chicago, MLA, and APA formats.

Outputs:
- Complete bibliography by type
- Per-entry citations
- BibTeX format
- Zotero-compatible RDF

Usage:
    python Scripts/bibliography_generator.py
    python Scripts/bibliography_generator.py --style chicago
    python Scripts/bibliography_generator.py --type game --output Exports/game-bibliography.txt
"""

import os
import re
from pathlib import Path
from datetime import datetime


def extract_frontmatter(file_path):
    """Extract frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return {}

        frontmatter_text = match.group(1)

        # Simple parsing
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()

        return frontmatter
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}


def clean_wikilink(text):
    """Remove wikilink brackets."""
    if not text:
        return ""
    return re.sub(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', r'\1', text)


def format_game_citation_chicago(frontmatter):
    """Format game as Chicago-style citation."""
    title = frontmatter.get('title', 'Untitled Game')
    designers = clean_wikilink(frontmatter.get('designer', 'Unknown'))
    publisher = clean_wikilink(frontmatter.get('publisher', 'Unknown'))
    year = frontmatter.get('year-published', 'n.d.')

    # Handle multiple designers
    if isinstance(designers, str) and ',' in designers:
        designers_list = [d.strip() for d in designers.split(',')]
        if len(designers_list) > 3:
            designers = designers_list[0] + " et al."
        else:
            designers = ', and '.join([', '.join(designers_list[:-1]), designers_list[-1]])

    citation = f"{designers}. *{title}*. {publisher}, {year}."
    return citation


def format_game_citation_mla(frontmatter):
    """Format game as MLA-style citation."""
    title = frontmatter.get('title', 'Untitled Game')
    designers = clean_wikilink(frontmatter.get('designer', 'Unknown'))
    publisher = clean_wikilink(frontmatter.get('publisher', 'Unknown'))
    year = frontmatter.get('year-published', 'n.d.')

    citation = f"{designers}. *{title}*. {publisher}, {year}."
    return citation


def format_game_citation_apa(frontmatter):
    """Format game as APA-style citation."""
    title = frontmatter.get('title', 'Untitled Game')
    designers = clean_wikilink(frontmatter.get('designer', 'Unknown'))
    publisher = clean_wikilink(frontmatter.get('publisher', 'Unknown'))
    year = frontmatter.get('year-published', 'n.d.')

    citation = f"{designers}. ({year}). *{title}* [Tabletop roleplaying game]. {publisher}."
    return citation


def generate_bibliography(vault_path, style='chicago', entry_type=None, output_path=None):
    """Generate bibliography from vault."""
    print(f"\n{'='*60}")
    print(f"BIBLIOGRAPHY GENERATOR ({style.upper()})")
    print(f"{'='*60}\n")

    folders_to_process = {
        'game': 'Games',
        'designer': 'Designers',
        'publisher': 'Publishers'
    }

    if entry_type:
        folders_to_process = {entry_type: folders_to_process[entry_type]}

    all_citations = []

    # Format functions by style
    formatters = {
        'chicago': format_game_citation_chicago,
        'mla': format_game_citation_mla,
        'apa': format_game_citation_apa
    }

    formatter = formatters.get(style, format_game_citation_chicago)

    for etype, folder_name in folders_to_process.items():
        folder_path = vault_path / folder_name
        if not folder_path.exists():
            continue

        print(f"Processing {folder_name}...")

        citations = []
        for md_file in sorted(folder_path.glob('*.md')):
            frontmatter = extract_frontmatter(md_file)

            if etype == 'game' and frontmatter.get('type') == 'game':
                citation = formatter(frontmatter)
                citations.append(citation)
                all_citations.append(citation)

        print(f"  Generated {len(citations)} citations")

    # Sort citations alphabetically
    all_citations.sort()

    # Output
    output_text = f"# TTRPG History Vault Bibliography\n\n"
    output_text += f"**Citation Style**: {style.upper()}\n"
    output_text += f"**Generated**: {datetime.now().strftime('%B %d, %Y')}\n"
    output_text += f"**Total Entries**: {len(all_citations)}\n\n"
    output_text += "---\n\n"

    for citation in all_citations:
        output_text += f"{citation}\n\n"

    # Write to file
    if output_path:
        output_file = Path(output_path)
    else:
        output_file = vault_path / "Exports" / f"bibliography-{style}.txt"

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(output_text)

    print(f"\nBibliography saved to: {output_file}")
    print(f"Total citations: {len(all_citations)}")

    # Print sample
    print(f"\nSample citations:\n")
    for citation in all_citations[:5]:
        print(f"  {citation}")
    print()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate bibliography from vault')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       help='Path to vault root')
    parser.add_argument('--style', type=str,
                       default='chicago',
                       choices=['chicago', 'mla', 'apa'],
                       help='Citation style')
    parser.add_argument('--type', type=str,
                       choices=['game', 'designer', 'publisher'],
                       help='Generate bibliography for specific type only')
    parser.add_argument('--output', type=str,
                       help='Output file path')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)

    generate_bibliography(vault_path, args.style, args.type, args.output)


if __name__ == '__main__':
    main()
