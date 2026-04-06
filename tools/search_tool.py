def search_tool(query: str):
    database = {
        "funding": "EXIST, Horizon Europe, BMWK Innovation Grants",
        "eligibility": "Startups, SMEs, EU-based entities, innovation-driven"
    }

    for key in database:
        if key in query.lower():
            return database[key]

    return "No data found"