# 🤖 AutoResearch Agent

[![Python Version](https://img.shields.io/badge/Python-3.14%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.136%2B-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.57%2B-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![LangGraph](https://img.shields.io/badge/LangGraph-1.2%2B-FF9800?logo=langchain&logoColor=white)](https://github.com/langchain-ai/langgraph)
[![Groq](https://img.shields.io/badge/Groq-Ultra--Fast-A855F7?logo=groq&logoColor=white)](https://groq.com/)
[![Tavily](https://img.shields.io/badge/Tavily-Web--Search-3B82F6)](https://tavily.com/)

A multi-agent AI research system built with LangGraph, LangChain, FastAPI, and Streamlit. Given any research query, 5 specialized agents autonomously plan, search, summarize, write, and review a comprehensive research report.

---

## 🏗️ Architecture

Below is the stateful execution flow of your multi-agent architecture:

```mermaid
graph TD
    %% Define Nodes
    Start([User Query]) --> Planner[Planner Agent]
    
    Planner -->|Splits query into sub-tasks| Researcher[Researcher Agent]
    
    Researcher -->|Performs Tavily Web Searches| Summarizer[Summarizer Agent]
    
    Summarizer -->|Synthesizes findings| Writer[Writer Agent]
    
    Writer -->|Drafts Markdown Report| Supervisor[Supervisor Agent]
    
    %% Conditional Router
    Supervisor --> Router{Supervisor Verdict?}
    
    Router -->|REVISION Needed<br/>Max 2 Loops| Writer
    Router -->|APPROVED| End([Final Report])

    %% Styling
    style Start fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff
    style Planner fill:#2196F3,stroke:#1976D2,stroke-width:2px,color:#fff
    style Researcher fill:#9C27B0,stroke:#7B1FA2,stroke-width:2px,color:#fff
    style Summarizer fill:#E91E63,stroke:#C2185B,stroke-width:2px,color:#fff
    style Writer fill:#FF9800,stroke:#F57C00,stroke-width:2px,color:#fff
    style Supervisor fill:#00BCD4,stroke:#0097A7,stroke-width:2px,color:#fff
    style Router fill:#FFEB3B,stroke:#FBC02D,stroke-width:2px,color:#333
    style End fill:#4CAF50,stroke:#388E3C,stroke-width:2px,color:#fff
```

- **Planner Agent** — breaks query into focused sub-tasks
- **Researcher Agent** — searches web in parallel using Tavily
- **Summarizer Agent** — condenses findings in parallel
- **Writer Agent** — compiles structured report
- **Supervisor Agent** — reviews quality, loops back if needed

---

## 🛠️ Tech Stack
**LangGraph** · **LangChain** · **FastAPI** · **Streamlit** · **Groq** · **Tavily** · **Python**

---

## 🚀 How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/aryanmakwana1801/Autoresearch-Agent.git
   cd Autoresearch-Agent
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Add API keys to `.env` file in the root folder:
   ```env
   GROQ_API_KEY="your-groq-api-key"
   TAVILY_API_KEY="your-tavily-api-key"
   ```
4. **Terminal 1 (Backend API)**:
   ```bash
   cd autoresearch-agent
   python backend/main.py
   ```
5. **Terminal 2 (Frontend Dashboard)**:
   ```bash
   cd autoresearch-agent
   streamlit run frontend/app.py
   ```

---

## 🌟 Key Features
- **Parallel web search and summarization** (3x faster)
- **Supervisor feedback loop** for quality control
- **REST API backend** with FastAPI
- **Interactive Streamlit UI** with pulsing progress tracking
- **Downloadable research reports** in Markdown format

---
*Developed by **Aryan Makwana**. Powered by LangGraph & Groq.*
