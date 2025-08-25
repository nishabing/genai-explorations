from dotenv import load_dotenv
load_dotenv()
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
import os


GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


async def run_agent():
   client = MultiServerMCPClient(
       {
           "github": {
               "command": "npx",
               "args": [
                   "-y",
                   "@modelcontextprotocol/server-github"
               ],
               "env": {
                   "GITHUB_PERSONAL_ACCESS_TOKEN": GITHUB_TOKEN
               },
               "transport": "stdio"
           },
           "filesystem": {
                "command": "npx",
                "args": [
                    "-y",
                    "@modelcontextprotocol/server-filesystem",
                    "/Users/nisha/Desktop",
                    "/Users/nisha/Projects"
                ],
               "transport": "stdio"
            }
        }
   )
   tools = await client.get_tools()
   agent = create_react_agent("openai:gpt-5-nano-2025-08-07", tools)
   response = await agent.ainvoke({"messages": "Add a new folder 'testMCP' in /Users/nisha/Projects folder. initialize git here and push to nishabing repository, create new if needed. Master will be default. please checkout a new local branch and push that as well. "})
   print(response["messages"][-1].content)


if __name__ == "__main__":
   asyncio.run(run_agent())