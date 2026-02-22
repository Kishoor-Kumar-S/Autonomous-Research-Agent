# Autonomous-Research-Agent
AI Research Agent: A stateful workflow that transforms a single topic into a professional Markdown report using agentic reasoning and real-time search orchestration
# Autonomous Multi-Agent Research System

An advanced AI-powered research assistant that automates deep-web data collection and technical report writing. This project demonstrates the implementation of **Agentic Workflows** using a stateful graph-based architecture to move beyond simple LLM prompting into autonomous task execution.

##  Overview
This agent acts as a digital researcher by leveraging **LangGraph** to orchestrate a team of specialized AI nodes. The system works in a stateful loop to plan, search, and synthesize information into a professional, downloadable Markdown report.

##  Technical Architecture
The system uses a **Directed Acyclic Graph (DAG)** to manage the research state across three primary nodes:

1.  **The Planner (Gemini 2.5):** Analyzes the user's topic and decomposes it into high-intent search queries.
2.  **The Researcher (Tavily AI):** Executes concurrent web searches using an AI-optimized search engine to retrieve vetted, noise-free data.
3.  **The Writer (Gemini 2.5):** Performs final synthesis, transforming raw data chunks into a structured, professional Markdown document.



##  Key Features
* **Stateful Orchestration:** Built with **LangGraph** to ensure reliable data flow and error handling between agents.
* **Production-Grade Search:** Integrated with **Tavily AI Search** for superior retrieval accuracy compared to standard web scrapers.
* **Real-time Progress Tracking:** Streamlit-based UI featuring live status updates for each agent node.
* **Exportable Intelligence:** One-click feature to download generated reports as `.md` files for immediate professional use.

##  Tech Stack
* **LLM:** Google Gemini 2.5 Flash
* **Orchestration:** LangChain & LangGraph
* **Web Search:** Tavily API (Optimized for AI Agents)
* **Interface:** Streamlit
* **Environment:** Python 3.10+

##  Setup & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Kishoor-Kumar-S/Autonomous-Research-Agent.git](https://github.com/Kishoor-Kumar-S/Autonomous-Research-Agent.git)
   cd Autonomous-Research-Agent
