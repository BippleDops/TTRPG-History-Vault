# Quality Standards

Comprehensive standards for vault content quality.

## Content Quality Tiers

### Tier 1: Minimal (Entry Accepted, Needs Expansion)
- 1,000+ words
- All required properties present
- 3+ WikiLinks
- 1+ Dataview query
- 1+ citation

**Status**: Acceptable for initial commit, flagged for expansion

### Tier 2: Standard (Production Quality)
- 2,000+ words
- All required + 50% optional properties
- 8+ WikiLinks
- 3 Dataview queries
- 3+ citations
- All sections complete

**Status**: Meets vault standards, ready for main branch

### Tier 3: Exemplary (Reference Quality)
- 3,000+ words
- All required + 80% optional properties
- 15+ WikiLinks
- 4+ Dataview queries
- 5+ citations from multiple sources
- All sections detailed and comprehensive
- Examples, quotes, or anecdotes included

**Status**: Featured content, model for other entries

## Writing Quality Standards

### Tone and Style
- **Encyclopedic**: Authoritative, factual, objective
- **Engaging**: Readable narrative flow, not dry bullet points
- **Accessible**: Explain jargon on first use, assume intelligent but non-expert reader

### Structure
- **Logical Flow**: Context → Details → Impact → Legacy
- **Scannable**: Use headers, bullet points, bold for key terms
- **Comprehensive**: Cover all major aspects (historical, mechanical, cultural)

### Language
- **Third Person**: Avoid "I", "you", "we"
- **Present/Past Tense Consistency**: Present for current facts, past for historical events
- **Active Voice Preferred**: "Gygax designed D&D" not "D&D was designed by Gygax"
- **Precise Vocabulary**: Use specific gaming terms correctly

### Citations
- **Primary Sources**: Original rulebooks, designer interviews, contemporary reviews
- **Secondary Sources**: Historical books (Peterson, Applecline), academic papers
- **Tertiary Sources**: Wikipedia, BGG (acceptable but cite better sources when possible)

## Technical Quality Standards

### Property Schema Compliance
- **100% Required Properties**: Never skip
- **80%+ Optional Properties**: Fill in everything possible
- **Correct Types**: Numbers as numbers, lists as lists, not strings
- **Consistent Formatting**: Dates always YYYY-MM-DD, names always "First Last"

### WikiLink Quality
- **Accuracy**: Links point to correct targets
- **Relevance**: Don't over-link trivial connections
- **Balance**: 8-15 links ideal (fewer = isolated, more = cluttered)
- **Bidirectional**: Always update reciprocal links

### Dataview Query Quality
- **Functional**: All queries execute without errors
- **Relevant**: Results meaningful to entry context
- **Performant**: Use WHERE clauses to limit scope
- **Readable**: Explicit column aliases, logical ordering

### Relationship Integrity
- **Bidirectional**: influence-on ↔ influenced-by consistent
- **Transitive**: Designer notable-works ↔ game designer consistent
- **Publisher**: key-releases ↔ game publisher consistent

## Research Quality Standards

### Source Requirements
- **Minimum 3 Sources**: For any entry
- **Primary Source Preferred**: Original rulebook, designer blog post, etc.
- **Cross-Verification**: Check facts across multiple sources
- **Citation Format**: "Author. *Title*. Publisher, Year. Page/URL."

### Fact-Checking
- **Dates**: Verify publication years (often disputed)
- **Names**: Check spelling of designers, publishers
- **Claims**: Verify "first" and "most" statements
- **Controversy**: Present multiple perspectives

### Disputed Information
- **Acknowledge**: Note when sources disagree
- **Present Multiple Views**: "According to Peterson..., but Gygax claimed..."
- **Cite Both**: Include both sources in references

## Maintenance Quality Standards

### Regular Updates
- **Annual Review**: Check if status changed (in-print → out-of-print)
- **New Editions**: Create entries for major new editions
- **Link Updates**: Verify no links broken as vault expands

### Version Control
- **Meaningful Commits**: Descriptive messages
- **Logical Grouping**: Related changes in single commit
- **No Mass Commits**: Don't commit 50 files at once without review

### Documentation
- **Update Changelog**: Note additions/changes
- **Update README**: If structure changes
- **Document Decisions**: Use comments for non-obvious choices

## Peer Review Standards

### For Reviewers
- **Constructive**: Suggest improvements, don't just criticize
- **Specific**: "Section X needs more detail on Y" not "Needs work"
- **Encouraging**: Recognize good work, welcome new contributors

### For Contributors
- **Receptive**: Accept feedback gracefully
- **Iterative**: Expect revisions, that's normal
- **Patient**: Quality takes time, don't rush

## Automated Quality Checks

### Pre-Merge Validation
- ✅ Link validator: 0 errors
- ✅ Schema validator: 0 errors, 85%+ completeness
- ✅ Reciprocal checker: 0 errors
- ✅ CI/CD pipeline: All checks pass

### Performance Benchmarks
- ✅ Vault load time: <3 seconds
- ✅ Query execution: <500ms per query
- ✅ Graph view render: <5 seconds
- ✅ Mobile responsiveness: Functional

---

*Quality standards evolve - suggest improvements via issues!*
