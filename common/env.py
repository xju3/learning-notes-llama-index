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
from enum import Enum

from llama_index.core import Settings
from dotenv import load_dotenv

from llama_index.embeddings.openai import OpenAIEmbedding

load_dotenv("../.env")

# variables
lms_host = os.getenv("LM_STUDIO_HOST")
lms_model = os.getenv("HF_EBED_QWEN")
ollama_host = os.getenv("OLLAMA_HOST")
ollama_model = os.getenv("OLLAMA_MODEL_MISTRAL")
#ollama_model = os.getenv("OLLAMA_MODEL_QWEN")
openai_api_key = os.getenv("OPENAI_API_KEY")

class LocalLLM(Enum):
    LM_STUDIO = 1,
    OLLAMA = 2


class AppConfig:
    def __init__(self, local_llm : LocalLLM = LocalLLM.LM_STUDIO) -> None:
        # logger
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        self.logger = logging.getLogger()
        # env database uri
        self.pg_uri = os.getenv("PG_URI")
        self.mongo_uri = os.getenv("MONGO_URI")
        self.logger.debug(f"\n pg: {self.pg_uri} \nmongo:{self.mongo_uri}")

        # local llm
        if local_llm == LocalLLM.OLLAMA:
            self.logger.debug(f"\nhost: {ollama_host}, model: {ollama_model}")
            self.llm = Ollama(model=ollama_model, base_url=f'{ollama_host}', request_timeout=120, json_mode=False)
            self.embedding = OllamaEmbedding(model_name=ollama_model, 
                                             base_url=ollama_host)
        else:
            cache_folder  = os.getenv("HF_EBED_CACHE_FOLDER")
            self.logger.debug(f"\nhost: {lms_host}, model: {lms_model}, cache: {cache_folder}")
            device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
            self.logger.debug(f"device: {device}")
            self.llm = OpenAI(api_base=f'{lms_host}/v1', api_key=openai_api_key)
            self.embedding =  HuggingFaceEmbedding(model_name='Alibaba-NLP/gte-Qwen2-1.5B-instruct', 
                                                   device='cpu', 
                                                   cache_folder=cache_folder)
        Settings.llm = self.llm
        Settings.embed_model = self.embedding
        Settings.chunk_size = 512
        Settings.chunk_overlap = 20
     
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