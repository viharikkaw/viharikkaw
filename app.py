import gradio as gr
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFacePipeline
from transformers import pipeline
import os


# Step 1: Load and split PDF into chunks
def create_vectorstore(pdf_path):
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()


    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)


    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore


# Step 2: Use a local HF model for generation
def build_llm():
    gen_pipeline = pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_length=200,
        temperature=0.3,
        do_sample=True,
    )
    return HuggingFacePipeline(pipeline=gen_pipeline)


# Globals to store chain
vectorstore = None
qa_chain = None


# Step 3: Gradio callbacks
def upload_pdf(pdf):
    global vectorstore, qa_chain
    vectorstore = create_vectorstore(pdf.name)
    llm = build_llm()
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return "✅ PDF uploaded and processed. Ask your questions!"


def ask_question(query):
    if not qa_chain:
        return "❌ Please upload a PDF first."
    return qa_chain.run(query)


# Step 4: Gradio UI
with gr.Blocks() as app:
    gr.Markdown("## 📄 RAG Chatbot (Offline, No OpenAI)")
    with gr.Row():
        pdf_input = gr.File(label="Upload your PDF", type="filepath")
        upload_btn = gr.Button("Process PDF")
    upload_output = gr.Textbox(label="Status", interactive=False)


    user_input = gr.Textbox(label="Ask a Question")
    response_output = gr.Textbox(label="Answer", lines=4)


    upload_btn.click(upload_pdf, inputs=pdf_input, outputs=upload_output)
    user_input.submit(ask_question, inputs=user_input, outputs=response_output)


app.launch()
