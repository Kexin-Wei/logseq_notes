---
paper_number: 2
title: "Vision Language Action Models in Robotic Manipulation: A Systematic Review"
year: 2025
venue: arXiv
section: S1
tier: S
status: skimmed
link: https://arxiv.org/abs/2507.10672
zotero: true
bibtex_key: vla_systematic_2025
primary_theme: vla-foundation
themes: [vla-foundation, survey]
is_baseline: false
is_survey: true
---
tags:: tier/S, survey, vla-foundation

# 02 — VLA Models in Robotic Manipulation: A Systematic Review

**Year:** 2025 | **Venue:** arXiv | **Section:** S1 | **Tier:** S | **Status:** (s) skimmed
**Link:** https://arxiv.org/abs/2507.10672

> Migrated from `Literature Review.md` archive (2026-04-19).

---

## Problem
No systematic comparison of VLA model architectures, benchmarks, and component choices for robotic manipulation.

## Key Insight
The dominant VLA stack has converged on **SigLIP vision + LLaMA language + diffusion action head**, trained on **Open X-Embodiment**, typically simulated in **NVIDIA Isaac Sim**.

## Method / Architecture Overview

A VLA model commonly has:
- **Encoder** — LLM-based, fuses visual information with the text-based query.
- **Decoder** — combines the encoder's output with a pure code structure for robot action, outputs the control signal for a simulated or real robot.

Dominant component choices:
- Vision encoder: **SigLIP**
- Language encoder: **LLaMA**
- Action decoder: **diffusion policy head**
- Dataset: **Open X-Embodiment** (standard public dataset)
- Simulator: **NVIDIA Isaac Sim** — supports LiDAR, force-torque feedback, large-scale RL, multi-robot / multi-agent, sim-to-real

## Key Models (from the survey)

| Model | Benchmark Datasets | Success Rate | Zero-Shot | Real-Robot | Notable Results |
|-------|-------------------|--------------|-----------|------------|-----------------|
| **RT-2** | Open X-Embodiment, BridgeData V2 | High | High | ✔ | Outperforms RT-1 and SayCan on generalization and zero-shot; strong internet-pretrained transfer |
| Octo | RLBench, Open X-Embodiment | Medium | Medium | ✔ | First diffusion-based generalist trained on 4M+ trajectories across 22 robots |
| **OpenVLA** | Open X-Embodiment, DROID | Medium | Medium | ✔ | LoRA fine-tuned, open-source VLA; competitive success with minimal tuning |
| Gato | Internal multi-task dataset | Medium | Medium | ✔ | Unified policy for vision, language, and robotics |
| **Pi-0** | Pi-Cross-Embodiment | Medium | Medium | ✔ | 200Hz+ low-latency control; generalizes to new embodiments |
| DexVLA | RT-X, RLBench | Medium | Medium | ✔ | Plug-in diffusion experts; cross-embodiment adaptation without fine-tuning |
| CLIPort | Ravens pick-and-place suite | Medium | Low | ✔ | CLIP-based dense transport, SOTA on tabletop tasks |
| **RoboAgent** | RoboSet | High | High | ✔ | CVAE action-chunking, semantic augmentation; strong real-world generalization |
| VIMA | VIMA dataset | Medium | Medium | ✔ | Prompt-based multimodal transformer; compositional generalization |
| **TLA** | TLA benchmark | Medium | High | ✔ | First language-tactile VLA; 85%+ success on contact-rich tasks |

*Success Rate: High (≥90%), Medium (70-90%), Low (<70%) — Zero-Shot: High (≥80% on unseen tasks), Medium (50-80%), Low (<50%)*

## Gap / Limitations
- Benchmarks focus on **success rate only**
- No standardised evaluation for **robustness, safety, or long-horizon tasks**

## Connections

- Complements: #1 Action Tokenization Survey, #63 Real-World Applications Review
- Models covered individually: #3 RT-2, #5 Octo, #6 OpenVLA, #7 pi_0, #54 TLA

---

## Writing-Ready Summary

### Citation
`@vla_systematic_2025` — _Authors_ (2025). *Vision Language Action Models in Robotic Manipulation: A Systematic Review*. arXiv:2507.10672.

### One-liner (paper-ready)
> A systematic review of VLA manipulation models [@vla_systematic_2025] identifies SigLIP+LLaMA+diffusion-head as the dominant architecture and Open X-Embodiment as the de facto benchmark.

### Alternative framings
- **As architecture consensus:** "The dominant VLA stack today combines SigLIP vision encoding, LLaMA language grounding, and a diffusion action head [@vla_systematic_2025]."
- **As gap motivator:** "Current VLA benchmarks focus narrowly on success rate, lacking standardized evaluation for robustness, safety, and long-horizon tasks [@vla_systematic_2025]."
- **As model-landscape reference:** "Among published VLAs [@vla_systematic_2025], RT-2, OpenVLA, and pi_0 remain the most commonly cited baselines; TLA is the first to integrate tactile input."

### Gap / what's next (contribution hook)
- Robustness, safety, long-horizon benchmarks missing
- No surgical-domain VLA evaluation
- Tactile/force inputs covered only by TLA

### Quotable snippets
- "SigLIP + LLaMA + diffusion head is the dominant architecture"
- "Open X-Embodiment is standard dataset"
