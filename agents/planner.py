from config import USE_REAL_LLM

if USE_REAL_LLM:
    import os
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def planner_agent(query: str):
    if not USE_REAL_LLM:
        return [
            "Search AI funding programs in Germany",
            "Find eligibility criteria",
            "Summarize results"
        ]

    prompt = f"Break into steps:\n{query}"

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    steps = res.choices[0].message.content.split("\n")
    return [s.strip() for s in steps if s.strip()]