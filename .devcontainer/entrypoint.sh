#!/bin/bash

# Start Ollama server in the background
ollama serve &

# Wait for Ollama server to be ready
echo "Waiting for Ollama server to start..."
echo "Ollama server is running!"
echo "Starting model $OLLAMA_MODEL..."
ollama run $OLLAMA_MODEL