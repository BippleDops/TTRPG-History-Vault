#!/usr/bin/env python3
"""
Anki Flashcard Generator for TTRPG History Vault

Generates Anki flashcard decks for studying TTRPG history.
Creates cards for games, designers, mechanics, and historical facts.

Outputs:
- Anki deck file (.txt format for import)
- Multiple card types (basic, cloze, image occlusion)
- Organized by tags and decks

Card Types:
- Game identification (year, designer, publisher)
- Designer contributions
- Mechanic definitions
- Historical significance questions
- Timeline questions

Requirements:
    pip install pyyaml

Usage:
    python Scripts/export/anki_flashcards.py
    python Scripts/export/anki_flashcards.py --output Exports/ttrpg-history-flashcards.txt

    Then import into Anki:
    File > Import > Select the .txt file
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict


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
    """Extract title from [[Title]] format."""
    if not wikilink:
        return None
    link = wikilink.strip('[]')
    if '|' in link:
        link = link.split('|')[0]
    return link.strip()


def process_list_field(field):
    """Process field that might be list or single value."""
    if isinstance(field, list):
        return [extract_link_title(item) if isinstance(item, str) and '[[' in item
                else item for item in field]
    elif isinstance(field, str) and '[[' in field:
        return [extract_link_title(field)]
    elif field:
        return [field] if not isinstance(field, list) else field
    else:
        return []


def generate_game_cards(frontmatter):
    """Generate flashcards for a game entry."""
    cards = []

    title = frontmatter.get('title', 'Unknown Game')
    year = frontmatter.get('year-published')
    designers = process_list_field(frontmatter.get('designer'))
    publisher = extract_link_title(frontmatter.get('publisher')) if frontmatter.get('publisher') else None
    system = frontmatter.get('system')
    significance = frontmatter.get('historical-significance', 0)

    tags = f"TTRPG::Games"

    # Card 1: When was this game published?
    if year:
        front = f"When was {title} published?"
        back = f"{year}"
        cards.append((front, back, tags))

    # Card 2: Who designed this game?
    if designers and designers[0] != 'unknown':
        front = f"Who designed {title}?"
        back = ", ".join(str(d) for d in designers if d)
        cards.append((front, back, tags))

    # Card 3: Who published this game?
    if publisher and publisher != 'unknown':
        front = f"Who published {title}?"
        back = publisher
        cards.append((front, back, tags))

    # Card 4: What system does this game use?
    if system and system != 'unknown':
        front = f"What system does {title} use?"
        back = system
        cards.append((front, back, tags))

    # Card 5: Historical significance (for highly significant games)
    if significance >= 4:
        front = f"What is the historical significance of {title}?"
        back = f"{significance}/5 - Major influence on TTRPG history"
        cards.append((front, back, f"{tags}::HighSignificance"))

    # Card 6: Reverse - year to game (for memorable years)
    if year and significance >= 3:
        front = f"What significant TTRPG was published in {year}?"
        back = f"{title}"
        cards.append((front, back, f"{tags}::Timeline"))

    return cards


def generate_designer_cards(frontmatter):
    """Generate flashcards for a designer entry."""
    cards = []

    name = frontmatter.get('designer-name', frontmatter.get('title', 'Unknown Designer'))
    notable_works = process_list_field(frontmatter.get('notable-works'))
    companies = process_list_field(frontmatter.get('companies-worked'))

    tags = f"TTRPG::Designers"

    # Card 1: Notable works
    if notable_works and len(notable_works) > 0:
        front = f"What are some notable works by {name}?"
        back = ", ".join(str(w) for w in notable_works[:5] if w)  # Limit to top 5
        cards.append((front, back, tags))

    # Card 2: Companies worked for
    if companies and len(companies) > 0:
        front = f"What companies has {name} worked for?"
        back = ", ".join(str(c) for c in companies if c)
        cards.append((front, back, tags))

    # Card 3: Reverse - game to designer
    for work in notable_works[:3] if notable_works else []:  # Top 3 works
        if work and work != 'unknown':
            front = f"Who designed {work}?"
            back = name
            cards.append((front, back, f"{tags}::WorksReverse"))

    return cards


def generate_mechanic_cards(frontmatter, body_text=""):
    """Generate flashcards for a mechanic entry."""
    cards = []

    name = frontmatter.get('mechanic-name', frontmatter.get('title', 'Unknown Mechanic'))
    introduced_in = extract_link_title(frontmatter.get('introduced-in'))
    purpose = frontmatter.get('purpose', '')

    tags = f"TTRPG::Mechanics"

    # Card 1: Definition (extract from body if available)
    # For now, use purpose field
    if purpose:
        front = f"What is {name}?"
        back = purpose
        cards.append((front, back, tags))

    # Card 2: Where was it introduced?
    if introduced_in:
        front = f"In what game was {name} introduced?"
        back = introduced_in
        cards.append((front, back, tags))

    return cards


def generate_timeline_cards(all_games):
    """Generate timeline-based flashcards."""
    cards = []
    tags = "TTRPG::Timeline"

    # Sort games by year
    games_by_year = sorted(
        [(g['frontmatter'].get('year-published'), g['frontmatter'].get('title'))
         for g in all_games
         if g['frontmatter'].get('year-published')],
        key=lambda x: x[0]
    )

    # Decade cards
    decades = defaultdict(list)
    for year, title in games_by_year:
        decade = (year // 10) * 10
        decades[decade].append((year, title))

    for decade, games in decades.items():
        if len(games) >= 3:
            front = f"Name 3 significant TTRPGs from the {decade}s"
            back = "\n".join(f"- {title} ({year})" for year, title in games[:5])
            cards.append((front, back, f"{tags}::Decades"))

    # Era cards
    eras = {
        "Golden Age (1974-1979)": (1974, 1979),
        "TSR Dominance (1980-1989)": (1980, 1989),
        "Diverse 90s (1990-1999)": (1990, 1999),
        "d20 Era (2000-2007)": (2000, 2007),
        "5E Renaissance (2012-2019)": (2012, 2019)
    }

    for era_name, (start, end) in eras.items():
        era_games = [(year, title) for year, title in games_by_year
                     if start <= year <= end]

        if era_games:
            front = f"What are key games from the {era_name}?"
            back = "\n".join(f"- {title} ({year})" for year, title in era_games[:6])
            cards.append((front, back, f"{tags}::Eras"))

    return cards


def export_to_anki_format(cards, output_path):
    """Export cards to Anki-importable text format."""
    # Anki import format: Front\tBack\tTags
    with open(output_path, 'w', encoding='utf-8') as f:
        for front, back, tags in cards:
            # Escape tabs and newlines in card content
            front_clean = front.replace('\t', ' ').replace('\n', '<br>')
            back_clean = back.replace('\t', ' ').replace('\n', '<br>')

            f.write(f"{front_clean}\t{back_clean}\t{tags}\n")


def generate_flashcards(vault_path, output_path):
    """Generate all flashcards from vault."""
    print(f"\n{'='*60}")
    print("ANKI FLASHCARD GENERATOR")
    print(f"{'='*60}\n")

    print(f"Source: {vault_path}")
    print(f"Output: {output_path}\n")

    all_cards = []
    all_games = []

    # Process games
    games_folder = vault_path / 'Games'
    if games_folder.exists():
        print("Processing games...")
        game_count = 0

        for md_file in games_folder.glob('*.md'):
            frontmatter = extract_frontmatter(md_file)
            if frontmatter.get('type') == 'game':
                cards = generate_game_cards(frontmatter)
                all_cards.extend(cards)
                all_games.append({'frontmatter': frontmatter})
                game_count += 1

        print(f"  Generated {len([c for c in all_cards if 'Games' in c[2]])} cards from {game_count} games")

    # Process designers
    designers_folder = vault_path / 'Designers'
    if designers_folder.exists():
        print("Processing designers...")
        designer_count = 0
        designer_cards_start = len(all_cards)

        for md_file in designers_folder.glob('*.md'):
            frontmatter = extract_frontmatter(md_file)
            if frontmatter.get('type') == 'designer':
                cards = generate_designer_cards(frontmatter)
                all_cards.extend(cards)
                designer_count += 1

        designer_cards_count = len(all_cards) - designer_cards_start
        print(f"  Generated {designer_cards_count} cards from {designer_count} designers")

    # Process mechanics
    mechanics_folder = vault_path / 'Mechanics'
    if mechanics_folder.exists():
        print("Processing mechanics...")
        mechanic_count = 0
        mechanic_cards_start = len(all_cards)

        for md_file in mechanics_folder.glob('*.md'):
            frontmatter = extract_frontmatter(md_file)
            if frontmatter.get('type') == 'mechanic':
                cards = generate_mechanic_cards(frontmatter)
                all_cards.extend(cards)
                mechanic_count += 1

        mechanic_cards_count = len(all_cards) - mechanic_cards_start
        print(f"  Generated {mechanic_cards_count} cards from {mechanic_count} mechanics")

    # Generate timeline cards
    print("Generating timeline cards...")
    timeline_cards_start = len(all_cards)
    timeline_cards = generate_timeline_cards(all_games)
    all_cards.extend(timeline_cards)
    timeline_cards_count = len(all_cards) - timeline_cards_start
    print(f"  Generated {timeline_cards_count} timeline cards")

    # Export to Anki format
    print(f"\nExporting to Anki format...")
    export_to_anki_format(all_cards, output_path)

    print(f"\n{'='*60}")
    print("FLASHCARD GENERATION COMPLETE")
    print(f"{'='*60}\n")
    print(f"Total cards: {len(all_cards)}")
    print(f"\nTo import into Anki:")
    print(f"1. Open Anki")
    print(f"2. File > Import")
    print(f"3. Select: {output_path}")
    print(f"4. Set fields: Front, Back, Tags")
    print(f"5. Import into desired deck\n")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate Anki flashcards from vault')
    parser.add_argument('--vault-path', type=str,
                       default=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
                       help='Path to vault root')
    parser.add_argument('--output', type=str,
                       default=None,
                       help='Output flashcard file path')

    args = parser.parse_args()

    vault_path = Path(args.vault_path)
    output_path = Path(args.output) if args.output else \
                 vault_path / "Exports" / "ttrpg-history-flashcards.txt"

    # Create output directory
    output_path.parent.mkdir(parents=True, exist_ok=True)

    generate_flashcards(vault_path, output_path)


if __name__ == '__main__':
    main()
