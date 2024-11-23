
import logging
import sys
import os
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from dotenv import load_dotenv

class AppConfig:
    def __init__(self) -> None:
        # config logging
        config = load_dotenv()
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        self.logger = logging.getLogger()
        ollama_host = os.getenv("OLLAMA_API")
        ollama_model = os.getenv("OLLAMA_MODEL")
        self.logger.debug(f"host: {ollama_host}, mode: {ollama_model}")
        # set local llm
        self.llm = Ollama(model=ollama_model, base_url=ollama_host, request_timeout=120)
        self.embedding = OllamaEmbedding(model_name=ollama_model, base_url=ollama_host)
     

    def logger(self):
        return self.logger   

    def llm(self):
        return self.llm

    def embedding(self):
        return self.embedding