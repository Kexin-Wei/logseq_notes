---
theme: vla-foundation
primary_count: 11
landmark_papers: [3, 4]
survey_papers: [1, 2]
key_gap_evidence: [51]
---

# Theme: Vision-Language-Action (VLA) Paradigm

## Scope

Methods that fine-tune pretrained vision-language models (VLMs) or equivalent multimodal architectures to output robot actions. Spans discrete action-token prediction, diffusion/flow-matching action heads, and dual-system architectures. **In scope:** general-purpose manipulation VLAs. **Out of scope:** pure perception models (→ surgical-perception), world-model policies (→ world-model), tactile-first models (→ tactile-force, though overlap exists).

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key, is_baseline
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "vla-foundation")
SORT year ASC, paper_number ASC
```

**Manual fallback list (if Dataview unavailable):**

| # | Paper | Year | Tier |
|---|-------|------|------|
| 1 | VLA Survey: Action Tokenization | 2025 | D |
| 2 | VLA Systematic Review | 2025 | S |
| 3 | RT-2 | 2023 | D |
| 4 | Diffusion Policy | 2023 | D |
| 5 | Octo | 2024 | K |
| 6 | OpenVLA | 2024 | K |
| 7 | pi_0 | 2024 | S |
| 8 | pi_0.5 | 2025 | S |
| 9 | Gemini Robotics 1.5 | 2025 | S |
| 10 | GR00T N1 | 2025 | S |
| 54 | TLA (also tactile-force) | 2025 | S |

---

## Related-Work Paragraph Skeleton (individual-paper use case)

> Vision-language-action (VLA) models emerged with RT-2 [@brohan2023rt2], which demonstrated that pretrained vision-language models can be fine-tuned to output robot actions as discrete text tokens. Concurrent work introduced denoising-diffusion action heads [@chi2023diffusion], enabling smoother multimodal control. Open-source efforts made the paradigm broadly accessible (Octo [@octo2024], OpenVLA [@openvla2024]) and scaled to flow-matching architectures with real-time inference (pi_0 [@pi02024]; pi_0.5 [@pi0_5_2025]). The current frontier targets large-scale multimodal reasoning (Gemini Robotics 1.5 [@gemini_robotics_1_5_2025]) and dual-system fast-slow architectures (GR00T N1 [@groot_n1_2025]). Despite rapid progress, VLAs remain primarily vision+language: TLA [@tla2025] is the first to integrate tactile input, and no open work extends the paradigm to surgical deformable-tissue manipulation. **[contribution hook: explain how your work fills this gap]**

## Review-Paper Paragraph Skeleton (taxonomy focus)

> Following the action-tokenization taxonomy of [@zhong2025vla], VLA models partition by action representation: (i) **discrete token prediction** (RT-2 [@brohan2023rt2], OpenVLA [@openvla2024]); (ii) **continuous diffusion or flow matching** (Diffusion Policy [@chi2023diffusion], pi_0 [@pi02024], pi_0.5 [@pi0_5_2025]); and (iii) **dual-system architectures** combining high-frequency reactive and lower-frequency deliberative modules (GR00T N1 [@groot_n1_2025]). Training uses VLM backbones (PaLI-X, PaliGemma, Gemini) with either FiLM-style injection or cross-attention over visual tokens. Evaluation has standardized on the Open X-Embodiment cross-embodiment benchmark and its derivatives. Parallel work on surgical VLMs (SurgVLM [@surgvlm2025]) has explored visual question answering but has not yet produced VLA-style closed-loop control. The integration of force and tactile modalities, highlighted as a research priority in [@forcefulfm2025], remains largely underexplored — with TLA [@tla2025] an early exception.

## Gap → Contribution hooks

1. **No tactile/force integration** across all major VLAs except #54 TLA (evidence: #51 survey)
2. **No surgical deformable-tissue VLA** — #40 SurgVLM is perception-only, #48 SRT-H is transformer-policy not VLA
3. **Action representation still contested** — tokens vs diffusion vs flow, no convergence
4. **No VLA with closed-loop world-model feedback** (evidence: #19 is cutting edge but not surgical)

## Survey Comparison

Three 2025 VLA surveys, placed side-by-side (migrated from earlier Literature Review notes):

| # | Paper | Focus | Model Taxonomy | Key Takeaway |
|---|-------|-------|----------------|--------------|
| 1 | Action Tokenization [@zhong2025vla] | Action representation | 8 action token types | Unifies VLA models by how actions are tokenised |
| 2 | Systematic Review [@vla_systematic_2025] | Model benchmarks & components | By benchmark performance | SigLIP+LLaMA+diffusion-head is the dominant architecture; Open X-Embodiment is standard |
| 63 | Real-World Applications [@vla_realworld_2025] | Architecture & training | Sensorimotor / World / Affordance | SFT of action head or LoRA is practical; hierarchical + CoT are emerging |

**Full model comparison table** (10 VLA models with benchmarks): see [02 - VLA Systematic Review](../Paper%20Notes/02%20-%20VLA%20Systematic%20Review.md).

**Model-by-action-head table** (7 models with action head families): see [63 - VLA Real-World Applications Review](../Paper%20Notes/63%20-%20VLA%20Real-World%20Applications%20Review.md).

---

## Key quotes / numbers bank (fill as you read)

- RT-2: emergent generalization over non-VLA baselines
- pi_0: 50 Hz real-time control
- TLA: 85%+ success on contact-rich tasks
- _[add as you fill individual D notes]_
