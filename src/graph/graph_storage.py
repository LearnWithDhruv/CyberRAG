from chromadb import ChromaDB
from src.config import config

class GraphStorage:
    def __init__(self):
        self.vector_db = ChromaDB(config.CHROMA_PATH)
    
    def store_graph(self, graph):
        embeddings = self._generate_embeddings(graph)
        self.vector_db.store(embeddings)
    
    def _generate_embeddings(self, graph):
        return [{"node": node, "embedding": [0.0] * 128} for node in graph.get_nodes()]
