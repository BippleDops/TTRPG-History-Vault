#!/usr/bin/env python3
"""
Coverage Gaps Analyzer for TTRPG History Vault

Identifies gaps in vault coverage by analyzing:
- Missing entries in historical timeline
- Underrepresented genres, systems, eras
- Broken wikilinks (references to non-existent entries)
- Geographic/cultural gaps
- Designer/publisher coverage gaps

Outputs:
- Gap analysis report
- Prioritized list of entries to create
- Broken link report
- CSV data for tracking

Usage:
    python Scripts/analytics/coverage_gaps.py
    python Scripts/analytics/coverage_gaps.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict, Counter


def extract_frontmatter(file_path):
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return {}, content

        frontmatter_text = match.group(1)
        return yaml.safe_load(frontmatter_text) or {}, content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}, ""


def extract_wikilinks(content):
    """Extract all wikilinks from content."""
    # Pattern: [[Link]] or [[Link|Display]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]'
    matches = re.findall(pattern, content)
    return [m.strip() for m in matches]


def load_all_entries(vault_path):
    """Load all vault entries."""
    entries = {
        'games': [],
        'designers': [],
        'publishers': [],
        'supplements': [],
        'controversies': [],
        'retroclones': [],
        'vtt': [],
        'mechanics': [],
        'other': []
    }

    entry_names = set()
    all_wikilinks = []

    # Define folders to scan
    folders = {
        'games': 'Games',
        'designers': 'Designers',
        'publishers': 'Publishers',
        'supplements': 'Supplements',
        'controversies': 'Controversies',
        'retroclones': 'Retroclones',
        'vtt': 'VTT Platforms',
        'mechanics': 'Mechanics'
    }

    for category, folder_name in folders.items():
        folder_path = vault_path / folder_name
        if folder_path.exists():
            for md_file in folder_path.glob('*.md'):
                frontmatter, content = extract_frontmatter(md_file)

                entry_name = frontmatter.get('title', md_file.stem)
                entry_names.add(entry_name)

                # Extract wikilinks from content
                links = extract_wikilinks(content)
                all_wikilinks.extend(links)

                entries[category].append({
                    'name': entry_name,
                    'path': str(md_file),
                    'frontmatter': frontmatter,
                    'wikilinks': links
                })

    return entries, entry_names, all_wikilinks


def analyze_broken_links(entry_names, all_wikilinks):
    """Identify wikilinks that point to non-existent entries."""
    link_counts = Counter(all_wikilinks)
    broken_links = {}

    for link, count in link_counts.items():
        if link not in entry_names:
            broken_links[link] = count

    return broken_links


def analyze_temporal_gaps(games):
    """Identify gaps in historical timeline."""
    if not games:
        return []

    years_covered = set()
    for game in games:
        year = game['frontmatter'].get('year-published')
        if year:
            years_covered.add(year)

    if not years_covered:
        return []

    min_year = min(years_covered)
    max_year = max(years_covered)

    # Identify major gaps (5+ consecutive years)
    gaps = []
    current_gap_start = None

    for year in range(min_year, max_year + 1):
        if year not in years_covered:
            if current_gap_start is None:
                current_gap_start = year
        else:
            if current_gap_start is not None:
                gap_length = year - current_gap_start
                if gap_length >= 5:
                    gaps.append((current_gap_start, year - 1, gap_length))
                current_gap_start = None

    return gaps


def analyze_genre_coverage(games):
    """Analyze genre representation."""
    genre_counts = Counter()

    for game in games:
        genres = game['frontmatter'].get('genre', [])
        if not isinstance(genres, list):
            genres = [genres] if genres else []

        for genre in genres:
            if genre:
                genre_counts[genre] += 1

    return genre_counts


def analyze_system_coverage(games):
    """Analyze system family representation."""
    system_counts = Counter()

    for game in games:
        system = game['frontmatter'].get('system')
        if system:
            system_counts[system] += 1

    return system_counts


def identify_missing_major_games():
    """List of historically significant games that should be in vault."""
    # This is a curated list of major games commonly considered essential
    essential_games = {
        'AD&D Era': [
            'Advanced Dungeons & Dragons (1977)',
            'AD&D 2nd Edition (1989)',
        ],
        'D&D Editions': [
            'D&D Third Edition (2000)',
            'D&D 3.5 Edition (2003)',
            'D&D Fourth Edition (2008)',
            'Basic D&D (1977)',
            'BECMI D&D (1983)',
        ],
        'Major Systems': [
            'GURPS (1986)',
            'Shadowrun (1989)',
            'Cyberpunk 2020 (1990)',
            'Vampire: The Masquerade (1991)',
            'Werewolf: The Apocalypse (1992)',
            'Mage: The Ascension (1993)',
            'Deadlands (1996)',
            'Savage Worlds (2003)',
            'Mutants & Masterminds (2002)',
        ],
        'Indie/Story Games': [
            'Sorcerer (2001)',
            'Dogs in the Vineyard (2004)',
            'Primetime Adventures (2004)',
            'Polaris (2005)',
            'Fiasco (2009)',
            'Dungeon World (2012)',
            'Fate Core (2013)',
            'Powered by the Apocalypse (2010)',
        ],
        'International': [
            'Warhammer Fantasy Roleplay (1986)',
            'Das Schwarze Auge (1984)',
            'Pendragon (1985)',
            'RuneQuest (1978)',
            'Ryuutama (2007)',
            'Kult (1991)',
        ],
        'Modern Era': [
            'Blades in the Dark (2017)',
            'Monster of the Week (2012)',
            'The Sprawl (2016)',
            '13th Age (2013)',
            'Numenera (2013)',
        ]
    }

    return essential_games


def generate_gap_report(entries, entry_names, all_wikilinks, output_dir):
    """Generate comprehensive gap analysis report."""

    print(f"\n{'='*60}")
    print("COVERAGE GAPS ANALYSIS")
    print(f"{'='*60}\n")

    # Current coverage stats
    print("Current Vault Coverage:\n")
    for category, items in entries.items():
        if items:
            print(f"  {category.title()}: {len(items)} entries")
    print(f"\n  Total Entries: {sum(len(items) for items in entries.values())}")

    # Broken links analysis
    print(f"\n{'='*60}")
    print("BROKEN LINKS (References to Non-Existent Entries)")
    print(f"{'='*60}\n")

    broken_links = analyze_broken_links(entry_names, all_wikilinks)

    if broken_links:
        print(f"Found {len(broken_links)} broken links ({sum(broken_links.values())} total references):\n")

        # Sort by frequency
        sorted_broken = sorted(broken_links.items(), key=lambda x: x[1], reverse=True)

        print("Most Referenced Missing Entries:\n")
        for link, count in sorted_broken[:20]:
            print(f"  [[{link}]] - {count} references")
    else:
        print("No broken links found!")

    # Temporal gaps
    print(f"\n{'='*60}")
    print("TEMPORAL GAPS (Years with No Coverage)")
    print(f"{'='*60}\n")

    temporal_gaps = analyze_temporal_gaps(entries['games'])

    if temporal_gaps:
        print("Significant gaps (5+ consecutive years):\n")
        for start, end, length in temporal_gaps:
            print(f"  {start}-{end} ({length} years)")
    else:
        print("No major temporal gaps found")

    # Genre coverage
    print(f"\n{'='*60}")
    print("GENRE REPRESENTATION")
    print(f"{'='*60}\n")

    genre_counts = analyze_genre_coverage(entries['games'])

    print("Games by Genre:\n")
    for genre, count in genre_counts.most_common():
        print(f"  {genre}: {count} games")

    # Underrepresented genres
    all_genres = {'fantasy', 'sci-fi', 'horror', 'modern', 'historical',
                 'superhero', 'cyberpunk', 'post-apocalyptic', 'western',
                 'universal', 'comedy', 'mystery'}

    missing_genres = all_genres - set(genre_counts.keys())
    if missing_genres:
        print(f"\nMissing Genres: {', '.join(missing_genres)}")

    # System coverage
    print(f"\n{'='*60}")
    print("SYSTEM FAMILY REPRESENTATION")
    print(f"{'='*60}\n")

    system_counts = analyze_system_coverage(entries['games'])

    print("Games by System:\n")
    for system, count in system_counts.most_common(15):
        print(f"  {system}: {count} games")

    # Essential games checklist
    print(f"\n{'='*60}")
    print("ESSENTIAL GAMES CHECKLIST")
    print(f"{'='*60}\n")

    essential_games = identify_missing_major_games()
    missing_essential = []

    for category, games in essential_games.items():
        print(f"{category}:")
        for game in games:
            # Extract base name for matching
            base_name = game.split('(')[0].strip()
            found = any(base_name.lower() in entry['name'].lower()
                       for entry in entries['games'])

            status = "✓" if found else "✗"
            print(f"  {status} {game}")

            if not found:
                missing_essential.append(game)
        print()

    # Priority recommendations
    print(f"\n{'='*60}")
    print("PRIORITY RECOMMENDATIONS")
    print(f"{'='*60}\n")

    print("High Priority Entries to Create:\n")

    print("1. BROKEN LINK TARGETS (most referenced):")
    for link, count in sorted_broken[:10]:
        print(f"   - {link} ({count} references)")

    print("\n2. ESSENTIAL MISSING GAMES:")
    for game in missing_essential[:10]:
        print(f"   - {game}")

    print("\n3. DESIGNER/PUBLISHER GAPS:")
    print("   - Create designer entries for game creators without profiles")
    print("   - Create publisher entries for major publishers")

    print("\n4. GEOGRAPHIC/CULTURAL GAPS:")
    print("   - Add European games (German, French, Swedish)")
    print("   - Add Japanese games (Ryuutama, Tenra Bansho Zero, etc.)")
    print("   - Add Latin American games")

    # Export CSV
    csv_path = output_dir / 'coverage-gaps.csv'
    with open(csv_path, 'w') as f:
        f.write("Type,Entry,References,Priority\n")

        for link, count in sorted_broken:
            priority = "High" if count >= 5 else "Medium" if count >= 2 else "Low"
            f.write(f"Broken Link,{link},{count},{priority}\n")

        for game in missing_essential:
            f.write(f"Essential Game,{game},0,High\n")

    print(f"\n\nGap analysis exported to: {csv_path}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Analyze TTRPG vault coverage gaps')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output directory for reports')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)
    output_dir = Path(args.output) if args.output else vault_path / "Attachments" / "Diagrams" / "analytics"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Analyzing vault at: {vault_path}")
    print(f"Output directory: {output_dir}")

    # Load all entries
    entries, entry_names, all_wikilinks = load_all_entries(vault_path)

    # Generate gap report
    generate_gap_report(entries, entry_names, all_wikilinks, output_dir)

    print(f"\n{'='*60}")
    print("Gap analysis complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
