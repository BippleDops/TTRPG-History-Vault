#!/usr/bin/env python3
"""
Innovation Timeline Visualizer for TTRPG History Vault

Creates interactive and static timeline visualizations showing major innovations
in TTRPG history, sized by historical significance and colored by system type.

Outputs:
- Interactive HTML timeline (plotly)
- Static timeline image (matplotlib)
- Innovation events CSV

Requirements:
    pip install plotly pandas matplotlib

Usage:
    python Scripts/analytics/innovation_timeline.py
    python Scripts/analytics/innovation_timeline.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
import sys
from pathlib import Path
from collections import defaultdict

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False

try:
    import plotly.graph_objects as go
    import plotly.express as px
    HAS_PLOTLY = True
except ImportError:
    HAS_PLOTLY = False
    print("Warning: plotly not installed. Install with: pip install plotly")


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
    """Load all game entries with innovation data."""
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
                'significance': frontmatter.get('historical-significance', 0),
                'innovation': frontmatter.get('innovation-score', 0),
                'designer': frontmatter.get('designer', 'unknown'),
                'publisher': frontmatter.get('publisher', 'unknown')
            })

    return games


def categorize_system(system_name):
    """Categorize system into broad types for color coding."""
    system_lower = str(system_name).lower()

    if 'd20' in system_lower or 'dnd' in system_lower or 'd&d' in system_lower:
        return 'd20/D&D Family'
    elif 'percentile' in system_lower or 'borp' in system_lower or 'brp' in system_lower:
        return 'Percentile/BRP'
    elif 'pbta' in system_lower or 'apocalypse' in system_lower:
        return 'PbtA'
    elif 'fitd' in system_lower or 'in the dark' in system_lower:
        return 'Forged in the Dark'
    elif 'fate' in system_lower or 'fudge' in system_lower:
        return 'Fate/Fudge'
    elif 'storyteller' in system_lower or 'world of darkness' in system_lower:
        return 'Storyteller'
    elif 'gurps' in system_lower or 'universal' in system_lower:
        return 'Universal Systems'
    elif 'custom' in system_lower or 'unique' in system_lower:
        return 'Custom/Unique'
    else:
        return 'Other'


def generate_static_timeline(games, output_dir):
    """Generate static matplotlib timeline."""

    if not games:
        print("No games to visualize")
        return

    print("Generating static timeline...")

    # Prepare data
    df = pd.DataFrame(games)
    df['system_category'] = df['system'].apply(categorize_system)

    # Filter to significant/innovative games only
    df_significant = df[(df['significance'] >= 3) | (df['innovation'] >= 3)].copy()

    if len(df_significant) == 0:
        print("No highly significant games found")
        return

    # Create figure
    fig, ax = plt.subplots(figsize=(20, 12))

    # Color mapping
    categories = df_significant['system_category'].unique()
    colors = plt.cm.Set3(range(len(categories)))
    color_map = dict(zip(categories, colors))

    # Plot points
    for category in categories:
        df_cat = df_significant[df_significant['system_category'] == category]

        ax.scatter(df_cat['year'],
                  df_cat['innovation'],
                  s=df_cat['significance'] * 200,
                  c=[color_map[category]],
                  alpha=0.6,
                  edgecolors='black',
                  linewidth=1.5,
                  label=category)

    # Annotate major innovations (significance >= 4 or innovation >= 4)
    df_major = df_significant[(df_significant['significance'] >= 4) |
                              (df_significant['innovation'] >= 4)]

    for _, game in df_major.iterrows():
        ax.annotate(game['title'],
                   xy=(game['year'], game['innovation']),
                   xytext=(5, 5),
                   textcoords='offset points',
                   fontsize=8,
                   fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.3',
                           facecolor='white',
                           edgecolor='gray',
                           alpha=0.7))

    # Formatting
    ax.set_xlabel('Year', fontsize=14, fontweight='bold')
    ax.set_ylabel('Innovation Score', fontsize=14, fontweight='bold')
    ax.set_title('TTRPG Innovation Timeline\n(Bubble size = Historical Significance)',
                fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

    # Set y-axis limits
    ax.set_ylim(0, 6)

    plt.tight_layout()

    output_path = output_dir / 'innovation-timeline-static.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Generated: {output_path}")
    plt.close()


def generate_interactive_timeline(games, output_dir):
    """Generate interactive plotly timeline."""

    if not HAS_PLOTLY:
        print("Plotly not installed, skipping interactive timeline")
        return

    print("Generating interactive timeline...")

    # Prepare data
    df = pd.DataFrame(games)
    df['system_category'] = df['system'].apply(categorize_system)

    # Filter to significant games
    df_significant = df[(df['significance'] >= 2) | (df['innovation'] >= 2)].copy()

    if len(df_significant) == 0:
        print("No significant games found")
        return

    # Create interactive scatter plot
    fig = px.scatter(df_significant,
                    x='year',
                    y='innovation',
                    size='significance',
                    color='system_category',
                    hover_name='title',
                    hover_data={
                        'year': True,
                        'innovation': True,
                        'significance': True,
                        'designer': True,
                        'system_category': False
                    },
                    title='Interactive TTRPG Innovation Timeline',
                    labels={
                        'year': 'Publication Year',
                        'innovation': 'Innovation Score',
                        'significance': 'Historical Significance',
                        'system_category': 'System Type'
                    },
                    size_max=40)

    # Update layout
    fig.update_layout(
        height=800,
        hovermode='closest',
        plot_bgcolor='white',
        font=dict(size=12),
        title_font_size=18,
        xaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='lightgray',
            zeroline=False,
            range=[0, 6]
        )
    )

    # Update traces
    fig.update_traces(
        marker=dict(
            line=dict(width=1, color='DarkSlateGray'),
            opacity=0.7
        )
    )

    # Save as HTML
    output_path = output_dir / 'innovation-timeline-interactive.html'
    fig.write_html(str(output_path))
    print(f"Generated: {output_path}")


def export_timeline_data(games, output_dir):
    """Export timeline data as CSV."""

    csv_path = output_dir / 'innovation-timeline-data.csv'

    df = pd.DataFrame(games)
    df['system_category'] = df['system'].apply(categorize_system)

    # Sort by year
    df = df.sort_values('year')

    # Select columns
    df_export = df[['title', 'year', 'system', 'system_category',
                   'significance', 'innovation', 'designer', 'publisher']]

    # Export
    df_export.to_csv(csv_path, index=False)
    print(f"Data exported to: {csv_path}")


def print_timeline_analysis(games):
    """Print text-based timeline analysis."""

    print(f"\n{'='*60}")
    print("INNOVATION TIMELINE ANALYSIS")
    print(f"{'='*60}\n")

    df = pd.DataFrame(games)

    # Decade analysis
    df['decade'] = (df['year'] // 10) * 10

    print("Major Innovations by Decade:\n")

    for decade in sorted(df['decade'].unique()):
        df_decade = df[df['decade'] == decade]
        df_significant = df_decade[(df_decade['significance'] >= 4) |
                                   (df_decade['innovation'] >= 4)]

        if len(df_significant) > 0:
            print(f"{decade}s:")
            for _, game in df_significant.sort_values('year').iterrows():
                print(f"  {game['year']}: {game['title']}")
                print(f"         Significance: {game['significance']}/5, Innovation: {game['innovation']}/5")
            print()

    # Most innovative games overall
    print(f"{'='*60}")
    print("MOST INNOVATIVE GAMES (Innovation Score >= 4)")
    print(f"{'='*60}\n")

    df_innovative = df[df['innovation'] >= 4].sort_values('innovation', ascending=False)

    for i, (_, game) in enumerate(df_innovative.iterrows(), 1):
        print(f"{i:2d}. {game['title']} ({game['year']})")
        print(f"     Innovation: {game['innovation']}/5 | Significance: {game['significance']}/5")
        print(f"     System: {game['system']}")
        print()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate TTRPG innovation timeline')
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

    # Print analysis
    print_timeline_analysis(games)

    # Generate visualizations
    if HAS_MATPLOTLIB:
        generate_static_timeline(games, output_dir)

    if HAS_PLOTLY:
        generate_interactive_timeline(games, output_dir)

    # Export data
    if HAS_MATPLOTLIB:  # pandas available
        export_timeline_data(games, output_dir)

    print(f"\n{'='*60}")
    print("Timeline generation complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
