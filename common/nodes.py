
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor, KeywordExtractor


def gen_nodes_by_pipeline(config, docs):
    # token_text_splitter = TokenTextSplitter(include_prev_next_rel=True)
    sentence_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=20, include_prev_next_rel=True)
    title_extractor = TitleExtractor()
    keyword_extractor = KeywordExtractor()
    # entity_extractor = EntityExtractor(device="cpu", label_entities=True)
    transformations = [sentence_splitter, title_extractor, keyword_extractor, config.embedding]
    pipeline = IngestionPipeline(transformations = transformations,)
    nodes = pipeline.run(documents=docs, num_workers=8,)
    config.logger.debug(f"nodes: {len(nodes)}")
