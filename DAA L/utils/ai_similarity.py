# --- FILE: utils/ai_similarity.py ---

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# BERT (already available)
def bert_similarity(text1, text2):
    from transformers import AutoTokenizer, AutoModel
    import torch

    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    model = AutoModel.from_pretrained("bert-base-uncased")

    def embed(text):
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        with torch.no_grad():
            outputs = model(**inputs).last_hidden_state
        return outputs.mean(dim=1).squeeze()

    emb1 = embed(text1)
    emb2 = embed(text2)
    return float(torch.nn.functional.cosine_similarity(emb1, emb2, dim=0).item()) * 100

# Sentence-BERT
sbert_model = SentenceTransformer("paraphrase-MiniLM-L6-v2")
def sbert_similarity(text1, text2):
    embeddings = sbert_model.encode([text1, text2])
    return float(cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]) * 100

# TF-IDF Cosine

def tfidf_cosine_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    return float(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]) * 100

