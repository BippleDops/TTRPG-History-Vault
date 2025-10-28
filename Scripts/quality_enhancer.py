#!/usr/bin/env python3
"""
Quality Enhancer for TTRPG History Vault

Suggests improvements to existing entries:
- Missing property fields
- Stub entries (too short)
- Missing wikilinks to related content
- Entries needing expansion
- Outdated information

Outputs:
- Quality report with prioritized suggestions
- Entry-by-entry improvement recommendations
- Automated suggestions for wikilinks

Usage:
    python Scripts/quality_enhancer.py
    python Scripts/quality_enhancer.py --type game
"""

import os
import re
from pathlib import Path
from collections import defaultdict


def extract_frontmatter_and_content(file_path):
    """Extract frontmatter and body content."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
        if not match:
            return {}, "", 0

        frontmatter_text = match.group(1)
        body = match.group(2)
        word_count = len(body.split())

        # Simple frontmatter parsing
        frontmatter = {}
        for line in frontmatter_text.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                frontmatter[key.strip()] = value.strip()

        return frontmatter, body, word_count

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}, "", 0


def analyze_entry_quality(file_path, entry_type):
    """Analyze single entry for quality issues."""
    frontmatter, body, word_count = extract_frontmatter_and_content(file_path)

    issues = []
    suggestions = []
    priority = "low"

    title = frontmatter.get('title', file_path.stem)

    # Check word count
    if word_count < 100:
        issues.append("stub")
        suggestions.append(f"Expand content (currently {word_count} words, aim for 500+)")
        priority = "high"
    elif word_count < 300:
        issues.append("short")
        suggestions.append(f"Add more detail ({word_count} words, aim for 500+)")
        priority = "medium"

    # Check for missing critical fields by type
    required_fields = {
        'game': ['year-published', 'designer', 'publisher', 'system'],
        'designer': ['designer-name', 'notable-works'],
        'publisher': ['publisher-name', 'founded'],
        'mechanic': ['mechanic-name', 'introduced-in']
    }

    if entry_type in required_fields:
        for field in required_fields[entry_type]:
            if field not in frontmatter or not frontmatter[field]:
                issues.append(f"missing-{field}")
                suggestions.append(f"Add {field} to frontmatter")
                if priority != "high":
                    priority = "medium"

    # Check for missing significance scores
    if entry_type == 'game':
        if 'historical-significance' not in frontmatter:
            issues.append("no-significance-score")
            suggestions.append("Add historical-significance rating (1-5)")
        if 'innovation-score' not in frontmatter:
            issues.append("no-innovation-score")
            suggestions.append("Add innovation-score rating (1-5)")

    # Check for wikilinks (should have some)
    wikilink_count = len(re.findall(r'\[\[([^\]]+)\]\]', body))
    if wikilink_count == 0:
        issues.append("no-wikilinks")
        suggestions.append("Add wikilinks to related entries (designers, publishers, related games)")
        if priority == "low":
            priority = "medium"
    elif wikilink_count < 3:
        issues.append("few-wikilinks")
        suggestions.append(f"Consider adding more wikilinks ({wikilink_count} found, aim for 5+)")

    # Check for headers/structure
    header_count = len(re.findall(r'^#+\s+', body, re.MULTILINE))
    if header_count < 3 and word_count > 300:
        issues.append("poor-structure")
        suggestions.append("Add section headers for better organization")

    # Check for references
    if 'References' not in body and 'Further Reading' not in body and word_count > 500:
        issues.append("no-references")
        suggestions.append("Add References or Further Reading section")

    return {
        'file': file_path.name,
        'title': title,
        'word_count': word_count,
        'wikilink_count': wikilink_count,
        'issues': issues,
        'suggestions': suggestions,
        'priority': priority
    }


def generate_quality_report(vault_path, entry_type=None):
    """Generate comprehensive quality report."""
    print(f"\n{'='*60}")
    print("QUALITY ENHANCEMENT ANALYSIS")
    print(f"{'='*60}\n")

    folders_to_check = {
        'game': 'Games',
        'designer': 'Designers',
        'publisher': 'Publishers',
        'mechanic': 'Mechanics',
        'supplement': 'Supplements'
    }

    if entry_type:
        folders_to_check = {entry_type: folders_to_check[entry_type]}

    all_results = defaultdict(list)

    for etype, folder_name in folders_to_check.items():
        folder_path = vault_path / folder_name
        if not folder_path.exists():
            continue

        print(f"Analyzing {folder_name}...")

        for md_file in folder_path.glob('*.md'):
            result = analyze_entry_quality(md_file, etype)
            if result['issues']:
                all_results[etype].append(result)

        print(f"  Found {len(all_results[etype])} entries needing improvement")

    # Print prioritized results
    print(f"\n{'='*60}")
    print("IMPROVEMENT PRIORITIES")
    print(f"{'='*60}\n")

    for priority in ['high', 'medium', 'low']:
        priority_entries = []
        for etype, results in all_results.items():
            priority_entries.extend([r for r in results if r['priority'] == priority])

        if priority_entries:
            print(f"{priority.upper()} PRIORITY ({len(priority_entries)} entries):\n")

            for entry in sorted(priority_entries, key=lambda x: x['word_count'])[:20]:
                print(f"  {entry['title']}")
                print(f"    File: {entry['file']}")
                print(f"    Words: {entry['word_count']} | Wikilinks: {entry['wikilink_count']}")
                print(f"    Issues: {', '.join(entry['issues'])}")
                print(f"    Suggestions:")
                for suggestion in entry['suggestions']:
                    print(f"      • {suggestion}")
                print()

    # Summary statistics
    print(f"\n{'='*60}")
    print("SUMMARY STATISTICS")
    print(f"{'='*60}\n")

    total_issues = sum(len(results) for results in all_results.values())
    print(f"Total entries needing improvement: {total_issues}")
    print(f"\nBy type:")
    for etype, results in all_results.items():
        print(f"  {etype.title()}: {len(results)} entries")

    print(f"\nBy priority:")
    for priority in ['high', 'medium', 'low']:
        count = sum(1 for results in all_results.values()
                   for r in results if r['priority'] == priority)
        print(f"  {priority.title()}: {count} entries")

    # Most common issues
    print(f"\nMost common issues:")
    all_issues = []
    for results in all_results.values():
        for result in results:
            all_issues.extend(result['issues'])

    from collections import Counter
    issue_counts = Counter(all_issues)
    for issue, count in issue_counts.most_common(10):
        print(f"  {issue}: {count} entries")

    print(f"\n{'='*60}")
    print("Use these recommendations to prioritize content improvement")
    print(f"{'='*60}\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Analyze vault content quality')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       help='Path to vault root')
    parser.add_argument('--type', type=str,
                       choices=['game', 'designer', 'publisher', 'mechanic', 'supplement'],
                       help='Analyze specific entry type only')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)

    generate_quality_report(vault_path, args.type)


if __name__ == '__main__':
    main()
