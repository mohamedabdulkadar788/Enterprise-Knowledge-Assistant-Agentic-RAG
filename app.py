import streamlit as st
from rag_agent import run_agent

st.set_page_config(page_title="Enterprise RAG Assistant", layout="centered")
st.title("📚 Enterprise Knowledge Assistant")

st.markdown("Ask any question related to your company policies, IT support, or HR handbook.")

query = st.text_input("🧠 Your question:")

if st.button("Ask"):
    if query.strip():
        with st.spinner("Searching your company knowledge base..."):
            response = run_agent(query)
            st.success(response)
    else:
        st.warning("Please enter a question.")