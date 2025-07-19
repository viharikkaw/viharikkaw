from transformers import AutoTokenizer,AutoModelForCausalLM 
import torch 
model_name="TinyLlama/TinyLlama-1.18-chat-v1.0" 
tokenizer=AutoTokenizer.from_pretrained(model_name) 
model=AutoModelForCausalLM.from_pretrained(model_name) 
#zero-shot 
prompt="Definition of python LLM?"
inputs=tokenizer(prompt,return_tensors="pt") 
outputs=model.generation(**inputs,max_new_tokens=30)  
response=tokenizer.decode(outputs[0]) 
print(response)
