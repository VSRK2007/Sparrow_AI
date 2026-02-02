import logging
from livekit.agents import function_tool, Runcontext
import requests
from langchain_community.tools import DuckDuckGoSearchRun

@function_tool()
async def get_weather(
    context: RunContext,
    city: str) -> str:
    """
    get the current weather for a given city.
    """
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3")
        if response.status_code == 200:
            logging.info(f"Weather in {city}: {response.text.strip()}")
            return response.text.strip()
        else:
            logging.error(f"Failed to get weather for {city}: {response.status_code}")
            return f"could not retrive weather for {city}."
    except Exception as e:
        logging.error(f"Error getting weather for {city}: {e}")
        return f"could not retrive weather for {city}."
    
    @function_tool()
    async def search_web(
       context: RunContext,
        query: str) -> str:
         """
         search the web using DuckDuckGo.
         """
         try:
             result = DuckDuckGoSearchRun().run(tool_input=query)
             logging.info(f"Search results for {query}: {result}")
             return result
         except Exception as e:
             logging.error(f"Error searching the web for {query}: {e}")
             return f"could not search the web for {query}."