# guide section 3 — giving the agent memory
# the agent remembers earlier turns on the same thread_id.
# run: python3 src/03_agent_with_memory.py

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

# load GROQ_API_KEY from .env
load_dotenv()

model = ChatGroq(model="llama-3.3-70b-versatile")

# a checkpointer stores conversation state between invokes.
# InMemorySaver keeps it in RAM (fine for demos).
agent = create_agent(
    model,
    tools=[],
    system_prompt="you are a friendly assistant with a good memory.",
    checkpointer=InMemorySaver(),
)

# the thread_id ties multiple invokes into one conversation
config = {"configurable": {"thread_id": "chat-1"}}

# turn 1: tell it a name
first = agent.invoke(
    {"messages": [{"role": "user", "content": "hi! my name is m0h."}]},
    config,
)
print("reply 1:", first["messages"][-1].content)

# turn 2: same thread_id, so it should recall the name
second = agent.invoke(
    {"messages": [{"role": "user", "content": "what's my name?"}]},
    config,
)
print("reply 2:", second["messages"][-1].content)
