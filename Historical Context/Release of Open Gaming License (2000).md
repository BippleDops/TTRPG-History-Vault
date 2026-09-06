---
aliases:
  - "Release of Open Gaming License"
  - "Open Gaming License"
  - "Open Game License"
  - "OGL"
type: historical-event
event-name: Release of the Open Gaming License
date: 2000-01-01
year: 2000
games-affected:
  - "[[Dungeons & Dragons Third Edition (2000)]]"
publishers-affected:
  - "[[Wizards of the Coast]]"
significance: 5
tags:
  - historical-event
  - ttrpg-history
  - ogl
  - d20-era
  - industry-changing
---

# Release of the Open Gaming License

**Date**: 2000
**Historical Significance**: ⭐ 5/5

## Overview

The Open Gaming License (OGL), released by Wizards of the Coast alongside Dungeons & Dragons Third Edition in 2000, represents one of the most transformative moments in RPG history. The OGL allowed third-party publishers to create content compatible with the d20 System, effectively opening D&D's mechanical foundation for community development while protecting Wizards' intellectual property.

This decision sparked the "d20 boom," created industry-wide standards, enabled countless new publishers, and fundamentally changed how RPG companies approached intellectual property and community creativity. The OGL's impact extended far beyond the initial intent, influencing open licensing across gaming and establishing precedents for community-driven content creation.

## Context and Background

In the late 1990s, Wizards of the Coast acquired TSR and began developing D&D Third Edition. Ryan Dancey, Wizards' VP of Tabletop Games, championed the OGL concept based on open-source software models. Dancey argued that D&D benefited from network effects—the more people creating compatible content, the more valuable the core D&D brand became.

Previous RPG publishers had guarded intellectual property jealously, viewing third-party content as competition. TSR had particularly antagonistic relationships with third-party creators, sending cease-and-desist letters to fan websites and shutting down unauthorized supplements.

The open-source software movement, particularly Linux's success, demonstrated that open licensing could create thriving ecosystems while maintaining brand value. Dancey proposed applying these principles to D&D, using the OGL to build a community platform rather than merely selling a product.

Internal debate at Wizards centered on risk—would open licensing cannibalize sales or strengthen the brand? Ultimately, Wizards adopted the OGL, betting that community creativity would expand the market more than third-party products would compete with official releases.

## Key Players

**Ryan Dancey**: VP of Tabletop Games at Wizards, primary architect of the OGL strategy. Dancey's vision transformed RPG publishing.

**Peter Adkison**: Wizards of the Coast CEO, approved the OGL despite internal concerns.

**Jonathan Tweet, Monte Cook, Skip Williams**: D&D 3rd Edition design team, created the d20 System the OGL would license.

**Wizards Legal Team**: Crafted the license language balancing openness with intellectual property protection.

**Third-Party Publishers**: Hundreds of companies that seized the opportunity to create d20 content.

## Games Affected

```dataview
TABLE file.link AS "Game", year-published AS "Year", publisher AS "Publisher"
FROM "Games"
WHERE year-published = number(2000) OR contains(games-affected, this.file.link) OR contains(string(tags), "d20") OR contains(string(tags), "ogl")
SORT title ASC
```

## Publishers Affected

The OGL affected virtually every RPG publisher:

**Beneficiaries**:
- Small publishers gained access to industry-standard mechanics
- New publishers entered the market using d20 as foundation
- Established publishers created d20 versions of their games

**Challenges**:
- Some publishers struggled with quality control as market flooded
- White Wolf and other major publishers faced competition from d20 alternatives
- The "d20 glut" eventually saturated the market

```dataview
TABLE file.link AS "Publisher", founded AS "Founded"
FROM "Publishers"
WHERE contains(publishers-affected, this.file.link) OR contains(string(tags), "d20-era")
```

## Immediate Impact

**Market Explosion**: Within months, dozens of publishers announced d20 products. By 2002, hundreds of d20-compatible products existed.

**Industry Standardization**: The d20 System became an industry standard, similar to how D&D established the RPG concept in 1974.

**New Publishers**: The OGL lowered barriers to entry, enabling new publishers to start with proven mechanics rather than designing from scratch.

**PDF Market**: Digital distribution via PDF became viable, with d20 supplements leading the way.

**Quality Variance**: The open license enabled anyone to publish, creating wide quality variance from amateur to professional products.

**Genre Expansion**: Publishers created d20 versions of nearly every genre—modern, sci-fi, horror, historical, superhero, etc.

## Long-term Consequences

**Paizo and Pathfinder**: When Wizards moved to D&D Fourth Edition without OGL support, Paizo created Pathfinder using the 3.5 OGL, eventually rivaling D&D in sales. This demonstrated the OGL's power—a third party could sustain a D&D alternative using Wizards' own licensed mechanics.

**OSR Movement**: The OGL enabled the Old School Renaissance (OSR), with designers creating retro-clones of early D&D editions using open mechanics.

**Industry Business Models**: The OGL influenced how publishers approached intellectual property, with some adopting similar open licensing.

**Community Empowerment**: Demonstrated that company and community could collaborate rather than operate adversarially.

**SRD Standard**: System Reference Documents (SRDs) became industry practice for communicating open mechanics.

**Legal Precedents**: Established legal frameworks for open gaming content still used today.

**2023 OGL Controversy**: The attempted OGL revision in 2023 created massive backlash, demonstrating the license's cultural importance. Community resistance forced Wizards to preserve OGL 1.0a.

## Industry Response

**Embraced by Small Publishers**: Most small publishers enthusiastically adopted d20 mechanics, creating an ecosystem around the license.

**Mixed Reception from Major Publishers**: White Wolf maintained separate mechanics but acknowledged the OGL's impact. Other publishers created d20 versions while maintaining proprietary systems.

**Quality Control Concerns**: Retailers faced challenges with flood of d20 products varying widely in quality.

**Creative Commons Influence**: The OGL inspired other open licenses in gaming, including Apocalypse World's Creative Commons license.

**WotC's Fourth Edition Decision**: Fourth Edition's restricted license showed Wizards' ambivalence about open licensing, though they returned to OGL-style openness with 5th Edition's SRD.

## Cultural Ripple Effects

**Democratization**: Publishing became accessible to hobbyists and amateurs, democratizing game creation.

**Community Culture**: The OGL fostered collaborative rather than competitive relationships between companies and fans.

**Educational Tool**: Game design students could learn using industry-standard mechanics rather than starting from scratch.

**Homebrew Legitimacy**: Fan creations gained quasi-official status when built on OGL mechanics.

**Open Culture**: Influenced broader gaming culture toward openness, community creation, and shared resources.

## Contemporary Commentary

**Ryan Dancey (2000)**: "The OGL is going to create an industry, not just support a game. It's about making D&D so ubiquitous that it becomes the default way people think about roleplaying."

**Monte Cook (2000)**: "The OGL changes everything. Now we're not just competing with other games—we're building a platform everyone can use."

**Publishers (2001-2002)**: Initial enthusiasm gave way to market saturation concerns as hundreds of d20 products competed for limited shelf space.

**Modern Perspective (2020s)**: The OGL is recognized as transformative, enabling Pathfinder, OSR games, and countless indie products while establishing community-company collaboration models.

## Historical Analysis

The OGL represents a radical shift in RPG publishing philosophy. TSR's aggressive IP protection had created adversarial relationships with fans. The OGL reversed this, inviting community participation and third-party creation.

The license's success validated open-source principles in commercial contexts. While some feared cannibalization, the OGL instead expanded the market, creating network effects that strengthened D&D's brand dominance.

However, the OGL's history reveals tensions between openness and control. Wizards' Fourth Edition pulled back from open licensing, though community resistance and Pathfinder's success demonstrated the OGL's cultural power. The 2023 OGL controversy showed that Wizards still viewed the license ambivalently, seeing it both as community benefit and potential business constraint.

The OGL ultimately proved that "rising tide lifts all boats"—the d20 boom expanded the RPG market, benefiting Wizards despite third-party competition. This lesson influenced business models across gaming industries.

## Timeline

- **1999**: Ryan Dancey proposes OGL concept at Wizards
- **January 2000**: OGL released alongside D&D Third Edition
- **2000-2002**: "d20 boom" with hundreds of compatible products
- **2003**: Market saturation creates "d20 glut," many publishers exit
- **2008**: Fourth Edition releases without OGL support
- **2009**: Paizo releases Pathfinder using 3.5 OGL
- **2008-2015**: OSR movement uses OGL for retro-clones
- **2014**: Fifth Edition releases with limited SRD
- **2023**: Attempted OGL revision creates backlash, Wizards preserves OGL 1.0a
- **2023**: Wizards releases D&D under Creative Commons alongside OGL

## Primary Sources and References

- Dancey, Ryan. "The Open Gaming Foundation." Various industry articles and interviews, 2000-2001.
- Open Gaming License 1.0a text. Wizards of the Coast, 2000.
- System Reference Document (SRD) for D&D 3rd Edition. Wizards of the Coast, 2000.
- Various publisher announcements and product releases, 2000-2003.
- Industry retrospectives and analyses, 2010s-2020s.
- The 2023 OGL controversy documentation and community response.
