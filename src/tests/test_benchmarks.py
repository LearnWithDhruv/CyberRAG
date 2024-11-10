import unittest
import time
from src.inference.benchmarks import Benchmark

class TestBenchmark(unittest.TestCase):
    def setUp(self):
        self.benchmark = Benchmark()

    def test_measure_time(self):
        def sample_function():
            time.sleep(0.1)
        self.benchmark.measure_time(sample_function)
        self.assertTrue(len(self.benchmark.results) > 0)

    def test_save_results(self):
        self.benchmark.save_results("benchmarks/test_response_times.json")
        with open("benchmarks/test_response_times.json", "r") as f:
            data = f.read()
        self.assertTrue(len(data) > 0)

if __name__ == "__main__":
    unittest.main()
