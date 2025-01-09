from utils import *
import json
available_callable_tools = {}

def tool(func):
    available_callable_tools[func.__name__] = func
    return func


@tool
def call_calculator(expression: str) -> int:
    """
    Evaluates a simple mathematical expression and returns the result.
    Args:
        expression: A string representing a mathematical expression (e.g., '12 + 8').

    Useful for basic arithmetic operations like addition, subtraction, multiplication, etc.
    """
    return eval(expression)

@tool
def fetch_weather_data(location: str) -> dict:
    """
    Fetches weather data for a specified location.
    Args:
        location: The name of the location for which to retrieve weather data.

    Useful for providing real-time weather information for specific locations.
    """
    # Simulate an API response (dummy data for illustration)
    return json.dumps({"location": location, "temperature": "22°C", "condition": "Clear"})

@tool
def get_time_date_weekday() -> dict:
    """
    Retrieves the current local time as a formatted string.

    Designed for scenarios where the local time is needed,
    such as in interactive systems or when specifically requested by users.
    """

    import datetime
    import asyncio

    x = datetime.datetime.now()
    formatted_time = x.strftime("%I:%M %p")
    date = x.strftime("%Y-%m-%d")
    weekday = x.strftime("%A")
    return json.dumps({"time": formatted_time, "date": date, "weekday": weekday})

@tool
def get_program_status(program_code):
    status = False
    error = ""

    if program_code == "901":
        status = True
    else:
        error = "Not found"
    return json.dumps({
        "status": status,
        "error": error
    })


available_tools = [
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
        name="get_program_status",
        tool_description="Retrieves the current status of a program.",
        parameters={
              **make_parameter_declaration(
                 name="program_code",
                 description="The code of the program to retrieve the status for.",
                 return_type="string"
              )
        },
        required_param="program_code"
    )
]


if __name__ == "__main__":
    for i, k in available_callable_tools.items():
        print(i, k) 

        
    
    