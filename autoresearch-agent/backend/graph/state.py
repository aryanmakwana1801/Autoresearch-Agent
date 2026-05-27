from typing import TypedDict, List, Optional

class ResearchState(TypedDict):
    query: str                        # Original user query
    sub_tasks: List[str]              # Planner breaks query into sub-tasks
    search_results: List[dict]        # Raw results from web search
    summaries: List[str]              # Summarized results
    final_report: str                 # Final compiled report
    supervisor_feedback: str          # Supervisor's review feedback
    iteration: int                    # How many review loops done
    status: str                       # Current pipeline status