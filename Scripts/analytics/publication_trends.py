#!/usr/bin/env python3
"""
Publication Trends Analyzer for TTRPG History Vault

Analyzes games published per year/decade/era and generates visualizations.

Outputs:
- Bar chart: Games published per year (1974-2024)
- Line graph: Cumulative game count over time
- Pie chart: Genre distribution by era
- CSV data for further analysis

Usage:
    python Scripts/analytics/publication_trends.py
    python Scripts/analytics/publication_trends.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
import sys
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime

try:
    import matplotlib
    matplotlib.use('Agg')  # Non-interactive backend
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("Warning: matplotlib and pandas not installed. Install with: pip install matplotlib pandas")


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
    """Load all game entries from vault."""
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
                'genre': frontmatter.get('genre', []),
                'system': frontmatter.get('system', 'unknown'),
                'significance': frontmatter.get('historical-significance', 0),
                'innovation': frontmatter.get('innovation-score', 0),
                'complexity': frontmatter.get('complexity', 0)
            })

    return games


def analyze_publication_trends(games, output_dir):
    """Analyze and visualize publication trends."""

    if not games:
        print("No games data found!")
        return

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Games per year
    years = [g['year'] for g in games]
    year_counts = Counter(years)

    # Statistics
    print(f"\n{'='*60}")
    print("PUBLICATION TRENDS ANALYSIS")
    print(f"{'='*60}\n")
    print(f"Total Games Analyzed: {len(games)}")
    print(f"Year Range: {min(years)} - {max(years)}")
    print(f"Average Games Per Year: {len(games) / (max(years) - min(years) + 1):.2f}")
    print(f"\nMost Productive Years:")
    for year, count in sorted(year_counts.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {year}: {count} games")

    # Decade analysis
    decade_counts = defaultdict(int)
    for year in years:
        decade = (year // 10) * 10
        decade_counts[decade] += 1

    print(f"\nGames by Decade:")
    for decade in sorted(decade_counts.keys()):
        print(f"  {decade}s: {decade_counts[decade]} games")

    # Genre analysis
    genre_counts = Counter()
    for game in games:
        for genre in game['genre'] if isinstance(game['genre'], list) else [game['genre']]:
            genre_counts[genre] += 1

    print(f"\nMost Popular Genres:")
    for genre, count in genre_counts.most_common(5):
        print(f"  {genre}: {count} games")

    # System analysis
    system_counts = Counter(g['system'] for g in games)
    print(f"\nMost Common Systems:")
    for system, count in system_counts.most_common(5):
        print(f"  {system}: {count} games")

    # CSV export
    csv_path = output_dir / "publication-data.csv"
    with open(csv_path, 'w') as f:
        f.write("Year,Title,Genre,System,Significance,Innovation,Complexity\n")
        for game in sorted(games, key=lambda g: g['year']):
            genres = ';'.join(game['genre']) if isinstance(game['genre'], list) else game['genre']
            f.write(f"{game['year']},{game['title']},{genres},{game['system']},{game['significance']},{game['innovation']},{game['complexity']}\n")
    print(f"\nData exported to: {csv_path}")

    # Generate visualizations if matplotlib available
    if HAS_MATPLOTLIB:
        generate_visualizations(games, year_counts, decade_counts, genre_counts, output_dir)
    else:
        print("\nSkipping visualizations (matplotlib not installed)")
        print("Install with: pip install matplotlib pandas")


def generate_visualizations(games, year_counts, decade_counts, genre_counts, output_dir):
    """Generate matplotlib visualizations."""

    # 1. Games per year (bar chart)
    plt.figure(figsize=(14, 6))
    years_range = range(min(year_counts.keys()), max(year_counts.keys()) + 1)
    counts = [year_counts.get(year, 0) for year in years_range]

    plt.bar(years_range, counts, color='steelblue', edgecolor='black', alpha=0.7)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Games Published', fontsize=12)
    plt.title('TTRPG Publications by Year (1974-2024)', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.xticks(range(min(years_range), max(years_range) + 1, 5), rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / 'games-per-year.png', dpi=300, bbox_inches='tight')
    print(f"Generated: {output_dir / 'games-per-year.png'}")
    plt.close()

    # 2. Cumulative games over time (line graph)
    plt.figure(figsize=(14, 6))
    cumulative = []
    total = 0
    for year in years_range:
        total += year_counts.get(year, 0)
        cumulative.append(total)

    plt.plot(years_range, cumulative, linewidth=2, color='darkgreen', marker='o', markersize=4)
    plt.fill_between(years_range, cumulative, alpha=0.3, color='lightgreen')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Cumulative Games', fontsize=12)
    plt.title('Cumulative TTRPG Count Over Time', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xticks(range(min(years_range), max(years_range) + 1, 5), rotation=45)
    plt.tight_layout()
    plt.savefig(output_dir / 'cumulative-games.png', dpi=300, bbox_inches='tight')
    print(f"Generated: {output_dir / 'cumulative-games.png'}")
    plt.close()

    # 3. Games by decade (bar chart)
    plt.figure(figsize=(10, 6))
    decades = sorted(decade_counts.keys())
    decade_values = [decade_counts[d] for d in decades]
    decade_labels = [f"{d}s" for d in decades]

    plt.bar(decade_labels, decade_values, color='coral', edgecolor='black', alpha=0.7)
    plt.xlabel('Decade', fontsize=12)
    plt.ylabel('Games Published', fontsize=12)
    plt.title('TTRPG Publications by Decade', fontsize=14, fontweight='bold')
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.savefig(output_dir / 'games-by-decade.png', dpi=300, bbox_inches='tight')
    print(f"Generated: {output_dir / 'games-by-decade.png'}")
    plt.close()

    # 4. Genre distribution (pie chart)
    plt.figure(figsize=(10, 8))
    top_genres = genre_counts.most_common(8)
    other_count = sum(count for _, count in genre_counts.items() if _ not in dict(top_genres))

    labels = [genre for genre, _ in top_genres]
    sizes = [count for _, count in top_genres]
    if other_count > 0:
        labels.append('Other')
        sizes.append(other_count)

    colors = plt.cm.Set3(range(len(labels)))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    plt.title('Genre Distribution Across All Games', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(output_dir / 'genre-distribution.png', dpi=300, bbox_inches='tight')
    print(f"Generated: {output_dir / 'genre-distribution.png'}")
    plt.close()

    # 5. Significance vs Innovation scatter plot
    plt.figure(figsize=(10, 8))
    significance_scores = [g['significance'] for g in games if g['significance'] > 0]
    innovation_scores = [g['innovation'] for g in games if g['significance'] > 0]

    plt.scatter(significance_scores, innovation_scores, alpha=0.6, s=100, c='purple', edgecolors='black')
    plt.xlabel('Historical Significance (1-5)', fontsize=12)
    plt.ylabel('Innovation Score (1-5)', fontsize=12)
    plt.title('Historical Significance vs. Innovation', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 6)
    plt.ylim(0, 6)

    # Add diagonal reference line
    plt.plot([0, 5], [0, 5], 'k--', alpha=0.3, linewidth=1)

    plt.tight_layout()
    plt.savefig(output_dir / 'significance-vs-innovation.png', dpi=300, bbox_inches='tight')
    print(f"Generated: {output_dir / 'significance-vs-innovation.png'}")
    plt.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Analyze TTRPG publication trends')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output directory for visualizations')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)
    output_dir = Path(args.output) if args.output else vault_path / "Attachments" / "Diagrams" / "analytics"

    print(f"Analyzing vault at: {vault_path}")
    print(f"Output directory: {output_dir}")

    games = load_games(vault_path)
    analyze_publication_trends(games, output_dir)

    print(f"\n{'='*60}")
    print("Analysis complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
