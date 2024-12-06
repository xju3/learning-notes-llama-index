import sys
# sys.path.append("../")

from common.env import AppConfig, LocalLLM
from llama_index.core import Settings
from neo4j import GraphDatabase
from dotenv import load_dotenv
from flask import Flask, request, jsonify

username = "neo4j"
password = "neo4j@sh123"
database = "movies"
uri = "bolt://localhost:7687/movies"

driver = GraphDatabase.driver(uri, auth=(username, password))

def get_schema_info():
    with driver.session() as session:
        labels = session.run("CALL db.labels()").value()
        relationships = session.run("CALL db.relationshipTypes()").value()
        properties = session.run("CALL db.propertyKeys()").value()

        return {
            "labels": labels,
            "relationships": relationships,
            "properties": properties
        }
    
# Example function to execute a Cypher query
def run_cypher_query(cypher_query):
    with driver.session() as session:
        result = session.run(cypher_query)
        return [record.data() for record in result]
    
def natural_language_to_cypher_with_schema(natural_query):
    # Get schema information
    schema_info = get_schema_info()

    # Format schema into prompt
    schema_prompt = f"""
    The Neo4j database schema includes the following:
    - Node labels: {', '.join(schema_info['labels'])}
    - Relationship types: {', '.join(schema_info['relationships'])}
    - Property keys: {', '.join(schema_info['properties'])}

    Based on this schema, translate the following natural language question into a Cypher query:
    Question: "{natural_query}"
    Cypher Query:
    """

    # Generate the query using the LLM
    response = Settings.llm(schema_prompt)
    return response.strip()

def query_neo4j_with_natural_language(natural_query):
    # Step 1: Convert natural language to Cypher
    cypher_query = natural_language_to_cypher_with_schema(natural_query)
    print(f"Generated Cypher Query: {cypher_query}")

    # Step 2: Execute the Cypher query
    results = run_cypher_query(cypher_query)

    # Step 3: Return the results
    return results



app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    natural_query = data.get('query')
    results = query_neo4j_with_natural_language(natural_query)
    return jsonify(results)

if __name__ == '__main__':
    config = AppConfig(local_llm=LocalLLM.LM_STUDIO)
    app.run(debug=True, port=3030)