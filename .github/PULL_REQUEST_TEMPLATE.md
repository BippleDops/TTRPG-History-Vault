# Pull Request

## Description

<!-- Provide a clear description of what this PR adds or changes -->

**Type of Change**:
- [ ] New game entry
- [ ] New publisher entry
- [ ] New designer entry
- [ ] New mechanic documentation
- [ ] New historical event entry
- [ ] Quality improvement to existing entry
- [ ] Link corrections
- [ ] Documentation update
- [ ] Bug fix
- [ ] Other (describe below)

**Summary**:
<!-- Brief summary of changes (1-2 sentences) -->

---

## Entries Added/Modified

<!-- List all new or modified entries -->

**New Entries**:
- [ ] `Games/[Game Title (Year)].md`
- [ ] `Publishers/[Publisher Name].md`
- [ ] `Designers/[Designer Name].md`

**Modified Entries**:
- [ ] `Path/to/entry.md` - Brief description of changes

---

## Validation Checklist

**Required - All must pass before PR can be merged**:

- [ ] All new entries use correct templates
- [ ] All required properties filled
- [ ] Property data types correct (numbers as numbers, lists as lists)
- [ ] WikiLinks use correct syntax `[[Target]]`
- [ ] Reciprocal relationships added (influence-on ↔ influenced-by, etc.)
- [ ] Related entries updated (publisher's key-releases, designer's notable-works)

**Code Validation** (run from vault root):
```bash
python Scripts/schema_validator.py
python Scripts/link_validator.py
python Scripts/reciprocal_link_checker.py
```

- [ ] `schema_validator.py` passes (exit code 0)
- [ ] `link_validator.py` passes (exit code 0)
- [ ] `reciprocal_link_checker.py` passes (exit code 0)

**Quality Standards** (see [[QUALITY-STANDARDS]]):

- [ ] New entries meet **Standard Quality** minimum:
  - 1,000+ words
  - 2-3 paragraphs per section
  - 4+ WikiLinks to related entries
  - All required properties filled

- [ ] Content is factually accurate
- [ ] Sources documented (if researched)
- [ ] Writing is clear and encyclopedic

---

## Related Issues

<!-- Link any related issues -->

Closes #<!-- issue number -->
Related to #<!-- issue number -->

---

## Additional Context

<!-- Add any additional context, screenshots, or notes -->

**Research Sources**:
-
-

**Notes for Reviewers**:
-

---

## Contributor Checklist

Before submitting:

- [ ] I have read [[CONTRIBUTING]]
- [ ] I have read [[QUALITY-STANDARDS]]
- [ ] My entries follow the property schemas in [[Property-Schema]]
- [ ] I have tested all embedded Datacore queries
- [ ] I have run all validation scripts and they pass
- [ ] My branch is up to date with `main`
- [ ] My commit messages follow the conventional format

**Commit Message Format**:
```
type: Brief description

- Detailed change 1
- Detailed change 2

Validation: All scripts pass
Quality: Standard/Exemplary
```

**Types**: `add`, `improve`, `fix`, `docs`, `refactor`

---

## Reviewer Notes

<!-- For maintainers/reviewers only -->

**Review Checklist**:
- [ ] Checkout branch and run validators locally
- [ ] Content quality meets standards
- [ ] Relationships properly reciprocated
- [ ] No merge conflicts
- [ ] Appropriate for main branch

**Feedback**:
<!-- Reviewers: Add feedback here -->
