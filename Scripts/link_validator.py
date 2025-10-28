#!/usr/bin/env python3
"""
WikiLink Integrity Checker for TTRPG History Vault

Scans all markdown files for [[WikiLinks]] and verifies targets exist.
Reports broken links, suggests fixes based on similar filenames.

Usage: python link_validator.py [--fix] [--report output.md]
"""

import os
import re
from pathlib import Path
from difflib import get_close_matches

VAULT_ROOT = Path(__file__).parent.parent
CONTENT_FOLDERS = ["Games", "Publishers", "Designers", "Mechanics", "Historical Context", "Research Archive", "Views"]

def find_all_notes():
    """Return set of all note titles (without .md extension)"""
    notes = set()
    for folder in CONTENT_FOLDERS:
        folder_path = VAULT_ROOT / folder
        if folder_path.exists():
            for file in folder_path.glob("*.md"):
                notes.add(file.stem)
    return notes

def extract_wikilinks(content):
    """Extract all WikiLinks from markdown content"""
    # Pattern matches [[Target]] and [[Target|Display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def validate_vault():
    """Main validation logic"""
    all_notes = find_all_notes()
    broken_links = []

    for folder in CONTENT_FOLDERS:
        folder_path = VAULT_ROOT / folder
        if not folder_path.exists():
            continue

        for file_path in folder_path.glob("*.md"):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            links = extract_wikilinks(content)
            for link in links:
                if link not in all_notes:
                    # Find close matches
                    suggestions = get_close_matches(link, all_notes, n=3, cutoff=0.6)
                    broken_links.append({
                        'file': str(file_path.relative_to(VAULT_ROOT)),
                        'broken_link': link,
                        'suggestions': suggestions
                    })

    return broken_links

def generate_report(broken_links):
    """Generate markdown report"""
    report = ["# WikiLink Integrity Report\n"]
    report.append(f"**Total Broken Links**: {len(broken_links)}\n\n")

    if not broken_links:
        report.append("✅ All WikiLinks are valid!\n")
    else:
        report.append("## Broken Links\n\n")
        for item in broken_links:
            report.append(f"### {item['file']}\n")
            report.append(f"- **Broken**: `[[{item['broken_link']}]]`\n")
            if item['suggestions']:
                report.append(f"- **Suggestions**: {', '.join(f'`[[{s}]]`' for s in item['suggestions'])}\n")
            report.append("\n")

    return "".join(report)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Validate WikiLinks in TTRPG vault")
    parser.add_argument("--report", help="Output report to file")
    args = parser.parse_args()

    broken = validate_vault()
    report = generate_report(broken)

    if args.report:
        with open(args.report, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Report written to {args.report}")
    else:
        print(report)
