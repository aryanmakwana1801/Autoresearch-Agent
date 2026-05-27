import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.2
)

def supervisor_agent(state: dict) -> dict:
    """Reviews the report quality and decides to approve or request revision."""
    query = state["query"]
    report = state["final_report"]
    iteration = state.get("iteration", 0)

    # Max 2 revision loops to avoid infinite loops
    if iteration >= 2:
        print("[Supervisor] Max iterations reached. Approving report.")
        return {"status": "approved", "iteration": iteration}

    prompt = f"""You are a strict research quality reviewer.

Original Query: {query}

Generated Report:
{report}

Evaluate this report on:
1. Does it fully answer the query?
2. Is it well structured?
3. Are there any gaps or missing insights?

Reply with ONLY one of:
- "APPROVED" if the report is good quality
- "REVISION: <specific feedback>" if it needs improvement
"""

    response = llm.invoke(prompt)
    verdict = response.content.strip()

    if verdict.startswith("APPROVED"):
        print("[Supervisor] Report APPROVED")
        return {"status": "approved", "iteration": iteration + 1}
    else:
        feedback = verdict.replace("REVISION:", "").strip()
        print(f"[Supervisor] Requesting REVISION: {feedback}")
        return {
            "status": "revision",
            "supervisor_feedback": feedback,
            "iteration": iteration + 1
        }