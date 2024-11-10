class ContextRetriever:
    def __init__(self, graph_storage):
        self.graph_storage = graph_storage
    
    def retrieve_context(self, query):
        return self.graph_storage.vector_db.retrieve(query)
