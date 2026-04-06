from config import USE_REAL_LLM
from memory.memory_store import get_memory_context

if USE_REAL_LLM:
    import os
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def executor_agent(query: str, context: str):
    memory_context = get_memory_context()

    if not USE_REAL_LLM:
        return f"""
AI Funding in Germany:

- EXIST Program
- Horizon Europe
- BMWK Innovation Grants

Eligibility:
- Startups / SMEs
- Innovation-driven
- EU-based entities

Previous Context:
{memory_context}
"""

    prompt = f"""
    Previous:
    {memory_context}

    Query:
    {query}

    Context:
    {context}
    """

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return res.choices[0].message.content