#!/usr/bin/env python3
"""
WikiLink Integrity Checker for TTRPG History Vault

Scans markdown files for [[WikiLinks]] and verifies that each target resolves
the way Obsidian resolves it: to a note's file name, to a vault-relative path,
or to an alias declared in a note's ``aliases:`` frontmatter. Links inside
fenced code blocks and inline code are ignored (Obsidian does not resolve
those either), as are Templater placeholders in ``Templates/``.

Usage:
    python link_validator.py [--report output.md] [--max-broken N] [--top N]

Exit status is 1 when the number of broken links exceeds ``--max-broken``
(default 0), so the script can act as a CI gate. The workflow in
``.github/workflows/validate.yml`` passes an explicit threshold that should be
lowered ("ratcheted") every time broken links are fixed.
"""

import argparse
import re
import sys
from collections import Counter
from difflib import get_close_matches
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent

# Folders that are never scanned for links and never provide link targets.
EXCLUDED_DIRS = {".obsidian", ".git", ".trash", ".Trash", "node_modules", "Exports"}
# Folders that provide targets but whose own links are not checked
# (templates contain Templater placeholders, not real links).
UNCHECKED_DIRS = {"Templates"}

WIKILINK_RE = re.compile(r"(?<!\!)\[\[([^\]\|#\^]+)(?:[#\^][^\]\|]*)?(?:\|[^\]]*)?\]\]")
FENCE_RE = re.compile(r"^[ \t]*(```|~~~).*?^[ \t]*\1[ \t]*$", re.MULTILINE | re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", re.DOTALL)


def _is_excluded(rel_path):
    return any(part in EXCLUDED_DIRS for part in rel_path.parts)


def iter_notes():
    """Yield every markdown note in the vault outside the excluded folders."""
    for path in sorted(VAULT_ROOT.rglob("*.md")):
        if not _is_excluded(path.relative_to(VAULT_ROOT)):
            yield path


def extract_aliases(content):
    """Return the aliases declared in a note's frontmatter (without PyYAML)."""
    match = FRONTMATTER_RE.match(content)
    if not match:
        return []
    aliases = []
    lines = match.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        key_match = re.match(r"^(aliases|alias):\s*(.*)$", line)
        if not key_match:
            i += 1
            continue
        inline = key_match.group(2).strip()
        if inline.startswith("["):
            for item in inline.strip("[]").split(","):
                item = item.strip().strip("\"'")
                if item:
                    aliases.append(item)
        elif inline:
            aliases.append(inline.strip("\"'"))
        i += 1
        while i < len(lines) and re.match(r"^\s+-\s+", lines[i]):
            aliases.append(re.sub(r"^\s+-\s+", "", lines[i]).strip().strip("\"'"))
            i += 1
    return aliases


def build_index():
    """Return (targets, alias_owner) for the whole vault."""
    targets = set()
    alias_owner = {}
    for path in iter_notes():
        rel = path.relative_to(VAULT_ROOT)
        targets.add(path.stem)
        targets.add(str(rel.with_suffix("")).replace("\\", "/"))
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for alias in extract_aliases(content):
            alias_owner.setdefault(alias, path.stem)
    # Non-markdown attachments (images, .base views, PDFs) are valid targets too.
    for path in VAULT_ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() != ".md" and not _is_excluded(path.relative_to(VAULT_ROOT)):
            targets.add(path.name)
            targets.add(path.stem)
    return targets, alias_owner


def extract_wikilinks(content):
    """Extract WikiLink targets, ignoring code fences and inline code."""
    content = FENCE_RE.sub("", content)
    content = INLINE_CODE_RE.sub("", content)
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(content)]


def resolves(target, targets, alias_owner):
    if target in targets or target in alias_owner:
        return True
    if target.endswith(".md") and target[:-3] in targets:
        return True
    return False


def validate_vault():
    """Return (broken_links, total_links)."""
    targets, alias_owner = build_index()
    broken_links = []
    total_links = 0
    resolvable_names = sorted(targets | set(alias_owner))

    for path in iter_notes():
        rel = path.relative_to(VAULT_ROOT)
        if rel.parts[0] in UNCHECKED_DIRS:
            continue
        content = path.read_text(encoding="utf-8", errors="replace")
        for link in extract_wikilinks(content):
            total_links += 1
            if resolves(link, targets, alias_owner):
                continue
            suggestions = get_close_matches(link, resolvable_names, n=3, cutoff=0.6)
            broken_links.append({
                "file": str(rel).replace("\\", "/"),
                "broken_link": link,
                "suggestions": suggestions,
            })
    return broken_links, total_links


def generate_report(broken_links, total_links, max_broken, top=30):
    """Generate a markdown report."""
    status = "✅ PASS" if len(broken_links) <= max_broken else "❌ FAIL"
    report = ["# WikiLink Integrity Report\n\n"]
    report.append(f"**Status**: {status} (broken: {len(broken_links)}, threshold: {max_broken})\n\n")
    report.append(f"**Total Links Checked**: {total_links}\n\n")
    report.append(f"**Total Broken Links**: {len(broken_links)}\n\n")

    if not broken_links:
        report.append("✅ All WikiLinks are valid!\n")
        return "".join(report)

    counts = Counter(item["broken_link"] for item in broken_links)
    report.append(f"## Most Common Broken Targets (top {top})\n\n")
    report.append("| Count | Target |\n|------:|--------|\n")
    for target, count in counts.most_common(top):
        report.append(f"| {count} | `[[{target}]]` |\n")
    report.append("\n## Broken Links by File\n\n")
    for item in broken_links:
        report.append(f"### {item['file']}\n")
        report.append(f"- **Broken**: `[[{item['broken_link']}]]`\n")
        if item["suggestions"]:
            report.append(f"- **Suggestions**: {', '.join(f'`[[{s}]]`' for s in item['suggestions'])}\n")
        report.append("\n")
    return "".join(report)


def main():
    parser = argparse.ArgumentParser(description="Validate WikiLinks in TTRPG vault")
    parser.add_argument("--report", help="Output report to file")
    parser.add_argument("--max-broken", type=int, default=0,
                        help="Maximum number of broken links tolerated before exiting 1 (default: 0)")
    parser.add_argument("--top", type=int, default=30,
                        help="How many of the most common broken targets to list (default: 30)")
    args = parser.parse_args()

    broken, total = validate_vault()
    report = generate_report(broken, total, args.max_broken, args.top)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Report written to {args.report}")
    else:
        print(report)

    print(f"Checked {total} links: {len(broken)} broken (threshold {args.max_broken})")
    if len(broken) > args.max_broken:
        print("FAIL: broken links exceed threshold", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
