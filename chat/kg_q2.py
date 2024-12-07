import sys
sys.path.append("../")

from common.llm import LlmConfig, LocalLLM
from neo4j import GraphDatabase
from llama_index.graph_stores.neo4j import Neo4jGraphStore

username = "kg"
password = "kg@sh123"
database = "movies"
uri = "bolt://localhost:7687"


driver = GraphDatabase.driver(uri, database=database, auth=(username, password))
config = LlmConfig(local_llm=LocalLLM.LM_STUDIO)
neo4j_store = Neo4jGraphStore(uri=uri, user=username, password=password, database=database)




