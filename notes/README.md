
[🇨🇳readme cn version](README_CN.md)

## book intro:
* [building-data-driven-applicatinos-wth-llama-index](https://www.packtpub.com/en-us/product/building-data-driven-applications-with-llamaindex-9781835089507)

## runing environment:
- using .env to save some sensitive informations
- here are the variables you need to define in .env.
```sh
    OLLAMA_API=http://localhost:11434
    OLLAMA_MODEL=mistral:latest
    MONGO_URI=mongodb://root:root@localhost
    PG_URI=postgresql://yourname:password@localhost:5433/db_name
    LLAMA_CLOUD_API_KEY=
    OPENAI_API_KEY=
```
- you need to create a .env file mannually under the source code directory.

## notifications
* the recommendions version of python is 3.11, otherwise it might has some incompatible issues.
* [env.py](env.py) is the basic settings for using local ollama
* [01.foundations.ipynb](01.foundations.ipynb) convered the knowledges of the book chapters from 1 to 5 , including:
    * reader, 
    * splitter, 
    * phaser, 
    * meta-data extractor, 
    * pipepine data ingestion.
    * indexing
    * storage context 
    * doc & nodes & index persistence.
* [02.retriever-query.ipynb](02.retriever-query.ipynb) convered the 6th and 7th chapters.
    * retrievers
        * VectorStoreIndex retrivers
        * DocumentSummaryIndex Retrivers
        * TreeIndex Retrivers
        * KnowledgeGraphIndex Retrivers
    * buiding more advanced retrival machanisms
        * native retrieval method
        * implementing metadata **filters**
        * using selector for more advanced decesion logic
        * transforming and rewriting queries
        * more specific sub-queries
    * Understanding the concepts of dense and sparse retrieval
        * dense retrival
        * sparse retrival
    * using postprocessor to rerank, transform and fiter nodes
        * how postprocessor works
        * SimilarlyPostProcessor
        * KeywordNodePostProcessor
        * PrevNextNodePostProcessor
        * LongContextRecorder
        * PIINodePostProcessor
        * NERPIINodePostProcessor
        * MetadataReplacementPostProcessor
        * SentenceEmbeddingPostProcessor
        * Time-based post processors
        * Re-ranking post processors
        * final thoughts about ndoe post processors
    * understanding response synthesizers
    * implementing output parsing techniques
        * extracting structured outputs using output parsers
        * extracting structured outputs using Pydantic Programs
    * building and using query engine
        * exploring different methods to building query engines
        * advanced uses of the QueryEngine interface.
* [03.chat-agent.ipynb](03.chat-agent.ipynb) introduces how to build a chat system working with agent.
    * chat 
        * discovering chatengine
        * understanding the different chat modes
    * agent
        * building tools and Tookspec classes for our agent
        * understanding reasoning loops
        * OpenAIAgent
        * **ReActAgent**
        * how do we interact with agents
        * enhancing our agents with the help of utility tools
        * using the LLMCompiler agent for more advanced scenarios
        * using the low-level-agent protocal API
* [04.customizing-deploying.ipynb](04.customizing-deploying.ipynb)
* [05.propmpt-engineering.ipynb](05.propmpt-engineering.ipynb)