#!/usr/bin/env python3
"""
JSON API Exporter for TTRPG History Vault

Exports vault content as structured JSON for API consumption, web applications,
or programmatic access.

Outputs:
- games.json - All game entries with full metadata
- designers.json - Designer entries
- publishers.json - Publisher entries
- index.json - Complete vault index
- api/v1/{type}/{id}.json - Individual entry endpoints

Requirements:
    pip install pyyaml

Usage:
    python Scripts/export/json_api_exporter.py
    python Scripts/export/json_api_exporter.py --output Exports/api/

    Serve with:
    cd Exports/api && python -m http.server 8000
"""

import os
import re
import yaml
import json
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def slugify(text):
    """Convert text to URL-safe slug."""
    slug = text.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug.strip('-')


def extract_frontmatter(file_path):
    """Extract YAML frontmatter and content from markdown."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
        if not match:
            return {}, ""

        frontmatter_text = match.group(1)
        body = match.group(2)

        frontmatter = yaml.safe_load(frontmatter_text) or {}

        return frontmatter, body
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return {}, ""


def extract_link_title(wikilink):
    """Extract title from [[Title]] format."""
    if not wikilink:
        return None
    link = wikilink.strip('[]')
    if '|' in link:
        link = link.split('|')[0]
    return link.strip()


def process_property_value(value):
    """Process frontmatter property values for JSON export."""
    if isinstance(value, list):
        # Process each item in list
        return [extract_link_title(item) if isinstance(item, str) and '[[' in item
                else item for item in value]
    elif isinstance(value, str) and '[[' in value:
        # Extract from wikilink
        return extract_link_title(value)
    else:
        return value


def export_entry(file_path, entry_type, output_dir):
    """Export single entry to JSON."""
    frontmatter, body = extract_frontmatter(file_path)

    if not frontmatter.get('type'):
        return None

    # Build JSON object
    entry = {
        'id': slugify(frontmatter.get('title', file_path.stem)),
        'type': entry_type,
        'title': frontmatter.get('title', file_path.stem),
        'metadata': {},
        'content': body.strip(),
        'source_file': file_path.name,
        'last_updated': datetime.fromtimestamp(file_path.stat().st_mtime).isoformat()
    }

    # Add all frontmatter as metadata
    for key, value in frontmatter.items():
        if key != 'type':  # Already included at top level
            entry['metadata'][key] = process_property_value(value)

    return entry


def export_collection(vault_path, folder_name, entry_type, output_dir):
    """Export all entries from a folder to JSON."""
    source_folder = vault_path / folder_name

    if not source_folder.exists():
        return []

    print(f"Exporting {entry_type}...")

    entries = []
    api_dir = output_dir / 'api' / 'v1' / entry_type

    for md_file in source_folder.glob('*.md'):
        entry = export_entry(md_file, entry_type, output_dir)
        if entry:
            entries.append(entry)

            # Save individual entry
            api_dir.mkdir(parents=True, exist_ok=True)
            entry_file = api_dir / f"{entry['id']}.json"

            with open(entry_file, 'w', encoding='utf-8') as f:
                json.dump(entry, f, indent=2, ensure_ascii=False)

    # Save collection
    collection_file = output_dir / f'{entry_type}.json'
    with open(collection_file, 'w', encoding='utf-8') as f:
        json.dump({
            'type': entry_type,
            'count': len(entries),
            'entries': entries,
            'generated': datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)

    print(f"  Exported {len(entries)} entries")
    return entries


def build_index(all_entries, output_dir):
    """Build master index of all entries."""
    print("\nBuilding master index...")

    index = {
        'vault': 'TTRPG History Vault',
        'version': '3.0',
        'generated': datetime.now().isoformat(),
        'stats': {
            'total_entries': sum(len(entries) for entries in all_entries.values()),
            'by_type': {entry_type: len(entries)
                       for entry_type, entries in all_entries.items()}
        },
        'collections': {
            entry_type: f'/api/v1/{entry_type}/'
            for entry_type in all_entries.keys()
        },
        'endpoints': {
            'all_games': '/games.json',
            'all_designers': '/designers.json',
            'all_publishers': '/publishers.json',
            'individual_entry': '/api/v1/{type}/{id}.json'
        }
    }

    # Add search index
    search_index = []
    for entry_type, entries in all_entries.items():
        for entry in entries:
            search_index.append({
                'id': entry['id'],
                'type': entry_type,
                'title': entry['title'],
                'url': f'/api/v1/{entry_type}/{entry["id"]}.json'
            })

    index['search_index'] = search_index

    # Save index
    index_file = output_dir / 'index.json'
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"  Created index with {len(search_index)} entries")


def create_api_documentation(output_dir):
    """Create API documentation."""
    docs = f"""# TTRPG History Vault JSON API

**Version**: 1.0
**Generated**: {datetime.now().strftime('%Y-%m-%d')}

## Overview

This JSON API provides programmatic access to the TTRPG History Vault content.

## Endpoints

### Collections

- `GET /games.json` - All game entries
- `GET /designers.json` - All designer entries
- `GET /publishers.json` - All publisher entries
- `GET /mechanics.json` - All mechanic entries
- `GET /index.json` - Master index

### Individual Entries

- `GET /api/v1/games/{{id}}.json` - Single game
- `GET /api/v1/designers/{{id}}.json` - Single designer
- etc.

## Response Format

### Collection Response

```json
{{
  "type": "games",
  "count": 100,
  "entries": [...],
  "generated": "2025-01-XX"
}}
```

### Entry Response

```json
{{
  "id": "dungeons-dragons-fifth-edition-2014",
  "type": "game",
  "title": "Dungeons & Dragons Fifth Edition (2014)",
  "metadata": {{
    "year-published": 2014,
    "designer": ["Mike Mearls", "Jeremy Crawford"],
    "publisher": "Wizards of the Coast",
    "system": "d20",
    "genre": ["fantasy"],
    "historical-significance": 5
  }},
  "content": "Markdown content here...",
  "source_file": "Dungeons & Dragons Fifth Edition (2014).md",
  "last_updated": "2025-01-XX"
}}
```

## Usage Examples

### JavaScript/Fetch

```javascript
fetch('/games.json')
  .then(res => res.json())
  .then(data => {{
    console.log(`Loaded ${{data.count}} games`);
    data.entries.forEach(game => {{
      console.log(game.title);
    }});
  }});
```

### Python

```python
import requests

games = requests.get('https://api.example.com/games.json').json()
print(f"Loaded {{games['count']}} games")

for game in games['entries']:
    print(game['title'])
```

### cURL

```bash
curl https://api.example.com/games.json | jq '.entries[].title'
```

## Filtering and Searching

Use client-side filtering on collections:

```javascript
// Find all games from 2014
const games2014 = data.entries.filter(g =>
  g.metadata['year-published'] === 2014
);

// Find games by designer
const mikeMearlsGames = data.entries.filter(g =>
  g.metadata.designer?.includes('Mike Mearls')
);
```

## CORS

If hosting this API, ensure CORS headers are configured for cross-origin access.

## License

Content licensed per individual entries. See source files for details.

---

*Generated from TTRPG History Vault*
"""

    readme_path = output_dir / 'API-DOCUMENTATION.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(docs)

    print(f"  Created API documentation")


def export_to_json(vault_path, output_path):
    """Export entire vault to JSON API."""
    print(f"\n{'='*60}")
    print("JSON API EXPORTER")
    print(f"{'='*60}\n")

    print(f"Source: {vault_path}")
    print(f"Output: {output_path}\n")

    # Create output directory
    output_path.mkdir(parents=True, exist_ok=True)

    # Export collections
    collections = {
        'games': ('Games', 'games'),
        'designers': ('Designers', 'designers'),
        'publishers': ('Publishers', 'publishers'),
        'mechanics': ('Mechanics', 'mechanics'),
        'supplements': ('Supplements', 'supplements'),
        'retroclones': ('Retroclones', 'retroclones'),
        'vtt-platforms': ('VTT Platforms', 'vtt-platforms'),
        'controversies': ('Controversies', 'controversies')
    }

    all_entries = {}

    for entry_type, (folder_name, json_name) in collections.items():
        entries = export_collection(vault_path, folder_name, entry_type, output_path)
        all_entries[entry_type] = entries

    # Build master index
    build_index(all_entries, output_path)

    # Create documentation
    create_api_documentation(output_path)

    print(f"\n{'='*60}")
    print("JSON API EXPORT COMPLETE")
    print(f"{'='*60}\n")
    print(f"Total entries: {sum(len(e) for e in all_entries.values())}")
    print(f"\nTo serve API locally:")
    print(f"  cd {output_path}")
    print(f"  python -m http.server 8000")
    print(f"\nThen access at: http://localhost:8000/index.json\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Export vault to JSON API')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output directory for JSON API')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)
    output_path = Path(args.output) if args.output else vault_path / "Exports" / "json-api"

    export_to_json(vault_path, output_path)


if __name__ == '__main__':
    main()
