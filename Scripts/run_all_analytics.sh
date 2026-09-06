#!/bin/bash
# Run All Analytics Scripts for TTRPG History Vault
# Generates complete data-driven insights across all vault content

set -e  # Exit on error

# Resolve the vault root relative to this script so it works from any checkout.
VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$VAULT_ROOT"

echo "=================================================="
echo "TTRPG HISTORY VAULT - ANALYTICS SUITE"
echo "=================================================="
echo ""
echo "Starting comprehensive analytics run..."
echo "Generated: $(date)"
echo ""

# 1. Publication Trends
echo "1/8 Running publication trends analysis..."
python3 Scripts/analytics/publication_trends.py
echo "✓ Complete"
echo ""

# 2. Influence Network
echo "2/8 Running influence network analysis..."
python3 Scripts/analytics/influence_network.py
echo "✓ Complete"
echo ""

# 3. Innovation Timeline
echo "3/8 Running innovation timeline analysis..."
python3 Scripts/analytics/innovation_timeline.py
echo "✓ Complete"
echo ""

# 4. Designer Matrix
echo "4/8 Running designer contribution analysis..."
python3 Scripts/analytics/designer_matrix.py
echo "✓ Complete"
echo ""

# 5. Coverage Gaps
echo "5/8 Running coverage gaps analysis..."
python3 Scripts/analytics/coverage_gaps.py
echo "✓ Complete"
echo ""

# 6. Complexity vs Popularity
echo "6/8 Running complexity analysis..."
python3 Scripts/analytics/complexity_popularity.py
echo "✓ Complete"
echo ""

# 7. System Family Tree
echo "7/8 Running system family tree analysis..."
python3 Scripts/analytics/system_family_tree.py
echo "✓ Complete"
echo ""

# 8. Era Comparison
echo "8/8 Running era comparison analysis..."
python3 Scripts/analytics/era_comparison.py
echo "✓ Complete"
echo ""

echo "=================================================="
echo "ANALYTICS COMPLETE"
echo "=================================================="
echo ""
echo "Outputs saved to: Attachments/Diagrams/analytics/"
echo ""
echo "Generated files:"
ls -lh Attachments/Diagrams/analytics/ | tail -n +2
echo ""
echo "View Analytics Dashboard: open 'Views/Analytics-Dashboard.md'"
echo ""
