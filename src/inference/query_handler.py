class QueryHandler:
    def parse_query(self, query):
        if "ports" in query:
            return {"type": "port"}
        elif "services" in query:
            return {"type": "service"}
        return {}