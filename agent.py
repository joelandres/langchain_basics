from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import tool
import wikipedia

load_dotenv()

@tool
def calculator(expression: str) -> str:
    """Evaluates a math expression."""
    return str(eval(expression))


@tool
def wiki_search(query: str) -> str:
    """Search Wikipedia for a topic."""
    try:
        return wikipedia.summary(query, sentences=2)
    except:
        return "No result found."

llm = AzureChatOpenAI(
    model="gpt-4o",
    temperature=0
)

tools = [calculator, wiki_search]

agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

response = agent.run(
    "What is the population of France divided by 2?"
)

print(response)