from sentence_transformers import SentenceTransformer

import pandas as pd

EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

def load_embedding_model():
    return SentenceTransformer(EMBEDDING_MODEL)