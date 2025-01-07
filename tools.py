def make_tool_declaration(name, tool_description, parameters=None):
    parameter_properties = {}

    if parameters:
        print("not none")
        parameter_properties = {
            "type": "object",
            "properties": parameters,
            "required": []
        }

    return {
        "type": "function",
        "function": {
            "name": name,
            "description": tool_description,
            "parameters": parameter_properties,
        }
    }

def make_parameter_declaration(name: str, description: str, return_type: str):
    return{
        name: {
            "type": return_type,
            "description": description
        }
    }

def userMessage(content):
    return {
        "role": "user",
        "content": content
    }

def SystemMessage(content):
    return {
        "role": "system",
        "content": content
    }

def AIMessage(content):
    return {
        "role": "assistant",
        "content": content
    }

def testAPI():
    import requests,os

    # Replace {model_id} with the actual model ID
    url = "https://api.mistral.ai/v1/models/mistral-large-latest"

    # Headers (example, modify as per API documentation)
    headers = {
        "Authorization": f"Bearer {os.environ["MISTRAL_API_KEY"]}",  # Replace with your actual token
        "Content-Type": "application/json",
    }


    try:
        # Test a simple GET request
        response = requests.get(url, headers=headers)
        
        # Output the result

        if response.status_code == 200:
            return True
        else:
            return False

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")





def call_calculator(expression: str) -> int:
    """
    Evaluates a simple mathematical expression and returns the result.
    Args:
        expression: A string representing a mathematical expression (e.g., '12 + 8').

    Useful for basic arithmetic operations like addition, subtraction, multiplication, etc.
    """
    return eval(expression)


def fetch_weather_data(location: str) -> dict:
    """
    Fetches weather data for a specified location.
    Args:
        location: The name of the location for which to retrieve weather data.

    Useful for providing real-time weather information for specific locations.
    """
    # Simulate an API response (dummy data for illustration)
    return {"location": location, "temperature": "22°C", "condition": "Clear"}



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
    return {"time": formatted_time, "date": date, "weekday": weekday}




