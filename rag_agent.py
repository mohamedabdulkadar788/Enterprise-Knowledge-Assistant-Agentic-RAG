from langchain_community.llms import Ollama
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.agents import initialize_agent, Tool
from langchain.chains import RetrievalQA

# Load your LLM
llm = Ollama(model="llama3")

# Load embeddings and vector DB
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local("embeddings", embedding_model, allow_dangerous_deserialization=True)
retriever = db.as_retriever()

# RAG chain for document search
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

def run_qa(query):
    return rag_chain({"query": query})['result']

def faq_tool(query):
    faqs = {
        "working hours": "Our working hours are from 9 AM to 6 PM, Monday to Friday.",
        "holiday": "The company observes all national public holidays.",
        "remote work": "Remote work is allowed up to 2 days per week with manager approval.",
        "casual leave": "Employees are entitled to 12 days of casual leave per calendar year.",
        "leave request": "Leave requests should be submitted via the HR portal at least 3 days in advance."
    }
    for key, answer in faqs.items():
        if key in query.lower():
            return answer
    return "I don't have an answer to that FAQ."

def hr_support_tool(query):
    # Simulated HR chatbot responses for common queries
    hr_responses = {
        "benefits": "Our benefits include health insurance, 401k matching, and paid time off.",
        "payroll": "Payroll is processed on the 30th of each month.",
        "performance review": "Performance reviews happen twice a year in June and December.",
        "training": "We offer regular training sessions for skill development.",
    }
    for key, answer in hr_responses.items():
        if key in query.lower():
            return answer
    return "Please contact HR directly for that information."

tools = [
    Tool(
        name="DocumentSearch",
        func=run_qa,
        description="Search company documents, policies, and manuals."
    ),
    Tool(
        name="FAQ",
        func=faq_tool,
        description="Answer frequently asked questions about company policies."
    ),
    Tool(
        name="HRSupport",
        func=hr_support_tool,
        description="Answer common HR-related questions."
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

