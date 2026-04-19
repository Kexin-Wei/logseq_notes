---
theme: surgical-sim
primary_count: 7
survey_papers: [21, 22, 23]
sim_platforms: [24, 25, 27]
---

# Theme: Surgical Simulation & Sim-to-Real

## Scope

Open-source simulators, digital twins, and sim-to-real transfer techniques specific to surgical robotics. **In scope:** surgical sim platforms (SurRoL, ORBIT-Surgical, SIM1), reality-gap surveys, digital-twin frameworks. **Out of scope:** RL policies trained in these sims (→ surgical-skill), world models of surgery (→ world-model).

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "surgical-sim")
SORT year ASC, paper_number ASC
```

**Manual fallback list:**

| # | Paper | Year | Tier | Role |
|---|-------|------|------|------|
| 21 | Surgical Digital Twins Survey | 2025 | S | Survey |
| 22 | Reality Gap Survey | 2025 | D | Survey |
| 23 | Sim-to-Real RL Survey | 2025 | K | Survey |
| 24 | SurRoL | 2021 | S | Platform |
| 25 | ORBIT-Surgical | 2024 | S | Platform |
| 26 | Med-Real2Sim | 2024 | K | Digital twin |
| 27 | SIM1 | 2026 | K | Platform (deformable) |

---

## Related-Work Paragraph Skeleton

> Training surgical robot policies typically requires simulation due to the cost and risk of real-robot data collection. Open-source platforms include SurRoL [@surrol2021], a Unity-based dVRK-compatible sim with material-point-method soft-body support; ORBIT-Surgical [@orbitsurgical2024], built atop NVIDIA Omniverse with GPU-accelerated physics and 14 standard surgical tasks; and SIM1 [@sim1_2026], targeting physics-aligned deformable-world simulation. Bridging simulation to real surgical robots raises the reality-gap problem [@realitygap2025]: sensor noise, tissue mechanics, and tool-tissue interaction rarely match simulator assumptions. General sim-to-real techniques in RL — domain randomization, system identification, adversarial domain adaptation — have been surveyed extensively [@simtoreal_rl_2025]. Medical digital twins [@medreal2sim2024] offer an alternative path via physics-informed self-supervised reconstruction of patient-specific models. **[contribution hook]**

## Review-Paper Paragraph Skeleton

> Surgical sim-to-real organizes along three axes: (i) **simulator fidelity** — rigid-body dVRK sims (SurRoL [@surrol2021]), GPU-accelerated scene simulation (ORBIT-Surgical [@orbitsurgical2024]), and deformable-physics extensions (SIM1 [@sim1_2026]); (ii) **transfer techniques** — domain randomization dominates, with recent additions of adversarial domain adaptation [@simtoreal_rl_2025] and physics-grounded self-supervision [@medreal2sim2024]; (iii) **evaluation protocols** — ex vivo tissue benchmarks (e.g., the cholecystectomy of SRT-H [@srth2025]) remain the gold standard, with live-animal validation emerging [@surgicalembodiedintel2025]. A parallel digital-twin literature [@digitaltwins2025] focuses on patient-specific modeling for preoperative planning rather than intraoperative policy learning, with only partial convergence between the communities.

## Gap → Contribution hooks

1. **No surgical sim supports force feedback at policy-training scale** (evidence: #51)
2. **Deformable-tissue sim remains fragmented** — SIM1 (#27) narrow, ORBIT-Surgical rigid-body dominant
3. **Digital twin vs policy sim** largely disjoint literatures
4. **Live-animal validation** still rare — mostly ex vivo

## Key quotes / numbers bank

- ORBIT-Surgical: 14 tasks, dVRK + STAR platforms
- SurRoL: open-source dVRK-compatible
- _[add as you read]_
