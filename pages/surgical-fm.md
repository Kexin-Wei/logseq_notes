---
theme: surgical-fm
primary_count: 6
landmark_papers: [36, 40]
secondary_papers: [18]
---

# Theme: Surgical Foundation Models (VLM / LLM)

## Scope

Large multimodal models trained on surgical data — vision-language models for VQA, LLMs for action planning, perspective papers on foundation-model-driven autonomy. **In scope:** SurgicalGPT, Surgical-LVLM, SurgVLM, LLM-SAP. **Out of scope:** VLA models for general robotics (→ vla-foundation), pure perception models (→ surgical-perception). **Secondary:** #18 Cosmos-Surg-dVRK (primary world-model but also a surgical foundation model).

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key, is_baseline
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "surgical-fm")
SORT year ASC, paper_number ASC
```

**Manual fallback list:**

| # | Paper | Year | Tier | Role |
|---|-------|------|------|------|
| 18 | Cosmos-Surg-dVRK (primary world-model) | 2025 | D | World FM |
| 36 | FMs for Surgical Autonomy | 2024 | D | Perspective |
| 38 | SurgicalGPT | 2023 | K | Early VLM |
| 39 | Surgical-LVLM | 2024 | K | Personalized VLM |
| 40 | SurgVLM | 2025 | D | Large-scale VLM |
| 41 | LLM-SAP | 2025 | S | LLM planning |
| 42 | Multi-Modal LLM Blood Suction | 2025 | K | LLM action |

---

## Related-Work Paragraph Skeleton

> Foundation models are increasingly positioned as the enabler of surgical autonomy [@generalfm2024]. Early surgical vision-language models — SurgicalGPT [@surgicalgpt2023], Surgical-LVLM [@surgicallvlm2024] — focused on visual question answering with limited task breadth. SurgVLM [@surgvlm2025] scales this to a 7-72B parameter surgical VLM trained on 1.81M frames across 16+ surgery types, representing the first large-scale surgical VLM. A parallel direction applies LLMs to surgical action planning: LLM-SAP [@llmsap2025] plans from task descriptions using Qwen-family models, and multi-modal LLM systems [@bloodsuction2025] make intraoperative decisions for bleeding management. On the world-model axis, Cosmos-Surg-dVRK [@cosmossurg2025] fine-tunes NVIDIA Cosmos for surgical simulation. The bridge between surgical VLMs and closed-loop policy remains largely unrealized — SurgVLM is a perception+language model, not a VLA. **[contribution hook]**

## Review-Paper Paragraph Skeleton

> Surgical foundation models cluster into three pipelines: (i) **VLMs for understanding** — SurgicalGPT [@surgicalgpt2023], Surgical-LVLM [@surgicallvlm2024], SurgVLM [@surgvlm2025] — which output language/VQA responses; (ii) **LLMs for planning** — LLM-SAP [@llmsap2025], blood-suction planners [@bloodsuction2025] — which produce discrete action plans from symbolic state; (iii) **World foundation models** — Cosmos-Surg-dVRK [@cosmossurg2025] — which produce action-conditioned video futures. All three pipelines rely on visual backbones inherited from general vision (ViT, CLIP, DINO), with surgical adaptation primarily at the instruction-tuning stage. No open surgical foundation model to date produces closed-loop robot control in the VLA sense; the field is actively converging toward this [@generalfm2024].

## Gap → Contribution hooks

1. **No surgical VLA** — SurgVLM is VQA, not action (evidence: #40)
2. **LLM planning is open-loop** — no integration with closed-loop control (#41, #42)
3. **No surgical FM integrates force/tactile** (evidence: #51)
4. **Evaluation fragmented** — VQA benchmarks ≠ action benchmarks
5. **Cosmos-Surg-dVRK** is the only world-FM for surgery — room for improvement

## Key quotes / numbers bank

- SurgVLM: 1.81M frames, 16+ surgery types, 7B-72B params
- _[add as you read]_
