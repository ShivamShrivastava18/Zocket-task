# Webpage Summarizer with Gemini 1.5 Pro

This project is a Streamlit-based AI agent that accepts a webpage URL, extracts its content, and generates concise bullet-point summaries using the Gemini 1.5 Pro model.

---

## Features

-  Accepts any public URL as input
-  Extracts main article content using `newspaper3k`
-  Summarizes using Google Gemini 1.5 Pro via `google-generativeai`
-  Outputs summaries in `Title: Summary` format
-  Simple and clean Streamlit interface

---

## 🛠Tech Stack

- Python 3.8+
- Streamlit
- newspaper3k
- google-generativeai
- python-dotenv

---

## Installation

```bash
git clone https://github.com/your-username/webpage-summarizer.git
cd webpage-summarizer
pip install -r requirements.txt
```
- Create a .env file in the root directory:
  
```bash
GEMINI_API_KEY=your_actual_api_key_here
```
---

## Usage 

```bash
streamlit run app.py
```
- Paste a URL in the input box
- Click Summarize
- View structured summaries instantly

---

## Sample

![1](https://github.com/user-attachments/assets/be2249e5-2ff2-415d-9c62-5546e47eacea)

![2](https://github.com/user-attachments/assets/c04fbd2f-132f-4195-85ae-24d211c8d1fa)

![3](https://github.com/user-attachments/assets/74f10148-e345-4863-8572-dbd192c3fc02)

![4](https://github.com/user-attachments/assets/545437f7-dbcb-4898-8f98-ce6df7a097af)



