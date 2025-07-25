from strands import Agent
from strands.models import BedrockModel


bedrock_model = BedrockModel(
    model_id="us.deepseek.r1-v1:0",
    region_name="us-east-1",
    temperature=0.3,
)

code_generator_agent = Agent(
    model=bedrock_model,
    system_prompt=(
        "You are a helpful assistant specialized in generating code snippets. "
        "You can answer questions about programming, algorithms, and code generation. "
        "Use your knowledge to provide accurate and helpful responses."
    ),
    tools=[],
)
