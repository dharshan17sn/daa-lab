import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

import streamlit as st
import time
import pandas as pd

from utils.scraper import scrape_articles
from utils.traditional import rabin_karp_similarity, boyer_moore_similarity
from utils.ai_similarity import bert_similarity
from utils.web_plagiarism import check_web_plagiarism

# App setup
st.set_page_config(
    page_title="Plagiarism Checker",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📚 Plagiarism Checker: AI vs Traditional + Web Detection")

os.makedirs("scraped_data", exist_ok=True)

# Sidebar: Input method
st.sidebar.header("Input Text")
input_method = st.sidebar.radio("Choose input method:", ("Upload .txt file", "Paste text"))

user_text = None
if input_method == "Upload .txt file":
    uploaded_file = st.sidebar.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file:
        user_text = uploaded_file.read().decode("utf-8")
elif input_method == "Paste text":
    user_text = st.sidebar.text_area("Paste your text here", height=200)

# Sidebar: Topic scraper
st.sidebar.header("Wikipedia Scraper")
topic_input = st.sidebar.text_area("Enter Wikipedia topics (one per line):", height=150)
topic_list = [t.strip() for t in topic_input.split("\n") if t.strip()]

if topic_list:
    if st.sidebar.button("📄 Scrape Topics"):
        with st.spinner("Scraping Wikipedia articles..."):
            scraped_files = scrape_articles(topic_list)
        if scraped_files:
            st.success(f"✅ Scraped {len(scraped_files)} article(s).")
        else:
            st.warning("⚠️ Scraping failed. Check the topic names.")

scraped_list = os.listdir("scraped_data")
if scraped_list:
    with st.expander("📂 Scraped Articles"):
        for file in scraped_list:
            path = os.path.join("scraped_data", file)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            st.download_button(f"📥 Download {file}", content, file_name=file, mime="text/plain")
else:
    st.info("ℹ️ No articles found yet. Scrape topics from the sidebar.")

# Local Plagiarism Detection
if user_text and scraped_list:
    st.subheader("🔍 Local Plagiarism Check (AI vs Traditional)")

    results = []
    for file in scraped_list:
        try:
            with open(f"scraped_data/{file}", "r", encoding="utf-8") as f:
                source_text = f.read()
        except Exception as e:
            st.error(f"Could not read {file}: {e}")
            continue

        rk_score = rabin_karp_similarity(user_text, source_text)
        bm_score = boyer_moore_similarity(user_text, source_text)

        try:
            bert_score = bert_similarity(user_text, source_text)
        except Exception as e:
            bert_score = 0.0
            st.error(f"BERT similarity failed for {file}: {e}")

        results.append({
            "Source": file,
            "Rabin-Karp (%)": rk_score,
            "Boyer-Moore (%)": bm_score,
            "BERT (%)": bert_score
        })

    df = pd.DataFrame(results)
    st.dataframe(df.style.format({
        "Rabin-Karp (%)": "{:.2f}",
        "Boyer-Moore (%)": "{:.2f}",
        "BERT (%)": "{:.2f}"
    }))

    st.bar_chart(df.set_index("Source")[[
        "Rabin-Karp (%)", "Boyer-Moore (%)", "BERT (%)"
    ]])

# Web Plagiarism Detection
if user_text:
    st.subheader("🌐 Web Plagiarism Check")
    if st.button("🔎 Check Web for Plagiarism"):
        with st.spinner("Searching web for possible matches..."):
            web_results = check_web_plagiarism(user_text)
        if web_results:
            web_df = pd.DataFrame(web_results)
            st.success("✅ Potential matches found!")
            st.dataframe(web_df.style.format({
                "Rabin-Karp (%)": "{:.2f}",
                "BERT (%)": "{:.2f}"
            }))
        else:
            st.warning("⚠️ No strong matches found online.")

st.markdown("---")
st.caption("Developed with Streamlit | AI + Traditional Plagiarism Detection")
