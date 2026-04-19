---
theme: world-model
primary_count: 10
landmark_papers: [12, 18]
survey_papers: [11]
key_bridge: [18]
---

# Theme: World Models for Embodied AI

## Scope

Methods that learn a latent predictive model of environment dynamics, usable for planning, policy rollout, or as an implicit policy. **In scope:** latent-dynamics models, JEPA-style encoders, action-conditioned video generators, joint video+action diffusion. **Out of scope:** pure VLA models (→ vla-foundation), simulator platforms (→ surgical-sim). **Bridge paper:** #18 Cosmos-Surg-dVRK connects this theme to surgical-fm.

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key, is_baseline
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "world-model")
SORT year ASC, paper_number ASC
```

**Manual fallback list:**

| # | Paper | Year | Tier |
|---|-------|------|------|
| 11 | World Models Survey | 2025 | D |
| 12 | World Models (Ha & Schmidhuber) | 2018 | D |
| 13 | LeCun JEPA | 2022 | S |
| 14 | DreamerV3 | 2024 | S |
| 15 | Genie | 2024 | S |
| 16 | UniSim | 2024 | K |
| 17 | Unified World Models | 2025 | S |
| 18 | Cosmos-Surg-dVRK (also surgical-fm) | 2025 | D |
| 19 | World Action Models | 2026 | S |
| 20 | LeWorldModel | 2026 | K |

---

## Related-Work Paragraph Skeleton (individual-paper use case)

> World models learn a latent predictive model of environment dynamics that can be used for planning or policy rollout. Ha and Schmidhuber [@ha2018world] introduced the vision-memory-controller decomposition that grounded modern work, later scaled by DreamerV3 [@dreamerv3_2024] to a single hyperparameter configuration solving 150+ diverse tasks. A parallel video-generation line — UniSim [@unisim2024], Genie [@genie2024] — treats world models as action-conditioned video generators. Recent work explores joint video-action pretraining (Unified World Models [@unifiedwm2025]), world models as zero-shot policies (World Action Models [@worldactionmodels2026]), and JEPA-style self-supervised dynamics (LeCun [@lecun2022], LeWorldModel [@leworldmodel2026]). In surgical robotics, Cosmos-Surg-dVRK [@cosmossurg2025] fine-tunes the NVIDIA Cosmos foundation model for dVRK simulation, representing the first bridge between modern world models and surgical autonomy. **[contribution hook]**

## Review-Paper Paragraph Skeleton (taxonomy focus)

> World models for embodied AI [@worldmodels2025survey] span four paradigms: (i) **recurrent latent-dynamics models** (Ha-Schmidhuber [@ha2018world], DreamerV3 [@dreamerv3_2024]); (ii) **action-conditioned video generators** (UniSim [@unisim2024], Genie [@genie2024]); (iii) **JEPA-style self-supervised encoders** (LeCun [@lecun2022], LeWorldModel [@leworldmodel2026]); and (iv) **joint video+action diffusion** (Unified WM [@unifiedwm2025]), the fourth enabling zero-shot policy extraction (World Action Models [@worldactionmodels2026]). Evaluation standards differ across paradigms — latent-dynamics models report simulated-RL scores (Atari, DMC), while video-generator world models use prediction-fidelity metrics — creating a metric fragmentation that impedes cross-paradigm comparison. Domain-specific adaptation to surgery is nascent: Cosmos-Surg-dVRK [@cosmossurg2025] is the sole surgical world model to date, trained on a limited dVRK corpus.

## Gap → Contribution hooks

1. **Only one surgical world model exists** (#18) — room for domain improvements
2. **No world model conditions on tactile/force** (evidence: #51)
3. **Policy extraction from video-generator WMs** (#19) untested on surgical tasks
4. **Metric fragmentation** — no unified evaluation between paradigms
5. **Ha-Schmidhuber V-M-C decomposition** never tested with deformable-tissue dynamics

## Key quotes / numbers bank

- DreamerV3: single hyperparameter set solves 150+ tasks
- Ha-Schmidhuber: "first to use generative world model trained end-to-end for RL"
- _[add as you read]_
