import streamlit as st
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
load_dotenv()

# Load Groq API key from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def add_bg_from_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            opacity: 0.6;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
add_bg_from_url("https://images.unsplash.com/photo-1504711434969-e33886168f5c?q=80&w=870&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")  # or any image URL


def extract_article_from_url(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        paragraphs = soup.find_all('p')
        return ' '.join(p.get_text() for p in paragraphs if len(p.get_text()) > 50)
    except Exception as e:
        return f"Error extracting article: {e}"

def summarize_with_groq(article_text, model="llama3-70b-8192"):
    endpoint = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        "Summarize the following news article into clear and concise bullet points:\n\n"
        "- Group points by region or theme if applicable (e.g., Europe, Asia, Technology).\n"
        "- Limit each group to 3–5 key highlights.\n"
        "- Use plain, informative language.\n\n"
        f"Article:\n{article_text}"
    )

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes news articles into bullet points."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post(endpoint, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Groq API Error: {response.text}"

# Streamlit App UI
st.set_page_config(page_title="News Summarizer", layout="centered")
st.title("📰 AI News Summarizer")

input_type = st.radio("Choose input type:", ["Paste Text", "Article URL"])
article_text = ""

if input_type == "Paste Text":
    article_text = st.text_area("Paste your article here:", height=300)
else:
    url = st.text_input("Enter the article URL:")
    if url:
        with st.spinner("Extracting article..."):
            article_text = extract_article_from_url(url)
            st.success("Article extracted successfully!")

if article_text:
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary = summarize_with_groq(article_text)
        st.subheader("📋 Summary:")
        st.markdown(summary)
