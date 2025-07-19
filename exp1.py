import gradio as gr 
from transformers import pipeline 
llm=pipeline("text-generation",model="gpt2") 
def display(name):
    return f"hello {name}"
gr.Interface(fn=display,inputs="text", outputs="text").launch()  