def evaluate_response(response: str):
    return {
        "length": len(response),
        "structured": "-" in response or "•" in response,
        "score": min(len(response)/100, 1.0)
    }