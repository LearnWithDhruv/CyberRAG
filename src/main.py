from src.ingestion.data_ingestor import DataIngestor
from src.ingestion.text_processor import TextProcessor
from src.ingestion.entity_relation_builder import EntityRelationBuilder
from src.graph.graph_builder import GraphBuilder
from src.graph.graph_storage import GraphStorage
from src.inference.query_handler import QueryHandler
from src.inference.context_retriever import ContextRetriever
from src.inference.response_generator import ResponseGenerator
from src.inference.benchmarks import Benchmark

def main():
    ingestor = DataIngestor()
    raw_data = ingestor.fetch_data("cybersecurity_walkthroughs")

    processor = TextProcessor()
    builder = EntityRelationBuilder()
    nodes, edges = [], []
    for data in raw_data:
        entities, relations = processor.process_text(data["text"])
        n, e = builder.build_graph_data(entities, relations)
        nodes.extend(n)
        edges.extend(e)

    graph_builder = GraphBuilder()
    graph_builder.create_graph(nodes, edges)
    storage = GraphStorage()
    storage.store_graph(graph_builder.graph)

    query_handler = QueryHandler()
    context_retriever = ContextRetriever(storage)
    response_generator = ResponseGenerator()
    benchmark = Benchmark()
    
    query = "What ports are running on target.com?"
    parsed_query = query_handler.parse_query(query)
    context = context_retriever.retrieve_context(parsed_query)
    response = benchmark.measure_time(response_generator.generate_response, context, query)
    
    print("Response:", response)
    benchmark.save_results()

if __name__ == "__main__":
    main()
