
import logging
import sys
import os
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core import Settings
from openai import OpenAI


class AppConfig:
    def __init__(self) -> None:
        # config logging
        ollama_host = os.getenv("OLLAMA_API")
        ollama_model = os.getenv("OLLAMA_MODEL")
        self.pg_uri = os.getenv("PG_URI")
        self.mongo_uri = os.getenv("MONGO_URI")
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        self.logger = logging.getLogger()
        #
        self.logger.debug(f"\nhost: {ollama_host}, \nmodel: {ollama_model}")
        self.logger.debug(f"\n{self.pg_uri} \n{self.mongo_uri}")
        # # set local llm
        # self.llm = OpenAI(base_url=f'{ollama_host}/v1', api_key='ollama')
        self.llm = Ollama(model=ollama_model, base_url=ollama_host, request_timeout=120)
        self.embedding = OllamaEmbedding(model_name=ollama_model, base_url=ollama_host)
        Settings.llm = self.llm
        Settings.embed_model = self.embedding
     
    def logger(self):
        return self.logger   

    def llm(self):
        return self.llm

    def embedding(self):
        return self.embedding
    
    def pg_uri(self):
        return self.pg_uri
    
    def mongo_uri(self):
        return self.mongo_uri