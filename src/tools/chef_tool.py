from strands import tool
from src.agents.chef_agent import chef_agent


@tool
def chef_assistant(query: str) -> str:
    result = None

    try:
        chef_agent_result = chef_agent(query)

        result = chef_agent_result
    except Exception as e:
        print(f"chef_assistant error = {e}")

    return str(result)
