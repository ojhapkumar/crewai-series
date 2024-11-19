from crewai.tools import BaseTool
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

class CustomServerDevTool(BaseTool):
    name: str = "Custom Serper Dev Tool"
    description: str = "Search the internet for news."
    
    def _run(self, query: str) -> str:
        print(f"Searching the internet for {query}")
        
        url = "https://google.serper.dev/news"

        payload = json.dumps({
            "q": query,
            "num": 20,
            "autocorrect": False,
            "tbs": "qdr:d"
        })

        headers = {
            'X-API-KEY': os.getenv("SERPER_API_KEY"),
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        # Parse the JSON response and extract just the news
        response_data = response.json()
        news_items = response_data.get('news', [])
        
        return json.dumps(news_items, indent=2)
