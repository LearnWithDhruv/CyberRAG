import unittest
from src.graph.graph_builder import GraphBuilder
from src.graph.graph_storage import GraphStorage

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.builder = GraphBuilder()
        self.storage = GraphStorage()

    def test_graph_creation(self):
        nodes = [{"type": "host", "value": "localhost"}]
        edges = [{"source": "localhost", "target": "80", "relation": "has port"}]
        self.builder.create_graph(nodes, edges)
        self.assertTrue(self.builder.graph.get_nodes())

    def test_graph_storage(self):
        self.storage.store_graph(self.builder.graph)
        self.assertTrue(self.storage.vector_db)

if __name__ == "__main__":
    unittest.main()
