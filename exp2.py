import gradio as gr 
from transformers import pipeline
from PIL import Image 
classifier=pipeline("image-classification",model="google/vit-base-patch16-224") 
#create function with model call 
def classify_image(image): 
    image=image.convert("RGB") 
    results=classifier(image) 
    return{res['label']:res['score'] for res in results[:3]}
gr.Interface(fn=classify_image,inputs=gr.Image(type="pil"),outputs=gr.Label(num_top_classes=3),title="Vision Transformer Image Classifier",description="upload an image to get top 3 predictions").launch() 