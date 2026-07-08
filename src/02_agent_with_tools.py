# guide section 2 — giving the agent tools
# same base agent, but now it can search the web and count words.
# run: python3 src/02_agent_with_tools.py

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

# load GROQ_API_KEY from .env
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

# tool 1: free web search via duckduckgo (no api key)
search = DuckDuckGoSearchRun()


# tool 2: a custom tool. the docstring tells the agent what it does,
# and type hints tell it the expected input/output.
@tool
def word_count(text: str) -> int:
    """count the number of words in the given text."""
    return len(text.split())


# pass both tools to the agent; it decides when to call each one
agent = create_agent(
    model,
    tools=[search, word_count],
    system_prompt="you are a research assistant. use your tools when helpful.",
)

# a prompt that needs search first, then the word_count tool
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": (
                    "search for a one-line summary of what langchain is, "
                    "then tell me how many words are in that summary."
                ),
            }
        ]
    }
)

print(result["messages"][-1].content)
