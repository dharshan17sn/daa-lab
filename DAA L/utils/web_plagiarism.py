import yake
from googlesearch import search
import requests
from bs4 import BeautifulSoup
from readability import Document
from time import sleep
from utils.traditional import rabin_karp_similarity
from utils.ai_similarity import bert_similarity

def extract_keywords(text, max_keywords=5):
    extractor = yake.KeywordExtractor()
    keywords = extractor.extract_keywords(text)
    return [kw[0] for kw in keywords[:max_keywords]]

def search_google(keywords, num_results=3):
    urls = set()
    for phrase in keywords:
        try:
            for result in search(phrase, num_results=num_results):
                urls.add(result)
        except Exception as e:
            print(f"Search failed for {phrase}: {e}")
    return list(urls)

def fetch_webpage_text(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=10)
        doc = Document(response.text)
        html = doc.summary()
        soup = BeautifulSoup(html, "html.parser")
        sleep(1)
        return soup.get_text()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return ""

def check_web_plagiarism(user_text, top_k=5):
    keywords = extract_keywords(user_text, max_keywords=5)
    urls = search_google(keywords, num_results=top_k)
    results = []

    for url in urls:
        page_text = fetch_webpage_text(url)
        if not page_text.strip() or page_text.strip() == user_text.strip():
            continue

        rk = rabin_karp_similarity(user_text, page_text)
        bert = bert_similarity(user_text, page_text)

        results.append({
            "URL": url,
            "Rabin-Karp (%)": round(rk, 2),
            "BERT (%)": round(bert, 2)
        })

    return results
