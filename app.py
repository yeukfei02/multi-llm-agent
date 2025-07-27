from dotenv import load_dotenv
from strands import Agent
from strands.models import BedrockModel
from src.tools.chef_tool import chef_assistant
from src.tools.weather_tool import weather_assistant
from src.tools.code_generator_tool import code_generator_assistant

load_dotenv()


def main():
    bedrock_model = BedrockModel(
        model_id="amazon.nova-micro-v1:0",
        region_name="us-east-1",
        temperature=0.5,
    )

    orchestrator = Agent(
        model=bedrock_model,
        system_prompt=(
            "You are a helpful assistant that can coordinate multiple agents. "
            "You can call different agents to answer questions about weather, cooking, and code generation. "
            "Use your knowledge to provide accurate and helpful responses."
        ),
        callback_handler=None,
        tools=[
            weather_assistant,
            chef_assistant,
            code_generator_assistant
        ]
    )

    query = "What is the weather now in China, Shenzhen?"
    response = orchestrator(query)
    print(f"orchestrator response = {response}\n")

    query = "Can you suggest a chinese food and its recipe for dinner?"
    response = orchestrator(query)
    print(f"orchestrator2 response = {response}\n")

    query = "Can you help me generate a Python code snippet of this problem? A car travels at 80 km/h for 2 hours and then at 60 km/h for 1 hour. What is the total distance traveled?"
    response = orchestrator(query)
    print(f"orchestrator3 response = {response}\n")


main()
