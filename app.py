from dotenv import load_dotenv
from strands import Agent
from strands.models import BedrockModel
from src.tools.chef_tool import chef_assistant
from src.tools.weather_tool import weather_assistant
from src.tools.code_generator_tool import code_generator_assistant

load_dotenv()


def main():
    bedrock_model = BedrockModel(
        model_id="us.amazon.nova-lite-v1:0",
        region_name="us-east-1",
        temperature=0.3,
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

    query = "What is the weather like in China Shenzhen? Can you suggest a chinese recipe for dinner? Also, can you help me generate a Python code snippet to fetch weather data?"
    response = orchestrator(query)
    print(f"\n orchestrator response = {response}")


main()
