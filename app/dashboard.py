import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from memory.memory_store import memory
from memory.memory_store import memory

st.title("📊 Agent System Analytics")

st.subheader("Total Queries")
st.write(len(memory))

st.subheader("Recent Queries")
for item in memory[-5:]:
    st.write("Q:", item["query"])
    st.write("A:", item["response"])
    st.divider()

# Simple metrics
lengths = [len(item["response"]) for item in memory]

if lengths:
    st.subheader("Response Length Stats")
    st.write({
        "avg_length": sum(lengths)/len(lengths),
        "max_length": max(lengths),
        "min_length": min(lengths)
    })