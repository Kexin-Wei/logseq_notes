---
theme: surgical-skill
primary_count: 8
landmark_papers: [48]
survey_papers: [43]
dataset_papers: [50]
---

# Theme: Autonomous Surgical Skill Learning

## Scope

IL and RL methods that train closed-loop surgical policies — on dVRK or simulator platforms — for tasks like suturing, tissue lifting, blood suction, and full procedures like cholecystectomy. **In scope:** SRT, SRT-H, RL platforms, surgical datasets. **Out of scope:** general robot learning (→ vla-foundation), sim platforms themselves (→ surgical-sim).

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key, is_baseline
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "surgical-skill")
SORT year ASC, paper_number ASC
```

**Manual fallback list:**

| # | Paper | Year | Tier | Method |
|---|-------|------|------|--------|
| 43 | DRL in Surgical Robotics Survey | 2023 | S | Survey |
| 44 | SRT | 2024 | S | IL / transformer |
| 45 | SurgicAI | 2024 | K | Platform |
| 46 | SurgIRL | 2024 | K | Incremental RL |
| 47 | Safe RL for Surgery | 2024 | K | Safe RL |
| 48 | SRT-H | 2025 | D | Hierarchical IL |
| 49 | Surgical Embodied Intelligence | 2025 | S | Open-source + RL |
| 50 | ImitateCholec | 2025 | S | Dataset |

---

## Related-Work Paragraph Skeleton

> Autonomous surgical skill learning [@drl_surgical_2023] combines imitation learning and reinforcement learning on dVRK or simulator platforms. SRT [@srt2024] trained transformer policies on teleoperated demonstrations for tissue lifting, needle pickup, and suturing. Its successor SRT-H [@srth2025] introduced a hierarchical decomposition to achieve autonomous cholecystectomy on ex vivo tissue with 100% accuracy, the current benchmark result in autonomous surgery. Concurrent work extends RL-based skill learning with open-source simulators and live-animal validation (Surgical Embodied Intelligence [@surgicalembodiedintel2025]). Training data increasingly relies on large-scale datasets: ImitateCholec [@imitatecholec2025] provides 18K+ demonstrations from 34 porcine cholecystectomies. Peripheral work addresses platform engineering (SurgicAI [@surgicai2024]), lifelong learning (SurgIRL [@surgirl2024]), and safety constraints (Safe RL [@saferl_surgery_2024]). **[contribution hook]**

## Review-Paper Paragraph Skeleton

> Surgical skill learning [@drl_surgical_2023] organizes along three axes: (i) **learning paradigm** — behavioral cloning (SRT [@srt2024]), hierarchical IL (SRT-H [@srth2025]), RL with safety constraints (Safe RL [@saferl_surgery_2024]), incremental lifelong RL (SurgIRL [@surgirl2024]); (ii) **task complexity** — spanning atomic skills (lifting, suturing) to full procedures (cholecystectomy [@srth2025]); (iii) **data source** — teleoperated demonstrations (ImitateCholec [@imitatecholec2025], 18K+ porcine demonstrations), simulated rollouts (Surgical Embodied Intelligence [@surgicalembodiedintel2025]), or hybrid. The field has converged on dVRK + ex vivo tissue as the canonical evaluation setting, with live-animal validation emerging as a higher bar [@surgicalembodiedintel2025]. Foundation-model integration remains early — most autonomous policies are task-specific rather than building on VLAs or surgical VLMs.

## Gap → Contribution hooks

1. **Transformer-policy ≠ VLA** — SRT-H doesn't leverage pretrained VLM knowledge
2. **No world-model-based surgical policy** (bridge to world-model theme, #18 is sim-only)
3. **No tactile/force in skill learning** (evidence: #51)
4. **Procedure-level success is still single-procedure** — no generalization across surgery types
5. **Ex vivo → in vivo gap** — most results ex vivo only

## Key quotes / numbers bank

- SRT-H: 100% accuracy on ex vivo cholecystectomy
- ImitateCholec: 18K+ demonstrations, 34 porcine subjects
- _[add as you read]_
