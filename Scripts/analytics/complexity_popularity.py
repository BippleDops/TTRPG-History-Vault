#!/usr/bin/env python3
"""
Complexity vs Popularity Analyzer for TTRPG History Vault

Analyzes relationship between game complexity and various success metrics.
Tests hypotheses about whether complex or simple games are more influential.

Outputs:
- Scatter plots: complexity vs significance, innovation, influence
- Statistical correlation analysis
- Complexity distribution by era
- CSV data

Requirements:
    pip install matplotlib pandas scipy

Usage:
    python Scripts/analytics/complexity_popularity.py
    python Scripts/analytics/complexity_popularity.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
from pathlib import Path
from collections import Counter

try:
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    from scipy import stats
    HAS_LIBS = True
except ImportError:
    HAS_LIBS = False
    print("Warning: matplotlib, pandas, and scipy not installed.")
    print("Install with: pip install matplotlib pandas scipy")


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
    """Load all game entries with complexity data."""
    games_folder = vault_path / "Games"
    games = []

    if not games_folder.exists():
        print(f"Games folder not found at {games_folder}")
        return games

    for md_file in games_folder.glob('*.md'):
        frontmatter = extract_frontmatter(md_file)
        if frontmatter.get('type') == 'game':
            games.append({
                'title': frontmatter.get('title', md_file.stem),
                'year': frontmatter.get('year-published', 0),
                'complexity': frontmatter.get('complexity', 0),
                'significance': frontmatter.get('historical-significance', 0),
                'innovation': frontmatter.get('innovation-score', 0),
                'system': frontmatter.get('system', 'unknown'),
                'genre': frontmatter.get('genre', [])
            })

    return games


def analyze_complexity_trends(games, output_dir):
    """Analyze complexity patterns and correlations."""

    if not games:
        print("No games data found!")
        return

    print(f"\n{'='*60}")
    print("COMPLEXITY vs POPULARITY ANALYSIS")
    print(f"{'='*60}\n")

    # Filter to games with complexity ratings
    games_with_complexity = [g for g in games if g['complexity'] > 0]

    if not games_with_complexity:
        print("No games with complexity ratings found!")
        return

    print(f"Analyzing {len(games_with_complexity)} games with complexity ratings\n")

    # Complexity distribution
    complexity_dist = Counter(g['complexity'] for g in games_with_complexity)

    print("Complexity Distribution:\n")
    for level in sorted(complexity_dist.keys()):
        count = complexity_dist[level]
        pct = count / len(games_with_complexity) * 100
        bar = '█' * int(pct / 2)
        print(f"  Level {level}: {count:3d} games ({pct:5.1f}%) {bar}")

    # Complexity by era
    print(f"\n{'='*60}")
    print("COMPLEXITY TRENDS OVER TIME")
    print(f"{'='*60}\n")

    games_with_years = [g for g in games_with_complexity if g['year'] > 0]

    if games_with_years:
        decades = {}
        for game in games_with_years:
            decade = (game['year'] // 10) * 10
            if decade not in decades:
                decades[decade] = []
            decades[decade].append(game['complexity'])

        print("Average Complexity by Decade:\n")
        for decade in sorted(decades.keys()):
            avg_complexity = sum(decades[decade]) / len(decades[decade])
            print(f"  {decade}s: {avg_complexity:.2f} (n={len(decades[decade])})")

    # Correlations
    print(f"\n{'='*60}")
    print("CORRELATION ANALYSIS")
    print(f"{'='*60}\n")

    # Complexity vs Significance
    games_sig = [g for g in games_with_complexity if g['significance'] > 0]
    if len(games_sig) > 2:
        complexity_vals = [g['complexity'] for g in games_sig]
        significance_vals = [g['significance'] for g in games_sig]

        if HAS_LIBS:
            corr, p_value = stats.pearsonr(complexity_vals, significance_vals)
            print(f"Complexity vs Historical Significance:")
            print(f"  Pearson correlation: {corr:.3f}")
            print(f"  P-value: {p_value:.4f}")
            print(f"  Interpretation: {'Significant' if p_value < 0.05 else 'Not significant'}")

            if corr > 0.3:
                print(f"  → More complex games tend to be more historically significant")
            elif corr < -0.3:
                print(f"  → Simpler games tend to be more historically significant")
            else:
                print(f"  → No strong relationship")
        print()

    # Complexity vs Innovation
    games_inn = [g for g in games_with_complexity if g['innovation'] > 0]
    if len(games_inn) > 2:
        complexity_vals = [g['complexity'] for g in games_inn]
        innovation_vals = [g['innovation'] for g in games_inn]

        if HAS_LIBS:
            corr, p_value = stats.pearsonr(complexity_vals, innovation_vals)
            print(f"Complexity vs Innovation:")
            print(f"  Pearson correlation: {corr:.3f}")
            print(f"  P-value: {p_value:.4f}")
            print(f"  Interpretation: {'Significant' if p_value < 0.05 else 'Not significant'}")

            if corr > 0.3:
                print(f"  → More complex games tend to be more innovative")
            elif corr < -0.3:
                print(f"  → Simpler games tend to be more innovative")
            else:
                print(f"  → No strong relationship")
        print()

    # System complexity patterns
    print(f"\n{'='*60}")
    print("COMPLEXITY BY SYSTEM TYPE")
    print(f"{'='*60}\n")

    system_complexity = {}
    for game in games_with_complexity:
        system = game['system']
        if system not in system_complexity:
            system_complexity[system] = []
        system_complexity[system].append(game['complexity'])

    # Only show systems with 2+ games
    system_avg = {system: sum(vals) / len(vals)
                 for system, vals in system_complexity.items()
                 if len(vals) >= 2}

    if system_avg:
        print("Average Complexity by System (2+ games):\n")
        for system, avg in sorted(system_avg.items(), key=lambda x: x[1], reverse=True):
            count = len(system_complexity[system])
            print(f"  {system}: {avg:.2f} (n={count})")

    # Export CSV
    csv_path = output_dir / 'complexity-data.csv'
    with open(csv_path, 'w') as f:
        f.write("Title,Year,Complexity,Significance,Innovation,System\n")
        for game in sorted(games_with_complexity, key=lambda g: g['year']):
            f.write(f"{game['title']},{game['year']},{game['complexity']},{game['significance']},{game['innovation']},{game['system']}\n")

    print(f"\n\nData exported to: {csv_path}")

    return games_with_complexity


def visualize_complexity(games, output_dir):
    """Generate complexity visualizations."""

    if not HAS_LIBS:
        print("Visualization libraries not available")
        return

    print("\nGenerating complexity visualizations...")

    games_with_data = [g for g in games
                       if g['complexity'] > 0 and g['significance'] > 0 and g['innovation'] > 0]

    if not games_with_data:
        print("Insufficient data for visualizations")
        return

    # 1. Complexity vs Significance scatter
    fig, ax = plt.subplots(figsize=(10, 8))

    x = [g['complexity'] for g in games_with_data]
    y = [g['significance'] for g in games_with_data]

    ax.scatter(x, y, alpha=0.6, s=100, c='steelblue', edgecolors='black', linewidths=1)

    # Add trend line
    if len(x) > 2:
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        ax.plot(sorted(set(x)), p(sorted(set(x))), "r--", alpha=0.8, linewidth=2, label='Trend')

    ax.set_xlabel('Complexity (1-5)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Historical Significance (1-5)', fontsize=12, fontweight='bold')
    ax.set_title('Complexity vs Historical Significance', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.legend()

    plt.tight_layout()
    output_path = output_dir / 'complexity-vs-significance.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Generated: {output_path}")
    plt.close()

    # 2. Complexity vs Innovation scatter
    fig, ax = plt.subplots(figsize=(10, 8))

    x = [g['complexity'] for g in games_with_data]
    y = [g['innovation'] for g in games_with_data]

    ax.scatter(x, y, alpha=0.6, s=100, c='coral', edgecolors='black', linewidths=1)

    # Add trend line
    if len(x) > 2:
        z = np.polyfit(x, y, 1)
        p = np.poly1d(z)
        ax.plot(sorted(set(x)), p(sorted(set(x))), "r--", alpha=0.8, linewidth=2, label='Trend')

    ax.set_xlabel('Complexity (1-5)', fontsize=12, fontweight='bold')
    ax.set_ylabel('Innovation Score (1-5)', fontsize=12, fontweight='bold')
    ax.set_title('Complexity vs Innovation', fontsize=14, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.legend()

    plt.tight_layout()
    output_path = output_dir / 'complexity-vs-innovation.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    print(f"Generated: {output_path}")
    plt.close()

    # 3. Complexity distribution over time
    games_with_years = [g for g in games if g['complexity'] > 0 and g['year'] > 0]

    if games_with_years:
        fig, ax = plt.subplots(figsize=(14, 6))

        df = pd.DataFrame(games_with_years)
        df['decade'] = (df['year'] // 10) * 10

        decade_complexity = df.groupby('decade')['complexity'].mean()

        ax.plot(decade_complexity.index, decade_complexity.values,
               marker='o', linewidth=2, markersize=8, color='darkgreen')

        ax.set_xlabel('Decade', fontsize=12, fontweight='bold')
        ax.set_ylabel('Average Complexity', fontsize=12, fontweight='bold')
        ax.set_title('Game Complexity Trends Over Time', fontsize=14, fontweight='bold', pad=20)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 5)

        plt.tight_layout()
        output_path = output_dir / 'complexity-trends.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        print(f"Generated: {output_path}")
        plt.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Analyze TTRPG complexity vs popularity')
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

    # Analyze complexity trends
    games_with_complexity = analyze_complexity_trends(games, output_dir)

    # Generate visualizations
    if HAS_LIBS and games_with_complexity:
        try:
            import numpy as np
            globals()['np'] = np
            visualize_complexity(games_with_complexity, output_dir)
        except Exception as e:
            print(f"Visualization error: {e}")
    else:
        print("\nSkipping visualizations (libraries not installed)")
        print("Install with: pip install matplotlib pandas scipy")

    print(f"\n{'='*60}")
    print("Complexity analysis complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
