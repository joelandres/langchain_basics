from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain.tools import tool
import wikipedia

# Load environment variables from .env
load_dotenv()

# 1️⃣ Define tools

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


# 2️⃣ Create LLM
llm = AzureChatOpenAI(
    model="gpt-4o",
    temperature=0
)

# 3️⃣ Register tools
tools = [calculator, wiki_search]

# 4️⃣ Initialize agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

# 5️⃣ Ask the agent something
response = agent.run(
    "What is the population of France divided by 2?"
)

print(response)