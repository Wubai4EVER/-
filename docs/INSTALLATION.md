# Installation Guide

1. **Clone the repository**  
   ```bash
   git clone https://github.com/you/kuromi-agent-framework.git
   cd kuromi-agent-framework
Install dependencies

bash
Copy
Edit
poetry install
# or pip install -r requirements.txt
Build any native/WASM components

bash
Copy
Edit
poetry run wasm-pack build --release --target python
Start with Docker Compose

bash
Copy
Edit
make docker
docker-compose up -d
Set environment variables

bash
Copy
Edit
export WALLET_SECRET="hex_key"
export QDRANT_URL="http://localhost:6333"
export LLM_API_URL="https://api.your-llm.com/v1"
export LLM_API_KEY="your_key_here"
export EMBED_API_URL="https://api.openai.com/v1/embeddings"
export EMBED_API_KEY="your_embedding_key"
