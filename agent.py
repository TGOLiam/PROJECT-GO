import os
from mistralai import Mistral
from tools import *

model = "mistral-large-latest"

with open('instructions.txt', 'r') as file:
  prompt_instructions = file.read()

client = Mistral(api_key=os.environ["MISTRAL_API_KEY"])
tools = [
    make_tool_declaration(
        name="get_time_date_weekday",
        tool_description="Retrieves the current local time as a formatted string.",
    )
]

messages = []






while True:
    query = input("User> ")
    ai_text = ''

    if not testAPI():
       continue
       
    
    messages.append(userMessage(query))

    response = client.agents.complete(
        agent_id="ag:0b708fe2:20250107:agent-go:7b247d5d",
        messages = messages,
        tools=tools,
        tool_choice="auto",
        max_tokens=300,
    )
    print(response.choices[0].message.content)
    print("---------")
    if response.choices[0].message.tool_calls is not None: print(response.choices[0].message.tool_calls)
    print(response.usage.total_tokens)
    print(f"AI: {response.usage.completion_tokens}")
    messages.append(AIMessage(response.choices[0].message.content))

