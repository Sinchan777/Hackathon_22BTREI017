import requests

class WebSearch:
    @staticmethod
    def simple_search(query: str) -> str:
        try:
            response = requests.get(
                "https://api.duckduckgo.com/",#Provide API key
                params={
                    "q": query,
                    "format": "json",
                    "no_html": 1,
                    "no_redirect": 1
                }
            )
            return response.json().get("AbstractText", "No results found")
        except Exception:
            return "Search failed"