#!/usr/bin/env python3
"""
System Family Tree Generator for TTRPG History Vault

Traces evolution of game systems through influence chains.
Identifies system families (d20, PbtA, FitD, etc.) and visualizes genealogy.

Outputs:
- System family tree diagrams
- Family lineage reports
- System evolution timelines
- CSV data

Requirements:
    pip install networkx matplotlib graphviz

Usage:
    python Scripts/analytics/system_family_tree.py
    python Scripts/analytics/system_family_tree.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

try:
    import networkx as nx
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    print("Warning: networkx and matplotlib not installed.")
    print("Install with: pip install networkx matplotlib")


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
    """Load all game entries with system and influence data."""
    games_folder = vault_path / "Games"
    games = []

    if not games_folder.exists():
        print(f"Games folder not found at {games_folder}")
        return games

    for md_file in games_folder.glob('*.md'):
        frontmatter = extract_frontmatter(md_file)
        if frontmatter.get('type') == 'game':
            # Parse influenced-by relationships
            influenced_by = frontmatter.get('influenced-by', [])
            if not isinstance(influenced_by, list):
                influenced_by = [influenced_by] if influenced_by else []

            influenced_by = [extract_link_title(link) for link in influenced_by if link]

            games.append({
                'title': frontmatter.get('title', md_file.stem),
                'year': frontmatter.get('year-published', 0),
                'system': frontmatter.get('system', 'unknown'),
                'influenced_by': influenced_by,
                'significance': frontmatter.get('historical-significance', 0),
                'innovation': frontmatter.get('innovation-score', 0)
            })

    return games


def categorize_system(system_name):
    """Categorize game into major system families."""
    system_lower = str(system_name).lower()

    if 'd20' in system_lower or 'dnd' in system_lower or 'd&d' in system_lower:
        return 'd20/D&D'
    elif 'pbta' in system_lower or 'apocalypse' in system_lower:
        return 'PbtA'
    elif 'fitd' in system_lower or 'in the dark' in system_lower or 'forged' in system_lower:
        return 'Forged in the Dark'
    elif 'fate' in system_lower or 'fudge' in system_lower:
        return 'Fate/Fudge'
    elif 'storyteller' in system_lower or 'world of darkness' in system_lower or 'wod' in system_lower:
        return 'Storyteller/WoD'
    elif 'percentile' in system_lower or 'brp' in system_lower or 'borp' in system_lower:
        return 'BRP/Percentile'
    elif 'gurps' in system_lower:
        return 'GURPS'
    elif 'custom' in system_lower or 'unique' in system_lower or 'original' in system_lower:
        return 'Custom/Unique'
    else:
        return 'Other'


def identify_system_families(games):
    """Identify major system families and their members."""
    families = defaultdict(list)

    for game in games:
        family = categorize_system(game['system'])
        families[family].append(game)

    return families


def build_family_tree(games, family_name):
    """Build directed graph for a specific system family."""
    # Get games in this family
    family_games = [g for g in games if categorize_system(g['system']) == family_name]

    if not family_games:
        return None

    G = nx.DiGraph()

    # Add nodes
    for game in family_games:
        G.add_node(game['title'],
                   year=game['year'],
                   system=game['system'],
                   significance=game['significance'])

    # Add edges based on influence
    for game in family_games:
        for influence in game['influenced_by']:
            # Check if influence is in the same family
            influence_game = next((g for g in family_games if g['title'] == influence), None)
            if influence_game:
                G.add_edge(influence, game['title'])

    return G


def analyze_system_families(games, output_dir):
    """Analyze system families and lineages."""

    print(f"\n{'='*60}")
    print("SYSTEM FAMILY TREE ANALYSIS")
    print(f"{'='*60}\n")

    families = identify_system_families(games)

    print("System Families Identified:\n")
    for family, members in sorted(families.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"{family}: {len(members)} games")

    # Detailed family analysis
    for family, members in sorted(families.items(), key=lambda x: len(x[1]), reverse=True):
        if len(members) < 2:
            continue

        print(f"\n{'='*60}")
        print(f"{family.upper()} FAMILY")
        print(f"{'='*60}\n")

        # Sort by year
        members.sort(key=lambda g: g['year'])

        print("Chronological Evolution:\n")
        for game in members:
            influences = ", ".join(game['influenced_by']) if game['influenced_by'] else "Original"
            print(f"  {game['year']}: {game['title']}")
            if game['influenced_by']:
                print(f"          ← Influenced by: {influences}")

        # Foundational games
        foundational = [g for g in members if not g['influenced_by'] or
                       all(inf not in [m['title'] for m in members]
                           for inf in g['influenced_by'])]

        if foundational:
            print(f"\n  Foundational Games in Family:")
            for game in foundational:
                print(f"    - {game['title']} ({game['year']})")

        # Most influential within family
        influence_counts = defaultdict(int)
        for game in members:
            for influence in game['influenced_by']:
                if any(m['title'] == influence for m in members):
                    influence_counts[influence] += 1

        if influence_counts:
            print(f"\n  Most Influential Within Family:")
            for game, count in sorted(influence_counts.items(),
                                     key=lambda x: x[1],
                                     reverse=True)[:5]:
                print(f"    - {game}: influenced {count} games in family")

    # Export family data
    csv_path = output_dir / 'system-families.csv'
    with open(csv_path, 'w') as f:
        f.write("Game,Year,System,Family,Influences,InfluencedBy,Significance\n")
        for game in sorted(games, key=lambda g: g['year']):
            family = categorize_system(game['system'])
            influences = ';'.join(game['influenced_by'])
            f.write(f"{game['title']},{game['year']},{game['system']},{family},,{influences},{game['significance']}\n")

    print(f"\n\nFamily data exported to: {csv_path}")

    return families


def visualize_family_trees(games, families, output_dir):
    """Generate family tree visualizations."""

    if not HAS_NETWORKX:
        print("NetworkX not available for visualizations")
        return

    print("\nGenerating family tree visualizations...")

    # Visualize major families
    major_families = {name: members for name, members in families.items()
                     if len(members) >= 3}

    for family_name in major_families:
        G = build_family_tree(games, family_name)

        if not G or G.number_of_nodes() == 0:
            continue

        print(f"Generating tree for {family_name}...")

        fig, ax = plt.subplots(figsize=(16, 12))

        # Use hierarchical layout if possible
        try:
            # Try to use graphviz for tree layout
            pos = nx.nx_agraph.graphviz_layout(G, prog='dot')
        except:
            # Fallback to spring layout
            pos = nx.spring_layout(G, k=2, iterations=50)

        # Node colors by year
        years = [G.nodes[node].get('year', 2000) for node in G.nodes()]
        node_colors = years

        # Node sizes by significance
        node_sizes = [G.nodes[node].get('significance', 3) * 300 for node in G.nodes()]

        # Draw
        nx.draw_networkx_nodes(G, pos,
                              node_size=node_sizes,
                              node_color=node_colors,
                              cmap='viridis',
                              alpha=0.8,
                              edgecolors='black',
                              linewidths=2)

        nx.draw_networkx_edges(G, pos,
                              edge_color='gray',
                              arrows=True,
                              arrowsize=20,
                              arrowstyle='->',
                              width=2,
                              alpha=0.6)

        # Labels
        labels = {node: f"{node}\n({G.nodes[node].get('year', '?')})"
                 for node in G.nodes()}

        nx.draw_networkx_labels(G, pos,
                               labels=labels,
                               font_size=8,
                               font_weight='bold')

        ax.set_title(f'{family_name} System Family Tree\n(Size = Historical Significance | Color = Year)',
                    fontsize=16, fontweight='bold', pad=20)

        # Colorbar
        sm = plt.cm.ScalarMappable(cmap='viridis',
                                   norm=plt.Normalize(vmin=min(years), vmax=max(years)))
        sm.set_array([])
        plt.colorbar(sm, ax=ax, label='Publication Year')

        plt.axis('off')
        plt.tight_layout()

        # Safe filename
        filename = family_name.replace('/', '-').replace(' ', '-').lower()
        output_path = output_dir / f'family-tree-{filename}.png'
        plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
        print(f"Generated: {output_path}")
        plt.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate TTRPG system family trees')
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

    # Analyze families
    families = analyze_system_families(games, output_dir)

    # Generate visualizations
    if HAS_NETWORKX:
        visualize_family_trees(games, families, output_dir)
    else:
        print("\nSkipping visualizations (networkx not installed)")
        print("Install with: pip install networkx matplotlib")

    print(f"\n{'='*60}")
    print("Family tree analysis complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
