import sys
sys.path.append("../")

from common.llm import LlmConfig, LocalLLM
from neo4j import GraphDatabase

import streamlit as st

username = "kg"
password = "kg@sh123"
database = "movies"
uri = "bolt://localhost:7687"


driver = GraphDatabase.driver(uri, database=database, auth=(username, password))
config = LlmConfig(local_llm=LocalLLM.LM_STUDIO)

# Function to run Cypher query in Neo4j
def run_cypher_query(cypher_query):
    with driver.session() as session:
        result = session.run(cypher_query)
        return [record.data() for record in result]

# Function to convert natural language to Cypher using LLM
def natural_language_to_cypher_with_schema(natural_query, schema_info):
    # Format schema into prompt
    schema_prompt = f"""
    The Neo4j database schema includes the following:
    - Node labels: {', '.join(schema_info['labels'])}
    - Relationship types: {', '.join(schema_info['relationships'])}
    - Property keys: {', '.join(schema_info['properties'])}

    Based on this schema, translate the following natural language question into a Cypher query:
    Question: "{natural_query}"
    I only need the Cypher Query codes, no explanations
    """

    print(schema_prompt)
    # config.logger(f"{schema_prompt}")
    # Generate Cypher query using the LLM
    response = config.llm.complete(schema_prompt)
    print(f"resp >>>>>>>>> {response.text}")
    cypher_query = response.text.replace("```", "").replace("cypher", "").replace(">", "")
    # md = markdown(response)
    # query_script = ''.join(BeautifulSoup(md).findAll(text=True))
    print(f"resp: -->>>>> {cypher_query}")
    return cypher_query.strip()
    # config.logger(f"{schema_prompt}")
    # return "MATCH (m:Movie)-[:DIRECTED]-(p:Person {name: 'Tom Hanks'}) RETURN m.title"

# Function to get schema info using APOC
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

# Streamlit Web Interface
st.title("Natural Language to Cypher Query")
st.write("Input a natural language query to interact with the Neo4j graph database.")

# Input field for natural language query
natural_query = st.text_input("Enter your query:")

# Button to process query
if st.button("Generate Query and Search"):
    if natural_query.strip():
        # Step 1: Get schema information
        schema_info = get_schema_info()

        # Step 2: Generate Cypher query using LLM
        with st.spinner("Generating Cypher query..."):
            cypher_query = natural_language_to_cypher_with_schema(natural_query, schema_info)
        st.write(f"**Generated Cypher Query:**\r\n{cypher_query}")

        # Step 3: Execute the Cypher query
        with st.spinner("Querying database..."):
            results = run_cypher_query(cypher_query)

        # Step 4: Display results
        if results:
            st.write("**Query Results:**")
            st.json(results)
        else:
            st.write("No results found for the query.")
    else:
        st.error("Please enter a valid query.")