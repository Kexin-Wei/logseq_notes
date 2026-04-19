---
paper_number: 63
title: "Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications"
year: 2025
venue: arXiv
section: S1
tier: S
status: skimmed
link: https://arxiv.org/abs/2503.08906
zotero: false
bibtex_key: vla_realworld_2025
primary_theme: vla-foundation
themes: [vla-foundation, survey]
is_baseline: false
is_survey: true
---

# 63 — VLA Models for Robotics: A Review Towards Real-World Applications

**Year:** 2025 | **Venue:** arXiv | **Section:** S1 | **Tier:** S | **Status:** (s) skimmed
**Link:** https://arxiv.org/abs/2503.08906

> Migrated from `Literature Review.md` archive (2026-04-19). Added to main lit review as paper #63.

---

## Problem
Gap between VLA research and real-world deployment — what architectures, training strategies, and data pipelines actually work?

## Key Insight
VLAs decompose into three model types — **sensorimotor**, **world**, **affordance** — with sensorimotor dominant in current practice; **hierarchical architectures** and **Chain-of-Thought reasoning** are the emerging directions; **tactile, memory, continual learning, and failure recovery** remain the key open problems.

## Taxonomy — Three VLA Model Types

| Type | What it does | Examples |
|------|--------------|----------|
| **Sensorimotor** | Takes visual + linguistic inputs, outputs actions directly (end-to-end) | RT-2, OpenVLA, π₀ |
| **World model** | Generates future visual observations; guides action generation | UniSim, Genie |
| **Affordance-based** | Represents environmental limitations given robot capabilities | (fewer published examples) |

Most current embodied AI uses direct **sensorimotor** end-to-end control.

## Key Models (from the review)

| Best Example | Action Head | Key Strength |
|--------------|-------------|--------------|
| **RT-1** | Discrete Token | Proven real-world robustness, 97% success on 700+ tasks |
| Octo | Diffusion | Flexible multi-robot generalist, strong sim-to-real |
| RDT-1B | Unified DiT | Unified architecture, 1.2B params, strong cross-embodiment |
| **OpenVLA** | Discrete Token | Open-source, 7B params |
| GO-1 / DexVLA | Diffusion | Best for dexterous manipulation |
| **π₀** | Flow Matching | 50 Hz control frequency, fastest inference |
| **GR00T N** | DiT | SOTA performance, NVIDIA-backed |

## Data Collection Methods
Three ways to collect VLA training data:
1. **Teleoperation** — operator controls robot directly
2. **Proxy devices** — mostly attached to end-effector during collection
3. **Human data** — same/similar devices but no robot in the loop

State-of-the-art data augmentation focuses on one modality at a time: vision, language, or action.

## Training Paradigms

1. **Supervised learning** — pretrain VLA, then fine-tune on specific dataset or teleoperation trajectories. Common practice: freeze backbone and tune only action head, or use **LoRA**. Pretrained VLM backbones: **PaLM-E** in RT-2, **PaliGemma** in π₀ / π₀.₅.
2. **Self-supervised learning** — three approaches: modality alignment, visual representation learning, latent action representation learning. The last is scalable to large unannotated datasets.
3. **Reinforcement learning** — either improves VLAs via environment interaction, or serves as low-level controller while VLA makes high-level decisions.

## Latency
**Real-Time Chunking (RTC)** mitigates delays in real-world execution.

## Emerging Directions
- **Hierarchical architectures** — tasks split into sub-tasks executed by low-level VLAs
- **Chain-of-Thought reasoning** — task decomposed into explicit reasoning steps before action

## Gap / Future Directions (stated by the paper)
- Add **tactile feedback** into the VLA
- Integrate **memory** for long, complex task planning
- **Continual learning** (online learning) for new environments
- **Failure detection and replanning** for robustness in real-world scenarios

## Connections

- Complements: #1 Action Tokenization Survey, #2 Systematic Review
- Hierarchical VLA → #10 GR00T N1 (dual-system architecture)
- CoT direction → related to world-model reasoning (#11 survey, #19 World Action Models)
- Tactile gap → directly supports #51 Forceful Robotic FMs
- Memory / long-horizon → #48 SRT-H (hierarchical surgery)

---

## Writing-Ready Summary

### Citation
`@vla_realworld_2025` — _Authors_ (2025). *Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications*. arXiv:2503.08906.

### One-liner (paper-ready)
> A review of VLAs for real-world robotics [@vla_realworld_2025] categorizes models into sensorimotor, world, and affordance types and identifies tactile feedback, memory, continual learning, and failure recovery as the key open problems.

### Alternative framings
- **As VLA taxonomy:** "VLAs can be partitioned into sensorimotor (direct action output), world-model-based (future-frame prediction), and affordance-based (capability-constrained) architectures [@vla_realworld_2025]."
- **As gap citation (strong for your tactile direction):** "Published VLA systems still lack tactile feedback, long-horizon memory, continual learning, and reliable failure recovery [@vla_realworld_2025]."
- **As training-recipe reference:** "Supervised fine-tuning of action heads (often via LoRA) remains the practical training recipe for VLAs [@vla_realworld_2025]."

### Gap / what's next (contribution hook)
- **Tactile feedback** — strongly motivates your direction if tactile-focused
- Long-horizon memory
- Continual / online learning
- Failure detection + replanning

### Quotable snippets
- "Adding more modalities like tactile feedback into the VLA" (stated future direction)
- "Hierarchical architectures and Chain-of-Thought reasoning are the recent highlights"
