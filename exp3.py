#image to text then translate to regional language
from transformers import BlipProcessor,BlipForConditionalGeneration
from PIL import Image
import requests
from transformers import MBartForConditionalGeneration,MBart50TokenizerFast 
processor=BlipProcessor.from_pretrained("salesforce/blip-image-captioning-base")
model=BlipForConditionalGeneration.from_pretrained("salesforce/blip-image-captioning-base")
url="https://plus.unsplash.com/premium_photo-1751906599417-05d9577656a2?q=80&w=2075&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
image=Image.open(requests.get(url,stream=True).raw).convert("RGB")
#create and initialize model and fretch text
inputs=processor(image,return_tensors="pt")
output=model.generate(**inputs)
caption=processor.decode(output[0])
#Load MBart model 
model_name="facebook/mbart-large-50-many-to-many-mmt" 
tokenizer=MBart50TokenizerFast.from_pretrained(model_name) 
model=MBartForConditionalGeneration.from_pretrained(model_name) 
tokenizer.scr_lang="en_XX" 
target_lang="te_IN" 
inp_lang=tokenizer(caption,return_tensors="pt") 
out_tok=model1.generate(**inp_lang,forced_bos_token_id=tokenizer.lang_code_to_id[target_lang]) 
caption_te=tokenizer.decode(out_tok[0]) 