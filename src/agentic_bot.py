import os
from typing import Annotated, Literal

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

load_dotenv()

llm = init_chat_model(
    model=os.getenv("OLLAMA_MODEL"),
    model_provider='ollama',
    base_url=os.getenv("OLLAMA_URL", "http://localhost:11434"),
)


class MessageClassifier(BaseModel):
    message_type: Literal["emotional", "logical"] = Field(
        ...,
        description="Classify if the message requires an emotional (therapist) or logical response.",
    )


class State(TypedDict):
    messages: Annotated[list, add_messages]
    message_type: str | None


def classify_message(state: State):
    last_message = state["messages"][-1]
    classifier_llm = llm.with_structured_output(MessageClassifier)
    result = classifier_llm.invoke([
        {
            "role": "system",
            "content": """Classify the user message as either:
            - 'emotional': if it asks for emotional support, therapy, deals with feelings, or personal problems
            - 'logical': if it asks for facts, information, logical analysis, or practical solutions
            """
        },
        {
            "role": "user",
            "content": last_message.content,
        }
    ])

    return {"message_type": result.message_type}


def router(state: State):
    message_type = state.get("message_type", "logical")
    if message_type == "emotional":
        return {"next": "therapist"}

    return {"next": "logical"}


def therapist_agent(state: State):


    """
    Acts as a compassionate therapist agent that processes the latest user message, focusing on emotional support.

    Args:
        state (State): A dictionary-like object containing a "messages" key, which is a list of message objects. The last message is assumed to be from the user.

    Returns:
        dict: A dictionary with a single key "messages", containing a list with the assistant's empathetic reply.
    """
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """You are a compassionate therapist. Focus on the emotional aspects of the user's message.
            Show empathy, validate their feelings, and help them process their emotions.
            Ask thoughtful questions to help them explore their feelings more deeply.
            Avoid giving logical solutions unless explicitly asked."""
        },
        {
            "role": "user",
            "content": last_message.content,
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}


def logical_agent(state: State):
    """
    Processes the current conversation state and generates a logical, fact-based assistant response.

    Args:
        state (State): The current conversation state, expected to contain a "messages" key with a list of message objects.

    Returns:
        dict: A dictionary containing the assistant's reply in the "messages" key, where the reply is direct, logical, and devoid of emotional content.
    """
    last_message = state["messages"][-1]
    messages = [
        {
            "role": "system",
            "content": """You are a purely logical assistant. Focus only on facts and information.
            Provide clear, concise answers based on logic and evidence.
            Do not address emotions or provide emotional support.
            Be direct and straightforward in your responses."""
        },
        {
            "role": "user",
            "content": last_message.content,
        }
    ]
    reply = llm.invoke(messages)
    return {"messages": [{"role": "assistant", "content": reply.content}]}


graph_builder = StateGraph(State)

graph_builder.add_edge(START, "classifier")

graph_builder.add_node("classifier", classify_message)
graph_builder.add_edge("classifier", "router")
graph_builder.add_node("router", router)
graph_builder.add_conditional_edges(
    "router",
    lambda state: state.get("next"),
    {
        "therapist": "therapist",
        "logical": "logical",
    },
)
graph_builder.add_node("therapist", therapist_agent)
graph_builder.add_node("logical", logical_agent)

graph_builder.add_edge("therapist", END)
graph_builder.add_edge("logical", END)

graph = graph_builder.compile()


def run_chatbot():
    state = {
        "messages": [],
        "message_type": None,
    }

    while True:
        user_input = input("Enter your message: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Seeyaa! 👋")
            break

        # state["messages"] = state.get("messages", []) + [{"role": "user", "content": user_input}]
        state["messages"].append({"role": "user", "content": user_input})

        state = graph.invoke(state)

        # Print the assistant's response
        if state.get("messages") and len(state["messages"]) > 0:
            assistant_response = state["messages"][-1]
            print(f"Assistant: {assistant_response.content}")


if __name__ == "__main__":
    run_chatbot()
   