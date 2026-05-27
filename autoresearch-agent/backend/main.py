from fastapi import FastAPI
from pydantic import BaseModel
from backend.graph.graph import research_graph

app = FastAPI(title="AutoResearch Agent API")

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def root():
    return {"message": "AutoResearch Agent is running!"}

@app.post("/research")
def run_research(request: QueryRequest):
    print(f"\n[API] Received query: {request.query}")
    
    initial_state = {
        "query": request.query,
        "sub_tasks": [],
        "search_results": [],
        "summaries": [],
        "final_report": "",
        "supervisor_feedback": "",
        "iteration": 0,
        "status": "started"
    }
    
    result = research_graph.invoke(initial_state)
    
    return {
        "query": request.query,
        "report": result["final_report"],
        "status": result["status"],
        "iterations": result["iteration"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)