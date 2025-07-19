#open source sentimental analyzer 
import gradio as gr 
from transformers import pipeline 

sentimental_analyzer=pipeline("sentiment-analysis")
def sentiment_analysis(text):
    result=sentimental_analyzer(text)[0]  
    label=result['label'] 
    accuracy=result['score'] 
    return f"{label}({accuracy})" 
gr.Interface(fn=sentiment_analysis,inputs=gr.Textbox(lines=4,placeholder="enter your text"),outputs="text").launch() 