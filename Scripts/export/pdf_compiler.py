#!/usr/bin/env python3
"""
PDF Anthology Compiler for TTRPG History Vault

Compiles vault entries into a comprehensive PDF anthology using Pandoc.
Creates professional academic-style PDF with table of contents, citations, and formatting.

Outputs:
- Single comprehensive PDF
- Sectioned by entry type
- Table of contents with page numbers
- Optional: Chapter per game/designer/topic

Requirements:
    pip install pyyaml
    Pandoc must be installed: https://pandoc.org/installing.html
    LaTeX distribution (for PDF generation): TeX Live, MacTeX, or MiKTeX

Usage:
    python Scripts/export/pdf_compiler.py
    python Scripts/export/pdf_compiler.py --output Exports/TTRPG-History-Vault.pdf
    python Scripts/export/pdf_compiler.py --section games --output Exports/Games-Anthology.pdf
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


def convert_for_pdf(content):
    """Convert Obsidian-specific syntax for PDF rendering."""
    # Convert wikilinks to plain text
    content = re.sub(r'\[\[([^\]|]+)(?:\|([^\]]+))?\]\]',
                    lambda m: m.group(2) if m.group(2) else m.group(1),
                    content)

    # Remove Datacore queries
    content = re.sub(r'```datacore.*?```', '', content, flags=re.DOTALL)

    # Convert embedded images to regular markdown images
    content = re.sub(r'!\[\[([^\]]+)\]\]', r'![\1](\1)', content)

    return content


def create_title_page():
    """Generate title page markdown."""
    return f"""---
title: "TTRPG History Vault"
subtitle: "A Comprehensive Encyclopedia of Tabletop Roleplaying Games"
author: "TTRPG History Vault Contributors"
date: "{datetime.now().strftime('%B %Y')}"
---

\\newpage

# About This Anthology

This document is a comprehensive compilation of the TTRPG History Vault, an encyclopedic resource documenting the history, design, and cultural impact of tabletop roleplaying games from 1974 to the present day.

**Coverage**: Games, Designers, Publishers, Mechanics, Controversies, and more

**Methodology**: Each entry is researched and documented with attention to historical accuracy, cultural context, and design analysis.

**Last Updated**: {datetime.now().strftime('%B %d, %Y')}

**License**: Content licensed under Creative Commons (see individual entries for details)

**Source**: https://github.com/yourusername/ttrpg-history-vault

\\newpage

"""


def compile_section(vault_path, section_name, folder_name):
    """Compile all entries from a section into markdown."""
    section_folder = vault_path / folder_name

    if not section_folder.exists():
        return ""

    print(f"Compiling {section_name}...")

    # Header for section
    output = f"# {section_name}\n\n\\newpage\n\n"

    # Get all markdown files, sorted by name
    md_files = sorted(section_folder.glob('*.md'))

    for md_file in md_files:
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()

        frontmatter, body = extract_frontmatter(content)

        # Convert content
        body = convert_for_pdf(body)

        # Add to output
        title = frontmatter.get('title', md_file.stem)
        output += f"## {title}\n\n"
        output += body
        output += "\n\n\\newpage\n\n"

    print(f"  Processed {len(md_files)} entries")

    return output


def compile_full_anthology(vault_path, output_path):
    """Compile complete vault into single PDF."""
    print(f"\n{'='*60}")
    print("PDF ANTHOLOGY COMPILER")
    print(f"{'='*60}\n")

    if not check_pandoc():
        print("ERROR: Pandoc not found!")
        print("Install from: https://pandoc.org/installing.html")
        return

    print(f"Source: {vault_path}")
    print(f"Output: {output_path}\n")

    # Create temporary markdown file
    temp_md = vault_path / "Exports" / "temp_anthology.md"
    temp_md.parent.mkdir(parents=True, exist_ok=True)

    # Build anthology content
    anthology = create_title_page()

    # Define sections in order
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
        section_content = compile_section(vault_path, section_name, folder_name)
        anthology += section_content

    # Write temporary markdown
    with open(temp_md, 'w', encoding='utf-8') as f:
        f.write(anthology)

    print(f"\nGenerated temporary markdown: {temp_md}")

    # Compile to PDF with Pandoc
    print("\nCompiling PDF with Pandoc...")

    pandoc_args = [
        'pandoc',
        str(temp_md),
        '-o', str(output_path),
        '--pdf-engine=xelatex',
        '--toc',
        '--toc-depth=2',
        '--number-sections',
        '-V', 'geometry:margin=1in',
        '-V', 'fontsize=11pt',
        '-V', 'linkcolor=blue',
        '-V', 'urlcolor=blue',
        '--highlight-style=tango'
    ]

    try:
        result = subprocess.run(pandoc_args, capture_output=True, text=True, timeout=300)

        if result.returncode == 0:
            print(f"\n{'='*60}")
            print("PDF COMPILATION SUCCESSFUL")
            print(f"{'='*60}\n")
            print(f"Output: {output_path}")
            print(f"Size: {output_path.stat().st_size / 1024 / 1024:.2f} MB")

            # Clean up temporary file
            temp_md.unlink()
            print(f"\nCleaned up temporary file")
        else:
            print(f"\nERROR: Pandoc compilation failed")
            print(f"STDERR: {result.stderr}")
            print(f"\nTemporary markdown saved at: {temp_md}")

    except subprocess.TimeoutExpired:
        print(f"\nERROR: Pandoc compilation timed out (>5 minutes)")
        print(f"Temporary markdown saved at: {temp_md}")

    except Exception as e:
        print(f"\nERROR: {e}")
        print(f"Temporary markdown saved at: {temp_md}")


def compile_section_only(vault_path, section_name, folder_name, output_path):
    """Compile single section to PDF."""
    print(f"\n{'='*60}")
    print(f"PDF COMPILER - {section_name.upper()} ONLY")
    print(f"{'='*60}\n")

    if not check_pandoc():
        print("ERROR: Pandoc not found!")
        return

    # Create temporary markdown
    temp_md = vault_path / "Exports" / f"temp_{section_name.lower()}.md"
    temp_md.parent.mkdir(parents=True, exist_ok=True)

    # Title page
    anthology = f"""---
title: "{section_name}"
subtitle: "From the TTRPG History Vault"
date: "{datetime.now().strftime('%B %Y')}"
---

\\newpage

"""

    # Compile section
    anthology += compile_section(vault_path, section_name, folder_name)

    # Write temp file
    with open(temp_md, 'w', encoding='utf-8') as f:
        f.write(anthology)

    # Compile with Pandoc
    pandoc_args = [
        'pandoc',
        str(temp_md),
        '-o', str(output_path),
        '--pdf-engine=xelatex',
        '--toc',
        '-V', 'geometry:margin=1in',
        '--highlight-style=tango'
    ]

    try:
        result = subprocess.run(pandoc_args, capture_output=True, text=True, timeout=120)

        if result.returncode == 0:
            print(f"\nPDF created: {output_path}")
            temp_md.unlink()
        else:
            print(f"\nERROR: {result.stderr}")

    except Exception as e:
        print(f"\nERROR: {e}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Compile vault to PDF anthology')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output PDF path')
    parser.add_argument('--section', type=str,
                       choices=['games', 'designers', 'publishers', 'mechanics', 'supplements'],
                       help='Compile only specific section')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)

    if args.section:
        # Section-specific compilation
        section_map = {
            'games': ("Games", "Games"),
            'designers': ("Designers", "Designers"),
            'publishers': ("Publishers", "Publishers"),
            'mechanics': ("Game Mechanics", "Mechanics"),
            'supplements': ("Supplements", "Supplements")
        }

        section_name, folder_name = section_map[args.section]
        output_path = Path(args.output) if args.output else \
                     vault_path / "Exports" / f"{args.section.title()}-Anthology.pdf"

        compile_section_only(vault_path, section_name, folder_name, output_path)
    else:
        # Full anthology
        output_path = Path(args.output) if args.output else \
                     vault_path / "Exports" / "TTRPG-History-Vault-Complete.pdf"

        compile_full_anthology(vault_path, output_path)


if __name__ == '__main__':
    main()
