import streamlit as st

st.set_page_config(page_title="📘 Algorithm Working", layout="wide")

st.title("📘 How Do These Algorithms Work?")
st.markdown("Let’s break down the core algorithms used in this app, explained in simple terms so anyone can understand.")

st.markdown("---")

# Rabin-Karp
st.header("🔹 Rabin-Karp Algorithm (Traditional)")
st.markdown("""
### 🧠 What is it?
Rabin-Karp is a **string searching algorithm**. Instead of comparing word-for-word, it **converts chunks of text into numbers** (called hashes) and compares those numbers. This is like checking fingerprints of sentences.

### 📦 How it works:
1. Break the text into chunks (e.g., 10 words each).
2. Convert each chunk into a hash number.
3. Check if that hash exists in the other document.

### 🛠️ Why use it?
- Very **fast** when searching for many patterns.
- Efficient for **exact matches**.

### 🕒 Time Complexity:
- **Best/Average Case:** O(n + m) *(like reading the document once)*
- **Worst Case:** O(n * m) *(if many hash collisions occur)*

> ℹ️ Think of Rabin-Karp like comparing barcodes instead of reading every letter.

### 🔍 Use in This App:
We compare hashed chunks of user text with scraped Wikipedia content to quickly spot matches.
""")

st.code("""
def rabin_karp_similarity(text1, text2):
    chunk_size = 10
    matches = 0
    total = 0
    words1 = text1.split()
    chunks = [' '.join(words1[i:i + chunk_size]) 
              for i in range(0, len(words1) - chunk_size + 1)]
    for chunk in chunks:
        if chunk in text2:
            matches += 1
        total += 1
    return (matches / total) * 100 if total > 0 else 0
""", language="python")

st.markdown("---")

# Boyer-Moore
st.header("🔹 Boyer-Moore Algorithm (Traditional)")
st.markdown("""
### 🧠 What is it?
Boyer-Moore is a **pattern matching algorithm** that's like a smart reader: it skips irrelevant parts when searching, instead of checking every letter.

### 📦 How it works:
1. Starts comparing from the **end of the pattern**.
2. If there's a mismatch, it **jumps ahead**, based on known rules.
3. This helps **avoid unnecessary comparisons**.

### 🛠️ Why use it?
- Much **faster** than naive search, especially for **long texts**.
- Saves time by **skipping**.

### 🕒 Time Complexity:
- **Best Case:** O(n / m)
- **Worst Case:** O(n * m) — but rarely happens in practice
> ℹ️ Imagine scanning for a word in a paragraph by looking at the last letter first. If it's not there, you jump ahead.

### 🔍 Use in This App:
We split user text into chunks and use Boyer-Moore to search each in the source document.
""")

st.code("""
def boyer_moore_similarity(text1, text2):
    # Split into chunks and use Boyer-Moore search
    ...
""", language="python")

st.markdown("---")

# BERT
st.header("🔹 BERT (AI-based)")
st.markdown("""
### 🧠 What is BERT?
BERT is a **deep learning model** developed by Google. It's trained on **huge amounts of text**, so it understands **context**, not just words.

> It’s like a super-smart reader who understands meaning, not just spelling.

### 📦 How it works:
1. Converts sentences into **numerical vectors** (embeddings).
2. Compares them using **cosine similarity**.
3. A high score = texts mean similar things.

### 🛠️ Why use it?
- Can catch **paraphrased or reworded plagiarism**.
- Useful when **words are different but meaning is same**.

### 🕒 Time Complexity:
- **Embedding:** O(n) per document (due to transformer model)
- **Similarity:** O(1) for cosine similarity

> ⚠️ Slower than traditional methods but more powerful.

### 🔍 Use in This App:
Used to detect **semantic similarity** — even if the text is rewritten, BERT can catch it.
""")

st.code("""
from transformers import AutoTokenizer, AutoModel
import torch

def bert_similarity(text1, text2):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    model = AutoModel.from_pretrained("bert-base-uncased")
    ...
""", language="python")

st.markdown("---")

st.success("Together, these algorithms combine speed, precision, and intelligence for strong plagiarism detection!")
