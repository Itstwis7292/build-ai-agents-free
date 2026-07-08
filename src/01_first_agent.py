# guide section 1 — your first agent
# a minimal agent: a free model + a system prompt, no tools yet.
# run: python3 src/01_first_agent.py

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.agents import create_agent

# load GROQ_API_KEY from .env
load_dotenv()

# a free, fast model on groq (no credit card needed)
model = ChatGroq(model="llama-3.3-70b-versatile")

# create_agent wires the model into an agent loop.
# no tools yet — this is just the model reasoning and replying.
agent = create_agent(
    model,
    tools=[],
    system_prompt="you are a concise, helpful assistant. answer directly.",
)

# invoke with a single user message
result = agent.invoke(
    {"messages": [{"role": "user", "content": "in one sentence, what is an AI agent?"}]}
)

# the final reply is the last message in the returned list
print(result["messages"][-1].content)
