import streamlit as st
from newspaper import Article
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()


GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")


def extract_text_from_url(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"⚠️ Error extracting content: {str(e)}"


def summarize_text_with_gemini(text):
    prompt = f"""You're a professional content analyst.

Analyze the following article and extract key points by identifying its main topics or themes. For each key point, generate a concise summary in this format:

**<Title>**: <Summary>

Instructions:
- Put each key point on a separate line.
- Make titles bold using markdown format (surrounded by ** on each side).
- Use informative, short titles (e.g., "Economic Impact", "Historical Significance", etc.).
- Avoid generic headings like "Summary".
- Focus on important facts, events, people, or implications.
- Format should be: **Title**: Summary

Here is the article:

{text}
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"⚠️ Gemini summarization error: {str(e)}"


st.set_page_config(page_title="Webpage Summarizer", page_icon="🧠", layout="centered")

st.markdown(
    """
    <h2 style='text-align: center; color: #4B8BBE;'>🌐 Webpage Summarizer with Gemini</h2>
    <p style='text-align: center; color: gray;'>Paste any article or blog URL below to generate a smart summary.</p>
    """,
    unsafe_allow_html=True
)

url_input = st.text_input("🔗 Enter the URL", placeholder="https://example.com/article")

if st.button("Summarize"):
    if not url_input:
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Extracting and summarizing..."):
            content = extract_text_from_url(url_input)
            
            if content.startswith("⚠️"):
                st.error(content)
            else:
                summary = summarize_text_with_gemini(content)
                
                if summary.startswith("⚠️"):
                    st.error(summary)
                else:
                    st.markdown("### ✨ Summary")
                    st.markdown(summary)

st.markdown("---")
st.markdown("<div style='text-align: center; color: lightgray;'>Built with ❤️ using Gemini 1.5 Pro</div>", unsafe_allow_html=True)
