# NEXUS · Multi-Agent Research Intelligence System

> Autonomous AI research platform that searches the web, scrapes sources, writes reports, and critiques its own output — without human intervention.

---

## Overview

NEXUS is a multi-agent AI system that automates the full research pipeline — from query to polished intelligence report. Rather than a single LLM answering from memory, NEXUS deploys a coordinated team of specialized agents: one searches the web, one selects and scrapes the most relevant sources, one synthesizes findings into a structured report, and a final Critic agent evaluates the output against strict quality thresholds — triggering rewrites until the standard is met.

Built with Python and LangChain, and wrapped in a real-time Streamlit interface with live agent-state visualization, NEXUS is a practical demonstration of production-grade agentic AI architecture.

---

## Architecture

NEXUS operates as a sequential multi-agent pipeline with an iterative feedback loop:
Query
│
▼
Search Agent          ← Tavily API: retrieves top web results
│
▼
URL Selector Agent    ← Ranks and selects highest-signal sources
│
▼
Scraper Agent         ← BeautifulSoup/Requests: extracts clean content
│
▼
Writer Agent          ← Synthesizes scraped data into a structured report
│
▼
Critic Agent          ← Evaluates report quality; loops back to Writer if below threshold
│
▼
Final Report

The Actor-Critic loop between the Writer and Critic is the core quality mechanism — the system does not finalize output until the Critic approves it.

---

## Features

- **Fully Autonomous Pipeline** — zero human intervention from query to final report
- **Actor-Critic Self-Reflection** — Writer drafts, Critic evaluates, loop repeats until quality threshold is met
- **Resilient Web Scraping** — custom BeautifulSoup scraper with anti-noise filtering, charset detection, and graceful failure handling
- **Real-Time UI** — live agent-state cards showing what each agent is doing at every step
- **Asynchronous Typewriter Rendering** — final report streams into the UI character by character
- **Headless Mode** — run the full pipeline from CLI without the UI

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent Orchestration | LangChain (LCEL) |
| Web Search | Tavily Search API |
| Web Scraping | BeautifulSoup4, Requests |
| LLM Backend | Groq / OpenAI compatible |
| Frontend | Streamlit (custom HTML/CSS) |
| Environment | Python-dotenv |

---

## Project Structure
nexus/
├── app.py                  # Streamlit UI entry point
├── pipeline2.py            # Headless CLI pipeline
├── agents/
│   ├── search_agent.py     # Tavily-powered web search
│   ├── url_selector.py     # Source ranking and selection
│   ├── scraper_agent.py    # Web content extraction
│   ├── writer_agent.py     # Report synthesis
│   └── critic_agent.py     # Quality evaluation and feedback
├── utils/
│   └── scraper_utils.py    # Anti-noise filtering, charset detection
├── .env                    # API keys (not committed)
├── requirements.txt
└── README.md

---

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/sahilarora007/nexus.git
cd nexus
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Configure environment variables**

Create a `.env` file in the root directory:
```env
TAVILY_API_KEY=your_tavily_api_key
GROQ_API_KEY=your_groq_api_key
```

**4. Launch the application**
```bash
# Web UI
streamlit run app.py

# Headless CLI mode
python pipeline2.py
```

---

## How It Works

1. Enter a research query in the UI
2. The Search Agent queries Tavily and retrieves the top web results
3. The URL Selector picks the most relevant sources
4. The Scraper Agent fetches and cleans the content from each source
5. The Writer Agent synthesizes all content into a structured report
6. The Critic Agent scores the report — if it falls below the quality threshold, the Writer revises
7. The approved report streams into the UI in real time

---

## Roadmap

- [ ] Parallel agent execution for faster scraping
- [ ] Persistent report storage and history
- [ ] Export reports as PDF or Markdown
- [ ] Source credibility scoring
- [ ] Support for multiple LLM providers (Anthropic, Gemini)
- [ ] Citation linking in final reports

---

## License

MIT License — free to use, modify, and distribute.
