from router.tool_router import route_tool
from tools.search_tool import search_tool
from tools.funding_api import funding_api

def retriever_agent(step: str):
    tool = route_tool(step)

    if tool == "funding_api":
        result = funding_api(step)
    else:
        result = search_tool(step)

    return f"[{tool}] {step} → {result}"