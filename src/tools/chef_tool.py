from strands import tool
from src.agents.chef_agent import chef_agent


@tool
def chef_assistant(query: str) -> str:
    chef_agent_result = chef_agent(query)
    print(f"chef_agent_result = {chef_agent_result}\n")

    return str(chef_agent_result)
