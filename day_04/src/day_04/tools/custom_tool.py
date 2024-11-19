from crewai.tools import BaseTool

class CustomServerDevTool(BaseTool):
    name: str = "Custom Serper Dev Tool"
    description: str = "Search the internet for news."
    
    def _run(query)