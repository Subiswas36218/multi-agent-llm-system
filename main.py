from agents.planner import planner_agent
from agents.retriever import retriever_agent
from agents.executor import executor_agent
from evaluation.metrics import evaluate_response
from memory.memory_store import store_interaction

def run_system(query: str):
    print("\nUSER QUERY:", query)

    steps = planner_agent(query)

    context = ""
    for step in steps:
        context += retriever_agent(step) + "\n"

    response = executor_agent(query, context)

    # Store memory
    store_interaction(query, response)

    metrics = evaluate_response(response)

    print("\nRESPONSE:\n", response)
    print("\nMETRICS:\n", metrics)


if __name__ == "__main__":
    run_system("Find AI funding in Germany and explain eligibility")