import unittest
from socialsync.analytics import TrendAnalyzer

class MockDataSource:
    def fetch_trends(self):
        return [
            {"name": "Trend A", "popularity": 100},
            {"name": "Trend B", "popularity": 200},
            {"name": "Trend C", "popularity": 150}
        ]

class TestTrendAnalyzer(unittest.TestCase):
    def test_analyze_trends(self):
        data_source = MockDataSource()
        analyzer = TrendAnalyzer(data_source)
        trends = analyzer.analyze_trends()
        self.assertEqual(trends[0]["name"], "Trend B")

    def test_generate_report(self):
        data_source = MockDataSource()
        analyzer = TrendAnalyzer(data_source)
        trends = analyzer.analyze_trends()
        report = analyzer.generate_report(trends)
        self.assertIn("Trend B (Popularity: 200)", report)

if __name__ == "__main__":
    unittest.main()