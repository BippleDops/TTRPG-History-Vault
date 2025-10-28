#!/usr/bin/env python3
"""
Era Comparison Analyzer for TTRPG History Vault

Compares different eras of TTRPG history across multiple dimensions:
- Design trends and innovation patterns
- Complexity evolution
- Genre popularity shifts
- Market dynamics

Outputs:
- Era comparison tables and charts
- Trend analysis reports
- Statistical comparisons
- CSV data

Requirements:
    pip install matplotlib pandas

Usage:
    python Scripts/analytics/era_comparison.py
    python Scripts/analytics/era_comparison.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict, Counter

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_LIBS = True
except ImportError:
    HAS_LIBS = False
    print("Warning: matplotlib and pandas not installed.")
    print("Install with: pip install matplotlib pandas")


def extract_frontmatter(file_path):
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return {}

        frontmatter_text = match.group(1)
        return yaml.safe_load(frontmatter_text) or {}
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}


def load_games(vault_path):
    """Load all game entries."""
    games_folder = vault_path / "Games"
    games = []

    if not games_folder.exists():
        print(f"Games folder not found at {games_folder}")
        return games

    for md_file in games_folder.glob('*.md'):
        frontmatter = extract_frontmatter(md_file)
        if frontmatter.get('type') == 'game' and 'year-published' in frontmatter:
            games.append({
                'title': frontmatter.get('title', md_file.stem),
                'year': frontmatter['year-published'],
                'system': frontmatter.get('system', 'unknown'),
                'genre': frontmatter.get('genre', []),
                'complexity': frontmatter.get('complexity', 0),
                'significance': frontmatter.get('historical-significance', 0),
                'innovation': frontmatter.get('innovation-score', 0),
                'designer': frontmatter.get('designer', 'unknown')
            })

    return games


def categorize_era(year):
    """Categorize year into TTRPG historical era."""
    if year < 1974:
        return "Pre-D&D"
    elif year < 1980:
        return "Golden Age (1974-1979)"
    elif year < 1990:
        return "TSR Dominance (1980-1989)"
    elif year < 2000:
        return "Diverse 90s (1990-1999)"
    elif year < 2008:
        return "d20 Era (2000-2007)"
    elif year < 2012:
        return "4E & Pathfinder (2008-2011)"
    elif year < 2020:
        return "5E Renaissance (2012-2019)"
    else:
        return "Modern Era (2020+)"


def analyze_eras(games, output_dir):
    """Analyze and compare different TTRPG eras."""

    if not games:
        print("No games data found!")
        return

    print(f"\n{'='*60}")
    print("ERA COMPARISON ANALYSIS")
    print(f"{'='*60}\n")

    # Group games by era
    eras = defaultdict(list)
    for game in games:
        era = categorize_era(game['year'])
        eras[era].append(game)

    # Era ordering
    era_order = [
        "Pre-D&D",
        "Golden Age (1974-1979)",
        "TSR Dominance (1980-1989)",
        "Diverse 90s (1990-1999)",
        "d20 Era (2000-2007)",
        "4E & Pathfinder (2008-2011)",
        "5E Renaissance (2012-2019)",
        "Modern Era (2020+)"
    ]

    # Filter to eras with games
    eras_with_games = [era for era in era_order if era in eras and eras[era]]

    print(f"Analyzing {len(eras_with_games)} eras:\n")

    # Print era summaries
    for era in eras_with_games:
        games_in_era = eras[era]

        print(f"{era}:")
        print(f"  Games: {len(games_in_era)}")

        if games_in_era:
            # Average metrics
            avg_complexity = sum(g['complexity'] for g in games_in_era if g['complexity'] > 0) / \
                           len([g for g in games_in_era if g['complexity'] > 0]) \
                           if any(g['complexity'] > 0 for g in games_in_era) else 0

            avg_significance = sum(g['significance'] for g in games_in_era if g['significance'] > 0) / \
                             len([g for g in games_in_era if g['significance'] > 0]) \
                             if any(g['significance'] > 0 for g in games_in_era) else 0

            avg_innovation = sum(g['innovation'] for g in games_in_era if g['innovation'] > 0) / \
                           len([g for g in games_in_era if g['innovation'] > 0]) \
                           if any(g['innovation'] > 0 for g in games_in_era) else 0

            print(f"  Avg Complexity: {avg_complexity:.2f}")
            print(f"  Avg Significance: {avg_significance:.2f}")
            print(f"  Avg Innovation: {avg_innovation:.2f}")

            # Genre distribution
            genre_counts = Counter()
            for game in games_in_era:
                genres = game['genre'] if isinstance(game['genre'], list) else [game['genre']]
                for genre in genres:
                    if genre:
                        genre_counts[genre] += 1

            top_genres = genre_counts.most_common(3)
            if top_genres:
                print(f"  Top Genres: {', '.join(f'{g}({c})' for g, c in top_genres)}")

            # System distribution
            system_counts = Counter(g['system'] for g in games_in_era if g['system'])
            top_systems = system_counts.most_common(3)
            if top_systems:
                print(f"  Top Systems: {', '.join(f'{s}({c})' for s, c in top_systems)}")

        print()

    # Trend analysis
    print(f"\n{'='*60}")
    print("TREND ANALYSIS ACROSS ERAS")
    print(f"{'='*60}\n")

    print("Complexity Trend:")
    for era in eras_with_games:
        games_in_era = eras[era]
        games_with_complexity = [g for g in games_in_era if g['complexity'] > 0]
        if games_with_complexity:
            avg = sum(g['complexity'] for g in games_with_complexity) / len(games_with_complexity)
            bar = '█' * int(avg * 5)
            print(f"  {era:30s} {avg:.2f} {bar}")

    print("\nInnovation Trend:")
    for era in eras_with_games:
        games_in_era = eras[era]
        games_with_innovation = [g for g in games_in_era if g['innovation'] > 0]
        if games_with_innovation:
            avg = sum(g['innovation'] for g in games_with_innovation) / len(games_with_innovation)
            bar = '█' * int(avg * 5)
            print(f"  {era:30s} {avg:.2f} {bar}")

    # Genre evolution
    print(f"\n{'='*60}")
    print("GENRE EVOLUTION ACROSS ERAS")
    print(f"{'='*60}\n")

    all_genres = set()
    for games_list in eras.values():
        for game in games_list:
            genres = game['genre'] if isinstance(game['genre'], list) else [game['genre']]
            all_genres.update(g for g in genres if g)

    for genre in sorted(all_genres):
        print(f"{genre}:")
        for era in eras_with_games:
            games_in_era = eras[era]
            count = sum(1 for g in games_in_era
                       for gen in (g['genre'] if isinstance(g['genre'], list) else [g['genre']])
                       if gen == genre)
            if count > 0:
                pct = count / len(games_in_era) * 100
                print(f"  {era:30s} {count:3d} ({pct:5.1f}%)")
        print()

    # Export CSV
    csv_path = output_dir / 'era-comparison.csv'
    with open(csv_path, 'w') as f:
        f.write("Era,GameCount,AvgComplexity,AvgSignificance,AvgInnovation,TopGenre,TopSystem\n")
        for era in eras_with_games:
            games_in_era = eras[era]

            avg_complexity = sum(g['complexity'] for g in games_in_era if g['complexity'] > 0) / \
                           len([g for g in games_in_era if g['complexity'] > 0]) \
                           if any(g['complexity'] > 0 for g in games_in_era) else 0

            avg_significance = sum(g['significance'] for g in games_in_era if g['significance'] > 0) / \
                             len([g for g in games_in_era if g['significance'] > 0]) \
                             if any(g['significance'] > 0 for g in games_in_era) else 0

            avg_innovation = sum(g['innovation'] for g in games_in_era if g['innovation'] > 0) / \
                           len([g for g in games_in_era if g['innovation'] > 0]) \
                           if any(g['innovation'] > 0 for g in games_in_era) else 0

            genre_counts = Counter()
            for game in games_in_era:
                genres = game['genre'] if isinstance(game['genre'], list) else [game['genre']]
                for genre in genres:
                    if genre:
                        genre_counts[genre] += 1

            top_genre = genre_counts.most_common(1)[0][0] if genre_counts else 'unknown'

            system_counts = Counter(g['system'] for g in games_in_era)
            top_system = system_counts.most_common(1)[0][0] if system_counts else 'unknown'

            f.write(f"{era},{len(games_in_era)},{avg_complexity:.2f},{avg_significance:.2f},{avg_innovation:.2f},{top_genre},{top_system}\n")

    print(f"\nEra comparison exported to: {csv_path}")

    return eras


def visualize_era_comparisons(eras, output_dir):
    """Generate era comparison visualizations."""

    if not HAS_LIBS:
        print("Visualization libraries not available")
        return

    print("\nGenerating era comparison visualizations...")

    # Era ordering
    era_order = [
        "Pre-D&D",
        "Golden Age (1974-1979)",
        "TSR Dominance (1980-1989)",
        "Diverse 90s (1990-1999)",
        "d20 Era (2000-2007)",
        "4E & Pathfinder (2008-2011)",
        "5E Renaissance (2012-2019)",
        "Modern Era (2020+)"
    ]

    eras_with_games = [era for era in era_order if era in eras and eras[era]]

    # 1. Games per era bar chart
    fig, ax = plt.subplots(figsize=(14, 8))

    era_names = eras_with_games
    game_counts = [len(eras[era]) for era in era_names]

    ax.bar(range(len(era_names)), game_counts, color='steelblue', edgecolor='black', alpha=0.7)
    ax.set_xticks(range(len(era_names)))
    ax.set_xticklabels(era_names, rotation=45, ha='right')
    ax.set_xlabel('Era', fontsize=12, fontweight='bold')
    ax.set_ylabel('Number of Games', fontsize=12, fontweight='bold')
    ax.set_title('Games Per Era', fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='y', alpha=0.3)

    plt.tight_layout()
    output_path = output_dir / 'era-game-counts.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Generated: {output_path}")
    plt.close()

    # 2. Complexity trend line
    fig, ax = plt.subplots(figsize=(14, 8))

    avg_complexities = []
    for era in eras_with_games:
        games_in_era = eras[era]
        games_with_complexity = [g for g in games_in_era if g['complexity'] > 0]
        if games_with_complexity:
            avg = sum(g['complexity'] for g in games_with_complexity) / len(games_with_complexity)
            avg_complexities.append(avg)
        else:
            avg_complexities.append(0)

    ax.plot(range(len(era_names)), avg_complexities,
           marker='o', linewidth=2, markersize=10, color='darkgreen')
    ax.set_xticks(range(len(era_names)))
    ax.set_xticklabels(era_names, rotation=45, ha='right')
    ax.set_xlabel('Era', fontsize=12, fontweight='bold')
    ax.set_ylabel('Average Complexity', fontsize=12, fontweight='bold')
    ax.set_title('Complexity Evolution Across Eras', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 5)

    plt.tight_layout()
    output_path = output_dir / 'era-complexity-trend.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Generated: {output_path}")
    plt.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Compare TTRPG eras')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output directory for visualizations')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)
    output_dir = Path(args.output) if args.output else vault_path / "Attachments" / "Diagrams" / "analytics"

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Analyzing vault at: {vault_path}")
    print(f"Output directory: {output_dir}")

    # Load games
    games = load_games(vault_path)

    if not games:
        print("No games found!")
        return

    # Analyze eras
    eras = analyze_eras(games, output_dir)

    # Generate visualizations
    if HAS_LIBS:
        visualize_era_comparisons(eras, output_dir)
    else:
        print("\nSkipping visualizations (matplotlib/pandas not installed)")
        print("Install with: pip install matplotlib pandas")

    print(f"\n{'='*60}")
    print("Era comparison complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
