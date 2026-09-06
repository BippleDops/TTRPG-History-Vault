---
aliases:
  - "Analytics Dashboard"
type: moc
title: Analytics Dashboard
category: analytics
status: active
last-updated: 2025-01-XX
tags:
  - analytics
  - data-visualization
  - insights
  - statistics
---

# Analytics Dashboard

**Purpose**: Central hub for data-driven insights into TTRPG history

This dashboard aggregates analytics from across the vault, providing quantitative insights into publication trends, influence networks, designer contributions, and historical patterns.

---

## Quick Stats

```datacore
TABLE WITHOUT ID
  "**Metric**" AS "",
  "**Value**" AS ""
FROM ""
WHERE type = "game"
LIMIT 1
FLATTEN [
  {Metric: "Total Games", Value: length(rows)},
  {Metric: "Year Range", Value: min(rows.year-published) + " - " + max(rows.year-published)},
  {Metric: "Average Significance", Value: round(average(rows.historical-significance), 2)},
  {Metric: "Average Innovation", Value: round(average(rows.innovation-score), 2)}
] AS row
```

---

## Analytics Scripts

Run these Python scripts from the vault root to generate visualizations and data exports:

### 1. Publication Trends

**Script**: `Scripts/analytics/publication_trends.py`

```bash
python Scripts/analytics/publication_trends.py
```

**Analyzes**:
- Games published per year (1974-2024)
- Cumulative game count over time
- Publication patterns by decade
- Genre distribution across all games
- Historical significance vs innovation correlation

**Outputs**:
- `games-per-year.png` - Bar chart of annual publications
- `cumulative-games.png` - Growth curve over time
- `games-by-decade.png` - Decade-level aggregation
- `genre-distribution.png` - Pie chart of genres
- `significance-vs-innovation.png` - Scatter plot analysis
- `publication-data.csv` - Raw data export

### 2. Influence Network

**Script**: `Scripts/analytics/influence_network.py`

```bash
python Scripts/analytics/influence_network.py
```

**Analyzes**:
- PageRank scores (most influential games)
- Betweenness centrality (bridge games)
- Community detection (OSR, PbtA, FitD families)
- In-degree and out-degree influence metrics

**Outputs**:
- `influence-network.png` - Network diagram visualization
- `influence-metrics.csv` - Centrality scores for all games

**Key Insights**:
- Which games influenced the most others?
- Which games are "bridges" between design traditions?
- What design communities/families exist?

### 3. Innovation Timeline

**Script**: `Scripts/analytics/innovation_timeline.py`

```bash
python Scripts/analytics/innovation_timeline.py
```

**Analyzes**:
- Major innovations plotted over time
- Innovation score trends by decade
- Relationship between year and innovation

**Outputs**:
- `innovation-timeline-static.png` - Static matplotlib timeline
- `innovation-timeline-interactive.html` - Interactive plotly visualization
- `innovation-timeline-data.csv` - Timeline data export

**Usage**: Embed the interactive HTML in presentations or export static image for print.

### 4. Designer Contribution Matrix

**Script**: `Scripts/analytics/designer_matrix.py`

```bash
python Scripts/analytics/designer_matrix.py
```

**Analyzes**:
- Most prolific designers (by game count)
- Most impactful designers (by avg significance)
- Most innovative designers (by avg innovation)
- Designer specializations (genres, systems, eras)

**Outputs**:
- `designer-game-counts.png` - Top 15 designers bar chart
- `designer-impact-matrix.png` - Significance vs innovation scatter
- `designer-metrics.csv` - Complete designer statistics

### 5. Coverage Gaps

**Script**: `Scripts/analytics/coverage_gaps.py`

```bash
python Scripts/analytics/coverage_gaps.py
```

**Analyzes**:
- Broken wikilinks (missing entries)
- Temporal gaps in historical coverage
- Underrepresented genres and systems
- Essential games not yet documented

**Outputs**:
- `coverage-gaps.csv` - Prioritized list of entries to create

**Purpose**: Guides v3.0 expansion efforts by identifying high-priority missing content.

### 6. Complexity vs Popularity

**Script**: `Scripts/analytics/complexity_popularity.py`

```bash
python Scripts/analytics/complexity_popularity.py
```

**Analyzes**:
- Correlation between complexity and historical significance
- Correlation between complexity and innovation
- Complexity trends over time
- System-specific complexity patterns

**Outputs**:
- `complexity-vs-significance.png` - Scatter plot with trend line
- `complexity-vs-innovation.png` - Scatter plot with trend line
- `complexity-trends.png` - Evolution over decades
- `complexity-data.csv` - Raw complexity metrics

**Research Questions**:
- Are simpler games more influential?
- Has TTRPG complexity increased or decreased over time?
- Do different system families have characteristic complexity levels?

### 7. System Family Tree

**Script**: `Scripts/analytics/system_family_tree.py`

```bash
python Scripts/analytics/system_family_tree.py
```

**Analyzes**:
- System families (d20, PbtA, FitD, BRP, Storyteller, etc.)
- Evolutionary lineages within families
- Foundational games vs derivatives
- Cross-family influence patterns

**Outputs**:
- `family-tree-{family}.png` - Visual tree for each major family
- `system-families.csv` - Family membership data

**Families Identified**:
- d20/D&D lineage
- Powered by the Apocalypse (PbtA)
- Forged in the Dark (FitD)
- Basic Roleplaying (BRP/percentile)
- Storyteller/World of Darkness
- GURPS and universal systems
- Fate/Fudge family

### 8. Era Comparison

**Script**: `Scripts/analytics/era_comparison.py`

```bash
python Scripts/analytics/era_comparison.py
```

**Analyzes**:
- Design trends across historical eras
- Complexity evolution
- Genre popularity shifts
- Innovation patterns by era

**Outputs**:
- `era-game-counts.png` - Games published per era
- `era-complexity-trend.png` - Complexity evolution line graph
- `era-comparison.csv` - Comparative statistics

**Eras Defined**:
1. Pre-D&D (before 1974)
2. Golden Age (1974-1979)
3. TSR Dominance (1980-1989)
4. Diverse 90s (1990-1999)
5. d20 Era (2000-2007)
6. 4E & Pathfinder (2008-2011)
7. 5E Renaissance (2012-2019)
8. Modern Era (2020+)

---

## Running All Analytics

To generate all visualizations and data exports at once:

```bash
cd "/Users/jonsussmanstudio/Desktop/Code Demonstrator For Karl/TTRPG-History-Vault"

python Scripts/analytics/publication_trends.py
python Scripts/analytics/influence_network.py
python Scripts/analytics/innovation_timeline.py
python Scripts/analytics/designer_matrix.py
python Scripts/analytics/coverage_gaps.py
python Scripts/analytics/complexity_popularity.py
python Scripts/analytics/system_family_tree.py
python Scripts/analytics/era_comparison.py
```

Or create a run-all script:

```bash
#!/bin/bash
for script in Scripts/analytics/*.py; do
    echo "Running $script..."
    python "$script"
    echo "---"
done
```

---

## Generated Visualizations

All visualizations are saved to: `Attachments/Diagrams/analytics/`

### Publication Trends
![Games Per Year](../Attachments/Diagrams/analytics/games-per-year.png)
![Cumulative Games](../Attachments/Diagrams/analytics/cumulative-games.png)
![Games by Decade](../Attachments/Diagrams/analytics/games-by-decade.png)

### Influence & Impact
![Influence Network](../Attachments/Diagrams/analytics/influence-network.png)
![Designer Impact Matrix](../Attachments/Diagrams/analytics/designer-impact-matrix.png)

### Innovation & Complexity
![Innovation Timeline](../Attachments/Diagrams/analytics/innovation-timeline-static.png)
![Complexity vs Significance](../Attachments/Diagrams/analytics/complexity-vs-significance.png)

### System Families
![d20 Family Tree](../Attachments/Diagrams/analytics/family-tree-d20-dnd.png)
![PbtA Family Tree](../Attachments/Diagrams/analytics/family-tree-pbta.png)

### Era Comparisons
![Era Game Counts](../Attachments/Diagrams/analytics/era-game-counts.png)
![Era Complexity Trend](../Attachments/Diagrams/analytics/era-complexity-trend.png)

---

## Data Exports

All CSV exports available in: `Attachments/Diagrams/analytics/`

- `publication-data.csv` - Complete game publication dataset
- `influence-metrics.csv` - Network centrality scores
- `designer-metrics.csv` - Designer contribution statistics
- `coverage-gaps.csv` - Missing entries prioritization
- `complexity-data.csv` - Complexity analysis dataset
- `system-families.csv` - System family membership
- `era-comparison.csv` - Era-level comparative statistics
- `innovation-timeline-data.csv` - Innovation events timeline

---

## Key Insights

### Most Influential Games (PageRank)

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  historical-significance AS "Significance"
FROM "Games"
WHERE historical-significance >= 4
SORT historical-significance DESC, year-published ASC
LIMIT 10
```

### Most Innovative Games

```datacore
TABLE WITHOUT ID
  file.link AS "Game",
  year-published AS "Year",
  innovation-score AS "Innovation"
FROM "Games"
WHERE innovation-score >= 4
SORT innovation-score DESC, year-published ASC
LIMIT 10
```

### Publication Volume by Decade

```datacore
TABLE WITHOUT ID
  decade AS "Decade",
  count AS "Games Published"
FROM "Games"
WHERE year-published > 0
FLATTEN floor(year-published / 10) * 10 AS decade
GROUP BY decade
SORT decade ASC
```

### Most Prolific Designers

```datacore
TABLE WITHOUT ID
  designer AS "Designer",
  count AS "Games"
FROM "Games"
WHERE designer != null AND designer != "unknown"
FLATTEN designer
GROUP BY designer
SORT count DESC
LIMIT 15
```

---

## Research Applications

This analytics suite supports:

### Academic Research
- Quantitative analysis of TTRPG history
- Citation-ready data exports
- Reproducible methodology

### Market Analysis
- Publisher trend identification
- Genre popularity tracking
- Innovation pattern recognition

### Educational Use
- Visual aids for teaching TTRPG history
- Data-driven storytelling
- Student research projects

### Community Insights
- Identify underrepresented areas
- Track OSR, indie, and mainstream trends
- Inform preservation priorities

---

## Requirements

Install Python dependencies:

```bash
pip install pyyaml matplotlib pandas networkx scipy plotly seaborn
```

**Optional** (for enhanced family tree layouts):
```bash
pip install pygraphviz
```

---

## Contributing New Analytics

To add new analytics scripts:

1. Create script in `Scripts/analytics/`
2. Follow naming convention: `{analysis_name}.py`
3. Include docstring with purpose and outputs
4. Export visualizations to `Attachments/Diagrams/analytics/`
5. Export data to same directory as CSV
6. Add section to this dashboard
7. Update README if significant addition

---

## Related

- [[README|Vault Documentation]]
- [[Quality Standards]] - Data quality requirements
- [[Validation Scripts]] - Automated quality checks
- [[Export Pipeline]] - Data distribution (v3.0)

---

*This analytics dashboard transforms the TTRPG History Vault from a static reference into a data-driven research platform, enabling quantitative insights into 50+ years of game design evolution.*

**Last Updated**: 2025-01-XX
**Script Count**: 8
**Visualization Count**: 15+
**Data Exports**: 8 CSV files
