> **Start date:** 2026-04-19
> **Status:** Still exploring — no locked research direction yet
> **Capacity:** 3-4 hrs/day reading + research
> **Goal:** One submission to a credible venue in the robot learning / surgical AI space

---

## Reality Check

A realistic end-to-end timeline for a first paper in surgical embodied AI — starting from *"still exploring"* — is **4-6 months to submission**, not 6-8 weeks. The other AI's compressed timeline (2-3 weeks for experiments) ignores:

- Time to get ORBIT-Surgical / SurRoL / dVRK sim working (~2 weeks alone)
- Debugging policy training that doesn't immediately fail (~2-3 weeks)
- Advisor review cycles (always longer than planned)
- Writing rewrites when results shift

**Don't commit to a conference deadline until after Phase 2 (advisor lock-in).**

---

## Phase-by-Phase Timeline

| #   | Phase                          | Dates                   | Duration | Output                                                      |
| --- | ------------------------------ | ----------------------- | -------- | ----------------------------------------------------------- |
| 1   | Reading + mental model         | 2026-04-19 → 2026-05-10 | 3 weeks  | Gap statement + 2-3 candidate ideas + unified S1-S8 diagram |
| 2   | Advisor discussion + idea lock | 2026-05-11 → 2026-05-17 | 1 week   | ONE chosen direction with advisor buy-in                    |
| 3   | Infrastructure setup           | 2026-05-18 → 2026-06-07 | 3 weeks  | Working sim/data pipeline, baseline running                 |
| 4   | Prototype experiment           | 2026-06-08 → 2026-07-19 | 6 weeks  | Weak-but-real evidence the idea works                       |
| 5   | Refinement + full experiments  | 2026-07-20 → 2026-08-30 | 6 weeks  | Publishable numbers, ablations, baselines                   |
| 6   | Writing + figures              | 2026-08-31 → 2026-09-27 | 4 weeks  | Full draft, polished figures                                |
| 7   | Advisor feedback + revision    | 2026-09-28 → 2026-10-18 | 3 weeks  | Submission-ready paper                                      |

**Total: ~26 weeks (~6 months) → first submission window around late October 2026**

---

## Conference / Journal Targets

> Sorted by next deadline (chronological). Filter via the **Status** column:
> - **Upcoming** — deadline in the future this cycle
> - **Open** — rolling submission (journals, challenges, workshops)
> - **Closed** — this cycle's deadline already passed

| Venue                                   | Type       | Next deadline                        | Status   | Fit for your work                          | Timing vs your plan                                   |
| --------------------------------------- | ---------- | ------------------------------------ | -------- | ------------------------------------------ | ----------------------------------------------------- |
| **NeurIPS 2026**                        | Conference | 2026-05-06                           | Upcoming | ML breadth                                 | **Impossible** — ~2 weeks away                        |
| **CoRL 2026**                           | Conference | 2026-05-29                           | Upcoming | Robot learning                             | Very tight — only viable if experiments already exist |
| **ICRA 2027**                           | Conference | ~2026-09-15                          | Upcoming | Robotics + surgical                        | **Stretch** — requires 3-4 week compression           |
| **IPCAI 2027**                          | Conference | ~2026-10-30                          | Upcoming | Surgical CAI (small focused venue)         | **Primary target** — aligns with Phase 7 end          |
| **RSS 2027**                            | Conference | ~2027-01-30                          | Upcoming | Robot learning (high bar)                  | Comfortable                                           |
| **MICCAI 2027**                         | Conference | ~2027-02-26                          | Upcoming | Medical imaging + surgery                  | Comfortable — strong fallback                         |
| **IROS 2027**                           | Conference | ~2027-03-02                          | Upcoming | Robotics breadth                           | Comfortable                                           |
| **CoRL 2027**                           | Conference | ~2027-05-29                          | Upcoming | Robot learning                             | Very comfortable, room for iteration                  |
| Hamlyn Surgical Robot Challenge         | Challenge  | Rolling entry                        | Open     | Surgical robotics visibility (video-based) | Parallel track, low extra cost                        |
| ICRA / IROS / CoRL / NeurIPS workshops  | Workshop   | 1-2 mo after main conf notifications | Open     | Early-stage work, lower bar                | Good safety net for workshop paper                    |
| IEEE RA-L                               | Journal    | Rolling (3-4 mo review)              | Open     | Robotics letters; ICRA/IROS linkage option | Safety net — submit when ready                        |
| IEEE T-MRB (Medical Robotics & Bionics) | Journal    | Rolling (3-6 mo review)              | Open     | Medical robotics                           | Safety net                                            |
| IJCARS                                  | Journal    | Rolling (3-6 mo review)              | Open     | Surgical + imaging                         | Safety net                                            |
| Science Robotics                        | Journal    | Rolling (3-6 mo review)              | Open     | Top-tier                                   | Stretch — very selective                              |
| IEEE T-RO                               | Journal    | Rolling (6-12 mo review)             | Open     | Top robotics journal                       | Stretch — long review cycle                           |
| Nature Machine Intelligence             | Journal    | Rolling (4-8 mo review)              | Open     | Top ML/robotics                            | Stretch — very selective                              |
| IPCAI 2026                              | Conference | 2025-10-30                           | Closed   | —                                          | —                                                     |
| RSS 2026                                | Conference | 2026-01-30                           | Closed   | —                                          | —                                                     |
| MICCAI 2026                             | Conference | 2026-02-26                           | Closed   | —                                          | —                                                     |
| IROS 2026                               | Conference | 2026-03-02                           | Closed   | —                                          | —                                                     |
| Hamlyn 2026 (papers)                    | Symposium  | Closed                               | Closed   | —                                          | —                                                     |

---

## Recommended Target Strategy

**Primary target: IPCAI 2027** (deadline ~late October 2026)
- Aligns well with your ~6-month timeline
- Smaller venue, strong surgical/CAI community fit
- Long abstracts option lowers the bar for first submission
- If missed, easy to pivot to MICCAI 2027 (Feb) or IROS 2027 (March)

**Stretch target: ICRA 2027** (deadline ~mid-September 2026)
- Requires compressing Phases 5-6 by ~3-4 weeks
- Only attempt if Phase 4 prototype looks strong by July 2026

**Safety net: RA-L rolling submission** 
- No fixed deadline, can submit when ready
- Option to link to ICRA 2027 or IROS 2027 for presentation

---

## Key Decision Points

- **2026-05-10** — End of reading phase. Do you have 2-3 candidate ideas? If not, extend reading by 1 week max.
- **2026-05-17** — Advisor meeting. Lock the research direction. Do NOT proceed to Phase 3 without this.
- **2026-06-07** — Infrastructure checkpoint. If sim/data isn't working by this date, timeline slips 1-2 weeks.
- **2026-07-19** — Prototype checkpoint. If there's NO signal the idea works, pivot or descope — don't push through to deadline.
- **2026-08-30** — Results lock. Stop running experiments, start writing. If numbers aren't stable, target the next conference cycle instead of forcing a bad paper.

---

## Risk Factors (watch for these)

1. **Advisor availability** — 1-week turnaround on feedback is optimistic. Add buffer.
2. **Sim-to-real gaps** — ORBIT-Surgical to dVRK transfer often takes longer than expected.
3. **Idea overlap** — arxiv drops weekly. Re-scan S1-S8 topics every 2-3 weeks for scooping risk.
4. **Compute access** — training VLAs or world models needs real GPU time. Confirm access in Phase 3.
5. **Dataset access** — some surgical datasets require institutional review/IRB. Start this paperwork in Phase 2.

---

## Sources

- [ICRA 2026 Call for Papers](https://2026.ieee-icra.org/contribute/call-for-icra-2026-papers-now-accepting-submissions/) — ICRA 2026 deadline was 2025-09-15, ICRA 2027 likely similar pattern (~mid-Sept 2026)
- [IROS 2026 Important Dates](https://2026.ieee-iros.org/about/important-dates/) — deadline 2026-03-02 (closed)
- [MICCAI 2026 Important Dates](https://conferences.miccai.org/2026/en/IMPORTANT-DATES.html) — deadline 2026-02-26 (closed)
- [CoRL 2026 Call for Papers](https://www.corl.org/contributions/call-for-papers) — deadline 2026-05-29
- [NeurIPS 2026 Dates](https://neurips.cc/Conferences/2026/Dates) — deadline 2026-05-06
- [RSS 2026 Call for Papers](https://roboticsconference.org/information/cfp/) — deadline 2026-01-30 (closed)
- [IPCAI 2026](https://sites.google.com/view/ipcai2026) — IPCAI 2026 deadline was 2025-10-30; IPCAI 2027 likely ~Oct 2026
- [Hamlyn Symposium 2026](https://www.hamlynsymposium.org/) — paper submissions closed, Surgical Robot Challenge still open
- [IJCARS (Springer)](https://link.springer.com/journal/11548) — rolling journal submission
