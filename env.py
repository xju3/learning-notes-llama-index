
import logging
import sys
import os
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding
from dotenv import load_dotenv
import psycopg2


class AppConfig:
    def __init__(self) -> None:
        # config logging
        config = load_dotenv()
        logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        self.logger = logging.getLogger(__name__)
        ollama_host = os.getenv("OLLAMA_API")
        ollama_model = os.getenv("OLLAMA_MODEL")
        self.logger.debug(f"host: {ollama_host}, mode: {ollama_model}")
        # set local llm
        self.llm = Ollama(model=ollama_model, base_url=ollama_host, request_timeout=120)
        self.embedding = OllamaEmbedding(model_name=ollama_model, base_url=ollama_host)
        # connect to database
        connection_string = f"postgresql://{os.getenv('PG_USER')}:{os.getenv('PG_PASS')}@{os.getenv('PG_HOST')}:{os.getenv('PG_PORT')}/{os.getenv('PG_DB')}?sslmode=require"
        self.logger.debug(f"conn: {connection_string}")
        self.conn = psycopg2.connect(connection_string)
        self.conn.autocommit = True

    def logger(self):
        return self.logger   

    def llm(self):
        return self.llm

    def embedding(self):
        return self.embedding
    
    def pg_conn(self):
        return self.conn
