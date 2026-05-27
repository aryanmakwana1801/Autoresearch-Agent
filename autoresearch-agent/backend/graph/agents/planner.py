import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

def planner_agent(state: dict) -> dict:
    """Breaks the user query into focused sub-tasks for research."""
    query = state["query"]

    prompt = f"""You are a research planner. Break the following query into 3-4 specific, 
focused sub-tasks that a researcher should investigate.

Query: {query}

Return ONLY a numbered list of sub-tasks. No explanation, no intro, just the list.
Example:
1. Sub-task one
2. Sub-task two
3. Sub-task three
"""
    response = llm.invoke(prompt)
    raw = response.content.strip()

    # Parse numbered list into clean list
    sub_tasks = []
    for line in raw.split("\n"):
        line = line.strip()
        if line and line[0].isdigit():
            # Remove "1. " prefix
            task = line.split(".", 1)[-1].strip()
            sub_tasks.append(task)

    print(f"[Planner] Generated {len(sub_tasks)} sub-tasks")
    return {"sub_tasks": sub_tasks, "status": "planned"}