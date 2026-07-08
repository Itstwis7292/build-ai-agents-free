# guide — the complete agent (all sections combined)
# provider fallback (groq -> gemini) + tools (search + word_count) + memory.
# run: python3 src/agent.py

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.checkpoint.memory import InMemorySaver

# load GROQ_API_KEY and GOOGLE_API_KEY from .env
load_dotenv()


# --- section 4: provider fallback ---
def get_model():
    """return a working free model, preferring groq and falling back to gemini."""
    try:
        model = ChatGroq(model="llama-3.3-70b-versatile")
        model.invoke("ping")  # confirm it actually responds
        return model
    except Exception as e:
        print(f"groq unavailable ({e}); falling back to google gemini.")
        return ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# --- section 2: tools ---
search = DuckDuckGoSearchRun()  # free web search, no key


@tool
def word_count(text: str) -> int:
    """count the number of words in the given text."""
    return len(text.split())


# --- section 3: memory ---
# InMemorySaver keeps conversation state in RAM across invokes
checkpointer = InMemorySaver()

# --- assemble the full agent ---
agent = create_agent(
    get_model(),
    tools=[search, word_count],
    system_prompt=(
        "you are a helpful research assistant. "
        "use your tools when they help, and remember the conversation."
    ),
    checkpointer=checkpointer,
)


def main():
    # one thread_id = one continuous conversation
    config = {"configurable": {"thread_id": "demo-1"}}

    # turn 1: give it something to remember + use a tool
    turn1 = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "my name is m0h. search for what an AI agent is and count the words in your summary.",
                }
            ]
        },
        config,
    )
    print("agent:", turn1["messages"][-1].content)

    # turn 2: same thread, so it should recall the name
    turn2 = agent.invoke(
        {"messages": [{"role": "user", "content": "what's my name?"}]},
        config,
    )
    print("agent:", turn2["messages"][-1].content)


if __name__ == "__main__":
    main()
