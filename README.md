# 🤖 LangGraph Demo

A demonstration project showcasing LangGraph integration with Ollama for building intelligent conversation agents. 🚀

## 📋 Overview

This project contains two different chatbot implementations using LangGraph and Ollama:

1. **Simple Bot** (`simple_bot.py`) - A basic chatbot that responds to user input 💬
2. **Agentic Bot** (`agentic_bot.py`) - An intelligent agent that classifies messages and routes them to specialized handlers (therapist or logical agent) 🧠

## ✨ Features

- **LangGraph Integration**: Uses LangGraph for building stateful conversation flows 🔄
- **Ollama Support**: Leverages local Ollama models for language processing 🏠
- **Message Classification**: Automatically classifies user messages as emotional or logical 🎯
- **Dual Agent System**: Routes messages to either a therapist agent or logical agent based on content 🤝
- **Interactive CLI**: Command-line interface for real-time conversations 💻

## 📁 Project Structure

```
langgraph-demo/
├── pyproject.toml          # Project dependencies and metadata
├── README.md               # This file
├── uv.lock                 # Lock file for dependencies
└── src/
    ├── simple_bot.py       # Basic chatbot implementation
    └── agentic_bot.py      # Advanced agentic chatbot with routing
```

## 📋 Prerequisites

- Python 3.13 or higher 🐍
- [Ollama](https://ollama.ai/) installed and running locally 🦙
- A compatible Ollama model (e.g., llama2, mistral, etc.) 🤖

## 🚀 Installation

1. **Clone the repository** 📥:
   ```bash
   git clone <repository-url>
   cd langgraph-demo
   ```

2. **Install dependencies using uv** (recommended) ⚡:
   ```bash
   uv sync
   ```

   Or using pip 📦:
   ```bash
   pip install -e .
   ```

3. **Set up environment variables** 🔧:
   Create a `.env` file in the project root:
   ```env
   OLLAMA_MODEL=gemma3:1b  # or your preferred model
   OLLAMA_URL=http://localhost:11434
   ```

4. **Ensure Ollama is running** 🏃:
   ```bash
   ollama serve
   ```

   And pull your desired model:
   ```bash
   ollama pull llama2
   ```

## 🎯 Usage

### Simple Bot 🤖

Run the basic chatbot:

```bash
python src/simple_bot.py
```

This will prompt you for a single message and return a response. 💭

### Agentic Bot 🧠

Run the advanced chatbot with message classification:

```bash
python src/agentic_bot.py
```

This starts an interactive conversation where:
- Messages are automatically classified as "emotional" or "logical" 📊
- Emotional messages are routed to a therapist agent 💚
- Logical messages are routed to a fact-based assistant 🧮
- Type `exit` or `quit` to end the conversation 👋

## ⚙️ How It Works

### Simple Bot Architecture 🏗️

1. User inputs a message 💬
2. Message is processed by the LLM through LangGraph 🔄
3. Response is generated and displayed ✨

### Agentic Bot Architecture 🏛️

1. **Classifier Node**: Analyzes the user's message and classifies it as emotional or logical 🔍
2. **Router Node**: Determines which agent should handle the message 🚦
3. **Therapist Agent**: Provides empathetic, emotional support responses 💚
4. **Logical Agent**: Provides fact-based, analytical responses 📊

The flow uses LangGraph's conditional edges to route messages appropriately. 🛤️

## 📦 Dependencies

- **langchain[ollama]**: LangChain framework with Ollama integration 🔗
- **langgraph**: Graph-based workflow orchestration 🌐
- **python-dotenv**: Environment variable management 🔧
- **ipykernel**: Jupyter notebook support 📓
- **pydantic**: Data validation and settings management ✅

## ⚙️ Configuration

The project uses environment variables for configuration:

- `OLLAMA_MODEL`: The Ollama model to use (default: specified in .env) 🤖
- `OLLAMA_URL`: The Ollama server URL (default: http://localhost:11434) 🌐

## 🤝 Contributing

1. Fork the repository 🍴
2. Create a feature branch 🌿
3. Make your changes ✏️
4. Add tests if applicable 🧪
5. Submit a pull request 🚀

## 🔒 License

Pablo Pin - devidence.dev ©

## 🛠️ Troubleshooting

### Common Issues ⚠️

1. **"Connection refused" error**: Ensure Ollama is running (`ollama serve`) 🔌
2. **Model not found**: Pull the required model (`ollama pull <model-name>`) 📥
3. **Environment variables not loaded**: Verify your `.env` file is in the project root 📁

### Getting Help 🆘

- Check the [LangGraph documentation](https://langchain-ai.github.io/langgraph/) 📚
- Visit the [Ollama documentation](https://ollama.ai/docs) 📖
- Open an issue in this repository 🐛

---

*This demo showcases the power of combining LangGraph's workflow orchestration with Ollama's local language models to create intelligent, context-aware conversation agents.* ✨🤖💫
