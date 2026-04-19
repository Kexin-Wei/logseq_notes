---
theme: tactile-force
primary_count: 4
survey_papers: [51]
gap_evidence: [51]
cross_cutting: true
---

# Theme: Tactile & Force Sensing (Gap Area)

## Scope

Methods that integrate tactile, force, or proprioceptive modalities into robot policies or foundation models. **In scope:** forceful FM survey, visuotactile perception, cross-sensor tactile representation, surgical tactile applications. **Secondary:** #54 TLA appears primarily in vla-foundation but is tactile-grounded. **This theme is the user's most likely gap area.**

## Members (auto via Dataview)

```dataview
TABLE year, venue, tier, bibtex_key
FROM "5. Embodied AI/Paper Notes"
WHERE contains(themes, "tactile-force")
SORT year ASC, paper_number ASC
```

**Manual fallback list:**

| # | Paper | Year | Tier | Role |
|---|-------|------|------|------|
| 51 | Forceful Robotic FMs | 2025 | D | Survey / gap-evidence |
| 52 | NeuralFeels | 2024 | S | Visuotactile perception |
| 53 | AnyTouch | 2025 | K | Cross-sensor repr. |
| 54 | TLA (primary vla-foundation) | 2025 | S | First tactile VLA |
| 55 | Colonoscopy Multimodal | 2026 | K | Surgical tactile |

---

## Related-Work Paragraph Skeleton

> Force and tactile sensing remain largely decoupled from the VLA and world-model paradigms [@forcefulfm2025]. NeuralFeels [@neuralfeels2024] demonstrates that visuotactile fusion improves pose tracking by 94% under occlusion. AnyTouch [@anytouch2025] proposes cross-sensor tactile representation learning across four distinct sensor types. TLA [@tla2025] is the first VLA to integrate tactile input, reporting 85%+ success on contact-rich manipulation. Surgical applications remain embryonic: multi-modal sensing in colonoscopy [@colonoscopy_multimodal_2026] is a rare example of force-aware surgical context modeling. The absence of tactile and force modalities in current surgical VLMs [@surgvlm2025] and surgical world models [@cosmossurg2025] is repeatedly flagged as a frontier [@forcefulfm2025; @zhong2025vla]. **[contribution hook: this is where your work lives]**

## Review-Paper Paragraph Skeleton

> The integration of tactile and force modalities into foundation-model policy learning is a nascent but rapidly growing area [@forcefulfm2025]. Methods partition by input representation: (i) **direct force/torque signals** from joint sensors, used in classical impedance control but rarely in learned policies; (ii) **tactile imagery** from GelSight/DIGIT sensors, used for pose estimation (NeuralFeels [@neuralfeels2024]) and cross-sensor transfer (AnyTouch [@anytouch2025]); (iii) **multimodal VLA inputs** — TLA [@tla2025] is the first published architecture to combine vision, language, and tactile for action generation. Surgical robotics provides a natural domain for such integration — tool-tissue interaction is inherently force-modulated — yet published examples remain limited to narrow applications [@colonoscopy_multimodal_2026]. Bridging tactile-grounded learning with surgical autonomy is an open research direction [@forcefulfm2025; @generalfm2024].

## Gap → Contribution hooks (high priority — user's likely direction)

1. **No surgical VLA uses tactile or force** (evidence: #51, #40, #48)
2. **No world model conditions on force input** (evidence: #11 survey silent on force)
3. **Tool-tissue interaction is fundamentally force-modulated** — strong domain alignment
4. **TLA (#54) shows tactile VLA works** in general robotics — surgical adaptation is the natural next step
5. **Surgical sim platforms lack force feedback** at policy-training scale (evidence: #22, #25)

## Key quotes / numbers bank

- NeuralFeels: 94% tracking improvement over vision-only under occlusion
- TLA: 85%+ success on contact-rich tasks
- _[add as you read]_
