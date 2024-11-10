from pymongo import MongoClient
from src.config import config

class DataIngestor:
    def __init__(self):
        self.client = MongoClient(config.MONGO_URI)
        self.db = self.client["cybersec_db"]
    
    def fetch_data(self, collection_name):
        collection = self.db[collection_name]
        return list(collection.find())
