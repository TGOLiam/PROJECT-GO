import yaml
with open("system_instructions.yaml", "r") as file:
    data = yaml.safe_load(file)
    system_instructions = data['system_instructions']


def make_tool_declaration(name: str, tool_description: str, required_param=[], parameters=None) -> dict:
    parameter_properties = {}

    if parameters is not None:
        parameter_properties = {
            "type": "object",
            "properties": parameters,
            "required": required_param
        }

    return {
        "type": "function",
        "function": {
            "name": name,
            "description": tool_description,
            "parameters": parameter_properties,
        }
    }

def make_parameter_declaration(name: str, description: str, return_type: str) -> dict:
    return{
        f"{name}": {
            "type": return_type,
            "description": description
        }
    }

def UserMessage(content: str) -> dict:
    return {
        "role": "user",
        "content": content
    }

def SystemMessage(content: str) -> dict:
    return {
        "role": "system",
        "content": content
    }

def AIMessage(content: str, tool_calls=None) -> dict:
    return {
        "role": "assistant",
        "content": content,
        "tool_calls": tool_calls
    }

def ToolMessage(content: str, tool_name: str, tool_call_id: str) -> dict:
    return {
        "role": "tool",
        "name": tool_name,
        "content": content,
        "tool_call_id": tool_call_id
    }

def word_count(text: str) -> int:
    return len(text.split())

def testAPI() -> bool:
    import requests,os
    url = "https://api.mistral.ai/v1/models/mistral-large-latest"

    headers = {
        "Authorization": f"Bearer {os.environ["MISTRAL_API_KEY"]}",
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



    