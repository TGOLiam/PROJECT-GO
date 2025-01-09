import os, json,time
from mistralai import Mistral
from tools import *
from utils import *

with open('instructions.txt', 'r') as file:
  prompt_instructions = file.read()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
tools = available_tools
callable_tools = available_callable_tools

messages = [SystemMessage(prompt_instructions)]

def invoke_chat_query():
    while True:
        try:
            response = client.chat.complete(
                model="mistral-large-latest",
                messages = messages,
                tools=tools,
                tool_choice="auto",
                max_tokens=300,
            )
            tool_calls = response.choices[0].message.tool_calls
            content = response.choices[0].message.content
            usage = response.usage

            messages.append(AIMessage(content=content, tool_calls=tool_calls))

            print(f"\033[92mAssistant: {response.choices[0].message.content}\033[0m")
            print("---------")
            print(f"Total Token Usage: {usage.total_tokens}")
            print(f"AI Token Usage: {usage.completion_tokens}")

            return response

        except ValueError as ve:
            print(f"ValueError: {ve}")
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(5)

def execute_tool_call(tool_calls):
    try:
        function_name = tool_calls[0].function.name
        arguments = json.loads(tool_calls[0].function.arguments)
        result = callable_tools[function_name](**arguments)

        print(f"Tool Result: {result}")
        print(f"Tool Name: {function_name}")
        print(f"Tool Arguments: {arguments}")
        print("---------")
        tool_message = ToolMessage(content=result, tool_name=function_name, tool_call_id=tool_calls[0].id)
        messages.append(tool_message)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(5)


while True:
    if testAPI() == False:
       print("Theres something wrong..")
       continue

    query = input("User> ")

    if query.lower() == "print":
        for i in messages:
            print(i)
        continue

    messages.append(userMessage(query))
    response = invoke_chat_query()

    tool_calls = response.choices[0].message.tool_calls

    if tool_calls is not None: 
        execute_tool_call(tool_calls)
        time.sleep(1)
        invoke_chat_query()
        
    

