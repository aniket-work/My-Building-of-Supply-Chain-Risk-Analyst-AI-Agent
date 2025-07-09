# tools.py
# Defines the tools that the AI agent can use to gather information.
# For this use case, we have a specialized tool for searching supply chain news.

import os
import httpx
from abc import ABC, abstractmethod

class BaseTool(ABC):
    """Abstract base class for all tools."""
    name: str
    description: str
    details: str

    @abstractmethod
    async def use(self, tool_input: str) -> str:
        """The core logic of the tool."""
        pass

class SupplyChainNewsSearchTool(BaseTool):
    """
    A tool for searching real-time news and reports related to the global supply chain.
    It uses the Tavily Search API to find relevant information.
    """
    name = "supply_chain_news_search"
    description = (
        "Searches for up-to-date news, articles, and reports on supply chain events. "
        "Use this to find information on port closures, trade tariffs, supplier issues, "
        "natural disasters affecting logistics, and geopolitical tensions."
    )
    details = (
        "<tool_details>\n"
        "  <name>supply_chain_news_search</name>\n"
        "  <description>Searches for real-time news and reports about the global supply chain.</description>\n"
        "  <parameters>\n"
        "    <param name='query' type='string' required='true'>A specific search query. For example: 'port congestion in Shanghai' or 'impact of semiconductor shortage on automotive industry'.</param>\n"
        "  </parameters>\n"
        "</tool_details>"
    )

    async def use(self, tool_input: str) -> str:
        """
        Performs a search using the Tavily API.

        Args:
            tool_input (str): The search query.

        Returns:
            str: A formatted string of search results or an error message.
        """
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            return "Error: TAVILY_API_KEY is not set. The search tool cannot function."

        url = "https://api.tavily.com/search"
        payload = {
            "api_key": api_key,
            "query": tool_input,
            "search_depth": "advanced",
            "include_answer": False,
            "max_results": 5
        }

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload)
                response.raise_for_status() # Raise an exception for bad status codes
                results = response.json()

                if not results.get("results"):
                    return f"No search results found for query: '{tool_input}'"

                # Format the results for the agent
                formatted_results = []
                for res in results["results"]:
                    formatted_results.append(f"- Title: {res['title']}\n  URL: {res['url']}\n  Snippet: {res['content']}\n")
                return "\n".join(formatted_results)

        except httpx.HTTPStatusError as e:
            return f"Error performing search: HTTP Status {e.response.status_code} - {e.response.text}"
        except Exception as e:
            return f"An unexpected error occurred during search: {e}"
