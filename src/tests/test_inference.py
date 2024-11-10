import unittest
from src.inference.query_handler import QueryHandler
from src.inference.context_retriever import ContextRetriever
from src.inference.response_generator import ResponseGenerator
from src.graph.graph_storage import GraphStorage

class TestInference(unittest.TestCase):
    def setUp(self):
        self.query_handler = QueryHandler()
        self.context_retriever = ContextRetriever(GraphStorage())
        self.response_generator = ResponseGenerator()

    def test_query_parsing(self):
        query = "What ports are running on localhost?"
        parsed_query = self.query_handler.parse_query(query)
        self.assertEqual(parsed_query.get("type"), "port")

    def test_context_retrieval(self):
        query = {"type": "port"}
        context = self.context_retriever.retrieve_context(query)
        self.assertIsNotNone(context)

    def test_response_generation(self):
        context = "Port 80 is open on localhost."
        query = "What ports are running on localhost?"
        response = self.response_generator.generate_response(context, query)
        self.assertIn("Port 80", response)

if __name__ == "__main__":
    unittest.main()
