> **⚠️ ARCHIVED 2026-04-19** — this file has been superseded by:
> - Main lit review: [Surgical AI Literature Review.md](../Surgical%20AI%20Literature%20Review.md)
> - Per-paper notes: [Paper Notes/](./Paper%20Notes/)
> - Thematic view: [Themes/_MOC.md](../Themes/_MOC.md)
>
> Content migrated as follows:
> - Action Tokenization notes → [Paper Notes/01 - VLA Survey - Action Tokenization.md](../Paper%20Notes/01%20-%20VLA%20Survey%20-%20Action%20Tokenization.md)
> - Systematic Review notes → [Paper Notes/02 - VLA Systematic Review.md](../Paper%20Notes/02%20-%20VLA%20Systematic%20Review.md)
> - Real-World Applications Review notes → [Paper Notes/63 - VLA Real-World Applications Review.md](../Paper%20Notes/63%20-%20VLA%20Real-World%20Applications%20Review.md) (added as paper #63)
> - Reality Gap 6-step recipe → [Paper Notes/22 - Reality Gap Survey.md](../Paper%20Notes/22%20-%20Reality%20Gap%20Survey.md)
> - Paper Comparison Table → [Themes/vla-foundation.md](../Themes/vla-foundation.md)
>
> The content below is kept for reference only. Do not edit.

---

## Paper Comparison Table

| Paper                                      | Focus                         | Model Taxonomy                    | Key Takeaway                                                                                             |
| ------------------------------------------ | ----------------------------- | --------------------------------- | -------------------------------------------------------------------------------------------------------- |
| VLA in Robotic Manipulation (2025)         | Model benchmarks & components | By benchmark performance          | SigLIP + LLaMA + diffusion head is the dominant architecture; Open X-Embodiment is standard dataset      |
| VLA Review: Real-World Applications (2025) | Architecture & training       | Sensorimotor / World / Affordance | Supervised fine-tuning of action head or LoRA is the practical approach; hierarchical + CoT are emerging |
| VLA Survey: Action Tokenization (2025)     | Action representation         | 8 action token types              | Unifies VLA understanding through how actions are tokenised; framework for comparing models              |

## Key Models

The most important models are:
- RT-2: has VLMs like PaLM-E and PaLI-X as the backbone and discretized action tokens as the sensorimotor model,

---

## Paper Notes

# [Vision Language Action Models in Robotic Manipulation: A Systematic Review](https://arxiv.org/abs/2507.10672)
- **The Problem:** No systematic comparison of VLA model architectures, benchmarks, and component choices for robotic manipulation.
- **The Solution:** VLA model has commonly a large-language-model based encoder for visual information and text-based query. The combination of the encoder's output and a pure code structure for robot action serves as the input of a decoder, which outputs the robot action to control either a simulated robot or a real robot.
  SigLIP is popular as a vision encoder, and LLama is widely used as a language encoder, while as decoder diffusion policy head is common. The most popular public dataset is Open X-Embodiment, and the most widely-used simulation platform is Nvidia Issac Sim, which supports common modern sensors like LiDAR, contains various features like force-torque feedback, large-scale reinforcement learning, multi robot simulation, multi agent simulation as well as sim-to-real transfer.
- **The Gap:** Benchmarks focus on success rate; no standardised evaluation for robustness, safety, or long-horizon tasks.

### Models

| Model         | Benchmark Datasets               | Success Rate | Zero-Shot | Real-Robot | Notable Results                                                                                               |
| ------------- | -------------------------------- | ------------ | --------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| ==RT-2==      | Open X-Embodiment, BridgeData V2 | High         | High      | ✔          | Outperforms RT-1 and SayCan on generalization and zero-shot; strong multi-robot, internet-pretrained transfer |
| Octo          | RLBench, Open X-Embodiment       | Medium       | Medium    | ✔          | First diffusion-based generalist trained on 4M+ trajectories across 22 robots; robust sim-to-real             |
| ==OpenVLA==   | Open X-Embodiment, DROID         | Medium       | Medium    | ✔          | LoRA fine-tuned, open-source VLA; competitive success with minimal tuning                                     |
| Gato          | Internal multi-task dataset      | Medium       | Medium    | ✔          | Unified policy for vision, language, and robotics; real-robot zero-shot transfer                              |
| ==Pi-0==      | Pi-Cross-Embodiment              | Medium       | Medium    | ✔          | 200Hz+ low-latency control; generalizes to new embodiments and setups                                         |
| DexVLA        | RT-X, RLBench                    | Medium       | Medium    | ✔          | Plug-in diffusion experts; cross-embodiment adaptation without fine-tuning                                    |
| CLIPort       | Ravens pick-and-place suite      | Medium       | Low       | ✔          | CLIP-based dense transport achieves state-of-the-art on tabletop tasks                                        |
| ==RoboAgent== | RoboSet                          | High         | High      | ✔          | CVAE action-chunking, semantic augmentation; strong real-world generalization                                 |
| VIMA          | VIMA dataset                     | Medium       | Medium    | ✔          | Prompt-based multimodal transformer; compositional generalization, real-robot demos                           |
| ==TLA==       | TLA benchmark                    | Medium       | High      | ✔          | First language-tactile VLA; achieves 85%+ success on contact-rich tasks                                       |

*Success Rate: High (≥90%), Medium (70-90%), Low (<70%) | Zero-Shot: High (≥80% on unseen tasks), Medium (50-80%), Low (<50%)*

# [Vision-Language-Action Models for Robotics: A Review Towards Real-World Applications](https://arxiv.org/abs/2503.08906)
- **The Problem:** Gap between VLA research and real-world deployment — what architectures, training strategies, and data pipelines actually work?
- **The Solution:**

### Models

| Best Example | Action Head    | Key Strength                                               |
| ------------ | -------------- | ---------------------------------------------------------- |
| ==RT-1==     | Discrete Token | Proven real-world robustness, 97% success on 700+ tasks    |
| Octo         | Diffusion      | Flexible multi-robot generalist, strong sim-to-real        |
| RDT-1B       | Unified DiT    | Unified architecture, 1.2B params, strong cross-embodiment |
| ==OpenVLA==  | Discrete Token | Open-source, 7B params, accessible for research            |
| GO-1/DexVLA  | Diffusion      | Best for dexterous manipulation tasks                      |
| ==$\pi_0$==  | Flow Matching  | 50Hz control frequency, fastest inference                  |
| ==GR00T N==  | DiT            | State-of-the-art performance, NVIDIA-backed                |
 This paper focuses more on the architectures and training strategies in VLAs. It categorises the models into three types, sensorimotor model,  world model and affordance-based model. 
 - A sensorimotor model takes visual and linguistic inputs and output actions. 
 - A world model focuses on the generation of future visual observation based on current inputs, which guides the action generation.
 - An affordance-based model demonstrates the environmental limitations given on robot's physical and perceptual capabilities.
Most of the embodied AI uses direct sensorimotor model to control the robot via end-to-end training and achieves great success rate, such as *RT-2*, *OpenVLA* and $\pi_0$.

It is worth to mention that hierarchical architectures and Chain-of-Thought reasoning are the recent highlights. The former splits a task into sub-tasks, which can be finished by low-level VLAs. The latter decomposes a task to steps.

### Dataset
There are three ways to collect data: teleoperation, via proxy devices and human data. Proxy devices are attached to the robot mostly to the end-effector. Although human data collection can use same or similar devices yet there is no robot integrated in the collection process.

State-of-art data augmentation methods mainly focus on one of the modalities, either vision, language or action.
### Training
VLA training has three types: supervised learning, self-supervised learning and reinforcement learning.
- Supervised learning relies commonly on a pre-trained VLA, then fine-tunes it given a specific dataset or human teleoperation trajectories. In the post-training, it is suggested to only fine-tune the action head or use Low-Rank Adaptation *LoRA*
	- It is a common approach to use pre-trained VLM as the backbone inside VLA, such as *PaLM-E* in *RT-2* and *PaliGemma* in $\pi_0$ and $\pi_{0.5}$. 
- Self-supervised learning in VLAs has three approaches: modality alignment, visual representation learning and latent action representation learning. Note that the last one is suitable for large and unannotated datasets and scalable.
- Reinforcement learning integrates via either improving VLAs by interacting with environment  or serving as a low-level controller while a VLA makes high-level decision.

### Latency
Real-Time Chunking *RTC* mitigates delays in real-world execution.

### Future directions
This paper states a clear and structured potential improvements for real-world embodied AI, including
- Adding more modalities like tactile feedback into the VLA.
- integrating memory into long and complex robot task planning.
- Continual learning (or online learning) to adapt to new environment with successful attempts.
- Failure detection and replanning to enhance robot robustness and reliability in real world scenarios.

- **The Gap:** Tactile feedback, memory for long-horizon planning, and failure recovery remain largely unaddressed in current VLA systems.

# [A Survey on Vision-Language-Action Models: An Action Tokenization Perspective](https://arxiv.org/abs/2501.02816)
- **The Problem:** No unified framework for comparing how different VLA models represent and generate actions.
- **The Solution:** This survey presents a unified framework for understanding VLA models through the lens of **action tokenization**. It categorises action tokens into eight types: language description, code, affordance, trajectory, goal state, latent representation, raw action, and reasoning.
- **The Gap:** The taxonomy is descriptive; no empirical comparison of which tokenization strategy works best for which task type.

![Action Token Visualization](attachments/figure2_action_tokens_visualization.jpeg)
*Figure 2: Visualization of action tokens in a single embodied task. Given the same vision and language inputs, different VLA models encode them into diverse action tokens, each conveying varying forms of actionable guidance.*

![VLA Venn Diagram](attachments/figure4_vla_venn_diagram.jpeg)
*Figure 4: A Venn diagram showing the interrelationships among key AI fields. VLA models intersect with digital AI, hardware, and robotics, representing a core subfield of Embodied AI and a key area in the progression towards AGI.*

# 2025 The Reality Gap in Robotics: Challenges, Solutions, and Best Practices
![[attachments/_page_5_Picture_0.jpeg]]![[attachments/_page_10_Figure_0.jpeg]]
## Sim-to-Real Recipe  
1. Design a simulation that represents all variables relevant for the target application. 
2. Attempt to reduce the different components of the reality gap as much as possible. 
3. Design training methods that can help overcome the remaining gap. 
4. Train policies in simulation (ideally under massive parallelization). 
5. Evaluate policies in the target real-world environment. 
6. Adjust simulation parameters based on real performance and retrain.