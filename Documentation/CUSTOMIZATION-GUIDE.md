# TTRPG History Vault - Customization Guide

This guide explains all the visual and functional customizations that have been added to enhance your vault experience.

---

## 🎨 CSS Snippets Installed

All CSS snippets are located in `.obsidian/snippets/` and are ready to enable.

### 1. Folder & File Icons (`ttrpg-folder-icons.css`)

**What it does**: Adds emoji icons to folders and special files for instant visual recognition.

**Icons Added**:
- 🎲 Games folder
- 🏢 Publishers folder
- 👤 Designers folder
- ⚙️ Mechanics folder
- 📰 Historical Context folder
- 📋 Templates folder
- 👁️ Views folder
- 🗄️ Research Archive folder
- 📝 Reviews & Analysis folder
- 📎 Attachments folder
- 📊 Dashboard files
- 🗺️ MOC files
- 📚 .base files
- 📖 README files

**How to enable**:
1. Go to Settings → Appearance → CSS snippets
2. Find `ttrpg-folder-icons` in the list
3. Click the toggle to enable
4. Restart Obsidian or reload the app

### 2. Custom Callouts (`ttrpg-callouts.css`)

**What it does**: Creates TTRPG-specific callout styles for highlighting different types of information.

**Available Callouts**:

```markdown
> [!game-stats] Game Statistics
> Your content here

> [!designer] Designer Information
> Your content here

> [!history] Historical Context
> Your content here

> [!mechanics] Mechanical Explanation
> Your content here

> [!publisher] Publisher Information
> Your content here

> [!impact] Significance & Impact
> Your content here

> [!source] Research Source
> Your content here

> [!timeline] Timeline Event
> Your content here

> [!early-era] Early Era Content
> Your content here

> [!golden-age] Golden Age Content
> Your content here

> [!modern-era] Modern Era Content
> Your content here
```

**Colors**:
- Game Stats: Green (#2E7D32)
- Designer: Blue (#1976D2)
- History: Purple (#9C27B0)
- Mechanics: Orange (#FF9800)
- Publisher: Teal (#009688)
- Impact: Red (#F44336)
- Source: Grey (#607D8B)
- Timeline: Pink (#E91E63)
- Early Era: Brown (#795548)
- Golden Age: Gold (#FFC107)
- Modern Era: Light Blue (#2196F3)

**How to enable**:
1. Settings → Appearance → CSS snippets
2. Enable `ttrpg-callouts`
3. Start using callouts in your notes!

### 3. Dashboard Layout (`dashboard-layout.css`)

**What it does**: Enhances the dashboard with better spacing, styled headers, and responsive layouts.

**Features**:
- Improved padding and spacing
- Accent-colored section headers
- Styled tables with background colors
- Grid layout for quick links
- Hover effects on links
- Responsive design for different screen sizes

**How to use**:
1. Enable the CSS snippet
2. Add `cssclass: dashboard` to your dashboard frontmatter:
```yaml
---
cssclass: dashboard
tags:
  - dashboard
  - moc
---
```

### 4. Graph View Colors (`graph-view-ttrpg.css`)

**What it does**: Color-codes graph nodes by folder type for visual clarity.

**Color Scheme**:
- Green nodes: Games
- Blue nodes: Publishers
- Purple nodes: Designers
- Orange nodes: Mechanics
- Red nodes: Historical Context
- Cyan nodes: Views
- Larger nodes: MOCs and Dashboard

**How to enable**:
1. Enable the `graph-view-ttrpg` snippet
2. Open Graph View (Ctrl/Cmd + G)
3. See your knowledge graph with color-coded nodes!

---

## 📋 Web Clipper Templates

Three specialized templates for capturing TTRPG research from the web.

### Template Locations

All templates are in `.obsidian/plugins/web-clipper-templates/`:
- `wikipedia-ttrpg.json` - For Wikipedia articles
- `youtube-ttrpg.json` - For YouTube videos
- `blog-article-ttrpg.json` - For blog posts and articles

### How to Install Templates

1. **Install the Obsidian Web Clipper browser extension**:
   - [Chrome/Edge](https://chrome.google.com/webstore)
   - [Firefox](https://addons.mozilla.org/firefox)
   - [Safari](https://apps.apple.com/app)

2. **Import templates**:
   - Click the Web Clipper extension icon
   - Click the gear icon (Settings)
   - Click "Import template"
   - Select each `.json` file from the folder above
   - Or copy-paste the JSON content directly

### Using the Templates

**Wikipedia Template**:
1. Visit any Wikipedia page about TTRPGs
2. Click Web Clipper icon
3. Select "TTRPG Wikipedia Article" template
4. Clip!
5. File appears in Research Archive/

**YouTube Template**:
1. Watch a TTRPG history video
2. Click Web Clipper icon
3. Select "TTRPG YouTube Video" template
4. Clip!
5. Video metadata and description saved to Research Archive/

**Blog/Article Template**:
1. Read an RPG news article or blog post
2. Click Web Clipper icon
3. Select "TTRPG Blog/Article" template
4. Clip!
5. Article content saved to Research Archive/

### Template Features

All templates automatically:
- Extract and format content
- Add proper frontmatter with metadata
- Include source URL and archive date
- Add appropriate tags
- Create research notes section
- Prompt for vault connections

---

## 🏠 Homepage Setup (Optional)

### Install Homepage Plugin

1. Settings → Community Plugins → Browse
2. Search for "Homepage"
3. Install and enable
4. Go to Settings → Homepage
5. Configure:
   - **Home note**: `Views/TTRPG-History-Dashboard`
   - **Open on startup**: ✅ Enabled
   - **Default view**: Reading View
   - **Revert to home note**: ✅ Enabled

Now your dashboard opens automatically when you launch Obsidian!

---

## 📊 Enhanced Dashboard Features

### Callout Usage Examples

Update your dashboard or any notes with these callout patterns:

**For Quick Stats**:
```markdown
> [!game-stats]+ Vault Statistics
> - **Total Games**: 5
> - **Total Publishers**: 5
> - **Total Designers**: 6
> - **Historical Events**: 3
```

**For Navigation Sections**:
```markdown
> [!timeline]+ Era Navigation
> - [[Early Era MOC|Early Era (1974-1985)]]
> - [[Golden Age MOC|Golden Age (1985-2000)]]
> - [[d20 Era MOC|d20 Era (2000-2008)]]
```

**For Important Information**:
```markdown
> [!impact] Getting Started
> 1. Install Templater plugin
> 2. Enable CSS snippets
> 3. Import Web Clipper templates
> 4. Start adding content!
```

---

## 🎯 Quick Reference: Enabling Everything

### 5-Minute Setup Checklist

- [ ] **CSS Snippets**:
  - [ ] Settings → Appearance → CSS snippets
  - [ ] Enable: `ttrpg-folder-icons`
  - [ ] Enable: `ttrpg-callouts`
  - [ ] Enable: `dashboard-layout`
  - [ ] Enable: `graph-view-ttrpg`

- [ ] **Dashboard Class**:
  - [ ] Open `Views/TTRPG-History-Dashboard.md`
  - [ ] Add `cssclass: dashboard` to frontmatter
  - [ ] Save

- [ ] **Homepage Plugin** (Optional):
  - [ ] Install from Community Plugins
  - [ ] Set home note to dashboard
  - [ ] Enable "Open on startup"

- [ ] **Web Clipper**:
  - [ ] Install browser extension
  - [ ] Import 3 JSON templates
  - [ ] Test on Wikipedia TTRPG page

- [ ] **Restart Obsidian** to see all changes!

---

## 🎨 Customization Options

### Changing Colors

Edit any `.css` file in `.obsidian/snippets/` to change colors:

**Callout Colors** (in `ttrpg-callouts.css`):
```css
.callout[data-callout="game-stats"] {
    --callout-color: 46, 125, 50;  /* RGB values */
}
```

Common RGB color codes:
- Red: `244, 67, 54`
- Blue: `33, 150, 243`
- Green: `76, 175, 80`
- Purple: `156, 39, 176`
- Orange: `255, 152, 0`
- Teal: `0, 150, 136`

**Folder Icon Colors**:
Change emoji in `ttrpg-folder-icons.css`:
```css
.nav-folder-title[data-path="Games"] .nav-folder-title-content::before {
    content: '🎮 ';  /* Change emoji here */
}
```

### Adding New Callouts

Add to `ttrpg-callouts.css`:
```css
.callout[data-callout="your-callout-name"] {
    --callout-color: 100, 150, 200;  /* Your RGB color */
    --callout-icon: lucide-icon-name;  /* Lucide icon */
}
```

Find icons at: https://lucide.dev/icons/

---

## 🔧 Troubleshooting

### CSS Snippets Not Working

1. Verify file is in `.obsidian/snippets/` folder
2. Check snippet is enabled in Settings → Appearance
3. Try reloading Obsidian (Ctrl/Cmd + R)
4. Check for CSS syntax errors (missing brackets, semicolons)

### Folder Icons Not Showing

1. Ensure exact folder names match CSS selectors
2. Restart Obsidian completely
3. Check if snippet is enabled
4. Try toggling snippet off and on again

### Callouts Not Rendering

1. Use exact callout name: `[!game-stats]` not `[!Game-Stats]`
2. Ensure CSS snippet is enabled
3. Check markdown syntax is correct
4. Switch to Reading View to see rendered callouts

### Web Clipper Templates Not Appearing

1. Verify JSON syntax is valid
2. Re-import template in extension settings
3. Check template triggers match the website
4. Update Web Clipper extension to latest version

### Dashboard Layout Not Applying

1. Verify frontmatter has `cssclass: dashboard`
2. Ensure `dashboard-layout.css` is enabled
3. View in Reading View (not Editing View)
4. Restart Obsidian

---

## 📚 Additional Resources

### Icon References

**Lucide Icons**: https://lucide.dev/icons/
- Full list of available icons for callouts
- Use format: `lucide-icon-name`

**Emoji Reference**: https://emojipedia.org/
- Search and copy emojis for folder icons
- Paste directly into CSS

### CSS Learning

**Obsidian CSS Snippets**: https://help.obsidian.md/Extending+Obsidian/CSS+snippets
- Official documentation
- Learn how to create custom snippets

**Community CSS Collection**: https://github.com/obsidian-community/obsidian-css-snippets
- Browse hundreds of community snippets
- Find inspiration for customizations

### Web Clipper

**Template Documentation**: https://help.obsidian.md/Web+Clipper/Web+Clipper+templates
- Official template syntax guide
- Learn advanced filters and selectors

**Template Variables**: https://help.obsidian.md/Web+Clipper/Web+Clipper+template+variables
- Complete list of available variables
- Schema.org metadata extraction

---

## 🎉 What's Been Enhanced

Your TTRPG History Vault now includes:

✅ **Visual Organization**
- Folder icons for instant recognition
- Color-coded graph view
- Styled dashboard with enhanced layout
- Professional callouts for content highlighting

✅ **Research Workflow**
- 3 specialized web clipper templates
- Automatic metadata extraction
- Structured research note format
- Easy vault integration prompts

✅ **Navigation**
- Homepage auto-opens dashboard
- Quick visual scanning with icons
- Color-coded knowledge graph
- Responsive layouts for all screen sizes

✅ **Professional Presentation**
- Polished visual design
- Consistent styling across vault
- Enhanced readability
- Publication-ready appearance

---

## 🚀 Next Steps

1. **Enable all CSS snippets** to see visual enhancements
2. **Add callouts** to existing game/publisher entries
3. **Install Web Clipper** and import templates
4. **Set up Homepage plugin** for automatic dashboard
5. **Start researching** and clipping TTRPG content!

Your vault is now a professional-grade TTRPG research and documentation system. Enjoy exploring and expanding your knowledge base!

---

*For questions or issues, refer to the main README.md or official Obsidian documentation.*
