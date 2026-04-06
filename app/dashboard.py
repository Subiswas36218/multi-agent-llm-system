import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from memory.memory_store import memory

st.set_page_config(page_title="Agent Analytics Dashboard", layout="wide")

st.title("📊 Multi-Agent AI System Dashboard")

# -------------------------
# 1. BASIC STATS
# -------------------------
st.header("📈 Overview")

total_queries = len(memory)
st.metric("Total Queries", total_queries)

if total_queries == 0:
    st.warning("No data yet. Run some queries first.")
    st.stop()

# -------------------------
# 2. DATA PREPARATION
# -------------------------
data = pd.DataFrame(memory)

data["query_length"] = data["query"].apply(len)
data["response_length"] = data["response"].apply(len)

# -------------------------
# 3. RECENT ACTIVITY
# -------------------------
st.header("🧠 Recent Interactions")

for i, row in data.tail(5).iterrows():
    with st.expander(f"Query: {row['query']}"):
        st.write("**Response:**")
        st.write(row["response"])

# -------------------------
# 4. RESPONSE LENGTH ANALYSIS
# -------------------------
st.header("📊 Response Length Analysis")

plt.figure()
plt.hist(data["response_length"])
plt.xlabel("Response Length")
plt.ylabel("Frequency")
st.pyplot(plt)

# -------------------------
# 5. QUERY LENGTH VS RESPONSE
# -------------------------
st.header("📉 Query vs Response Length")

plt.figure()
plt.scatter(data["query_length"], data["response_length"])
plt.xlabel("Query Length")
plt.ylabel("Response Length")
st.pyplot(plt)

# -------------------------
# 6. SUMMARY METRICS
# -------------------------
st.header("📌 Summary Statistics")

stats = {
    "Average Query Length": round(data["query_length"].mean(), 2),
    "Average Response Length": round(data["response_length"].mean(), 2),
    "Max Response Length": int(data["response_length"].max()),
    "Min Response Length": int(data["response_length"].min())
}

st.json(stats)

# -------------------------
# 7. TOOL USAGE ESTIMATION
# -------------------------
st.header("🔀 Tool Usage (Estimated)")

def detect_tool(response):
    if "funding" in response.lower():
        return "funding_api"
    return "search_tool"

data["tool"] = data["response"].apply(detect_tool)

tool_counts = data["tool"].value_counts()

st.bar_chart(tool_counts)

# -------------------------
# 8. DOWNLOAD DATA
# -------------------------
st.header("⬇️ Export Data")

csv = data.to_csv(index=False)
st.download_button("Download CSV", csv, "agent_data.csv", "text/csv")