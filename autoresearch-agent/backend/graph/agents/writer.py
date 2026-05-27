import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5
)

def writer_agent(state: dict) -> dict:
    """Compiles all summaries into a structured final report."""
    query = state["query"]
    summaries = state["summaries"]
    feedback = state.get("supervisor_feedback", "")

    summaries_text = "\n".join(f"- {s}" for s in summaries)

    feedback_section = ""
    if feedback:
        feedback_section = f"\nPrevious review feedback to incorporate:\n{feedback}\n"

    prompt = f"""You are an expert research writer. Write a comprehensive, well-structured report.

Research Query: {query}
{feedback_section}
Research Findings:
{summaries_text}

Write a detailed report with these sections:
# Research Report: {{topic}}

## Executive Summary
## Key Findings
## Detailed Analysis
## Conclusion

Make it professional, insightful, and well-organized.
"""

    response = llm.invoke(prompt)
    report = response.content.strip()

    print("[Writer] Report compiled successfully")
    return {"final_report": report, "status": "written"}