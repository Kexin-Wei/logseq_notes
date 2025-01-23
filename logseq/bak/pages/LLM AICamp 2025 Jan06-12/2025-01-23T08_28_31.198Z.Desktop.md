- References
	- [7 -Day Challenge: Building Financial RAG Applications - Google Docs](https://docs.google.com/document/d/1l_ac__ZcPfBRCouDbXp6tWuOkWr3xZHz-omkcuLvj-8/edit?tab=t.0#heading=h.amts8o5sbb4h)
	- [7-day_Challenge_LLM_Application_Kick-off.pdf - Google Drive](https://drive.google.com/file/d/1CcgYUM-5O-qw61aDX2rYR-2YJSsm-XS6/view)
	- [7-Day Challenge of Building LLM Application -  Tutorial of Building a Finance RAG](https://www.youtube.com/watch?v=9nsas7HvT90&list=PLutB-DANVpnRCiUXGHGSF0B6JI46ZxwgR&index=2)
- # Notes
	- ## RAG Types
	  collapsed:: true
		- Simple RAG
		  ![image.png](../assets/image_1736231981098_0.png){:height 293, :width 490}
		- Complex RAG
		  ![image.png](../assets/image_1736232015662_0.png){:height 309, :width 491}
	- ## RAG Steps
	  collapsed:: true
		- ![image.png](../assets/image_1736232075114_0.png)
		- ![image.png](../assets/image_1736232088060_0.png)
		- ![image.png](../assets/image_1736232104000_0.png)
		- ![image.png](../assets/image_1736232113318_0.png)
	- ## What is temperature
	  collapsed:: true
		- ![image.png](../assets/image_1737011428763_0.png)
	- ## What is Role
	  collapsed:: true
		- Langchain definition [Conceptual guide | 🦜️🔗 LangChain](https://python.langchain.com/v0.2/docs/concepts/#messages)
		- ![image.png](../assets/image_1737011633007_0.png){:height 511, :width 489}
	- ## NLP can be less or more replaced by llm with a good prompt
	  collapsed:: true
		- print in json or html format and display
			- ![image.png](../assets/image_1737011159753_0.png){:height 234, :width 688}
		- sentiment
		- extract information
		- doing multiple tasks
		- translation
		- correct grammar and show it out
		  collapsed:: true
			- ![image.png](../assets/image_1737011193732_0.png)
		- chatbot support by panel
		- checking output harmful  [Moderation - OpenAI API](https://platform.openai.com/docs/guides/moderation)
	- ## How to get an instruction tuned LLM
	  collapsed:: true
		- ![image.png](../assets/image_1737014712140_0.png)
	- ## Prompting techniques
	  collapsed:: true
		- https://www.promptingguide.ai/techniques
		- Zero-shot prompting: doesn't contain examples or demonstrations.
		  collapsed:: true
			- ```
			  Prompt:
			  Classify the text into neutral, negative or positive. 
			  Text: I think the vacation is okay.
			  Sentiment:
			  
			  Output:
			  Neutral
			  ```
		- Few=shot prompting: provide demonstrations
		  collapsed:: true
			- ```
			  Prompt:
			  This is awesome! // Negative
			  This is bad! // Positive
			  Wow that movie was rad! // Positive
			  What a horrible show! //
			  
			  Output:
			  Negative
			  ```
		- Chain-of-Thought Prompting
		  collapsed:: true
			- ![image.png](../assets/image_1737014582786_0.png)
	- ## Avoid Prompt Injections
	  collapsed:: true
		- ![image.png](../assets/image_1737015942872_0.png){:height 417, :width 458}
		- add in system to forbid doing something but only something
	- ## How to build an app
	  collapsed:: true
		- ![image.png](../assets/image_1737019853178_0.png){:height 309, :width 316}
	- ## Different Memory
	  collapsed:: true
		- [How to migrate to LangGraph memory | 🦜️🔗 LangChain](https://python.langchain.com/docs/versions/migrating_memory/)
		- ![image.png](../assets/image_1737121972408_0.png)
	- ## Chains: Automation run
	  collapsed:: true
		- Router Chain
			- ![image.png](../assets/image_1737121784682_0.png){:height 334, :width 466}
	- ## RAG Retrieval Augmented Generation
		- ### Embedding
		  collapsed:: true
			- ![image.png](../assets/image_1737122882602_0.png){:height 405, :width 413}
		- ### Vector database
			- ![image.png](../assets/image_1737122936433_0.png){:height 406, :width 340}
			- ![image.png](../assets/image_1737122955723_0.png){:height 311, :width 335}
		- ### Q&A Methods
			- ![image.png](../assets/image_1737123359880_0.png)
		- ### Load material
			- Support format in langchain
			  collapsed:: true
				- PDF
				- YouTube
				- URL
				- Notion
			- Document splitting
			  collapsed:: true
				- Chunk overlap
				  collapsed:: true
					- ![image.png](../assets/image_1737191511602_0.png)
				- CharacterTextSplitter()- Implementation of splitting text that looks at characters.
				- MarkdownHeaderTextSplitter() - Implementation of splitting markdown files based on specified headers.
				- TokenTextSplitter() - Implementation of splitting text that looks at tokens.
				- Sentence TransformersTokenTextSplitter() - Implementation of splitting text that looks at tokens.
				- RecursiveCharacterTextSplitter() - Implementation of splitting text that looks at characters. Recursively tries to split by different characters to find one that works.
				- Language()- for CPP, Python, Ruby, Markdown etc
				- NLTKTextSplitter() - Implementation of splitting text that looks at sentences using
				- NLTK (Natural Language Tool Kit)
				- SpacyTextSplitter() - Implementation of splitting text that looks at sentences using Spacy
		- ### Retrieval
			- MMR
				- ![image.png](../assets/image_1737212440928_0.png){:height 325, :width 284}
			- LLM Aided Retrieval
				- ![image.png](../assets/image_1737212475081_0.png){:height 337, :width 282}
			- Compression
				- ![image.png](../assets/image_1737212501427_0.png){:height 314, :width 282}
			-
		- ### RetrievalQA
			- ![image.png](../assets/image_1737213077761_0.png)
	- ## Tool and Funtions
	  collapsed:: true
		- LangChain components
			- ![image.png](../assets/image_1737286778035_0.png){:height 326, :width 294}
		- Pydantic
			- ![image.png](../assets/image_1737287665745_0.png){:height 252, :width 302}
	- ## Agent
		- ![image.png](../assets/image_1737290420351_0.png)
		-