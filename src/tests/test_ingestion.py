import unittest
from src.ingestion.data_ingestor import DataIngestor
from src.ingestion.text_processor import TextProcessor
from src.ingestion.entity_relation_builder import EntityRelationBuilder

class TestIngestion(unittest.TestCase):
    def setUp(self):
        self.ingestor = DataIngestor()
        self.processor = TextProcessor()
        self.builder = EntityRelationBuilder()

    def test_data_fetch(self):
        data = self.ingestor.fetch_data("cybersecurity_walkthroughs")
        self.assertIsInstance(data, list)  # Check if data fetched is a list

    def test_text_processing(self):
        sample_text = "Host has a port running a vulnerable service."
        entities, relations = self.processor.process_text(sample_text)
        self.assertTrue(len(entities) > 0)
        self.assertTrue(len(relations) > 0)

    def test_entity_relation_builder(self):
        entities = [{"type": "host", "value": "localhost"}]
        relations = [{"source": "localhost", "target": "80", "relation": "has port"}]
        nodes, edges = self.builder.build_graph_data(entities, relations)
        self.assertTrue(len(nodes) > 0)
        self.assertTrue(len(edges) > 0)

if __name__ == "__main__":
    unittest.main()
