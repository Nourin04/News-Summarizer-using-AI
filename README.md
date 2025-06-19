# 🧠⚡ AI-Powered News Summarizer

Tired of wading through endless news articles just to get the main points?

**This AI-powered news summarizer does the hard work for you** — transforming long-form news into clear, concise, and well-organized bullet points in seconds. Built with the blazing-fast **Groq API** and the powerful **LLaMA 3** model, this app helps you stay informed without information overload.

Whether you're reading from a URL or pasting raw content, get instant summaries — straight to the point.

---

## 🔗 Live App

Try it now: [🌐 Deployed Summarizer on Streamlit](https://news-summarizer-using-ai.streamlit.app/)



## 🔍 Features

- 🔗 Summarize from a **URL** or **pasted text**
- ✅ Uses **Groq API** for fast, accurate summaries
- 📝 Output in **clear bullet points**, grouped by topic or region
- 🎨 Beautiful interface with background image
- ☁️ **Deployable to Streamlit Cloud**


---

## 🧠 Model Details

- **Model Used**: `llama3-70b-8192` via [Groq API](https://console.groq.com/)
- **Prompting Style**: Structured, task-specific prompt for bullet-point summaries.

---

## 🛠️ Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/news-summarizer-groq.git
cd news-summarizer-groq
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Up API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_actual_groq_api_key
```

Or set it as an environment variable:

```bash
export GROQ_API_KEY=your_actual_groq_api_key
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📁 File Structure

```
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies      
├── README.md
```


---



## 🛠️ Tech Stack

**Frontend & UI:**
- 🧩 **Streamlit** – For building the interactive web UI
- 🎨 **Custom CSS** – Injected via `st.markdown()` for background images and styling

**Backend & Logic:**
- 🐍 **Python 3** – Core programming language
- 📤 **Groq API** – Connects to the LLaMA 3 model for ultra-fast text summarization
- 🧠 **LLaMA 3 (70B)** – Large language model used via Groq for summarization

**Web Scraping & Input Processing:**
- 🌐 **requests** – For fetching article content from URLs
- 🥣 **BeautifulSoup (bs4)** – For parsing and extracting readable text from HTML

**Configuration & Deployment:**
- 🔐 **python-dotenv** – To load the Groq API key securely from a `.env` file (local dev)
- ☁️ **Streamlit Cloud** – For deploying the app online with secret management


---

