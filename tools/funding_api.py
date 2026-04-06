import requests

def funding_api(query: str):
    try:
        url = "https://api.publicapis.org/entries"
        res = requests.get(url, timeout=5)

        if res.status_code == 200:
            data = res.json()
            return f"Retrieved {len(data.get('entries', []))} entries (simulated funding data)"

    except Exception:
        # ✅ Fallback (VERY IMPORTANT)
        return fallback_funding_data(query)


def fallback_funding_data(query: str):
    return """
Top AI Funding Programs in Germany:

1. EXIST Startup Grant
   - For university-based startups
   - Covers living expenses + resources

2. Horizon Europe
   - EU-wide funding program
   - Supports innovation and research

3. BMWK Innovation Grants
   - Government funding for tech innovation

Eligibility:
- Startups or SMEs
- Innovation-driven idea
- EU/Germany-based entity
"""