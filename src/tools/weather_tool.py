import os
from strands import tool
from src.agents.weather_agent import weather_agent


@tool
def weather_assistant(query: str) -> str:
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

    weather_agent_http_request_response = weather_agent.tool.http_request(
        method="GET",
        url=f"https://api.openweathermap.org/data/2.5/weather?q={query}&appid={OPEN_WEATHER_API_KEY}"
    )
    print(
        f"\n weather_agent_http_request_response = {weather_agent_http_request_response}")

    weather_agent_result = weather_agent(query)
    print(f"\n weather_agent_result = {weather_agent_result}")

    return str(weather_agent_result)
