from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model


from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_chroma import Chroma

from langchain_google_genai import GoogleGenerativeAIEmbeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector_store = Chroma(collection_name="educosys_genai_info",
           embedding_function=embeddings,
           persist_directory="./chroma_genai",
       )

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

query = "give me curriculcum of week 1 of educosys genai course?"
docs = retriever.invoke(query)

for i, doc in enumerate(docs, start=1):
    print(f"Result {i}:")
    print(f"**")
    print(doc.page_content)
    print("-----------------")