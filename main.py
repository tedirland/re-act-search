from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

load_dotenv()


@tool
def search(query: str) -> str:
    """
    Searches the web for the given query and returns relevant results.
    Args: query: The search query.
    Returns: The search results.
    """
    print(f"Searching for: {query}")
    return "Plainfiled weather is Sunny"


llm = ChatOpenAI(model="gpt-4", temperature=0)
tools = [search]
agent = create_agent(llm, tools)


def main():
    result = agent.invoke(
        {"messages": HumanMessage(content="What is the weather like in Plainfield?")}
    )
    print(result)


if __name__ == "__main__":
    main()
