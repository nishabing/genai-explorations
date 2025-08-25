from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()

load_dotenv()
agent = create_react_agent(
    model="groq:llama-3.3-70b-versatile",  
    tools=[],  
    prompt="Answer questions about starship enterprise only",
    checkpointer=checkpointer    
)

# Run the agent
config = {"configurable": {"thread_id": "1"}}
response=agent.invoke(
    {"messages": [{"role": "user", "content": "who is Spock, briefly"}]},
    config
)

print(response["messages"][-1].content)
print("------")
response=agent.invoke(
    {"messages": [{"role": "user", "content": "when was he born"}]},
    {"configurable": {"thread_id": "1"}} # does not remember when we give a different thread_id than previous
)

print(response["messages"][-1].content)
