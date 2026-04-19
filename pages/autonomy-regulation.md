---
theme: autonomy-regulation
primary_count: 8
survey_papers: [37, 56, 57, 58]
---

# Theme: Autonomy Levels, Safety & Regulation

## Scope

Frameworks, taxonomies, and regulatory perspectives on surgical robot autonomy — LASR levels, IDEAL, FDA guidance, historical reviews, six-layer architectures. **In scope:** anything about *whether* surgical autonomy is safe, regulated, or approved. **Out of scope:** methods to achieve autonomy (→ surgical-skill), foundation models (→ surgical-fm).

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "autonomy-regulation")
SORT year ASC, paper_number ASC
```

**Manual fallback list:**

| # | Paper | Year | Tier | Role |
|---|-------|------|------|------|
| 37 | Surgical Robotics Classification Review | 2024 | S | Review |
| 56 | Autonomy in Surgical Robotics | 2021 | S | Foundational review |
| 57 | Decade Retrospective | 2021 | S | Historical |
| 58 | FDA-Cleared Robots: LASR Levels | 2024 | S | Systematic review |
| 59 | IDEAL Framework | 2024 | S | Dev. framework |
| 60 | Will Your Next Surgeon Be a Robot? | 2025 | S | Perspective |
| 61 | Human-Robot Collaboration | 2025 | K | Taxonomy |
| 62 | Six-Layer Architecture | 2025 | K | Architecture |

---

## Related-Work Paragraph Skeleton

> Surgical robot autonomy is constrained by regulatory and safety considerations [@attanasio2021autonomy]. The levels-of-autonomy-for-surgical-robotics (LASR) framework [@lasr2024] taxonomizes existing systems on a 1-5 scale; a 2024 systematic review [@lasr2024] finds that all FDA-cleared surgical robots between 2015-2023 remain at Level 1-2 (teleoperation with assistance). Development frameworks such as IDEAL [@ideal2024] structure the evaluation pathway from exploratory trials to long-term monitoring. Recent perspectives [@willyournextsurgeon2025] project how emerging FDA draft guidance on AI-enabled surgical devices may alter this trajectory. Complementary work on human-robot collaboration [@hrc_surgery_2025] and six-layer embodied architectures [@sixlayer2025] provides structural frameworks, emphasizing incremental autonomy within verifiable safety envelopes. **[contribution hook]**

## Review-Paper Paragraph Skeleton

> The autonomy-regulation literature [@attanasio2021autonomy; @decaderetro2021] defines three conceptual layers: (i) **taxonomic frameworks** — LASR levels 1-5 [@lasr2024], classification of surgical robots [@surgicalrobotics_class_2024]; (ii) **development protocols** — IDEAL stages [@ideal2024] structuring clinical validation; (iii) **prospective regulation** — FDA draft guidance on AI-enabled surgical devices, reviewed in [@willyournextsurgeon2025]. Despite the explosion of research on autonomous skill learning [@srth2025; @surgicalembodiedintel2025], the regulatory landscape remains conservative: no FDA-cleared system exceeds LASR Level 2. Structural proposals — human-robot collaboration taxonomies [@hrc_surgery_2025], six-layer architectures [@sixlayer2025] — emphasize incremental autonomy within verifiable safety envelopes, providing conceptual frames that research prototypes rarely engage with explicitly.

## Gap → Contribution hooks

1. **Research–regulation gap** — methods papers rarely engage LASR framework explicitly
2. **Safety envelope verification** for VLA/world-model policies is open
3. **IDEAL stages** haven't been mapped to foundation-model-driven systems
4. **FDA draft guidance** too new for empirical studies

## Key quotes / numbers bank

- LASR systematic review: all FDA-cleared robots 2015-2023 at Level 1-2
- _[add as you read]_
