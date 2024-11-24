from transformers import pipeline
from datasets import load_dataset

MODEL_NAME = "NlpHUST/gpt2-vietnamese"
DATASET = "5CD-AI/Vietnamese-Ecommerce-Alpaca"

def load_model():
    """Load model from huggingface"""
    return pipeline("text-generation", model=MODEL_NAME, device="cpu")

def download_dataset(data_file_name: str):
    """Download dataset to save as our vector database"""
    dataset = load_dataset(DATASET, split='train')
    dataset.to_csv(data_file_name)