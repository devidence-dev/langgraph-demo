import os
import json
from typing import Annotated

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

load_dotenv()

print("Loading environment variables...")
print("OLLAMA_MODEL:", os.getenv("OLLAMA_MODEL"))
print("OLLAMA_URL:", os.getenv("OLLAMA_URL"))

llm = init_chat_model(
    model=os.getenv("OLLAMA_MODEL"),
    model_provider='ollama',
    base_url=os.getenv("OLLAMA_URL", "http://localhost:11434"),
)


class State(TypedDict):
    """
    Represents the state of the bot, containing a list of messages.

    Attributes:
        messages (list): A list of messages, with additional processing or validation
            provided by the 'add_messages' annotation.
    """
    messages: Annotated[list, add_messages]


graph_builder = StateGraph(State)


def chatbot(state: State):
    """
    Processes the current conversation state and generates a response using the language model.

    Args:
        state (State): The current state of the conversation, expected to contain a "messages" key.

    Returns:
        dict: A dictionary with a single key "messages", containing the response from the language model.
    """
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_edge(START, "chatbot")
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge("chatbot", END)

graph = graph_builder.compile()

user_input = input("Enter your message: ")
state = graph.invoke({"messages": [{"role": "user", "content": user_input}]})

# print("state:", state)

print(state["messages"][-1].content)
