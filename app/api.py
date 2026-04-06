from fastapi import FastAPI
from main import run_system

app = FastAPI()

@app.get("/run")
def run(query: str):
    return {"result": run_system(query)}