<<<<<<< HEAD
# 🧠 Enterprise Knowledge Assistant (Agentic RAG + LLaMA 3)

This is an end-to-end intelligent assistant that helps employees find answers from internal HR, IT, and policy documents using Retrieval-Augmented Generation and LLaMA 3 (8B via Ollama).

## ✨ Features
- Multi-document PDF ingestion
- Local LLM (LLaMA 3) via Ollama — privacy-friendly!
- LangChain Agent + FAISS-powered vector search
- Clean Streamlit UI

## 🚀 Run the Project

1. Place your PDFs in the `/data` folder
2. Install dependencies:  
```bash
pip install -r requirements.txt
```
3. Generate the vector store:
```bash
python ingest.py
```
4. Run the Streamlit app:
```bash
streamlit run app.py
```

## 🖼️ Sample Use Cases
- "How many vacation days do I get?"
- "Who handles VPN issues?"
- "What’s the process to reimburse client dinner?"
=======
# Enterprise-Knowledge-Assistant---Agentic-RAG
>>>>>>> 233fbb35fd3912723da6ba3b411e16989217b0d0
