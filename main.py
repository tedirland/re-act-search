from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch

load_dotenv()


llm = ChatOpenAI(model="gpt-5", temperature=0)
tools = [TavilySearch()]
agent = create_agent(llm, tools)


def main():
    result = agent.invoke(
        {
            "messages": HumanMessage(
                content="Please look for 3 job postings for a SaaS sales engineer in Chicago."
            )
        }
    )
    print(result)


if __name__ == "__main__":
    main()
