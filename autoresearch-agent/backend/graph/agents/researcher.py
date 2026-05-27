from backend.tools.search_tool import web_search

def researcher_agent(state: dict) -> dict:
    """Searches the web for each sub-task and collects results."""
    sub_tasks = state["sub_tasks"]
    all_results = []

    for task in sub_tasks:
        print(f"[Researcher] Searching: {task}")
        results = web_search(task, max_results=3)
        for r in results:
            r["task"] = task  # tag which task this result belongs to
        all_results.extend(results)

    print(f"[Researcher] Collected {len(all_results)} total results")
    return {"search_results": all_results, "status": "researched"}