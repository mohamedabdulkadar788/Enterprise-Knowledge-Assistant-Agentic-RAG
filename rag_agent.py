from langchain_community.llms import Ollama
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA

llm = Ollama(model="llama3")

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("embeddings", embedding_model, allow_dangerous_deserialization=True)
retriever = db.as_retriever()

rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def run_qa(query):
    result = rag_chain({"query": query})
    return result['result']

tools = [
    Tool(
        name="DocumentSearch",
        func=run_qa,
        description="Useful for answering company policy, HR, or IT questions."
    )
]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)

def run_agent(query):
    return agent.run(query)
