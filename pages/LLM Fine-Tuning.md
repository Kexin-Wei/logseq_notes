# Full Fine-Tuning (update everything)
	- All weights in the pretrained model get updated
	- Works well with enough data, but risks **overfitting** on small datasets
	- Example: Fine-tuning BERT for medical note classification (urgent vs routine)
	- ```python
	  from transformers import BertForSequenceClassification, Trainer, TrainingArguments
	  from datasets import Dataset
	  
	  # Pretrained BERT — already knows English, grammar, semantics
	  model = BertForSequenceClassification.from_pretrained(
	      "bert-base-uncased",
	      num_labels=2  # urgent vs routine
	  )
	  
	  # Your small domain-specific dataset
	  data = {
	      "text": [
	          "Patient showing signs of cardiac arrest, immediate intervention needed",
	          "Routine follow-up, vitals stable, no complaints",
	          "Severe bleeding, unresponsive, BP dropping fast",
	          "Annual checkup, all labs within normal range",
	      ],
	      "label": [1, 0, 1, 0]  # 1=urgent, 0=routine
	  }
	  dataset = Dataset.from_dict(data)
	  
	  # Tokenize
	  from transformers import BertTokenizer
	  tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
	  
	  def tokenize(example):
	      return tokenizer(example["text"], padding="max_length", truncation=True)
	  
	  dataset = dataset.map(tokenize, batched=True)
	  
	  # Training args — note the SMALL learning rate
	  training_args = TrainingArguments(
	      output_dir="./results",
	      num_train_epochs=3,
	      learning_rate=2e-5,      # small LR to preserve pretrained knowledge
	      per_device_train_batch_size=2,
	  )
	  
	  trainer = Trainer(
	      model=model,
	      args=training_args,
	      train_dataset=dataset,
	  )
	  
	  trainer.train()  # all ~110M parameters get updated
	  ```
- # Freezing Layers (only train the top)
	- Freeze all encoder layers — keep their learned representations
	- Only the classification head (new layer on top) gets trained
	- Like telling the med student: "your general knowledge is solid, just learn how to make this specific decision"
	- ```python
	  # Freeze all BERT encoder layers
	  for param in model.bert.parameters():
	      param.requires_grad = False
	  
	  # Only the classification head gets trained
	  for param in model.classifier.parameters():
	      param.requires_grad = True
	  
	  # Now training only updates a few thousand parameters instead of 110M
	  trainer.train()
	  ```
- # LoRA (Parameter-Efficient Fine-Tuning)
	- Modern approach, especially popular for LLMs where full fine-tuning is too expensive
	- Injects small trainable matrices into attention layers
	- Original weights stay **frozen**, only LoRA adapters train
	- ```python
	  from peft import LoraConfig, get_peft_model, TaskType
	  from transformers import AutoModelForCausalLM
	  
	  model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")
	  
	  # LoRA config — inject small trainable matrices into attention layers
	  lora_config = LoraConfig(
	      task_type=TaskType.CAUSAL_LM,
	      r=8,              # rank of the update matrices (small = efficient)
	      lora_alpha=32,    # scaling factor
	      lora_dropout=0.1,
	      target_modules=["q_proj", "v_proj"],  # only modify attention projections
	  )
	  
	  # Wrap the model — original weights are FROZEN, only LoRA adapters train
	  model = get_peft_model(model, lora_config)
	  model.print_trainable_parameters()
	  # Output: "trainable params: 4,194,304 || all params: 6,742,609,920 || 0.06%"
	  ```
- # Comparison
	- | Approach | Params Updated | Cost | Risk of Forgetting |
	  |---|---|---|---|
	  | Full fine-tuning | All (~100%) | High | High if small dataset |
	  | Layer freezing | Top layers only | Medium | Low |
	  | LoRA / Adapters | ~0.1% via small matrices | Low | Very low |
	- The tradeoff is always: **how much to adapt** vs **how much to retain**