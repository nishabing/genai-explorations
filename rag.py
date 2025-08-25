import bs4
from langchain.chat_models import init_chat_model


from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from langchain_chroma import Chroma

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from dotenv import load_dotenv
load_dotenv()
#Load and chunk contents of the blog
loader = WebBaseLoader(
    web_paths=["https://www.educosys.com/course/genai"]
    )
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(docs)
#print(all_splits)

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


vectorstore = Chroma(collection_name="educosys_genai_info", embedding_function=embeddings, persist_directory="./chroma_genai")

vectorstore.add_documents(documents=all_splits)

results = vectorstore.get(include=["documents", "embeddings"])

for i, (doc, emb) in enumerate(zip(results["documents"], results["embeddings"]), 1):
    print(f"--- Chunk {i} ---")
    print("Text:", doc[:200], "...")  # print first 200 chars of text
    print("Embedding length:", len(emb))  # number of dimensions
    print("Embedding sample:", emb[:20], "...")  # print first 20 values
    print()
