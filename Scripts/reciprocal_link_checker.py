#!/usr/bin/env python3
"""
Reciprocal Link Checker for TTRPG History Vault

Validates bidirectional relationships between vault entries.
Identifies missing reciprocal links that break relationship consistency.

Examples of relationships that should be bidirectional:
- Game influence-on ↔ influenced-by
- Publisher key-releases ↔ Game publisher
- Designer notable-works ↔ Game designer
- Mechanic games-using ↔ appears in game

Usage:
    python reciprocal_link_checker.py
    python reciprocal_link_checker.py --fix-dry-run
    python reciprocal_link_checker.py --verbose
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Define reciprocal relationship patterns
RECIPROCAL_RELATIONSHIPS = {
    'influence-on': {
        'reverse_property': 'influenced-by',
        'description': 'Game influences should be reciprocal'
    },
    'influenced-by': {
        'reverse_property': 'influence-on',
        'description': 'Game influences should be reciprocal'
    },
    'key-releases': {
        'reverse_property': 'publisher',
        'target_folder': 'Games',
        'description': 'Publisher key releases should match game publishers'
    },
    'notable-works': {
        'reverse_property': 'designer',
        'target_folder': 'Games',
        'description': 'Designer notable works should match game designers'
    },
    'games-using': {
        'reverse_property': 'mechanics',
        'target_folder': 'Games',
        'description': 'Mechanic usage should be documented in games'
    }
}


def extract_frontmatter(file_path: Path) -> Tuple[Dict, str]:
    """
    Extract YAML frontmatter and remaining content from markdown file.

    Returns:
        (frontmatter_dict, full_content)
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match frontmatter between --- delimiters
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return {}, content

        frontmatter_text = match.group(1)
        frontmatter = yaml.safe_load(frontmatter_text) or {}

        return frontmatter, content

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}, ""


def extract_wikilinks(text: str) -> Set[str]:
    """Extract all [[WikiLinks]] from text, returning set of target pages."""
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    matches = re.findall(pattern, text)
    return set(matches)


def normalize_filename(name: str) -> str:
    """Normalize filename for comparison (remove .md extension if present)."""
    return name.replace('.md', '')


def find_all_vault_files(vault_path: Path) -> Dict[str, Path]:
    """
    Build index of all markdown files in vault.

    Returns:
        Dict mapping normalized filename to file path
    """
    file_index = {}

    for folder in ['Games', 'Publishers', 'Designers', 'Mechanics', 'Historical Context',
                   'Actual Play', 'Awards', 'Controversies', 'Conventions',
                   'Digital Adaptations', 'Retroclones', 'Supplements', 'VTT Platforms']:
        folder_path = vault_path / folder
        if not folder_path.exists():
            continue

        for md_file in folder_path.glob('*.md'):
            normalized_name = normalize_filename(md_file.stem)
            file_index[normalized_name] = md_file

    return file_index


def check_reciprocal_links(vault_path: Path, verbose: bool = False) -> Dict:
    """
    Check all reciprocal relationships in vault.

    Returns:
        Results dict with broken relationships and statistics
    """
    results = {
        'total_relationships': 0,
        'valid_relationships': 0,
        'broken_relationships': 0,
        'issues': []
    }

    # Build file index
    file_index = find_all_vault_files(vault_path)

    if verbose:
        print(f"Found {len(file_index)} files in vault")
        print("")

    # Check each file
    for file_name, file_path in file_index.items():
        frontmatter, _ = extract_frontmatter(file_path)

        if not frontmatter:
            continue

        # Check each property that has reciprocal relationships
        for prop_name, relationship_info in RECIPROCAL_RELATIONSHIPS.items():
            if prop_name not in frontmatter:
                continue

            prop_value = frontmatter[prop_name]

            # Handle different property value types
            linked_items = []
            if isinstance(prop_value, list):
                linked_items = [extract_wikilinks(str(item)) for item in prop_value]
                linked_items = set().union(*linked_items) if linked_items else set()
            elif isinstance(prop_value, str):
                linked_items = extract_wikilinks(prop_value)
            else:
                continue

            # Check each linked item
            for linked_name in linked_items:
                results['total_relationships'] += 1

                normalized_linked = normalize_filename(linked_name)

                # Find the linked file
                if normalized_linked not in file_index:
                    results['broken_relationships'] += 1
                    results['issues'].append({
                        'type': 'missing_target',
                        'source_file': file_name,
                        'source_property': prop_name,
                        'target_file': linked_name,
                        'description': f"Target file not found"
                    })
                    if verbose:
                        print(f"✗ {file_name} → {linked_name}: Target file not found")
                    continue

                # Check reciprocal link
                target_path = file_index[normalized_linked]
                target_frontmatter, _ = extract_frontmatter(target_path)

                reverse_prop = relationship_info['reverse_property']

                if reverse_prop not in target_frontmatter:
                    results['broken_relationships'] += 1
                    results['issues'].append({
                        'type': 'missing_reciprocal',
                        'source_file': file_name,
                        'source_property': prop_name,
                        'target_file': linked_name,
                        'target_property': reverse_prop,
                        'description': f"Missing reciprocal link"
                    })
                    if verbose:
                        print(f"✗ {file_name}.{prop_name} → {linked_name}: Missing {reverse_prop}")
                    continue

                # Check if reciprocal link points back
                reverse_value = target_frontmatter[reverse_prop]
                reverse_links = set()

                if isinstance(reverse_value, list):
                    reverse_links = [extract_wikilinks(str(item)) for item in reverse_value]
                    reverse_links = set().union(*reverse_links) if reverse_links else set()
                elif isinstance(reverse_value, str):
                    reverse_links = extract_wikilinks(reverse_value)

                # Normalize and check
                reverse_links_normalized = {normalize_filename(link) for link in reverse_links}

                if normalize_filename(file_name) not in reverse_links_normalized:
                    results['broken_relationships'] += 1
                    results['issues'].append({
                        'type': 'incomplete_reciprocal',
                        'source_file': file_name,
                        'source_property': prop_name,
                        'target_file': linked_name,
                        'target_property': reverse_prop,
                        'description': f"Reciprocal property exists but doesn't link back"
                    })
                    if verbose:
                        print(f"✗ {file_name}.{prop_name} → {linked_name}.{reverse_prop}: Doesn't link back")
                else:
                    results['valid_relationships'] += 1
                    if verbose:
                        print(f"✓ {file_name}.{prop_name} ↔ {linked_name}.{reverse_prop}")

    return results


def generate_report(results: Dict, output_path: Path = None) -> str:
    """Generate markdown report of reciprocal link issues."""
    report_lines = [
        "# Reciprocal Link Validation Report",
        "",
        f"**Total Relationships Checked**: {results['total_relationships']}",
        f"**Valid**: {results['valid_relationships']} ({results['valid_relationships']/results['total_relationships']*100:.1f}%)" if results['total_relationships'] > 0 else "**Valid**: 0 (0.0%)",
        f"**Broken**: {results['broken_relationships']}",
        "",
        "---",
        ""
    ]

    if results['issues']:
        report_lines.append("## Issues Found")
        report_lines.append("")

        # Group by issue type
        by_type = defaultdict(list)
        for issue in results['issues']:
            by_type[issue['type']].append(issue)

        # Missing target files
        if 'missing_target' in by_type:
            report_lines.append("### Missing Target Files")
            report_lines.append("")
            report_lines.append("These links point to files that don't exist:")
            report_lines.append("")
            for issue in by_type['missing_target']:
                report_lines.append(f"- `{issue['source_file']}` → `[[{issue['target_file']}]]` (property: `{issue['source_property']}`)")
            report_lines.append("")

        # Missing reciprocal properties
        if 'missing_reciprocal' in by_type:
            report_lines.append("### Missing Reciprocal Properties")
            report_lines.append("")
            report_lines.append("These files are linked but don't have the reciprocal property:")
            report_lines.append("")
            for issue in by_type['missing_reciprocal']:
                report_lines.append(f"- `{issue['source_file']}.{issue['source_property']}` → `{issue['target_file']}` (needs `{issue['target_property']}`)")
            report_lines.append("")

        # Incomplete reciprocal links
        if 'incomplete_reciprocal' in by_type:
            report_lines.append("### Incomplete Reciprocal Links")
            report_lines.append("")
            report_lines.append("These files have the reciprocal property but don't link back:")
            report_lines.append("")
            for issue in by_type['incomplete_reciprocal']:
                report_lines.append(f"- `{issue['source_file']}.{issue['source_property']}` → `{issue['target_file']}.{issue['target_property']}` (should link back to `[[{issue['source_file']}]]`)")
            report_lines.append("")

    else:
        report_lines.append("## ✓ No Issues Found")
        report_lines.append("")
        report_lines.append("All reciprocal relationships are valid!")
        report_lines.append("")

    report_lines.extend([
        "---",
        "",
        "## Recommendations",
        "",
        "To fix broken reciprocal relationships:",
        "",
        "1. **Missing Target Files**: Check if the linked file was renamed or moved. Update the link.",
        "2. **Missing Reciprocal Properties**: Add the missing property to the target file's frontmatter.",
        "3. **Incomplete Reciprocal Links**: Add the source file to the target's reciprocal property list.",
        "",
        "---",
        "",
        "*Generated by reciprocal_link_checker.py*"
    ])

    report = "\n".join(report_lines)

    # Write to file if output path provided
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport written to: {output_path}")

    return report


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Check reciprocal links in TTRPG History Vault')
    parser.add_argument('--vault-path', type=str, help='Path to vault root',
                       default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parser.add_argument('--verbose', action='store_true', help='Show all relationships including valid ones')
    parser.add_argument('--output', type=str, help='Output report to file',
                       default=None)

    args = parser.parse_args()

    vault_path = Path(args.vault_path)

    print(f"Checking reciprocal links in: {vault_path}")
    print("")

    results = check_reciprocal_links(vault_path, args.verbose)

    print("\n" + "="*60)
    print("RECIPROCAL LINK CHECK SUMMARY")
    print("="*60)
    print(f"Total Relationships: {results['total_relationships']}")
    print(f"Valid: {results['valid_relationships']}")
    print(f"Broken: {results['broken_relationships']}")
    print("")

    # Generate and save report
    output_path = Path(args.output) if args.output else vault_path / "reciprocal-links-report.md"
    generate_report(results, output_path)

    # Exit with error code if any broken relationships found
    exit(0 if results['broken_relationships'] == 0 else 1)


if __name__ == '__main__':
    main()
