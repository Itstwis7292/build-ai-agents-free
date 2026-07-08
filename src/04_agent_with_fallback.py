# guide section 4 — provider fallback
# try groq first; if it fails (rate limit, key issue, outage),
# fall back to google gemini automatically. both are free.
# run: python3 src/04_agent_with_fallback.py

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

# load GROQ_API_KEY and GOOGLE_API_KEY from .env
load_dotenv()


def get_model():
    """return a working free model, preferring groq and falling back to gemini."""
    try:
        model = ChatGroq(model="llama-3.3-70b-versatile")
        # a tiny live call to confirm the model actually responds
        model.invoke("ping")
        return model
    except Exception as e:
        print(f"groq unavailable ({e}); falling back to google gemini.")
        return ChatGoogleGenerativeAI(model="gemini-2.5-flash")


# build the agent on whichever model is available
agent = create_agent(
    get_model(),
    tools=[],
    system_prompt="you are a concise, helpful assistant.",
)

result = agent.invoke(
    {"messages": [{"role": "user", "content": "say hello and name the model provider you think you are."}]}
)

print(result["messages"][-1].content)
