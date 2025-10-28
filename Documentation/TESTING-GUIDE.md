# Testing Guide

Comprehensive guide to testing vault functionality before committing changes.

## Pre-Commit Testing Checklist

### 1. Property Schema Validation

**Run Schema Validator**:
```bash
python Scripts/schema_validator.py --report schema-test.md
```

**Expected Results**:
- ✅ 0 errors for new entries
- ⚠️ Warnings acceptable for optional properties
- 90%+ completeness score

**Common Issues**:
- Missing required property → Add to frontmatter
- Wrong property type → Convert (string to number, etc.)
- Empty required field → Fill in value

### 2. Link Integrity Check

**Run Link Validator**:
```bash
python Scripts/link_validator.py --report link-test.md
```

**Expected Results**:
- ✅ 0 broken WikiLinks
- All suggestions reviewed

**Fixing Broken Links**:
- Target doesn't exist → Create stub entry or remove link
- Typo in link → Fix spelling
- Wrong folder → Correct path

### 3. Reciprocal Relationship Verification

**Run Reciprocal Checker**:
```bash
python Scripts/reciprocal_link_checker.py --report reciprocal-test.md
```

**Expected Results**:
- ✅ All influence-on/influenced-by relationships bidirectional
- ✅ Designer notable-works matches game designer properties
- ✅ Publisher key-releases matches game publisher properties

**Fixing Issues**:
- Missing reciprocal → Add to target file's property list
- Mismatched designer → Update either game or designer entry
- Orphaned reference → Remove or correct

### 4. Datacore Query Testing

**Manual Testing**:
1. Open entry in Obsidian
2. Switch to Reading View
3. Verify all ```datacore blocks render tables
4. Check query results are relevant (not empty, not excessive)

**Expected Results**:
- All queries display without "Error" messages
- Results have 1+ rows (unless legitimately empty)
- Column aliases display correctly ("Game" not "file.link")

**Fixing Query Errors**:
```datacore
Error: Property 'year-publihsed' not found
```
→ Fix typo: `year-published`

```datacore
Error: Folder 'Game' not found
```
→ Fix folder name: `"Games"`

### 5. Mobile Responsiveness Test

**If on desktop**:
1. Settings → Appearance → Reduce mode
2. Resize window to narrow width
3. Check entry renders well (no overflow, readable text)

**If on mobile device**:
1. Open Obsidian mobile app
2. Navigate to new/modified entries
3. Verify:
   - WikiLinks tappable
   - Datacore tables scroll horizontally
   - Images fit screen

### 6. Graph View Verification

**Testing**:
1. Open Graph View (Ctrl/Cmd + G)
2. Search for new entry title
3. Verify:
   - Node appears (entry was indexed)
   - Edges connect to related entries (WikiLinks created)
   - Node color matches type (if using graph CSS)

**Expected Results**:
- New game entry connects to publisher, designer, influenced games
- No isolated nodes (orphans)

### 7. Bases View Check

**Testing**:
1. Open relevant .base file (All-Games.base, Publishers.base, etc.)
2. Verify new entry appears in table
3. Check property values display correctly
4. Test sorting by different columns
5. Test filtering

**Expected Results**:
- Entry visible in appropriate Bases view
- All properties populated
- Sorting/filtering functional

## Post-Commit Regression Testing

### Full Vault Validation

**After merging PR or significant changes**:

```bash
# Run all validators
python Scripts/link_validator.py --report validation/links.md
python Scripts/schema_validator.py --report validation/schema.md
python Scripts/reciprocal_link_checker.py --report validation/reciprocal.md

# Check for regressions
diff validation/links.md validation/links-previous.md
```

**Performance Benchmarking**:
1. Close and reopen vault
2. Time load duration (should be <3 seconds)
3. Test query performance (run complex query, time execution)

**Smoke Tests**:
- Open 5 random entries → All render correctly
- Run 5 Datacore queries → All return results
- Check graph view → Loads in <5 seconds
- Open mobile app → Syncs and displays

## Automated Testing (CI/CD)

If using GitHub Actions (see `.github/workflows/validate.yml`):

**Triggers**:
- Every pull request to main/develop
- Every push to main

**Checks**:
1. Link validation (fails on broken links)
2. Schema validation (warns on incompleteness)
3. Reciprocal validation (fails on mismatches)

**Viewing Results**:
- Check "Actions" tab in GitHub
- Review validation reports in job summary
- Download artifacts for detailed reports

## Emergency Rollback

**If tests fail after commit**:

```bash
# Revert last commit
git revert HEAD

# Or reset to previous state
git reset --hard HEAD~1

# Push fix
git push --force-with-lease
```

**Preserving Work**:
```bash
# Save changes to stash before reverting
git stash save "Failed changes for review"

# Later, reapply and fix
git stash pop
# Fix issues
# Re-test
# Commit again
```

---

*Test thoroughly - fixing after commit is harder than testing before!*
