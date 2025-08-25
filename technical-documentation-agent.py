from pydantic import BaseModel
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
class TechnicalDoc(BaseModel):
    problem: str
    solution: str
    goals: str
    milestones: str

agent = create_react_agent(
    model="groq:llama-3.3-70b-versatile",  
    tools=[],  
    prompt="You are a software developer who writes design documents",
    response_format=TechnicalDoc
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "Write a detailed design document for a user re-engagement framework"}]}
)

print(response["structured_response"])