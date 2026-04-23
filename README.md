# NEXUS · Multi-Agent Research Intelligence System

NEXUS is an advanced, autonomous multi-agent research platform designed to radically accelerate information gathering, synthesis, and reporting. By orchestrating a pipeline of specialized AI agents—spanning Search, Intelligent Web Scraping, Writing, and a Self-Reflecting Critic—the system dynamically crawls the web to distill high-signal data into comprehensive, fact-checked intelligence reports. Engineered with Python and LangChain, and wrapped in a highly polished, asynchronous Streamlit UI with real-time state visualizations, NEXUS demonstrates a sophisticated mastery of agentic AI architectures, self-evaluating LLM loops, and modern full-stack development.

## 🚀 Key Features

- **Autonomous Agent Workflows**: Seamlessly coordinates specialized agents (Search, URL Selection, Scraper, Writer, Critic) to emulate an expert human research team.
- **Iterative Self-Reflection**: Employs an iterative Actor-Critic loop where the Writer's draft is rigorously evaluated by a Critic agent, enforcing strict quality thresholds before finalization.
- **Resilient Web Intelligence**: Integrates the Tavily Search API with a robust, custom-built web scraper (BeautifulSoup/Requests) featuring anti-noise filtering and intelligent charset detection.
- **Premium Real-Time Frontend**: Features a stunning, cyberpunk-inspired Streamlit interface complete with live progress tracking, dynamic "agent thinking" state cards, and asynchronous typewriter rendering.

## 🛠 Tech Stack

- **Core Engine:** Python, LangChain
- **Search & Data Extraction:** Tavily API, BeautifulSoup4, Requests
- **User Interface:** Streamlit (with custom HTML/CSS)

## ⚡ Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your environment:
   Create a `.env` file and add your `TAVILY_API_KEY` (along with any required LLM provider keys).
3. Launch the application:
   ```bash
   streamlit run app.py
   ```
   *(Alternatively, run the headless pipeline via `python pipeline2.py`)*
