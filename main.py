from typing import List

from pydantic import BaseModel, Field
from dotenv import load_dotenv

# from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


class Source(BaseModel):
    """Schema for a source used by the agengt"""

    url: str = Field(description="The URL of the source")


class AgentResponse(BaseModel):
    """Schema for the agent's response"""

    answer: str = Field(description="The final answer provided by the agent")
    sources: List[Source] = Field(
        default_factory=list,
        description="A list of sources used by the agent to generate the answer",
    )


load_dotenv()


llm = ChatOpenAI(model="gpt-4")
tools = [TavilySearch()]
agent = create_agent(llm, tools, response_format=AgentResponse)


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
