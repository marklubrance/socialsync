import unittest
from socialsync.backend_integration import BackendIntegration
import sqlite3

class TestBackendIntegration(unittest.TestCase):
    def setUp(self):
        self.backend = BackendIntegration(":memory:")

    def test_initialize_database(self):
        self.backend.initialize_database()
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='posts'")
        self.assertIsNotNone(cursor.fetchone())

    def test_save_and_fetch_posts(self):
        self.backend.initialize_database()
        self.backend.save_post_to_db("tiktok", "Test post")
        posts = self.backend.fetch_posts_from_db()
        self.assertEqual(len(posts), 1)
        self.assertEqual(posts[0]["platform"], "tiktok")

    def test_cache_data(self):
        self.backend.cache_data("key", "value")
        self.assertEqual(self.backend.get_cached_data("key"), "value")

if __name__ == "__main__":
    unittest.main()