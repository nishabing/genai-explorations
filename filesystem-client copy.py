from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os


async def run_agent():
   client = MultiServerMCPClient(
       {
           "NishaFileSystem": {
               "command": "python",
               "args": [
                   "./filesystem-mcp.py"
               ],
               "transport":"stdio"
           }
        }
   )
   tools = await client.get_tools()
   agent = create_react_agent("openai:gpt-5-nano-2025-08-07", tools)
   response = await agent.ainvoke({"messages": "delete file test.txt"})
   print(response["messages"][-1].content)


if __name__ == "__main__":
   asyncio.run(run_agent())