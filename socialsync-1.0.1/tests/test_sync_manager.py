import unittest
from unittest.mock import patch, MagicMock
from socialsync.sync_manager import SyncManager
from socialsync.api import SocialSyncAPI

class TestSyncManager(unittest.TestCase):
    @patch("socialsync.api.SocialSyncAPI.post_content")
    def test_sync_posts(self, mock_post_content):
        mock_post_content.return_value = {"status": "success"}
        auth_handler = MagicMock()
        sync_manager = SyncManager(platforms=["tiktok"], auth_handlers={"tiktok": auth_handler})
        sync_manager.sync_posts("Test post")
        mock_post_content.assert_called_once()

    @patch("socialsync.api.SocialSyncAPI.fetch_trends")
    def test_sync_trends(self, mock_fetch_trends):
        mock_fetch_trends.return_value = [{"name": "Trend A", "popularity": 100}]
        auth_handler = MagicMock()
        sync_manager = SyncManager(platforms=["tiktok"], auth_handlers={"tiktok": auth_handler})
        trends = sync_manager.sync_trends()
        self.assertIn("tiktok", trends)
        self.assertEqual(len(trends["tiktok"]), 1)

if __name__ == "__main__":
    unittest.main()