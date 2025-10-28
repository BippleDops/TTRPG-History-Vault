#!/usr/bin/env python3
"""
EPUB Ebook Generator for TTRPG History Vault

Generates EPUB ebooks from vault content using Pandoc.
Creates portable, readable ebooks for e-readers, tablets, and reading apps.

Outputs:
- EPUB 3.0 format ebook
- Embedded metadata
- Table of contents
- Optional cover image

Requirements:
    pip install pyyaml
    Pandoc must be installed: https://pandoc.org/installing.html

Usage:
    python Scripts/export/epub_generator.py
    python Scripts/export/epub_generator.py --output Exports/TTRPG-History-Vault.epub
    python Scripts/export/epub_generator.py --section games --output Exports/Games.epub
"""

import os
import re
import yaml
import subprocess
from pathlib import Path
from datetime import datetime


def check_pandoc():
    """Check if Pandoc is installed."""
    try:
        result = subprocess.run(['pandoc', '--version'],
                              capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content

    frontmatter_text = match.group(1)
    body = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_text) or {}
    except:
        frontmatter = {}

    return frontmatter, body


def convert_for_epub(content):
    """Convert Obsidian-specific syntax for EPUB rendering."""
    # Convert wikilinks to plain text (no hyperlinks in EPUB)
    content = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]',
                    lambda m: f"*{m.group(2) if m.group(2) else m.group(1)}*",
                    content)

    # Remove Datacore queries
    content = re.sub(r'```datacore.*?```', '', content, flags=re.DOTALL)

    # Convert embedded images
    content = re.sub(r'!\[\[([^\]]+)\]\]', r'![\1](images/\1)', content)

    return content


def create_metadata_yaml(title, author="TTRPG History Vault Contributors"):
    """Create Pandoc metadata YAML."""
    return f"""---
title: "{title}"
author: "{author}"
date: "{datetime.now().strftime('%Y-%m-%d')}"
language: en-US
rights: "Creative Commons Attribution-ShareAlike 4.0"
---

"""


def compile_section(vault_path, section_name, folder_name):
    """Compile all entries from a section into markdown."""
    section_folder = vault_path / folder_name

    if not section_folder.exists():
        return ""

    print(f"Compiling {section_name}...")

    output = f"# {section_name}\n\n"

    md_files = sorted(section_folder.glob('*.md'))

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = extract_frontmatter(content)
        body = convert_for_epub(body)

        title = frontmatter.get('title', md_file.stem)
        output += f"## {title}\n\n"
        output += body
        output += "\n\n"

    print(f"  Processed {len(md_files)} entries")
    return output


def generate_epub(vault_path, output_path, section=None):
    """Generate EPUB ebook."""
    print(f"\n{'='*60}")
    print("EPUB EBOOK GENERATOR")
    print(f"{'='*60}\n")

    if not check_pandoc():
        print("ERROR: Pandoc not found!")
        print("Install from: https://pandoc.org/installing.html")
        return

    print(f"Source: {vault_path}")
    print(f"Output: {output_path}\n")

    # Create temporary markdown
    temp_dir = vault_path / "Exports" / "temp"
    temp_dir.mkdir(parents=True, exist_ok=True)
    temp_md = temp_dir / "temp_epub.md"

    # Build content
    if section:
        # Single section
        section_map = {
            'games': ("Games", "Games"),
            'designers': ("Designers", "Designers"),
            'publishers': ("Publishers", "Publishers"),
            'mechanics': ("Game Mechanics", "Mechanics"),
            'supplements': ("Supplements", "Supplements")
        }

        section_name, folder_name = section_map[section]
        title = f"TTRPG History Vault: {section_name}"

        content = create_metadata_yaml(title)
        content += compile_section(vault_path, section_name, folder_name)

    else:
        # Full anthology
        title = "TTRPG History Vault: Complete Encyclopedia"
        content = create_metadata_yaml(title)

        content += f"""
# TTRPG History Vault

**A Comprehensive Encyclopedia of Tabletop Roleplaying Games**

This ebook contains the complete TTRPG History Vault, documenting the history, design, and cultural impact of tabletop roleplaying games from 1974 to the present.

**Generated**: {datetime.now().strftime('%B %d, %Y')}

**License**: Creative Commons Attribution-ShareAlike 4.0

**Source**: https://github.com/yourusername/ttrpg-history-vault

---

"""

        # All sections
        sections = [
            ("Games", "Games"),
            ("Designers", "Designers"),
            ("Publishers", "Publishers"),
            ("Game Mechanics", "Mechanics"),
            ("Supplements and Adventures", "Supplements"),
            ("Retroclones", "Retroclones"),
            ("Virtual Tabletop Platforms", "VTT Platforms"),
            ("Controversies and Debates", "Controversies")
        ]

        for section_name, folder_name in sections:
            content += compile_section(vault_path, section_name, folder_name)

    # Write temporary markdown
    with open(temp_md, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"\nCompiling EPUB with Pandoc...")

    # Pandoc command
    pandoc_args = [
        'pandoc',
        str(temp_md),
        '-o', str(output_path),
        '--toc',
        '--toc-depth=2',
        '--epub-chapter-level=2',
        '-V', 'lang=en-US'
    ]

    # Add cover image if available
    cover_path = vault_path / 'Attachments' / 'Images' / 'cover.png'
    if cover_path.exists():
        pandoc_args.extend(['--epub-cover-image', str(cover_path)])

    try:
        result = subprocess.run(pandoc_args, capture_output=True, text=True, timeout=180)

        if result.returncode == 0:
            print(f"\n{'='*60}")
            print("EPUB GENERATION SUCCESSFUL")
            print(f"{'='*60}\n")
            print(f"Output: {output_path}")
            print(f"Size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")

            # Clean up
            temp_md.unlink()
            print(f"\nCleaned up temporary files")

        else:
            print(f"\nERROR: Pandoc compilation failed")
            print(f"STDERR: {result.stderr}")
            print(f"\nTemporary markdown saved at: {temp_md}")

    except subprocess.TimeoutExpired:
        print(f"\nERROR: Pandoc timed out")
        print(f"Temporary markdown saved at: {temp_md}")

    except Exception as e:
        print(f"\nERROR: {e}")
        print(f"Temporary markdown saved at: {temp_md}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate EPUB ebook from vault')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output EPUB path')
    parser.add_argument('--section', type=str,
                       choices=['games', 'designers', 'publishers', 'mechanics', 'supplements'],
                       help='Generate EPUB for specific section only')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)

    if args.section:
        output_path = Path(args.output) if args.output else \
                     vault_path / "Exports" / f"TTRPG-Vault-{args.section.title()}.epub"
    else:
        output_path = Path(args.output) if args.output else \
                     vault_path / "Exports" / "TTRPG-History-Vault-Complete.epub"

    generate_epub(vault_path, output_path, args.section)


if __name__ == '__main__':
    main()
