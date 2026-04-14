# Reference
	- [Coursera Learn AI Agents](https://www.coursera.org/learn/learn-ai-agents/)
	- [AI Agents in LangGraph](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)
	- [Multi AI Agent Systems with crewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/)
- # How to Build
	- Posts
	- ## Harness
		- References
			- [Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/)
				- ### Core Idea
					- LLMs are surprisingly good at reasoning about what is important to implement and what the next steps are.
					- one item per loop: trust Ralph to decide what's the most important thing to implement.
					- Core loop command: `while :; do cat PROMPT.md | claude-code ; done`
				- ### Loop Structure
					- phase one: generate + phase two: backpressure
					- Speed of the feedback loop matters more than perfect correctness
					- Context budget: ~170k tokens per loop; primary context acts as scheduler, not executor
					- Spawn subagents for expensive operations; avoid primary context window bloat
				- ### Essential File Stack (loaded every loop)
					- `@PROMPT.md` — main instructions for the loop
					- `@fix_plan.md` — prioritized bullet list of incomplete work, sorted by importance
					- `@specs/*` — one spec per file, written before implementation
					- `@AGENT.md` — the heart of the loop, instructs how Ralph should compile and run the project
				- ### Testing & Backpressure
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
				- ### Todo List & Placeholder Prevention
					- the todo list: Consider searching for TODO, minimal implementations and placeholders
					- LLMs chase compilation rewards; instruct them to implement fully, e.g. "DO NOT IMPLEMENT PLACEHOLDER... WE WANT FULL IMPLEMENTATIONS"
					- Generate fresh todo lists periodically using dedicated planning loops — delete and regenerate, don't let them grow stale
					- Always instruct: "Before making changes search codebase (don't assume not implemented)" — ripgrep can yield false negatives
				- ### Self-Improvement & Bug Tracking
					- ralph can take himself to university
					  The @AGENT.md is the heart of the loop. It instructs how Ralph should compile and run the project. If Ralph discovers a learning, permit him to self-improve:
					  
					  > When you learn something new about how to run the compiler or examples make sure you update @AGENT.md using a subagent but keep it brief. For example if you run commands multiple times before learning the correct command then that file should be updated.
					  
					  During a loop, Ralph might determine that something needs to be fixed. It's crucial to capture that reasoning.
					  
					  > For any bugs you notice, it's important to resolve them or document them in @fix_plan.md to be resolved using a subagent even if it is unrelated to the current piece of work after documenting it in @fix_plan.md
				- ### Feedback Loop
					- loop back is everything
					  
					  You want to program in ways where Ralph can loop himself back into the LLM for evaluation. This is incredibly important. Always look for opportunities to loop Ralph back on itself. This could be as simple as instructing it to add additional logging, or in the case of a compiler, asking Ralph to compile the application and then looking at the LLVM IR representation.
					  
					  > You may add extra logging if required to be able to debug the issues.
				- ### Subagents
					- Parallelize reads/searches/writes (up to 500 subagents) for non-critical work
					- Restrict builds/tests to single subagent to avoid backpressure collapse
					- Primary context acts as scheduler, subagents are the executors
				- ### Specs & Correctness
					- Begin projects with long conversations establishing requirements; generate formal specs before implementation
					- One spec per file in `@specs/` directory
					- If Ralph produces wrong code, specs are likely wrong — check for contradictions
					- Operator bears responsibility for spec accuracy, not the tool
				- ### Git & Recovery
					- Commit after tests pass with descriptive messages, push, create git tag on zero errors
					- Start at 0.0.0; increment patch version per successful cycle
					- You *will* wake to broken codebases that don't compile — decision: `git reset --hard` and restart, or craft rescue prompts
					- Try different LLM models (e.g. Gemini) if one gets stuck in error loops
				- ### Limitations
					- ~90% completion with Ralph, final 10% needs senior engineering judgment
					- Best suited for greenfield projects, not legacy codebases
					- Ralph has three states: underbaked, baked, or baked with unspecified behaviors
					- Watch `@fix_plan.md` like a hawk; throw it out and regenerate if needed
			- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
				- an **initializer agent** that sets up the environment on the first run, and a **coding agent** that is tasked with making incremental progress in every session, while leaving clear artifacts for the next session.
				- You can find code examples in the accompanying [quickstart.](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding)
				- The Claude Agent SDK is a powerful, general-purpose agent harness adept at coding, as well as other tasks that require the model to use tools to gather context, plan, and execute. It has context management capabilities such as compaction, which enables an agent to work on a task without exhausting the context window.
			- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
			- [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
		-
