# Build AI Agents — Completely Free (2026)

a beginner's guide to building a real AI agent from scratch.
**$0 / no credit card / open-source.**

## intro

you can build a real AI agent — one that reasons, uses tools, and loops until the
job is done — without paying anything. no api bill, no credit card on file, no
trial that expires. the whole stack is free: **LangChain** for the agent loop, a
**free model** (Groq or Google Gemini), and your own machine to run it on.

this repo walks you from a five-line agent up to a complete one with tools,
memory, and automatic provider fallback. every file runs on its own.

## the free stack

- **LangChain / LangGraph** — the open-source framework that runs the agent loop
  (reason → call tool → observe → repeat). free and MIT-licensed.
  https://github.com/langchain-ai/langchain
- **Groq free tier** — blazing-fast inference on open models like llama 3.3, free
  and no card required. https://console.groq.com
- **Google AI Studio** — free Gemini api keys, also no card.
  https://aistudio.google.com

we use Groq as the default and Gemini as a fallback, so you always have a working
model even if one provider is down or rate-limited.

## setup

**1. check python.** you need python 3.10+ (mac users: use `python3` and `pip3`).

```bash
python3 --version
```

**2. install the dependencies.**

```bash
pip3 install -r requirements.txt
```

**3. add your free keys.** copy the example env file and fill it in:

```bash
cp .env.example .env
```

then open `.env` and paste your keys:

- **GROQ_API_KEY** — sign in at https://console.groq.com, create a key. no card needed.
- **GOOGLE_API_KEY** — grab one at https://aistudio.google.com. also no card needed.

you only strictly need the Groq key to start; the Google key is for the fallback
in sections 4 and the complete agent.

## what's in here

each file in `src/` is a standalone step in the guide.

| file | what it teaches |
| --- | --- |
| `src/01_first_agent.py` | your first agent — a free model + a system prompt, no tools |
| `src/02_agent_with_tools.py` | giving the agent tools — web search + a custom word-count tool |
| `src/03_agent_with_memory.py` | memory — remembering earlier turns on the same thread |
| `src/04_agent_with_fallback.py` | provider fallback — try Groq, fall back to Gemini automatically |
| `src/agent.py` | the complete agent — tools + memory + fallback, all combined |

## run it

run the complete agent:

```bash
python3 src/agent.py
```

or run any section on its own:

```bash
python3 src/01_first_agent.py
python3 src/02_agent_with_tools.py
python3 src/03_agent_with_memory.py
python3 src/04_agent_with_fallback.py
```

## honest notes

- **free tiers shift month to month.** limits, model names, and what's offered
  change often. if a model name errors, check the provider's console for the
  current one.
- **most no-key models train on your prompts.** free tiers frequently use your
  inputs to improve their models — so keep sensitive or private data off them.
- **InMemorySaver is RAM-only.** the memory in section 3 vanishes when the process
  exits. for real persistence, swap it for a database-backed checkpointer.
- **DuckDuckGo free search rate-limits.** if search starts failing, you're likely
  being throttled — slow down or add a small delay between calls.

---

built for [@exploraX_](https://x.com/exploraX_)
