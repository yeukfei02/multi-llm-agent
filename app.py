import os
from dotenv import load_dotenv
from src.agents.weather_agent import weather_agent
from src.agents.chef_agent import chef_agent
from src.agents.code_generator_agent import code_generator_agent

load_dotenv()


def main():
    # weather agent
    weather_agent_func()

    # chef agent
    chef_agent_func()

    # code generator agent
    code_generator_agent_func()


def weather_agent_func():
    OPEN_WEATHER_API_KEY = os.getenv("OPEN_WEATHER_API_KEY")

    weather_agent_http_request_response = weather_agent.tool.http_request(
        method="GET",
        url=f"https://api.openweathermap.org/data/2.5/weather?q=Shenzhen&appid={OPEN_WEATHER_API_KEY}"
    )
    print(
        f"weather_agent_http_request_response = {weather_agent_http_request_response}\n")

    weather_agent_result = weather_agent(
        "What is the current weather in Shenzhen?"
    )
    print(f"weather_agent_result = {weather_agent_result}\n")


def chef_agent_func():
    chef_agent_result = chef_agent("What is a good recipe for chicken curry?")
    print(f"chef_agent_result = {chef_agent_result}\n")


def code_generator_agent_func():
    code_generator_agent_result = code_generator_agent(
        "How to write a Python function to solve this question: A car travels at 90 km/h for 2 hours, then at 60 km/h for another 3 hours. What is the average speed of the car for the entire journey?")
    print(f"code_generator_agent_result = {code_generator_agent_result}\n")


main()
