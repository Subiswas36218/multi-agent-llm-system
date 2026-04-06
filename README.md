<h1 align="center">🤖 Multi-Agent AI System</h1>

<p align="center">
Agent-Based AI • Tool-Orchestrated Reasoning • Memory-Aware Systems
</p>

<p align="center">
<a href="https://multi-agent-llm-system-dkwzj8rotcwuyqekioeu64.streamlit.app/">
🚀 <b>Live Demo</b>
</a>
</p>

<p align="center">
<img src="https://img.shields.io/badge/Status-Live-success"/>
<img src="https://img.shields.io/badge/Architecture-Multi--Agent-blue"/>
<img src="https://img.shields.io/badge/UI-Streamlit-red"/>
</p>

---

## 🎥 Live Demo

👉 Try the app here:
🔗 https://multi-agent-llm-system-dkwzj8rotcwuyqekioeu64.streamlit.app/

💡 Recommended query: 
Find AI funding opportunities in Germany and explain eligibility criteria

---

## 🧠 Overview

This project implements a **multi-agent AI system** using Large Language Models (LLMs) to simulate:

- 🧩 Task decomposition
- 🔀 Tool routing
- 🔎 Tool-integrated retrieval
- 🧠 Memory-aware reasoning
- ✍️ Contextual response generation

Instead of relying on a single LLM, the system uses **specialized agents** to improve modularity, control, and interpretability.

---

## 💡 Why This Project?

Traditional LLM applications rely on a single model, limiting control and reasoning transparency.

This project demonstrates how **agent-based AI systems**:

- Improve reasoning through task decomposition
- Enable dynamic tool selection
- Provide modular and scalable architecture
- Simulate real-world intelligent assistants

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

## 🔄 System Flow

1. User submits query
2. Planner agent decomposes the task
3. Tool router selects appropriate tools
4. Retriever gathers relevant data
5. Memory module injects past context
6. Executor generates final response

---

## 🤖 Agent Components

### 🧩 Planner Agent
- Breaks queries into structured steps
- Enables multi-step reasoning

### 🔀 Tool Router
- Dynamically selects tools based on intent
- Supports extensibility

### 🔎 Retriever Agent
- Interacts with external tools/APIs
- Fetches contextual data

### 🧠 Memory Module
- Stores previous interactions
- Enables context-aware responses

### ✍️ Executor Agent
- Generates structured responses
- Combines reasoning + retrieved context

---

## ⚙️ Features

- ✅ Multi-agent architecture
- ✅ Dynamic tool routing
- ✅ Memory-aware reasoning
- ✅ Fault-tolerant tool integration (fallback system)
- ✅ ChatGPT-style Streamlit UI
- ✅ Analytics dashboard for system evaluation
- ✅ Modular and extensible design

---

## 📊 Analytics Dashboard

The system includes a built-in dashboard to analyze:

- Query and response patterns
- Response length distribution
- Tool usage behavior
- Interaction history

---

## 🛠️ Engineering Highlights

- Designed modular multi-agent architecture
- Implemented tool routing logic
- Built memory-aware reasoning pipeline
- Added fallback mechanisms for robustness
- Developed interactive UI and analytics dashboard

---

## 📦 Tech Stack

- **Python**
- **Streamlit**
- **OpenAI API (optional)**
- **Pandas / Matplotlib (dashboard)**
- **FastAPI (optional backend)**

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

Compare different funding programs

🔐 Configuration



The system supports two modes:

Mock Mode (default) → No API required

LLM Mode → Requires OpenAI API key

📚 Key Learnings

Designing agent-based AI systems

Orchestrating LLM workflows

Implementing tool routing and memory

Building reliable AI systems with fallbacks

Connecting research concepts to real applications

🔮 Future Work

Vector database memory (FAISS)

Agent-to-agent communication (A2A)

Real-time web search integration

Chat-style UI enhancements

🧠 Project Summary

Built a multi-agent AI system that decomposes tasks, dynamically selects tools, and generates context-aware responses using modular components. The system integrates memory, tool routing, and external tools, simulating real-world intelligent assistant architectures.

🤝 Contributing

Contributions are welcome. Feel free to open issues or PRs.
