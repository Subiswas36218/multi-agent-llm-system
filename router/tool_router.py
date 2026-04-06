def route_tool(step: str):
    step_lower = step.lower()

    if "funding" in step_lower:
        return "funding_api"
    elif "eligibility" in step_lower:
        return "funding_api"
    else:
        return "search_tool"