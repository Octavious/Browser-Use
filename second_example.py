from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
from pydantic import SecretStr
import os
from dotenv import load_dotenv
load_dotenv()

import asyncio
api_key = os.getenv("GEMINI_API_KEY")

initial_actions = [
	{'open_tab': {'url': 'https://www.topuniversities.com/student-info/choosing-university/worlds-top-100-universities'}},
]
# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', api_key=SecretStr(os.getenv('GEMINI_API_KEY')))

# Create agent with the model
agent = Agent(
    task="get the names, location, rank of top 100 universities in the world, this website has pagination",
    llm=llm,
    initial_actions=initial_actions
)

async def main():
    result = await agent.run()
    print(result)

asyncio.run(main())