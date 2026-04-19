tags:: template, tier/D

- ## D (Deep Read) Template
  Copy this when starting notes for a **landmark method paper** (~2-hour deep read). Filled-in reference: `03 - RT-2.md` (under `Embodied AI/Paper Notes/`).
- ### Frontmatter (at top, between `---` fences)
  ```yaml
  paper_number: NN
  title: "..."
  year: YYYY
  venue: ...
  section: S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8
  tier: D
  status: unread | skimmed | read
  link: https://...
  bibtex_key: authorYYYYfirstword
  primary_theme: vla-foundation | world-model | surgical-sim | surgical-perception | surgical-fm | surgical-skill | tactile-force | autonomy-regulation
  themes: [<primary>, landmark]
  is_baseline: true | false
  is_survey: false
  ```
- ### Immediately after frontmatter
  `tags:: tier/D, landmark, <theme>` (add `baseline-candidate` if applicable)
- ### Title line
  `# NN — <Paper Title>`
- ## Content
	- ### Problem
	  _What gap / failure mode this method addresses._
	- ### Method ← LEAD with this
	  _Architecture + training recipe + inference pipeline. Figures go here._
	- ### Key results / numbers
	  _Headline numbers. Comparisons to baselines._
	- ### Author-flagged limitations
	  _What the paper itself admits doesn't work._
- ## Connections
	- **Built on:** [predecessor / backbone]
	- **Variants:** [follow-up or alternative approaches]
	- **Superseded by:** [if applicable]
	- **Surgical analog:** [parallel method in surgical domain]
	- **Survey coverage:** [surveys that categorize this paper]
- ## For My Work
	- **Steal:** [technique / idea you'd reuse]
	- **Critique:** [weakness you'd address]
	- **Baseline?** [yes / no / conditional]
	- **Gap-hook:** [what limitation opens a contribution opportunity]
- ## Writing Assets
	- ### Citation
	  `@bibtex_key` — Authors (Year). *Title*. Venue.
	- ### One-liner ← functions as TL;DR
	  > Drop-in sentence naming the key contribution.
	- ### Alternative framings
		- **As paradigm origin:** "..."
		- **As baseline:** "..."
	- ### Quotable snippets
		- _[verbatim quotes on deep read]_
