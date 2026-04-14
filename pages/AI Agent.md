# Reference
	- [Coursera Learn AI Agents](https://www.coursera.org/learn/learn-ai-agents/)
	- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)
	- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- # How to Build
	- Posts
	- ## Harness
		- ### Guidance
			- TODO: summarize after reading all references
		- ### References & Notes
			- [Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/)
				- LLMs are surprisingly good at reasoning about what is important to implement and what the next steps are.
				- one item per loop: trust Ralph to decide what's the most important thing to implement.
				- Core loop command: `while :; do cat PROMPT.md | claude-code ; done`
				- phase one: generate + phase two: backpressure
				- Speed of the feedback loop matters more than perfect correctness
				- Context budget: ~170k tokens per loop; primary context acts as scheduler, not executor
				- Spawn subagents for expensive operations; avoid primary context window bloat
				- Essential file stack (loaded every loop):
					- `@PROMPT.md` — main instructions for the loop
					- `@fix_plan.md` — prioritized bullet list of incomplete work, sorted by importance
					- `@specs/*` — one spec per file, written before implementation
					- `@AGENT.md` — the heart of the loop, instructs how Ralph should compile and run the project
				- Unit test: run a test just for that unit of code that was implemented and improved.
				- capture the importance of tests in the moment — include docstrings explaining *why* tests exist, future loops lose reasoning context
				- no cheating:
				  ```markdown
				  After implementing functionality or resolving problems, run the tests for that unit of code that was improved. If functionality is missing then it's your job to add it as per the application specifications. Think hard.
				  ```
				- Python, JavaScript, and Ruby:
				  If you're using a dynamically typed language, I must stress the importance of wiring in a static analyser/type checker when Ralphing, such as
				  [Dialyzer](https://www.erlang.org/doc/apps/dialyzer/dialyzer.html)
				  [Pyrefly](https://pyrefly.org/)
				  If you do not, then you will run into a bonfire of outcomes.
				- the todo list: Consider searching for TODO, minimal implementations and placeholders
				- LLMs chase compilation rewards; instruct them to implement fully, e.g. "DO NOT IMPLEMENT PLACEHOLDER... WE WANT FULL IMPLEMENTATIONS"
				- Generate fresh todo lists periodically — delete and regenerate, don't let them grow stale
				- Always instruct: "Before making changes search codebase (don't assume not implemented)" — ripgrep can yield false negatives
				- ralph can take himself to university
				  The @AGENT.md is the heart of the loop. It instructs how Ralph should compile and run the project. If Ralph discovers a learning, permit him to self-improve:
				  
				  > When you learn something new about how to run the compiler or examples make sure you update @AGENT.md using a subagent but keep it brief. For example if you run commands multiple times before learning the correct command then that file should be updated.
				  
				  During a loop, Ralph might determine that something needs to be fixed. It's crucial to capture that reasoning.
				  
				  > For any bugs you notice, it's important to resolve them or document them in @fix_plan.md to be resolved using a subagent even if it is unrelated to the current piece of work after documenting it in @fix_plan.md
				- loop back is everything
				  
				  You want to program in ways where Ralph can loop himself back into the LLM for evaluation. This is incredibly important. Always look for opportunities to loop Ralph back on itself. This could be as simple as instructing it to add additional logging, or in the case of a compiler, asking Ralph to compile the application and then looking at the LLVM IR representation.
				  
				  > You may add extra logging if required to be able to debug the issues.
				- Subagents: parallelize reads/searches/writes (up to 500), restrict builds/tests to single subagent
				- Specs: begin with long conversations establishing requirements, generate formal specs before implementation. Wrong code usually means wrong specs.
				- Git: commit after tests pass, push, tag on zero errors, increment patch version from 0.0.0
				- Recovery: expect broken codebases; `git reset --hard` or rescue prompts; try different models if stuck
				- ~90% completion with Ralph, final 10% needs senior engineering judgment; best for greenfield projects
			- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
				- an **initializer agent** that sets up the environment on the first run, and a **coding agent** that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session.
				- You can find code examples in the accompanying [quickstart.](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding)
				- The Claude Agent SDK is a powerful, general-purpose agent harness adept at coding, as well as other tasks that require the model to use tools to gather context, plan, and execute. It has context management capabilities such as compaction, which enables an agent to work on a task without exhausting the context window.
			- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
				- With this in mind, I wrote four grading criteria that I gave to both the generator and evaluator agents in their prompts:
				- **Design quality:** Does the design feel like a coherent whole rather than a collection of parts? Strong work here means the colors, typography, layout, imagery, and other details combine to create a distinct mood and identity.
				- **Originality:** Is there evidence of custom decisions, or is this template layouts, library defaults, and AI-generated patterns? A human designer should recognize deliberate creative choices. Unmodified stock components—or telltale signs of AI generation like purple gradients over white cards—fail here.
				- **Craft:** Technical execution: typography hierarchy, spacing consistency, color harmony, contrast ratios. This is a competence check rather than a creativity check. Most reasonable implementations do fine here by default; failing means broken fundamentals.
				- **Functionality:** Usability independent of aesthetics. Can users understand what the interface does, find primary actions, and complete tasks without guessing?
				- I ran 5 to 15 iterations per generation, with each iteration typically pushing the generator in a more distinctive direction as it responded to the evaluator's critique.
				- Across runs, the evaluator's assessments improved over iterations before plateauing, with headroom still remaining. Some generations refined incrementally. Others took sharp aesthetic turns between iterations.
				- Later implementations tended to be better as a whole, but I regularly saw cases where I preferred a middle iteration over the last one.
			- [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
		-