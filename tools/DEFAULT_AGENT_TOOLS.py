from utils import make_parameter_declaration, make_tool_declaration
import json, os, time
from tools.MATH_AGENT import MATH_CALLABLE_TOOLS, MATH_TOOLS
from tools.WEB_AGENT_TOOLS import WEB_CALLABLE_TOOLS, WEB_TOOLS

with open('instructions/WEB_AGENT.txt', 'r') as file:
  web_instructions = file.read()

DEFAULT_callable_tools = {}
def tool(func):
    DEFAULT_callable_tools[func.__name__] = func
    return func

@tool
def math_agent(query):
    from agent import Agent

    pirate = Agent(
        system_instructions="You are a math solver",
        allow_print=False,
        window_size=4,
        tools=MATH_TOOLS,
        callable_tools=MATH_CALLABLE_TOOLS
    )

    response = pirate.invoke_chat_query(query)
    return response.choices[0].message.content

@tool
def web_agent(query):
    from agent import Agent

    web = Agent(
        system_instructions=web_instructions,
        allow_print=False,
        window_size=4,
        tools=WEB_TOOLS,
        callable_tools=WEB_CALLABLE_TOOLS,
    )

    response = web.invoke_chat_query(query)
    time.sleep(1)
    return response.choices[0].message.content


DEFAULT_tools = [
    make_tool_declaration(
        name="math_agent",
        tool_description="Ask this agent for when answering math related queries",
        parameters={
              **make_parameter_declaration(
                 name="query",
                 description="The query to send to the math agent.",
                 return_type="string"
              )
        },
    ),


    make_tool_declaration(
        name="web_agent",
        tool_description="Ask this web searching agent for when answering accurate and detailed information related queries",
        parameters={
              **make_parameter_declaration(
                 name="query",
                 description="The query to send to the web agent.",
                 return_type="string"
              )
        },
    ),
]

if __name__ == "__main__":
    for i, k in DEFAULT_callable_tools.items():
        print(i, k)
    query = input("Enter: ") 
    web_agent(query)
        
    
    