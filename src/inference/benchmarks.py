import time
import json

class Benchmark:
    def __init__(self):
        self.results = []
    
    def measure_time(self, func, *args):
        start = time.time()
        result = func(*args)
        end = time.time()
        self.results.append({"function": func.__name__, "time_taken": end - start})
        return result
    
    def save_results(self, filename="benchmarks/response_times.json"):
        with open(filename, "w") as f:
            json.dump(self.results, f, indent=4)
