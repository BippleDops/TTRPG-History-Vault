#!/usr/bin/env python3
"""
Schema Validator for TTRPG History Vault

Validates that all vault entries conform to their expected property schemas.
Calculates completeness scores and identifies missing required properties.

Usage:
    python schema_validator.py
    python schema_validator.py --entry-type games
    python schema_validator.py --verbose
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple
from collections import defaultdict

# Schema definitions matching Property-Schema.md
SCHEMAS = {
    'game': {
        'folder': 'Games',
        'required': {
            'title', 'type', 'publisher', 'designer', 'year-published',
            'system', 'genre', 'complexity', 'historical-significance',
            'innovation-score', 'tags', 'status'
        },
        'optional': {
            'edition', 'player-count', 'setting', 'influence-on',
            'influenced-by', 'purchase-date', 'personal-rating', 'play-experience'
        }
    },
    'publisher': {
        'folder': 'Publishers',
        'required': {
            'type', 'publisher-name', 'founded', 'headquarters',
            'era-active', 'significance', 'tags'
        },
        'optional': {
            'defunct', 'key-releases', 'notable-designers'
        }
    },
    'designer': {
        'folder': 'Designers',
        'required': {
            'type', 'designer-name', 'active-years', 'tags'
        },
        'optional': {
            'birth-year', 'notable-works', 'publishers-worked-with',
            'innovations', 'awards'
        }
    },
    'mechanic': {
        'folder': 'Mechanics',
        'required': {
            'type', 'mechanic-name', 'first-appearance', 'year-introduced',
            'complexity', 'popularity', 'tags'
        },
        'optional': {
            'games-using', 'description'
        }
    },
    'historical-event': {
        'folder': 'Historical Context',
        'required': {
            'type', 'event-name', 'date', 'year', 'significance', 'tags'
        },
        'optional': {
            'games-affected', 'publishers-affected'
        }
    },
    'actual-play': {
        'folder': 'Actual Play',
        'required': {
            'type', 'show-title', 'format', 'system-used', 'cast',
            'first-episode', 'status', 'platform', 'cultural-impact',
            'audience-size', 'tags'
        },
        'optional': {
            'final-episode', 'episode-count', 'notable-moments'
        }
    },
    'award': {
        'folder': 'Awards',
        'required': {
            'type', 'award-name', 'founded', 'categories',
            'administering-body', 'significance', 'tags'
        },
        'optional': {
            'defunct', 'notable-winners'
        }
    },
    'controversy': {
        'folder': 'Controversies',
        'required': {
            'type', 'controversy-name', 'year', 'parties-involved',
            'impact-areas', 'resolution', 'significance', 'tags'
        },
        'optional': {
            'ongoing', 'related-events'
        }
    },
    'convention': {
        'folder': 'Conventions',
        'required': {
            'type', 'convention-name', 'founded', 'location',
            'frequency', 'attendance', 'significance', 'tags'
        },
        'optional': {
            'defunct', 'notable-events', 'featured-guests'
        }
    },
    'digital-adaptation': {
        'folder': 'Digital Adaptations',
        'required': {
            'type', 'adaptation-title', 'source-game', 'platform',
            'developer', 'release-year', 'adaptation-type',
            'adaptation-quality', 'tags'
        },
        'optional': {
            'player-count', 'critical-reception', 'commercial-success'
        }
    },
    'retroclone': {
        'folder': 'Retroclones',
        'required': {
            'type', 'clone-title', 'emulates', 'publisher', 'designer',
            'year-published', 'license', 'design-goals', 'tags'
        },
        'optional': {
            'differences-from-original', 'community-reception'
        }
    },
    'supplement': {
        'folder': 'Supplements',
        'required': {
            'type', 'supplement-title', 'parent-game', 'publisher',
            'year-published', 'supplement-type', 'page-count',
            'notable-content', 'tags'
        },
        'optional': {
            'designer', 'historical-significance', 'critical-reception'
        }
    },
    'vtt-platform': {
        'folder': 'VTT Platforms',
        'required': {
            'type', 'platform-name', 'launch-year', 'supported-systems',
            'features', 'pricing-model', 'user-base', 'impact-on-industry',
            'tags'
        },
        'optional': {
            'defunct', 'notable-integrations', 'community-content'
        }
    }
}


def extract_frontmatter(file_path: Path) -> Dict:
    """Extract YAML frontmatter from markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Match frontmatter between --- delimiters
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return {}

        frontmatter_text = match.group(1)
        return yaml.safe_load(frontmatter_text) or {}

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}


def validate_entry(file_path: Path, schema: Dict) -> Tuple[bool, List[str], float]:
    """
    Validate a single entry against its schema.

    Returns:
        (is_valid, missing_properties, completeness_score)
    """
    frontmatter = extract_frontmatter(file_path)

    if not frontmatter:
        return False, ["No frontmatter found"], 0.0

    # Check required properties
    missing_required = []
    for prop in schema['required']:
        if prop not in frontmatter or frontmatter[prop] in [None, '', []]:
            missing_required.append(prop)

    # Calculate completeness score
    all_properties = schema['required'] | schema['optional']
    present_properties = set(frontmatter.keys()) & all_properties
    completeness = len(present_properties) / len(all_properties) * 100

    is_valid = len(missing_required) == 0

    return is_valid, missing_required, completeness


def validate_vault(vault_path: Path, entry_type: str = None, verbose: bool = False) -> Dict:
    """
    Validate all entries in the vault or a specific entry type.

    Returns summary statistics and detailed results.
    """
    results = {
        'total_files': 0,
        'valid_files': 0,
        'invalid_files': 0,
        'by_type': defaultdict(lambda: {
            'total': 0,
            'valid': 0,
            'invalid': 0,
            'avg_completeness': 0.0,
            'issues': []
        })
    }

    # Determine which schemas to check
    schemas_to_check = {entry_type: SCHEMAS[entry_type]} if entry_type else SCHEMAS

    for type_name, schema in schemas_to_check.items():
        folder_path = vault_path / schema['folder']

        if not folder_path.exists():
            if verbose:
                print(f"Folder not found: {folder_path}")
            continue

        # Find all markdown files
        md_files = list(folder_path.glob('*.md'))

        completeness_scores = []

        for md_file in md_files:
            results['total_files'] += 1
            results['by_type'][type_name]['total'] += 1

            is_valid, missing_props, completeness = validate_entry(md_file, schema)
            completeness_scores.append(completeness)

            if is_valid:
                results['valid_files'] += 1
                results['by_type'][type_name]['valid'] += 1
                if verbose:
                    print(f"✓ {md_file.name} - {completeness:.1f}% complete")
            else:
                results['invalid_files'] += 1
                results['by_type'][type_name]['invalid'] += 1
                results['by_type'][type_name]['issues'].append({
                    'file': md_file.name,
                    'missing': missing_props,
                    'completeness': completeness
                })
                print(f"✗ {md_file.name} - Missing: {', '.join(missing_props)} ({completeness:.1f}% complete)")

        # Calculate average completeness
        if completeness_scores:
            results['by_type'][type_name]['avg_completeness'] = sum(completeness_scores) / len(completeness_scores)

    return results


def generate_report(results: Dict, output_path: Path = None) -> str:
    """Generate a markdown report of validation results."""
    report_lines = [
        "# Schema Validation Report",
        "",
        f"**Total Files Checked**: {results['total_files']}",
        f"**Valid**: {results['valid_files']} ({results['valid_files']/results['total_files']*100:.1f}%)" if results['total_files'] > 0 else "**Valid**: 0 (0.0%)",
        f"**Invalid**: {results['invalid_files']}",
        "",
        "---",
        ""
    ]

    # By-type breakdown
    report_lines.append("## Validation by Entry Type")
    report_lines.append("")

    for type_name, type_results in sorted(results['by_type'].items()):
        report_lines.extend([
            f"### {type_name.replace('-', ' ').title()}",
            "",
            f"- **Total**: {type_results['total']}",
            f"- **Valid**: {type_results['valid']}",
            f"- **Invalid**: {type_results['invalid']}",
            f"- **Average Completeness**: {type_results['avg_completeness']:.1f}%",
            ""
        ])

        if type_results['issues']:
            report_lines.append("**Issues Found**:")
            report_lines.append("")
            for issue in type_results['issues']:
                report_lines.append(f"- `{issue['file']}` ({issue['completeness']:.1f}% complete)")
                report_lines.append(f"  - Missing: {', '.join(issue['missing'])}")
            report_lines.append("")

    report_lines.extend([
        "---",
        "",
        "*Generated by schema_validator.py*"
    ])

    report = "\n".join(report_lines)

    # Write to file if output path provided
    if output_path:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"\nReport written to: {output_path}")

    return report


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Validate TTRPG History Vault schemas')
    parser.add_argument('--vault-path', type=str, help='Path to vault root',
                       default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    parser.add_argument('--entry-type', type=str, help='Validate specific entry type only',
                       choices=list(SCHEMAS.keys()))
    parser.add_argument('--verbose', action='store_true', help='Show all files including valid ones')
    parser.add_argument('--output', type=str, help='Output report to file',
                       default=None)

    args = parser.parse_args()

    vault_path = Path(args.vault_path)

    print(f"Validating vault at: {vault_path}")
    print(f"Entry type: {args.entry_type or 'all'}")
    print("")

    results = validate_vault(vault_path, args.entry_type, args.verbose)

    print("\n" + "="*60)
    print("VALIDATION SUMMARY")
    print("="*60)

    # Generate and display report
    output_path = Path(args.output) if args.output else vault_path / "validation-report.md"
    generate_report(results, output_path)

    # Exit with error code if any invalid files found
    exit(0 if results['invalid_files'] == 0 else 1)


if __name__ == '__main__':
    main()
