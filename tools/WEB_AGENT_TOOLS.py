from utils import make_parameter_declaration, make_tool_declaration
import json,os
from tavily import TavilyClient
tavily_client = TavilyClient(api_key=os.environ['TVLY_API_KEY'])

WEB_CALLABLE_TOOLS = {}
def tool(func):
    WEB_CALLABLE_TOOLS[func.__name__] = func
    return func

@tool
def full_search(query):
    response = tavily_client.search(query=query, max_results=5, search_depth='advanced')
    return json.dumps(response)

WEB_TOOLS = [
    make_tool_declaration(
        name="full_search",
        tool_description="Tool for detailed searching.",
        parameters={
            **make_parameter_declaration(
                name="query",
                description="The query to be searched",
                return_type="string"
            )
        },
        required_param=['query']
    )

    

    


]

if __name__ == "__main__":
    for i, k in WEB_CALLABLE_TOOLS.items():
        print(i, k) 

        
    
    