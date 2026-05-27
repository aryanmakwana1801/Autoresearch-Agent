import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

def summarizer_agent(state: dict) -> dict:
    """Summarizes each search result into concise insights."""
    search_results = state["search_results"]
    summaries = []

    for result in search_results:
        if not result.get("content"):
            continue

        prompt = f"""Summarize the following web content into 2-3 concise, informative sentences.
Focus on key facts and insights relevant to: {result.get('task', 'the research query')}

Content:
{result['content'][:2000]}

Summary:"""

        response = llm.invoke(prompt)
        summary = f"[{result['title']}] {response.content.strip()}"
        summaries.append(summary)

    print(f"[Summarizer] Created {len(summaries)} summaries")
    return {"summaries": summaries, "status": "summarized"}