from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()
llm = ChatOllama(
    model="gemma3:270m"
)

result=llm.invoke("what is an LLM")
print(result.content)