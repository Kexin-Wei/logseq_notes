tags:: template, tier/D, survey

- ## Review / Survey Paper Template
  Copy this when starting notes for a **survey or review paper**. Filled-in reference: `01 - VLA Survey - Action Tokenization.md` (under `Embodied AI/Paper Notes/`).
- ### Frontmatter (at top, between `---` fences)
  ```yaml
  paper_number: NN
  title: "..."
  year: YYYY
  venue: arXiv / Nature / IEEE ...
  section: S1 | S2 | S3 | S4 | S5 | S6 | S7 | S8
  tier: D
  status: unread | skimmed | read
  link: https://...
  bibtex_key: authorYYYYfirstword
  primary_theme: vla-foundation | world-model | surgical-sim | surgical-perception | surgical-fm | surgical-skill | tactile-force | autonomy-regulation
  themes: [<primary>, survey]
  is_baseline: false
  is_survey: true
  ```
- ### Immediately after frontmatter
  `tags:: tier/D, survey, <theme>`
- ### Title line
  `# NN — <Paper Title>`
- ## Content
	- ### Problem
	  _What gap in the literature prompted this survey._
	- ### Taxonomy / Framework ← LEAD with this
	  _The organizing axis the survey contributes — usually 3-8 categories. The "steal-able" framework._
	- ### Coverage
	  _Scope: # papers reviewed, year range, subfields included._
	- ### Author-flagged gaps
	  _What the survey itself says is unsolved / needs future work._
- ## Connections
	- **Complements:** #X survey (adjacent axis)
	- **Taxonomy applies to:** #A, #B, #C (papers this taxonomy categorizes)
	- **Gap ties to:** #Z (paper exemplifying a flagged gap)
- ## For My Work
	- **Steal:** [the taxonomy / framework]
	- **Critique:** [what the framework misses]
	- **Baseline?** N/A (survey)
	- **Gap-hook:** [what this survey leaves open that your contribution could fill]
- ## Writing Assets
	- ### Citation
	  `@bibtex_key` — Authors (Year). *Title*. Venue.
	- ### One-liner ← functions as TL;DR
	  > Drop-in sentence for related-work paragraph.
	- ### Alternative framings
		- **As taxonomy foundation:** "..."
		- **As gap-motivation:** "..."
	- ### Quotable snippets
		- _[verbatim quotes on deep read]_
