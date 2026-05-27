import os
from tavily import TavilyClient  # type: ignore
from dotenv import load_dotenv

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def web_search(query: str, max_results: int = 5) -> list[dict]:
    """Search the web and return list of results with title, url, content."""
    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=max_results
        )
        results = []
        for r in response.get("results", []):
            results.append({
                "title": r.get("title", ""),
                "url": r.get("url", ""),
                "content": r.get("content", "")
            })
        return results
    except Exception as e:
        return [{"title": "Error", "url": "", "content": str(e)}]