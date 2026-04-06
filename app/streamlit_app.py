import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st

from agents.planner import planner_agent
from agents.retriever import retriever_agent
from agents.executor import executor_agent
from memory.memory_store import store_interaction

st.set_page_config(page_title="Multi-Agent AI System")

st.title("🤖 Multi-Agent LLM System")

query = st.text_input("Enter your query")

if st.button("Run Agent System"):
    if query:
        st.subheader("🧩 Plan")
        steps = planner_agent(query)
        for s in steps:
            st.write("-", s)

        st.subheader("🔎 Retrieval")
        context = ""
        for step in steps:
            result = retriever_agent(step)
            context += result + "\n"
            st.write(result)

        st.subheader("✍️ Final Response")
        response = executor_agent(query, context)
        st.write(response)

        # Store memory
        store_interaction(query, response)