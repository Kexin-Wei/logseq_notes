---
theme: surgical-perception
primary_count: 8
survey_papers: [28, 29]
---

# Theme: Surgical Perception (LVM, 3DGS, SAM)

## Scope

Methods that adapt large vision models to surgical scene understanding: segmentation, tracking, 3D reconstruction, and synthetic-data generation. **In scope:** SAM/SAM-2 variants for surgery, 3D Gaussian Splatting for endoscopic reconstruction, foundation-model surveys. **Out of scope:** VLMs with language output (→ surgical-fm), VLAs with perception (→ vla-foundation).

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "surgical-perception")
SORT year ASC, paper_number ASC
```

**Manual fallback list:**

| # | Paper | Year | Tier | Method family |
|---|-------|------|------|---------------|
| 28 | LVMs for RAS | 2025 | D | Review |
| 29 | Scene Understanding Survey | 2025 | S | Survey |
| 30 | SurgicalGaussian | 2024 | S | 3DGS |
| 31 | Endo-4DGS | 2024 | K | 3DGS |
| 32 | Surgical-DeSAM | 2024 | S | SAM |
| 33 | Realistic Surgical Dataset (3DGS) | 2024 | K | Data gen |
| 34 | SAGS | 2025 | K | 3DGS |
| 35 | ReSurgSAM2 | 2025 | K | SAM-2 |

---

## Related-Work Paragraph Skeleton

> Surgical scene understanding has been transformed by large vision models [@lvmras2025]. Foundation segmenters such as Surgical-DeSAM [@surgicaldesam2024] adapt SAM for instrument segmentation, achieving 89-91% Dice on EndoVis 2017/2018; ReSurgSAM2 [@resurgsam2_2025] extends SAM-2 to referring segmentation in surgical video. Dynamic scene reconstruction has shifted from NeRF to 3D Gaussian Splatting: SurgicalGaussian [@surgicalgaussian2024] and Endo-4DGS [@endo4dgs2024] reconstruct deformable endoscopic scenes in real time, while SAGS [@sags2025] achieves state-of-the-art on EndoNeRF and SCARED benchmarks. Synthetic-data pipelines built on 3DGS [@realistic3dgs2024] offer a scalable alternative to curated real surgical corpora. Together these perception primitives — segmentation, tracking, reconstruction — form the input layer for surgical foundation models [@generalfm2024; @surgvlm2025] and autonomous policy pipelines [@srth2025]. **[contribution hook]**

## Review-Paper Paragraph Skeleton

> The surgical perception landscape [@lvmras2025; @scene_understanding_2025] can be partitioned into three task families: (i) **segmentation** (instrument and anatomy), where SAM-family adaptations dominate — Surgical-DeSAM [@surgicaldesam2024] for surgical instruments, ReSurgSAM2 [@resurgsam2_2025] for referring segmentation; (ii) **3D reconstruction** of deformable scenes, where 3D Gaussian Splatting variants (SurgicalGaussian, Endo-4DGS, SAGS) have replaced NeRF as the dominant paradigm; (iii) **synthetic data generation**, leveraging 3DGS pipelines [@realistic3dgs2024] to augment scarce annotated corpora. Common backbones — SAM, SAM-2, DINO, CLIP — are largely inherited from general vision with lightweight surgical adaptation. Cross-task models (unified segmentation+reconstruction+understanding) remain rare.

## Gap → Contribution hooks

1. **Segmentation, reconstruction, understanding remain siloed** — no unified surgical perception model
2. **No perception model outputs force-predictive features** (bridge to tactile-force theme)
3. **3DGS surgical datasets are tiny** compared to general vision — data bottleneck
4. **Evaluation benchmarks are not standardized** across tasks

## Key quotes / numbers bank

- Surgical-DeSAM: 89.6-90.7% Dice on EndoVis 2017/2018
- SAGS: SOTA on EndoNeRF and SCARED
- _[add as you read]_
