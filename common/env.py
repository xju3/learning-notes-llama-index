import logging
import sys
sys.path.append("./")
import os
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import torch


from llama_index.core import Settings
from dotenv import load_dotenv

from llama_index.embeddings.openai import OpenAIEmbedding


class AppConfig:
    def __init__(self) -> None:
        load_dotenv("../.env")
        # logger
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        self.logger = logging.getLogger()
        # env llm model and host
        # host = os.getenv("OLLAMA_HOST")
        # model = os.getenv("OLLAMA_MODEL_QWEN")
        host = os.getenv("LM_STUDIO_HOST")
        model = os.getenv("HF_EBED_QWEN")
        openai_api_key = os.getenv("OPENAI_API_KEY")
        self.logger.debug(f"\nhost: {host}, model: {model}")
        # env database uri
        self.pg_uri = os.getenv("PG_URI")
        self.mongo_uri = os.getenv("MONGO_URI")
        self.logger.debug(f"\n pg: {self.pg_uri} \nmongo:{self.mongo_uri}")
        # using local llm
        # ollama
        # self.llm = Ollama(model=model, base_url=f'{host}/v1', request_timeout=120, json_mode=False)
        # self.embedding = OllamaEmbedding(model_name=model, base_url=host)
        # lmstudio.
        device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
        self.logger.debug(f"device: {device}")
        self.llm = OpenAI(api_base=f'{host}/v1', api_key=openai_api_key)
        self.embedding =  HuggingFaceEmbedding(model_name=model, device='cpu', cache_folder=os.getenv("HF_EBED_CACHE_FOLDER"))
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