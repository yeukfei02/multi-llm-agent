import os
from dotenv import load_dotenv
from strands import Agent
from strands.models import BedrockModel
from strands_tools import http_request

load_dotenv()

OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

bedrock_model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-20240620-v1:0",
    region_name="us-east-1",
    temperature=0.5,
)

weather_agent = Agent(
    model=bedrock_model,
    system_prompt=(
        "You are a helpful assistant specialized in providing weather information. "
        "You can answer questions about current weather conditions, forecasts, and related topics. "
        f"First, call api, use OPEN_WEATHER_API_KEY env to do a get request to get geocoding data from http://api.openweathermap.org/geo/1.0/direct?q=query&limit=1&appid={OPEN_WEATHER_API_KEY}"
        f"Then use geocoding lat lon to do a get request to get weather data from http://api.openweathermap.org/data/2.5/weather?lat=lat&lon=lon&appid={OPEN_WEATHER_API_KEY}"
        "Use your knowledge to provide accurate and helpful responses."
    ),
    tools=[http_request],
)
