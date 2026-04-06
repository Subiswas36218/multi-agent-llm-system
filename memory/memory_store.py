memory = []

def store_interaction(query, response):
    memory.append({"query": query, "response": response})

def get_memory_context(limit=3):
    context = ""
    for item in memory[-limit:]:
        context += f"Q: {item['query']}\nA: {item['response']}\n"
    return context