from strands import tool
from src.agents.code_generator_agent import code_generator_agent


@tool
def code_generator_assistant(query: str) -> str:
    result = None

    try:
        code_generator_agent_result = code_generator_agent(query)
        print(
            f"\n code_generator_agent_result = {code_generator_agent_result}")

        result = code_generator_agent_result
    except Exception as e:
        print(f"code_generator_assistant error = {e}")

    return str(result)
