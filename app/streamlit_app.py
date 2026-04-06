import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agents.planner import planner_agent
from agents.retriever import retriever_agent
from agents.executor import executor_agent
from memory.memory_store import store_interaction

st.set_page_config(page_title="Multi-Agent AI", layout="wide")

st.title("🤖 Multi-Agent AI Assistant")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Input
query = st.chat_input("Ask something...")

if query:
    # User message
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.write(query)

    # System processing
    steps = planner_agent(query)

    context = ""
    for step in steps:
        context += retriever_agent(step) + "\n"

    response = executor_agent(query, context)

    store_interaction(query, response)

    # Assistant message
    with st.chat_message("assistant"):
        st.write(response)

    st.session_state.messages.append({"role": "assistant", "content": response})