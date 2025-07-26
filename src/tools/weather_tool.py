from strands import tool
from src.agents.weather_agent import weather_agent


@tool
def weather_assistant(query: str) -> str:
    result = None

    try:
        weather_agent_result = weather_agent(query)

        result = weather_agent_result
    except Exception as e:
        print(f"weather_assistant error = {e}")

    return str(result)
