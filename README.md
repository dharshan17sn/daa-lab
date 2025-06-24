
# 📚 Plagiarism Checker: AI vs Traditional + Web Detection

A powerful and interactive plagiarism detection tool built using **Streamlit**, combining traditional algorithms (like Rabin-Karp) with modern **AI-based similarity detection (BERT)**. It also performs **live web plagiarism checking** using `yake`, Google Search, and semantic comparison.

---

## 🚀 Features

- 🔍 **Traditional Plagiarism Detection** using Rabin-Karp algorithm  
- 🤖 **AI-Based Plagiarism Detection** using BERT sentence embeddings  
- 🌐 **Web Plagiarism Detection** using keyword extraction and live Google search  
- 📄 **Wikipedia Article Scraping** based on user-specified topics  
- 🧹 Auto-clears previously scraped data before new scrapes  
- 📥 **Download** scraped Wikipedia files for offline analysis  
- 📊 Beautiful visualizations for similarity scores using Streamlit  

---

## 📁 Project Structure

.
├── app.py                        # Main Streamlit application
├── scraped_data/                # Folder where scraped articles are saved
├── utils/
│   ├── ai_similarity.py         # BERT-based similarity
│   ├── scraper.py               # Wikipedia scraping utility
│   ├── traditional.py           # Rabin-Karp similarity
│   └── web_plagiarism.py        # Web search and similarity check
└── requirements.txt             # Python dependencies

```


## ✅ Requirements

Make sure Python 3.8+ is installed.

### Install dependencies

```
pip install -r requirements.txt
```

Your `requirements.txt` should include:

```
streamlit
wikipedia
beautifulsoup4
readability-lxml
transformers
torch
scikit-learn
sentence-transformers
yake
googlesearch-python
```

---

## 🧠 How It Works

### 1. **Input Text**
- Upload a `.txt` file or paste your own text.

### 2. **Scrape Wikipedia**
- Enter topics (one per line) to scrape.
- Articles are saved in `scraped_data/`.

### 3. **Local Plagiarism Check**
- Compares user text with scraped articles using:
  - Rabin-Karp string matching
  - BERT-based semantic similarity

### 4. **Web Plagiarism Check**
- Extracts keywords using YAKE.
- Searches Google.
- Fetches and cleans page content.
- Compares using Rabin-Karp and BERT.

---

## 📦 Run the App

```bash
streamlit run app.py
```

---

## 🙌 Acknowledgements

- [Streamlit](https://streamlit.io/)
- [HuggingFace Transformers](https://huggingface.co/transformers/)
- [Sentence-Transformers](https://www.sbert.net/)
- [Wikipedia Python API](https://pypi.org/project/wikipedia/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [readability-lxml](https://pypi.org/project/readability-lxml/)
- [YAKE](https://github.com/LIAAD/yake)

---
