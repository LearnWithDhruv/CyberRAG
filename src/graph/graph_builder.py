from langgraph import LangGraph

class GraphBuilder:
    def __init__(self):
        self.graph = LangGraph()
    
    def create_graph(self, nodes, edges):
        for node in nodes:
            self.graph.add_node(node["type"], node["value"])
        for edge in edges:
            self.graph.add_edge(edge["source"], edge["target"], edge["relation"])
