#!/usr/bin/env python3
"""
Designer Contribution Matrix for TTRPG History Vault

Analyzes designer contributions across games, systems, and innovations.
Creates matrix visualizations and rankings.

Outputs:
- Designer-Game matrix heatmap
- Designer contribution rankings
- Designer specialization analysis (genres, systems, eras)
- CSV data for further analysis

Requirements:
    pip install matplotlib pandas seaborn

Usage:
    python Scripts/analytics/designer_matrix.py
    python Scripts/analytics/designer_matrix.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
import sys
from pathlib import Path
from collections import defaultdict, Counter

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns
    HAS_LIBS = True
except ImportError:
    HAS_LIBS = False
    print("Warning: matplotlib, pandas, and seaborn not installed.")
    print("Install with: pip install matplotlib pandas seaborn")


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


def extract_link_title(wikilink):
    """Extract title from [[Title]] or [[Title|Display]] format."""
    if not wikilink:
        return None
    link = wikilink.strip('[]')
    if '|' in link:
        link = link.split('|')[0]
    return link.strip()


def load_games(vault_path):
    """Load all game entries with designer information."""
    games_folder = vault_path / "Games"
    games = []

    if not games_folder.exists():
        print(f"Games folder not found at {games_folder}")
        return games

    for md_file in games_folder.glob('*.md'):
        frontmatter = extract_frontmatter(md_file)
        if frontmatter.get('type') == 'game':
            # Parse designer (can be string or list)
            designers = frontmatter.get('designer', [])
            if not isinstance(designers, list):
                designers = [designers] if designers else []

            # Extract from wikilinks if present
            designers = [extract_link_title(d) if isinstance(d, str) and '[[' in d else d
                        for d in designers if d]

            games.append({
                'title': frontmatter.get('title', md_file.stem),
                'year': frontmatter.get('year-published', 0),
                'designers': designers,
                'system': frontmatter.get('system', 'unknown'),
                'genre': frontmatter.get('genre', []),
                'significance': frontmatter.get('historical-significance', 0),
                'innovation': frontmatter.get('innovation-score', 0),
                'publisher': frontmatter.get('publisher', 'unknown')
            })

    return games


def analyze_designers(games, output_dir):
    """Analyze designer contributions and patterns."""

    if not games:
        print("No games data found!")
        return

    print(f"\n{'='*60}")
    print("DESIGNER CONTRIBUTION ANALYSIS")
    print(f"{'='*60}\n")

    # Build designer-game mapping
    designer_games = defaultdict(list)
    designer_systems = defaultdict(set)
    designer_genres = defaultdict(Counter)
    designer_decades = defaultdict(Counter)
    designer_significance = defaultdict(list)
    designer_innovation = defaultdict(list)

    for game in games:
        for designer in game['designers']:
            if designer and designer != 'unknown':
                designer_games[designer].append(game['title'])
                designer_systems[designer].add(game['system'])

                # Track genres
                genres = game['genre'] if isinstance(game['genre'], list) else [game['genre']]
                for genre in genres:
                    if genre:
                        designer_genres[designer][genre] += 1

                # Track decades
                if game['year'] > 0:
                    decade = (game['year'] // 10) * 10
                    designer_decades[designer][decade] += 1

                # Track scores
                if game['significance'] > 0:
                    designer_significance[designer].append(game['significance'])
                if game['innovation'] > 0:
                    designer_innovation[designer].append(game['innovation'])

    # Calculate metrics
    designer_metrics = []
    for designer in designer_games:
        game_count = len(designer_games[designer])
        system_count = len(designer_systems[designer])

        avg_significance = sum(designer_significance[designer]) / len(designer_significance[designer]) if designer_significance[designer] else 0
        avg_innovation = sum(designer_innovation[designer]) / len(designer_innovation[designer]) if designer_innovation[designer] else 0

        max_significance = max(designer_significance[designer]) if designer_significance[designer] else 0
        max_innovation = max(designer_innovation[designer]) if designer_innovation[designer] else 0

        # Primary genre
        primary_genre = designer_genres[designer].most_common(1)[0][0] if designer_genres[designer] else 'unknown'

        # Active decades
        active_decades = len(designer_decades[designer])

        designer_metrics.append({
            'designer': designer,
            'game_count': game_count,
            'system_count': system_count,
            'avg_significance': avg_significance,
            'avg_innovation': avg_innovation,
            'max_significance': max_significance,
            'max_innovation': max_innovation,
            'primary_genre': primary_genre,
            'active_decades': active_decades
        })

    # Sort by game count
    designer_metrics.sort(key=lambda x: x['game_count'], reverse=True)

    # Print top designers
    print("Most Prolific Designers (by game count):\n")
    for i, dm in enumerate(designer_metrics[:15], 1):
        print(f"{i:2d}. {dm['designer']}")
        print(f"     Games: {dm['game_count']} | Systems: {dm['system_count']} | Decades Active: {dm['active_decades']}")
        print(f"     Avg Significance: {dm['avg_significance']:.2f}/5 | Avg Innovation: {dm['avg_innovation']:.2f}/5")
        print(f"     Primary Genre: {dm['primary_genre']}")
        print()

    # Most significant designers (by average significance)
    print(f"\n{'='*60}")
    print("Most Impactful Designers (by avg historical significance)")
    print(f"{'='*60}\n")

    designer_metrics_sig = sorted(designer_metrics,
                                  key=lambda x: x['avg_significance'],
                                  reverse=True)

    for i, dm in enumerate(designer_metrics_sig[:10], 1):
        if dm['avg_significance'] > 0:
            print(f"{i:2d}. {dm['designer']}")
            print(f"     Avg Significance: {dm['avg_significance']:.2f}/5 (max: {dm['max_significance']})")
            print(f"     Games: {dm['game_count']} | Systems: {dm['system_count']}")
            print()

    # Most innovative designers
    print(f"\n{'='*60}")
    print("Most Innovative Designers (by avg innovation score)")
    print(f"{'='*60}\n")

    designer_metrics_inn = sorted(designer_metrics,
                                  key=lambda x: x['avg_innovation'],
                                  reverse=True)

    for i, dm in enumerate(designer_metrics_inn[:10], 1):
        if dm['avg_innovation'] > 0:
            print(f"{i:2d}. {dm['designer']}")
            print(f"     Avg Innovation: {dm['avg_innovation']:.2f}/5 (max: {dm['max_innovation']})")
            print(f"     Games: {dm['game_count']} | Systems: {dm['system_count']}")
            print()

    # Genre specialists
    print(f"\n{'='*60}")
    print("Genre Specialists")
    print(f"{'='*60}\n")

    genre_map = defaultdict(list)
    for dm in designer_metrics:
        if dm['game_count'] >= 2:  # Only designers with multiple games
            genre_map[dm['primary_genre']].append(dm['designer'])

    for genre in sorted(genre_map.keys()):
        if genre != 'unknown' and len(genre_map[genre]) > 0:
            print(f"{genre.title()}: {', '.join(genre_map[genre][:5])}")

    # Export CSV
    csv_path = output_dir / 'designer-metrics.csv'
    with open(csv_path, 'w') as f:
        f.write("Designer,GameCount,SystemCount,AvgSignificance,AvgInnovation,MaxSignificance,MaxInnovation,PrimaryGenre,ActiveDecades\n")
        for dm in designer_metrics:
            f.write(f"{dm['designer']},{dm['game_count']},{dm['system_count']},{dm['avg_significance']:.2f},{dm['avg_innovation']:.2f},{dm['max_significance']},{dm['max_innovation']},{dm['primary_genre']},{dm['active_decades']}\n")

    print(f"\n\nData exported to: {csv_path}")

    return designer_metrics, designer_games


def visualize_designer_matrix(designer_metrics, designer_games, output_dir):
    """Create visual designer contribution matrix."""

    if not HAS_LIBS:
        print("Visualization libraries not available")
        return

    print("\nGenerating designer contribution visualizations...")

    # Top designers bar chart
    fig, ax = plt.subplots(figsize=(12, 8))

    top_designers = designer_metrics[:15]
    names = [dm['designer'] for dm in top_designers]
    game_counts = [dm['game_count'] for dm in top_designers]
    avg_sigs = [dm['avg_significance'] for dm in top_designers]

    # Create bars colored by average significance
    bars = ax.barh(names, game_counts, color=plt.cm.RdYlGn(
        [sig / 5.0 for sig in avg_sigs]))

    ax.set_xlabel('Number of Games', fontsize=12, fontweight='bold')
    ax.set_ylabel('Designer', fontsize=12, fontweight='bold')
    ax.set_title('Top 15 Most Prolific TTRPG Designers\n(Color = Avg Historical Significance)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(axis='x', alpha=0.3)

    # Add value labels
    for i, (bar, count) in enumerate(zip(bars, game_counts)):
        ax.text(count + 0.1, bar.get_y() + bar.get_height()/2,
               str(count),
               va='center', fontsize=9)

    plt.tight_layout()
    output_path = output_dir / 'designer-game-counts.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Generated: {output_path}")
    plt.close()

    # Significance vs Innovation scatter
    fig, ax = plt.subplots(figsize=(12, 10))

    designers_with_scores = [dm for dm in designer_metrics
                             if dm['avg_significance'] > 0 and dm['avg_innovation'] > 0]

    x = [dm['avg_significance'] for dm in designers_with_scores]
    y = [dm['avg_innovation'] for dm in designers_with_scores]
    sizes = [dm['game_count'] * 50 for dm in designers_with_scores]

    ax.scatter(x, y, s=sizes, alpha=0.6, c='purple', edgecolors='black', linewidths=1)

    # Label top designers
    top_to_label = sorted(designers_with_scores,
                         key=lambda x: x['game_count'],
                         reverse=True)[:10]

    for dm in top_to_label:
        ax.annotate(dm['designer'],
                   xy=(dm['avg_significance'], dm['avg_innovation']),
                   xytext=(5, 5),
                   textcoords='offset points',
                   fontsize=8,
                   bbox=dict(boxstyle='round,pad=0.3',
                           facecolor='white',
                           edgecolor='gray',
                           alpha=0.7))

    ax.set_xlabel('Average Historical Significance', fontsize=12, fontweight='bold')
    ax.set_ylabel('Average Innovation Score', fontsize=12, fontweight='bold')
    ax.set_title('Designer Impact Matrix\n(Bubble size = Number of Games)',
                fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 5.5)
    ax.set_ylim(0, 5.5)

    # Diagonal reference line
    ax.plot([0, 5], [0, 5], 'k--', alpha=0.3, linewidth=1)

    plt.tight_layout()
    output_path = output_dir / 'designer-impact-matrix.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Generated: {output_path}")
    plt.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Analyze TTRPG designer contributions')
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

    # Analyze designers
    designer_metrics, designer_games = analyze_designers(games, output_dir)

    # Generate visualizations
    if HAS_LIBS:
        visualize_designer_matrix(designer_metrics, designer_games, output_dir)
    else:
        print("\nSkipping visualizations (matplotlib/pandas/seaborn not installed)")
        print("Install with: pip install matplotlib pandas seaborn")

    print(f"\n{'='*60}")
    print("Designer analysis complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
