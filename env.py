
import logging
import sys
import os
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# config logging
logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)
# read env values.
ollama_host = os.getenv("OLLAMA_API", "http://localhost:11434")
ollama_model = "mistral:latest"
logger.info(f"ollama_host: {ollama_host}")
logger.info(f"ollama_model: {ollama_model}")
# settging ollama host and model.
llm = Ollama(model=ollama_model, base_url=ollama_host, request_timeout=120)
resp = llm.complete(prompt="Hello!")
logger.info(resp)