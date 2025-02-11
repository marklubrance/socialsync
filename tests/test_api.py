import unittest
from unittest.mock import patch, MagicMock
from socialsync.api import SocialSyncAPI

class TestSocialSyncAPI(unittest.TestCase):
    @patch("requests.request")
    def test_post_content(self, mock_request):
        mock_request.return_value = MagicMock(status_code=201, json=lambda: {"id": 123})
        api = SocialSyncAPI(base_url="https://api.example.com", auth_handler=MagicMock())
        response = api.post_content("Test post")
        self.assertEqual(response["id"], 123)

if __name__ == "__main__":
    unittest.main()