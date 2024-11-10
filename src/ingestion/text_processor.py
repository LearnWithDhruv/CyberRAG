from langchain import LangChain

class TextProcessor:
    def __init__(self):
        self.chain = LangChain()
    
    def process_text(self, text):
        entities = self.chain.extract_entities(text)
        relations = self.chain.extract_relations(text)
        return entities, relations
