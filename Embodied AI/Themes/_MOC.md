---
type: moc
themes: 8
total_papers: 62
---

# Themes MOC (Map of Content)

Cross-cutting thematic view of the 62 papers in the Surgical AI Literature Review. Each paper has exactly one `primary_theme` but may appear in multiple `themes` (secondary tags like `landmark`, `survey`, `baseline-candidate`, `gap-evidence`, `sim-platform`, `dataset`).

> **Dataview setup:** Some views below use the Dataview plugin. Install via `Settings → Community plugins → Browse → Dataview`. Without Dataview, the manual fallback lists in each theme file still work.

---

## Themes

| Theme | Papers | File |
|-------|--------|------|
| Vision-Language-Action (VLA) Paradigm | 11 | [vla-foundation](vla-foundation.md) |
| World Models for Embodied AI | 10 | [world-model](world-model.md) |
| Surgical Simulation & Sim-to-Real | 7 | [surgical-sim](surgical-sim.md) |
| Surgical Perception (LVM, 3DGS, SAM) | 8 | [surgical-perception](surgical-perception.md) |
| Surgical Foundation Models (VLM/LLM) | 6 | [surgical-fm](surgical-fm.md) |
| Autonomous Surgical Skill Learning | 8 | [surgical-skill](surgical-skill.md) |
| Tactile & Force Sensing | 4 | [tactile-force](tactile-force.md) |
| Autonomy Levels & Regulation | 8 | [autonomy-regulation](autonomy-regulation.md) |

---

## Global Queries

### All landmark papers

```dataview
TABLE year, venue, primary_theme, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "landmark")
SORT year DESC
```

### All baseline candidates

```dataview
TABLE year, venue, primary_theme, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE is_baseline = true
SORT primary_theme ASC
```

### All surveys / reviews

```dataview
TABLE year, venue, primary_theme, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE is_survey = true
SORT primary_theme ASC, year DESC
```

### All deep reads (D) by status

```dataview
TABLE year, primary_theme, status
FROM "5. Embodied AI/Paper Notes"
WHERE tier = "D"
SORT status ASC, primary_theme ASC
```

### Papers tagged as gap-evidence (for motivating your contribution)

```dataview
TABLE year, venue, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "gap-evidence")
```

---

## Cross-reference matrix (fill in as you read)

| Method / Dataset / Platform | Appears in themes | Representative papers |
|-----------------------------|-------------------|----------------------|
| dVRK (platform) | surgical-sim, surgical-skill | #24, #25, #44, #48 |
| SAM / SAM-2 (backbone) | surgical-perception | #32, #35 |
| 3D Gaussian Splatting | surgical-perception | #30, #31, #33, #34 |
| ORBIT-Surgical / Omniverse | surgical-sim | #25 |
| SurRoL | surgical-sim, surgical-skill | #24 |
| Cholecystectomy (task) | surgical-skill | #48, #50 |
| Diffusion action head | vla-foundation | #4, #7, #8 |
| Transformer backbone | vla-foundation, surgical-skill | #3, #44, #48 |

_Extend this table as you read — helps catch overlaps across themes when writing._

---

## Writing workflow (recommended)

1. **Before writing related work:** open the theme files relevant to your contribution (usually 2-4 themes).
2. **Copy the "Related-Work Paragraph Skeleton"** from each theme into your draft.
3. **Replace bibtex_key placeholders** with your actual citations (`@authorYYYYkeyword`).
4. **Fill in the gap→contribution hook** at the end of each theme paragraph.
5. **For a review paper:** use the "Review-Paper Paragraph Skeleton" instead — it organizes by taxonomy axis rather than chronology.
