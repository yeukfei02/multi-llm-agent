from strands import Agent
from strands.models import BedrockModel
from strands_tools import http_request


bedrock_model = BedrockModel(
    model_id="us.amazon.nova-micro-v1:0",
    region_name="us-east-1",
    temperature=0.3,
)

weather_agent = Agent(
    model=bedrock_model,
    system_prompt=(
        "You are a helpful assistant specialized in providing weather information. "
        "You can answer questions about current weather conditions, forecasts, and related topics. "
        "Use your knowledge to provide accurate and helpful responses."
    ),
    tools=[http_request],
)
