def make_tool_declaration(name, tool_description, required_param='', parameters=None, ):
    parameter_properties = {}

    if parameters is not None:
        parameter_properties = {
            "type": "object",
            "properties": parameters,
            "required": [required_param]
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
        f"{name}": {
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

def AIMessage(content, tool_calls=None):
    return {
        "role": "assistant",
        "content": content,
        "tool_calls": tool_calls
    }

def ToolMessage(content, tool_name, tool_call_id):
    return {
        "role": "tool",
        "name": tool_name,
        "content": content,
        "tool_call_id": tool_call_id
    }

def testAPI():
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
