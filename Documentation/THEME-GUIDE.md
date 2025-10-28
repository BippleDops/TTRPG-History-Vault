# TTRPG Historian Theme Guide

## Overview

The **TTRPG Historian** theme provides a classic fantasy/parchment aesthetic inspired by vintage RPG manuals, illuminated manuscripts, and gaming tables. It creates an immersive historical research environment perfect for documenting TTRPG history.

---

## Features

### 🎲 TTRPG-Specific Aesthetics

This theme is specifically designed to evoke the experience of reading classic RPG manuals, rolling dice at a gaming table, and exploring character sheets. Every element has RPG-inspired styling.

**Color Palette:**
- **Parchment backgrounds** (#F4ECD8) - Vintage game book feel
- **Deep burgundy accents** (#8B1538) - Classic D&D red
- **Gold highlights** (#D4AF37) - Treasure and magic items
- **Dark brown text** (#2C1810) - Quill ink on parchment
- **Cream secondary backgrounds** (#FFF8E7) - Aged paper texture

**Typography:**
- **Body text**: Crimson Text (serif) - RPG manual readable prose
- **Headers**: Cinzel (decorative serif) - Fantasy/medieval styling
- **UI elements**: Quattrocento Sans - Modern game UI text
- **Code**: Inconsolata (monospace) - Game stats/mechanics

### ⚔️ RPG-Themed Elements

**Headers (H1-H6)** - Dice and Combat Icons
- H1: 🎲 Title 🎲 (D20 dice decorations)
- H2: ⚄ Title (Dice pip decoration)
- Gold bottom borders like RPG manual sections
- Cinzel fantasy font for that classic RPG feel
- Uppercase H1 styling like D&D chapter headers

**Properties/Frontmatter** - Character Sheet Style
- "⚔️ CHARACTER SHEET ⚔️" header at top
- RPG stat block layout
- Burgundy labels with gold borders
- Looks like an actual D&D character sheet!

**Tables (Datacore Queries)** - Monster Stat Blocks
- "🎲 ADVENTURE LOG 🎲" header label
- Burgundy gradient header like D&D 5e stat blocks
- Gold double border underneath (classic RPG style)
- Alternating row colors for readability
- 3px burgundy border around entire table
- Hover effects glow like selected spell
- Looks like official D&D monster/NPC stat blocks!

**Callouts** - D&D Ability Score Boxes
- Each callout type has RPG-themed label:
  - **Note**: 📖 LORE (blue, like Intelligence)
  - **Tip**: 💡 WISDOM (gold, like Wisdom)
  - **Warning**: ⚠️ DANGER (orange, like Dexterity)
  - **Danger**: 💀 CRITICAL (red, like Constitution)
- Labels appear above callout like ability score names
- Bordered like character sheet sections
- Dice pip (⚄) decoration on title

**Lists** - Initiative Tracker & Dice Pips
- Unordered lists: ⚅ Dice pip bullets
- Ordered lists: Initiative-style numbers in Cinzel font
- Looks like rolling dice for each item!

**Blockquotes** - NPC Dialogue Boxes
- "💬 QUOTE" label at top
- Gold border like speech bubbles
- Dice emoji (🎲) at bottom right
- Styled like NPC conversation text

**Embeds** - Quest Cards
- "📜 LINKED ENTRY" label at top
- Burgundy border with gold accent
- Looks like a quest card or adventure hook
- Shadow effect like physical card

**Horizontal Rules** - Session Dividers
- 🎲 ⚔️ 🎲 centered icons
- Gold double border (like page breaks in RPG books)
- Separates content like campaign chapters

**Links**
- Internal links: Deep burgundy with underline
- Hover: Gold underline with parchment background
- External links: Blue-gray with dotted underline

**Properties/Frontmatter**
- Gold-bordered card at top of entries
- Parchment-dark background
- Uppercase property keys in burgundy
- Clean, structured layout

**Callouts**
- Parchment-light background
- 6px colored left border
- Cinzel font for titles
- Type-specific colors (note, tip, warning, danger)

**Tags**
- Parchment background with border
- Hover: Burgundy background with light text
- Rounded corners, compact spacing

**Horizontal Rules**
- Gold 2px line with centered sword icon (⚔)
- Visual section separators

**Code Blocks**
- Parchment-dark background
- Burgundy left border (4px)
- Syntax highlighting compatible

**Blockquotes**
- Gold left border
- Parchment-dark background
- Decorative opening quote mark
- Italic text styling

**Graph View**
- Burgundy nodes
- Gold tag nodes
- Parchment link lines
- Cohesive with overall aesthetic

**Sidebar** - Campaign Folders & Dungeon Maps
- Dungeon grid texture background (30px squares)
- RPG-specific folder icons:
  - 🎲 Games folder
  - ✍️ Designers folder
  - 🏰 Publishers folder
  - ⚙️ Mechanics folder
  - 🎭 Actual Play folder
  - 🗺️ Other folders
  - 📖 Root vault
- Active file: Burgundy gradient with gold border (like selected spell)
- Hover: Slides right with gold accent (interactive feel)
- Transform animations for responsive feel

**Ribbon (Left Icons)** - Quest Bar
- ⚔️ Sword icon at top (party leader marker)
- Burgundy gradient background (vertical)
- Gold border (4px, like gilded edge)
- Hover: Icons glow gold and scale up
- Active: Gold background with burgundy icon
- Looks like a vertical quest tracker!

**Status Bar** - RPG Manual Footer
- "📖 TTRPG HISTORY VAULT" label on left
- Burgundy gradient background (horizontal)
- Gold double border on top
- Each status item has ⚄ dice pip prefix
- Separated by gold dividers
- Looks like the footer of a D&D rulebook!

**Body Content** - Gaming Table Texture
- Subtle grid pattern overlay (20px squares)
- Reminiscent of battle maps and graph paper
- Very faint so it doesn't interfere with reading
- Evokes the feel of sitting at a gaming table

---

## Dark Mode

The theme includes comprehensive dark mode support with inverted colors:

- **Background**: Dark brown (#1A1410)
- **Text**: Light parchment (#E8DCC4)
- **Accents**: Maintain burgundy and gold
- **Links**: Gold color scheme for visibility
- **All elements adapted** for comfortable night reading

---

## Activating the Theme

### In Obsidian:

1. Open **Settings** (⚙️ icon)
2. Navigate to **Appearance**
3. Under **Themes**, scroll to **Community themes**
4. Find "TTRPG Historian" in the dropdown
5. Click to apply

### The theme is pre-configured:
- ✅ Already set in `.obsidian/appearance.json`
- ✅ Font size: 17px (optimal for readability)
- ✅ Compatible with all existing CSS snippets
- ✅ Works with Datacore and Templater plugins

---

## Customization

### Adjusting Colors

Edit `.obsidian/themes/TTRPG Historian/theme.css` and modify the `:root` variables:

```css
:root {
  /* Change primary background */
  --parchment-bg: #YOUR_COLOR;

  /* Change accent color */
  --burgundy: #YOUR_COLOR;

  /* Change gold highlights */
  --gold: #YOUR_COLOR;
}
```

### Adjusting Typography

```css
body {
  /* Change body font */
  --font-text: 'Your Font', serif;

  /* Change base font size */
  --font-text-size: 18px;
}
```

### Creating CSS Snippets

For minor customizations without editing the theme:

1. Create a new file in `.obsidian/snippets/`
2. Name it `my-custom-styles.css`
3. Add your CSS overrides
4. Enable in Settings → Appearance → CSS snippets

---

## Compatibility

**Works with:**
- ✅ Datacore plugin (tables beautifully styled)
- ✅ Templater plugin
- ✅ Graph view (custom node/link colors)
- ✅ Properties/Frontmatter (enhanced card display)
- ✅ All core Obsidian features
- ✅ Mobile (responsive design)
- ✅ Print (print-specific styles included)
- ✅ All existing CSS snippets in the vault

**Optimized for:**
- Long-form historical writing
- Database-style Datacore queries
- Research and citation work
- Graph-based exploration
- Academic documentation

---

## Design Philosophy

The TTRPG Historian theme creates an environment that feels like working with historical manuscripts and vintage gaming materials. Key design principles:

1. **Readability First**: Serif fonts and high contrast for long reading sessions
2. **Historical Aesthetic**: Parchment and book-inspired visuals
3. **Visual Hierarchy**: Clear distinction between headers, body, and metadata
4. **Data Clarity**: Tables and queries styled for analytical work
5. **Immersive Experience**: Decorative elements enhance without distracting
6. **Professional Presentation**: Suitable for research, education, and publication

---

## Tips for Best Experience

**Font Recommendations:**
If the theme fonts aren't loading, install these system fonts:
- [Crimson Text](https://fonts.google.com/specimen/Crimson+Text)
- [Cinzel](https://fonts.google.com/specimen/Cinzel)
- [Quattrocento Sans](https://fonts.google.com/specimen/Quattrocento+Sans)
- [Inconsolata](https://fonts.google.com/specimen/Inconsolata)

**Display Settings:**
- Use **Reading View** for final presentation
- Use **Source Mode** or **Live Preview** for editing
- Enable **Readable line length** for optimal readability
- Adjust base font size in Appearance settings if needed

**Graph View:**
- Enable **Force Layout** for best visual results
- Adjust node size to 3-5 for clarity
- Enable **Link arrows** to show relationships
- Use **Color groups** to see entry type distribution

---

## Updating the Theme

To update the theme with new features:

1. Edit `.obsidian/themes/TTRPG Historian/theme.css`
2. Save changes
3. Reload Obsidian (Cmd/Ctrl + R)
4. Changes apply immediately

---

## Version History

### v1.0 (October 2025)
- Initial release
- Parchment aesthetic with burgundy/gold accents
- Complete dark mode support
- Datacore table optimization
- Custom decorative elements
- Print-ready styles
- Mobile responsive design

---

## Credits

**Created for:** TTRPG History Vault v4.0

**Inspired by:**
- Classic D&D Player's Handbook design
- Illuminated medieval manuscripts
- Vintage gaming table aesthetics
- Modern web typography standards

**Fonts:**
- Crimson Text by Sebastian Kosch
- Cinzel by Natanael Gama
- Quattrocento Sans by Pablo Impallari
- Inconsolata by Raph Levien

---

## Support

For theme issues or customization help, see:
- [[START-HERE]] - Quick start guide
- [[SESSION-COMPLETION-REPORT]] - Latest vault updates
- `Documentation/` folder - Advanced guides

---

**Enjoy your historically immersive research environment!** 🎲📚⚔
