class EntityRelationBuilder:
    def build_graph_data(self, entities, relations):
        nodes = [{"type": entity["type"], "value": entity["value"]} for entity in entities]
        edges = [{"source": rel["source"], "target": rel["target"], "relation": rel["relation"]} for rel in relations]
        return nodes, edges