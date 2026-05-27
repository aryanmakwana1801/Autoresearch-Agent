from langgraph.graph import StateGraph, END
from backend.graph.state import ResearchState
from backend.graph.agents.planner import planner_agent
from backend.graph.agents.researcher import researcher_agent
from backend.graph.agents.summarizer import summarizer_agent
from backend.graph.agents.writer import writer_agent
from backend.graph.agents.supervisor import supervisor_agent

def route_supervisor(state: dict) -> str:
    """Routes based on supervisor decision."""
    if state.get("status") == "approved":
        return "end"
    else:
        return "writer"  # Loop back to writer with feedback

def build_graph():
    graph = StateGraph(ResearchState)

    # Add all agent nodes
    graph.add_node("planner", planner_agent)
    graph.add_node("researcher", researcher_agent)
    graph.add_node("summarizer", summarizer_agent)
    graph.add_node("writer", writer_agent)
    graph.add_node("supervisor", supervisor_agent)

    # Define the flow
    graph.set_entry_point("planner")
    graph.add_edge("planner", "researcher")
    graph.add_edge("researcher", "summarizer")
    graph.add_edge("summarizer", "writer")
    graph.add_edge("writer", "supervisor")

    # Supervisor either approves (END) or loops back to writer
    graph.add_conditional_edges(
        "supervisor",
        route_supervisor,
        {
            "end": END,
            "writer": "writer"
        }
    )

    return graph.compile()

research_graph = build_graph()