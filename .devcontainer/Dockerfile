FROM python:3.13-slim-bookworm

# Install uv
RUN apt-get update && apt-get install -y curl && \
    curl -LsSf https://astral.sh/uv/install.sh | sh && \
    apt-get remove -y curl && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Add uv to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy the application code
COPY ./src /app/src
COPY ./pyproject.toml /app/pyproject.toml
COPY ./uv.lock /app/uv.lock

# Install dependencies
RUN uv pip install --system --no-cache-dir .

# Keep the container running
CMD ["sleep", "infinity"]
