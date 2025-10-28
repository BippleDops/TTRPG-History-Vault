#!/usr/bin/env python3
"""
Influence Network Analyzer for TTRPG History Vault

Analyzes the network of influences between games, designers, and systems.
Uses graph theory to identify influential games, bridge games, and communities.

Outputs:
- Influence network diagram (NetworkX visualization)
- PageRank scores (most influential games)
- Betweenness centrality (bridge games between eras/communities)
- Community detection (game families: OSR, PbtA, FitD, etc.)
- CSV data with centrality metrics

Requirements:
    pip install networkx matplotlib pandas

Usage:
    python Scripts/analytics/influence_network.py
    python Scripts/analytics/influence_network.py --output Attachments/Diagrams/analytics/
"""

import os
import re
import yaml
import sys
from pathlib import Path
from collections import defaultdict

try:
    import networkx as nx
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import pandas as pd
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    print("Warning: networkx, matplotlib, and pandas not installed.")
    print("Install with: pip install networkx matplotlib pandas")


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
    # Remove [[ and ]]
    link = wikilink.strip('[]')
    # If there's a |, take the part before it
    if '|' in link:
        link = link.split('|')[0]
    return link.strip()


def load_games(vault_path):
    """Load all game entries with influence relationships."""
    games_folder = vault_path / "Games"
    games = []

    if not games_folder.exists():
        print(f"Games folder not found at {games_folder}")
        return games

    for md_file in games_folder.glob('*.md'):
        frontmatter = extract_frontmatter(md_file)
        if frontmatter.get('type') == 'game':
            # Parse influenced-by and influence-on relationships
            influenced_by = frontmatter.get('influenced-by', [])
            influence_on = frontmatter.get('influence-on', [])

            # Handle both list and single values
            if not isinstance(influenced_by, list):
                influenced_by = [influenced_by] if influenced_by else []
            if not isinstance(influence_on, list):
                influence_on = [influence_on] if influence_on else []

            # Extract titles from wikilinks
            influenced_by = [extract_link_title(link) for link in influenced_by if link]
            influence_on = [extract_link_title(link) for link in influence_on if link]

            games.append({
                'title': frontmatter.get('title', md_file.stem),
                'year': frontmatter.get('year-published', 0),
                'designer': frontmatter.get('designer', 'unknown'),
                'publisher': frontmatter.get('publisher', 'unknown'),
                'system': frontmatter.get('system', 'unknown'),
                'genre': frontmatter.get('genre', []),
                'significance': frontmatter.get('historical-significance', 0),
                'innovation': frontmatter.get('innovation-score', 0),
                'influenced_by': influenced_by,
                'influence_on': influence_on
            })

    return games


def build_influence_graph(games):
    """Build directed graph of game influences."""
    G = nx.DiGraph()

    # Add nodes with attributes
    for game in games:
        G.add_node(game['title'],
                   year=game['year'],
                   significance=game['significance'],
                   innovation=game['innovation'],
                   system=game['system'])

    # Add edges (directed: influenced_by -> this game)
    for game in games:
        for influence in game['influenced_by']:
            if influence:  # Skip empty influences
                # Add edge from influencer to influenced
                G.add_edge(influence, game['title'])

    return G


def analyze_network(G, games, output_dir):
    """Analyze network metrics and generate insights."""

    if len(G.nodes()) == 0:
        print("No games with influence relationships found!")
        return

    print(f"\n{'='*60}")
    print("INFLUENCE NETWORK ANALYSIS")
    print(f"{'='*60}\n")

    print(f"Network Statistics:")
    print(f"  Total Games: {G.number_of_nodes()}")
    print(f"  Total Influence Links: {G.number_of_edges()}")
    print(f"  Network Density: {nx.density(G):.4f}")

    # Check if graph is connected
    if G.number_of_nodes() > 0:
        largest_cc = max(nx.weakly_connected_components(G), key=len)
        print(f"  Largest Connected Component: {len(largest_cc)} games ({len(largest_cc)/G.number_of_nodes()*100:.1f}%)")

    # PageRank - Most Influential Games
    print(f"\n{'='*60}")
    print("MOST INFLUENTIAL GAMES (PageRank)")
    print(f"{'='*60}\n")

    pagerank = nx.pagerank(G)
    top_influential = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:10]

    for i, (game, score) in enumerate(top_influential, 1):
        year = G.nodes[game].get('year', 'Unknown')
        significance = G.nodes[game].get('significance', 0)
        print(f"{i:2d}. {game} ({year})")
        print(f"     PageRank: {score:.4f} | Significance: {significance}/5")

    # Betweenness Centrality - Bridge Games
    print(f"\n{'='*60}")
    print("BRIDGE GAMES (Betweenness Centrality)")
    print(f"{'='*60}\n")
    print("Games that connect different eras or design traditions:\n")

    betweenness = nx.betweenness_centrality(G)
    top_bridges = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:10]

    for i, (game, score) in enumerate(top_bridges, 1):
        if score > 0:  # Only show games with actual bridge role
            year = G.nodes[game].get('year', 'Unknown')
            print(f"{i:2d}. {game} ({year}) - Centrality: {score:.4f}")

    # In-degree and Out-degree
    print(f"\n{'='*60}")
    print("MOST INFLUENTIAL (Out-degree)")
    print(f"{'='*60}\n")
    print("Games that influenced the most other games:\n")

    out_degree = dict(G.out_degree())
    top_influencers = sorted(out_degree.items(), key=lambda x: x[1], reverse=True)[:10]

    for i, (game, count) in enumerate(top_influencers, 1):
        if count > 0:
            year = G.nodes[game].get('year', 'Unknown')
            print(f"{i:2d}. {game} ({year}) - Influenced {count} games")

    print(f"\n{'='*60}")
    print("MOST INFLUENCED (In-degree)")
    print(f"{'='*60}\n")
    print("Games that drew from the most influences:\n")

    in_degree = dict(G.in_degree())
    top_influenced = sorted(in_degree.items(), key=lambda x: x[1], reverse=True)[:10]

    for i, (game, count) in enumerate(top_influenced, 1):
        if count > 0:
            year = G.nodes[game].get('year', 'Unknown')
            print(f"{i:2d}. {game} ({year}) - Drew from {count} influences")

    # Community Detection (if graph is large enough)
    if G.number_of_nodes() > 5:
        print(f"\n{'='*60}")
        print("GAME FAMILIES (Community Detection)")
        print(f"{'='*60}\n")

        # Convert to undirected for community detection
        G_undirected = G.to_undirected()
        try:
            communities = nx.community.greedy_modularity_communities(G_undirected)
            print(f"Detected {len(communities)} game families/communities:\n")

            for i, community in enumerate(communities, 1):
                if len(community) > 1:  # Only show communities with multiple games
                    print(f"Family {i} ({len(community)} games):")
                    for game in sorted(community):
                        year = G.nodes[game].get('year', 'Unknown')
                        print(f"  - {game} ({year})")
                    print()
        except:
            print("Community detection not available for this graph structure")

    # Export metrics to CSV
    csv_path = output_dir / "influence-metrics.csv"
    with open(csv_path, 'w') as f:
        f.write("Game,Year,PageRank,Betweenness,InDegree,OutDegree,Significance,Innovation\n")
        for game in sorted(G.nodes()):
            year = G.nodes[game].get('year', 'Unknown')
            pr = pagerank.get(game, 0)
            bc = betweenness.get(game, 0)
            in_deg = in_degree.get(game, 0)
            out_deg = out_degree.get(game, 0)
            sig = G.nodes[game].get('significance', 0)
            inn = G.nodes[game].get('innovation', 0)
            f.write(f"{game},{year},{pr:.6f},{bc:.6f},{in_deg},{out_deg},{sig},{inn}\n")

    print(f"\nMetrics exported to: {csv_path}")

    return pagerank, betweenness, in_degree, out_degree


def visualize_network(G, pagerank, output_dir):
    """Generate network visualization."""

    if G.number_of_nodes() == 0:
        print("No nodes to visualize")
        return

    print(f"\nGenerating network visualization...")

    # Create figure
    plt.figure(figsize=(20, 16))

    # Use spring layout for positioning
    pos = nx.spring_layout(G, k=2, iterations=50, seed=42)

    # Node sizes based on PageRank
    node_sizes = [pagerank.get(node, 0) * 10000 for node in G.nodes()]

    # Node colors based on year
    years = [G.nodes[node].get('year', 2000) for node in G.nodes()]

    # Draw network
    nx.draw_networkx_nodes(G, pos,
                          node_size=node_sizes,
                          node_color=years,
                          cmap='viridis',
                          alpha=0.7,
                          edgecolors='black',
                          linewidths=1)

    nx.draw_networkx_edges(G, pos,
                          edge_color='gray',
                          alpha=0.3,
                          arrows=True,
                          arrowsize=10,
                          arrowstyle='->',
                          connectionstyle='arc3,rad=0.1')

    # Labels for top influential games only (to avoid clutter)
    top_games = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:15]
    labels = {game: game for game, _ in top_games}

    nx.draw_networkx_labels(G, pos,
                           labels=labels,
                           font_size=8,
                           font_weight='bold')

    plt.title('TTRPG Influence Network\n(Node size = Influence | Color = Publication Year)',
             fontsize=16, fontweight='bold', pad=20)

    # Add colorbar for years
    sm = plt.cm.ScalarMappable(cmap='viridis',
                               norm=plt.Normalize(vmin=min(years), vmax=max(years)))
    sm.set_array([])
    cbar = plt.colorbar(sm, ax=plt.gca(), label='Publication Year')

    plt.axis('off')
    plt.tight_layout()

    output_path = output_dir / 'influence-network.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', facecolor='white')
    print(f"Generated: {output_path}")
    plt.close()


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Analyze TTRPG influence networks')
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

    if not HAS_NETWORKX:
        print("\nERROR: NetworkX is required for influence network analysis")
        print("Install with: pip install networkx matplotlib pandas")
        sys.exit(1)

    # Load games
    games = load_games(vault_path)

    if not games:
        print("No games found!")
        return

    # Build influence graph
    G = build_influence_graph(games)

    # Analyze network
    pagerank, betweenness, in_degree, out_degree = analyze_network(G, games, output_dir)

    # Visualize network
    visualize_network(G, pagerank, output_dir)

    print(f"\n{'='*60}")
    print("Analysis complete!")
    print(f"{'='*60}\n")


if __name__ == '__main__':
    main()
