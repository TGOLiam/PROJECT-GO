from utils import make_parameter_declaration, make_tool_declaration
import json
DEFAULT_callable_tools = {}

#Note: All of these are just dummy functions to demonstrate the concept of tools

def tool(func):
    DEFAULT_callable_tools[func.__name__] = func
    return func

@tool
def call_calculator(expression: str) -> int:
    return eval(expression)

@tool
def fetch_weather_data(location: str) -> dict:
    return json.dumps({"location": location, "temperature": "22°C", "condition": "Clear"})

@tool
def get_time_date_weekday() -> dict:
    import datetime
    import asyncio

    x = datetime.datetime.now()
    formatted_time = x.strftime("%I:%M %p")
    date = x.strftime("%Y-%m-%d")
    weekday = x.strftime("%A")
    return json.dumps({"time": formatted_time, "date": date, "weekday": weekday})

DEFAULT_tools = [
    make_tool_declaration(
        name="get_time_date_weekday",
        tool_description="Retrieves the current local time as a formatted string.",
    ),

    make_tool_declaration(
        name="fetch_weather_data",
        tool_description="Fetches weather data for a given location.",
        parameters={
           **make_parameter_declaration(
                name="location",
                description="The location to fetch weather data for.",
                return_type="string"
           )
        },
        required_param="location" 
    ),

    make_tool_declaration(
        name="pirate_agent",
        tool_description="A pirate-themed agent. You will paraphrase pirate_agent's responses back to the user.",
        parameters={
              **make_parameter_declaration(
                 name="query",
                 description="The query to send to the pirate agent.",
                 return_type="string"
              )
        },
    ),

]

if __name__ == "__main__":
    for i, k in DEFAULT_callable_tools.items():
        print(i, k) 

        
    
    