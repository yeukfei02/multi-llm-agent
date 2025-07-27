from strands import Agent
from strands.models import BedrockModel


bedrock_model = BedrockModel(
    model_id="us.meta.llama3-1-70b-instruct-v1:0",
    region_name="us-east-1",
    temperature=0.5,
)

chef_agent = Agent(
    model=bedrock_model,
    system_prompt=(
        "You are a helpful assistant specialized in providing cooking and recipe information. "
        "You can answer questions about ingredients, cooking techniques, and meal planning. "
        "Use your knowledge to provide accurate and helpful responses."
    ),
    tools=[],
)
