from utils import make_parameter_declaration, make_tool_declaration
import json,os
from tavily import TavilyClient

DB_CALLABLE_TOOLS = {}
def tool(func):
    DB_CALLABLE_TOOLS[func.__name__] = func
    return func

x = ''

DB_TOOLS = [
    
]

if __name__ == "__main__":
    for i, k in DB_CALLABLE_TOOLS.items():
        print(i, k) 

        
    
    