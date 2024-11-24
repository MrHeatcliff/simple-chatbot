from utils import *
from rag import *

from datasets import load_dataset

import numpy as np
import pandas as pd
import os

import faiss

import gradio as gr

DATASET_PATH = "vietnamese_ecommerce_alpaca_train.csv"

# check dataset downloaded or not
if not os.path.isfile(DATASET_PATH):
    # Load the dataset
    dataset = load_dataset("5CD-AI/Vietnamese-Ecommerce-Alpaca", split='train')
    # Save the dataset to a local directory as CSV
    dataset.to_csv('vietnamese_ecommerce_alpaca_train.csv')

# load model
pipe = load_model()


#load embedded
embedding_model = load_embedding_model()
embeddings = embedding_model.encode("init")

#read dataset, get output column
df = pd.read_csv("vietnamese_ecommerce_alpaca_train.csv")
documents = df['output'].tolist()

if not os.path.isfile("embeddings.npy"):
    #embedd output
    embeddings = embedding_model.encode(documents)
    np.save('embeddings.npy', embeddings)
else:
    embeddings = np.load('embeddings.npy')

# save embedding to faiss
index = faiss.IndexFlatL2(embeddings.shape[1])  # Index for vector search
index.add(embeddings)

chat_history = []

def chatchit(query):
    # context = ""
    query_embedding = embedding_model.encode([query])
    D, I = index.search(query_embedding, k=1)
    context = documents[I[0][0]]
    prompt = f"{query} với context là {context}"
    output0 = pipe(prompt, max_length=300)
    bot_response = output0[0]['generated_text']
    # Loại bỏ phần prompt khỏi kết quả
    bot_response = bot_response.replace(f"{query} với context là", "").strip()
    chat_history.append(("👤 " + query, "🤖 " + bot_response))
    return chat_history

with gr.Blocks(theme=gr.themes.Default()) as chatbot_interface:
    gr.Markdown( """
        # 🤖 Chatbot
        Ask me anything and I'll answer based on the provided context.
        """)
    chatbot = gr.Chatbot(label="Chat History")
    with gr.Row():
        query = gr.Textbox(placeholder="Hỏi tôi bất cứ thứ gì", show_label=False)
        send_button = gr.Button("Send")
    send_button.click(chatchit, inputs=[query], outputs=chatbot)
    query.submit(chatchit, inputs=[query], outputs=chatbot)

# Launch the chatbot
chatbot_interface.launch()