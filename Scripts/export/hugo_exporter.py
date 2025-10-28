#!/usr/bin/env python3
"""
Hugo Static Site Exporter for TTRPG History Vault

Converts vault markdown files to Hugo-compatible format for static site generation.
Transforms Obsidian-specific syntax (wikilinks, Datacore queries) to Hugo-compatible equivalents.

Outputs:
- Hugo content directory structure
- Hugo frontmatter (TOML or YAML)
- Converted markdown content
- Asset organization (images, diagrams)
- Configuration files

Requirements:
    pip install pyyaml

Usage:
    python Scripts/export/hugo_exporter.py
    python Scripts/export/hugo_exporter.py --output Exports/hugo-site/

    Then build Hugo site:
    cd Exports/hugo-site && hugo
"""

import os
import re
import yaml
import shutil
from pathlib import Path
from datetime import datetime


def convert_wikilinks_to_hugo(content):
    """Convert [[Wikilink]] to Hugo markdown links."""
    # Pattern: [[Link]] or [[Link|Display]]
    def replace_wikilink(match):
        link_content = match.group(1)
        if '|' in link_content:
            link, display = link_content.split('|', 1)
        else:
            link = link_content
            display = link_content

        # Convert to Hugo link format: [Display](/link/)
        # Slugify the link
        slug = link.lower().replace(' ', '-').replace('(', '').replace(')', '')
        return f'[{display}](/{slug}/)'

    pattern = r'\[\[([^\]]+)\]\]'
    return re.sub(pattern, replace_wikilink, content)


def remove_datacore_queries(content):
    """Remove or convert Datacore query blocks."""
    # Pattern: ```datacore ... ```
    pattern = r'```datacore.*?```'

    # Replace with notice that queries aren't rendered in static export
    replacement = r'*[Dynamic query removed - see live vault for interactive results]*'

    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def convert_obsidian_embeds(content):
    """Convert ![[image.png]] to Hugo image syntax."""
    # Pattern: ![[image.png]]
    def replace_embed(match):
        filename = match.group(1)
        # Assume images are in /static/images/
        return f'![{filename}](/images/{filename})'

    pattern = r'!\[\[([^\]]+)\]\]'
    return re.sub(pattern, replace_embed, content)


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)$', content, re.DOTALL)
    if not match:
        return {}, content

    frontmatter_text = match.group(1)
    body = match.group(2)

    try:
        frontmatter = yaml.safe_load(frontmatter_text) or {}
    except:
        frontmatter = {}

    return frontmatter, body


def convert_frontmatter_to_hugo(frontmatter, entry_type):
    """Convert Obsidian frontmatter to Hugo frontmatter."""
    hugo_fm = {
        'title': frontmatter.get('title', 'Untitled'),
        'date': frontmatter.get('year-published', datetime.now().year),
        'type': entry_type,
        'draft': False
    }

    # Add tags
    tags = frontmatter.get('tags', [])
    if tags:
        hugo_fm['tags'] = tags if isinstance(tags, list) else [tags]

    # Add genre as categories for games
    if entry_type == 'game':
        genres = frontmatter.get('genre', [])
        if genres:
            hugo_fm['categories'] = genres if isinstance(genres, list) else [genres]

    # Preserve custom fields
    for key, value in frontmatter.items():
        if key not in ['title', 'type', 'tags', 'genre'] and not key.startswith('_'):
            # Skip complex types
            if isinstance(value, (str, int, float, bool)):
                hugo_fm[key] = value

    return hugo_fm


def process_markdown_file(input_path, output_path, entry_type):
    """Process single markdown file for Hugo export."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract frontmatter
    frontmatter, body = extract_frontmatter(content)

    # Convert body content
    body = convert_wikilinks_to_hugo(body)
    body = remove_datacore_queries(body)
    body = convert_obsidian_embeds(body)

    # Convert frontmatter
    hugo_frontmatter = convert_frontmatter_to_hugo(frontmatter, entry_type)

    # Write Hugo-compatible file
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        # Write Hugo frontmatter
        f.write('---\n')
        yaml.dump(hugo_frontmatter, f, default_flow_style=False, allow_unicode=True)
        f.write('---\n\n')

        # Write body
        f.write(body)


def export_to_hugo(vault_path, output_path):
    """Export entire vault to Hugo site structure."""
    print(f"\n{'='*60}")
    print("HUGO STATIC SITE EXPORTER")
    print(f"{'='*60}\n")

    print(f"Source: {vault_path}")
    print(f"Output: {output_path}\n")

    # Create Hugo directory structure
    content_dir = output_path / 'content'
    static_dir = output_path / 'static'
    config_dir = output_path

    # Content sections
    sections = {
        'games': vault_path / 'Games',
        'designers': vault_path / 'Designers',
        'publishers': vault_path / 'Publishers',
        'supplements': vault_path / 'Supplements',
        'mechanics': vault_path / 'Mechanics',
        'controversies': vault_path / 'Controversies',
        'retroclones': vault_path / 'Retroclones',
        'vtt-platforms': vault_path / 'VTT Platforms'
    }

    total_files = 0

    for section_name, source_folder in sections.items():
        if not source_folder.exists():
            continue

        print(f"Processing {section_name}...")

        section_output = content_dir / section_name
        section_output.mkdir(parents=True, exist_ok=True)

        for md_file in source_folder.glob('*.md'):
            # Create output path
            output_file = section_output / md_file.name

            # Process file
            process_markdown_file(md_file, output_file, section_name.rstrip('s'))
            total_files += 1

        print(f"  Exported {len(list(source_folder.glob('*.md')))} files")

    # Copy assets
    print("\nCopying assets...")

    # Images
    images_source = vault_path / 'Attachments' / 'Images'
    if images_source.exists():
        images_dest = static_dir / 'images'
        if images_dest.exists():
            shutil.rmtree(images_dest)
        shutil.copytree(images_source, images_dest)
        print(f"  Copied images to {images_dest}")

    # Diagrams
    diagrams_source = vault_path / 'Attachments' / 'Diagrams'
    if diagrams_source.exists():
        diagrams_dest = static_dir / 'diagrams'
        if diagrams_dest.exists():
            shutil.rmtree(diagrams_dest)
        shutil.copytree(diagrams_source, diagrams_dest)
        print(f"  Copied diagrams to {diagrams_dest}")

    # Generate Hugo config
    print("\nGenerating Hugo configuration...")
    config_path = config_dir / 'config.yaml'

    hugo_config = {
        'baseURL': 'https://ttrpg-history.example.com/',
        'languageCode': 'en-us',
        'title': 'TTRPG History Vault',
        'theme': 'hugo-book',  # Recommended theme for documentation
        'params': {
            'description': 'Comprehensive encyclopedia of tabletop roleplaying game history',
            'author': 'TTRPG History Vault Contributors',
            'BookRepo': 'https://github.com/yourusername/ttrpg-history-vault',
            'BookSection': '*'
        },
        'menu': {
            'main': [
                {'name': 'Games', 'url': '/games/', 'weight': 1},
                {'name': 'Designers', 'url': '/designers/', 'weight': 2},
                {'name': 'Publishers', 'url': '/publishers/', 'weight': 3},
                {'name': 'Mechanics', 'url': '/mechanics/', 'weight': 4}
            ]
        },
        'taxonomies': {
            'tag': 'tags',
            'category': 'categories'
        }
    }

    with open(config_path, 'w') as f:
        yaml.dump(hugo_config, f, default_flow_style=False)

    print(f"  Created config.yaml")

    # Create README for Hugo site
    readme_path = config_dir / 'README.md'
    with open(readme_path, 'w') as f:
        f.write("""# TTRPG History Vault - Hugo Static Site

This is an auto-generated Hugo static site export from the TTRPG History Vault.

## Building the Site

1. Install Hugo: https://gohugo.io/installation/

2. Install recommended theme:
   ```bash
   git clone https://github.com/alex-shpak/hugo-book themes/hugo-book
   ```

3. Build the site:
   ```bash
   hugo
   ```

4. Preview locally:
   ```bash
   hugo server
   ```

5. Deploy:
   - Site files generated in `public/` directory
   - Deploy to Netlify, GitHub Pages, Vercel, or any static host

## Updating Content

Re-run the export script from the main vault:
```bash
python Scripts/export/hugo_exporter.py
```

## Customization

- Edit `config.yaml` to change site settings
- Modify theme in `themes/` directory
- Add custom CSS in `static/css/`

---

*Auto-generated from TTRPG History Vault on """ + datetime.now().strftime('%Y-%m-%d') + "*\n")

    print(f"\n{'='*60}")
    print("EXPORT COMPLETE")
    print(f"{'='*60}\n")
    print(f"Total files exported: {total_files}")
    print(f"\nNext steps:")
    print(f"1. cd {output_path}")
    print(f"2. Install Hugo theme: git clone https://github.com/alex-shpak/hugo-book themes/hugo-book")
    print(f"3. Build site: hugo")
    print(f"4. Preview: hugo server")
    print(f"\nSite will be in {output_path}/public/\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Export vault to Hugo static site')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output directory for Hugo site')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)
    output_path = Path(args.output) if args.output else vault_path / "Exports" / "hugo-site"

    export_to_hugo(vault_path, output_path)


if __name__ == '__main__':
    main()
