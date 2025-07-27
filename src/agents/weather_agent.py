from strands import Agent
from strands.models import BedrockModel


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
        "Use your knowledge to provide accurate and helpful responses."
    ),
    tools=[],
)
