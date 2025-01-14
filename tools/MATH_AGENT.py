from utils import make_parameter_declaration, make_tool_declaration
import json

MATH_CALLABLE_TOOLS = {}
def tool(func):
    MATH_CALLABLE_TOOLS[func.__name__] = func
    return func

@tool
def basic_arithmetic(expression):
    try:
        # Evaluate the math expression
        result = eval(expression)
        return str(result)  # Convert result to string
    except Exception as e:
        return f"Error: {e}"  # Return error message as string

MATH_TOOLS = [
    make_tool_declaration(
        name="basic_arithmetic",
        tool_description="tool for solving arithmetic problems",
        parameters={
            **make_parameter_declaration(
                name="expression",
                description="The expression of the problem to be solved. THIS NEEDS TO BE A STRING",
                return_type="string"
            ),
        },
        required_param=['expression']
    ),
]

if __name__ == "__main__":
    for i, k in MATH_CALLABLE_TOOLS.items():
        print(i, k) 

        
    
    