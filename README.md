<h1 align="center">🤖 Multi-Agent LLM System</h1>
<p align="center">
Agent-Based AI • Tool-Orchestrated Reasoning • LLM Systems
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python"/>
  <img src="https://img.shields.io/badge/Streamlit-Live_App-red?logo=streamlit"/>
  <img src="https://img.shields.io/badge/OpenAI-LLM-black?logo=openai"/>
  <img src="https://img.shields.io/badge/Docker-Ready-blue?logo=docker"/>
</p>

<p align="center">
  <a href="https://multi-agent-llm-system-dkwzj8rotcwuyqekioeu64.streamlit.app/" target="_blank">
    🚀 <b>Live Demo</b>
  </a>
</p>

---

## 🎥 Live Demo

👉 Try the app here:  
🔗 https://multi-agent-llm-system-dkwzj8rotcwuyqekioeu64.streamlit.app/

💡 Recommended query: Find AI funding opportunities in Germany and explain eligibility criteria

---

## 🧠 Overview

This project implements a **multi-agent AI system** using Large Language Models (LLMs) to simulate:

- 🧩 Task decomposition
- 🔎 Tool orchestration
- 🧠 Multi-step reasoning
- 🧠 Memory-aware responses

Instead of a single monolithic model, the system uses **specialized agents** for improved control, modularity, and interpretability.

---

## 🏗️ Architecture
User Query

↓

🧩 Planner Agent

↓

🔀 Tool Router

↓

🔎 Retriever Agent

↓

🧠 Memory Module

↓

✍️ Executor Agent

↓

Final Response

---

## 🤖 Agent Components

### 🧩 Planner Agent
- Breaks complex queries into structured steps
- Enables multi-step reasoning

### 🔀 Tool Router
- Dynamically selects tools based on task
- Supports modular system expansion

### 🔎 Retriever Agent
- Integrates external tools and APIs
- Fetches relevant contextual data

### 🧠 Memory Module
- Stores previous interactions
- Enables context-aware responses

### ✍️ Executor Agent
- Generates final structured answers
- Combines reasoning + retrieved knowledge

---

## ⚙️ Features

- ✅ Multi-agent architecture
- ✅ Tool routing logic
- ✅ Memory-aware reasoning
- ✅ Fault-tolerant tool integration (fallback system)
- ✅ Interactive Streamlit UI
- ✅ Modular and extensible design

---

## 📦 Tech Stack

- **Python**
- **Streamlit**
- **OpenAI API (optional)**
- **FastAPI (optional)**
- **Docker-ready architecture**

---

## ▶️ Run Locally

```bash
git clone https://github.com/Subiswas36218/multi-agent-llm-system.git
cd multi-agent-llm-system

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt
streamlit run app/streamlit_app.py

🧪 Example Queries

Find AI funding opportunities in Germany

What are the eligibility criteria?

Suggest funding for an AI startup

🔐 Configuration



The system supports two modes:

Mock Mode (default) → No API required

LLM Mode → Requires OpenAI API key

🔮 Future Improvements

🧠 Vector database memory (FAISS)

🔗 Agent-to-Agent communication (A2A)

🌐 Real-time web search integration

☁️ AWS deployment

🎨 Chat-style UI

🎯 Real-World Relevance



This project reflects real-world AI systems used in:

Intelligent personal assistants

Automotive AI systems

Enterprise AI workflows

Decision-support systems

🤝 Contributing

Contributions are welcome. Feel free to open issues or PRs.
