import os, json,time
from mistralai import Mistral
from tools.DEFAULT_AGENT import DEFAULT_tools, DEFAULT_callable_tools
from utils import word_count, UserMessage, SystemMessage, AIMessage, ToolMessage, testAPI

with open('instructions/DEFAULT_AGENT.txt', 'r') as file:
  prompt_instructions = file.read()

class Agent:
    def __init__(
        self,
        system_instructions: str = prompt_instructions,
        chat_history: list[dict] = [],
        client= Mistral(api_key=os.environ["MISTRAL_API_KEY"]),
        model: str = "mistral-large-latest", 
        tools: list[dict] = DEFAULT_tools,
        callable_tools: dict = DEFAULT_callable_tools,
        tool_choice: str = "auto",
        max_tokens: int = 300,
        temperature: float = 0.56,
        stream: bool = False,
        window_size: int = 7,
        allow_print: bool = True
    ):
        chat_history.append(SystemMessage(system_instructions))
        self.client = client
        self.chat_history = chat_history
        self.model = model
        self.tools = tools
        self.tool_choice = tool_choice
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.stream = stream
        self.callable_tools = callable_tools
        self.total_tokens = 0
        self.window_size = window_size
        self.allow_print = allow_print

    def invoke_chat_query(self, query: str = None) -> dict:
        if query is not None:
            self.chat_history.append(UserMessage(query))

        while True:
            try:
                response = self.client.chat.complete(
                    model=self.model,
                    messages = self.chat_history,
                    tools=self.tools,
                    tool_choice=self.tool_choice,
                    max_tokens=self.max_tokens,
                    temperature=self.temperature,
                    stream=self.stream
                )
                tool_calls = response.choices[0].message.tool_calls
                content = response.choices[0].message.content
                usage = response.usage

                self.chat_history.append(AIMessage(content=content, tool_calls=tool_calls))

                self.total_tokens += usage.total_tokens

                if self.allow_print:
                    print(f"\033[92mAssistant: {response.choices[0].message.content}\033[0m")
                    print("---------")
                    print(f"Tool calls: {tool_calls}")
                    print(f"Token Usage: {usage.total_tokens}")
                    print(f"AI Token Usage: {usage.completion_tokens}")
                    print(f"Total Token Usage: {self.total_tokens}")
                    print(f"Word Count: {word_count(content)}")

                if tool_calls is not None: 
                    self.execute_tool_call(tool_calls)
                    time.sleep(1)
                    self.invoke_chat_query()

                if len(self.chat_history) > self.window_size + 1:
                    print(f"Larger than {self.window_size}")
                    self.delete_past_messages()

                return response

            except ValueError as ve:
                print(f"ValueError: {ve}")
            except Exception as e:
                print(f"An error occurred: {e}")
            time.sleep(5)

    def execute_tool_call(self, tool_calls) -> None:
        try:
            function_name = tool_calls[0].function.name
            arguments = json.loads(tool_calls[0].function.arguments)
            result = self.callable_tools[function_name](**arguments)

            print(f"Tool Result: {result}")
            print(f"Tool Name: {function_name}")
            print(f"Tool Arguments: {arguments}")
            print("---------")

            tool_message = ToolMessage(content=result, tool_name=function_name, tool_call_id=tool_calls[0].id)
            self.chat_history.append(tool_message)

        except Exception as e:
            print(f"An error occurred: {e}")
            time.sleep(5)

    def delete_past_messages(self):
        total_len = len(self.chat_history)
        threshold = total_len - self.window_size
        for i in range(1, threshold):
            self.chat_history.pop(1)
    

def console_chat():
    if testAPI() == False:
        print("Theres something wrong..")

    agent = Agent()

    while True:
        query = input("User> ")
        
        if query.lower() == "print":
            for i in agent.chat_history:
                print(i)
            continue

        agent.invoke_chat_query(query=query)
        
if __name__ == "__main__":
    console_chat()        
    

