#!/bin/bash

# Start Ollama server in the background
ollama serve &

# Wait for Ollama server to be ready
echo "Waiting for Ollama server to start..."
max_attempts=30
attempt=0
while ! curl -s http://localhost:11434/api/version &>/dev/null; do
  attempt=$((attempt+1))
  if [ $attempt -eq $max_attempts ]; then
    echo "Ollama server failed to start after $max_attempts attempts"
    exit 1
  fi
  echo "Waiting for Ollama server (attempt $attempt/$max_attempts)..."
  sleep 2
done

echo "Ollama server is running!"
echo "Starting model $OLLAMA_MODEL..."
ollama run $OLLAMA_MODEL