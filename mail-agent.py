from pydantic import BaseModel
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()
class MailResponse(BaseModel):
    subject: str
    body: str

agent = create_react_agent(
    model="groq:llama-3.3-70b-versatile",  
    tools=[],  
    prompt="Write an email with subject and body, My name is Nisha",
    response_format=MailResponse
)

response = agent.invoke(
    {"messages": [{"role": "user", "content": "Write an email to my manager asking for leave for 5 days"}]}
)

print(response["structured_response"])