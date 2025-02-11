import requests
from typing import Dict, Any, Optional
from socialsync.auth import AuthHandler
# from sklearn.linear_model import LinearRegression 
from typing import List, Dict, Optional

class SocialSyncAPI:
    def __init__(self, platform: str, auth_handler: AuthHandler):
        self.platform = platform
        self.auth_handler = auth_handler
        self.base_url = self._get_base_url()
        self.cache = {}

    def _get_base_url(self) -> str:
        urls = {
            "tiktok": "https://open-api.tiktok.com",
            "instagram": "https://graph.instagram.com",
            "twitter": "https://api.twitter.com/2"
        }
        return urls.get(self.platform)

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict[str, Any]] = None, data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        headers = {"Authorization": f"Bearer {self.auth_handler.access_token}"}
        url = f"{self.base_url}/{endpoint}"
        response = requests.request(method, url, headers=headers, params=params, json=data)

        if response.status_code == 401 and self.auth_handler.is_token_expired():
            self.auth_handler.get_access_token(refresh_token=self.auth_handler.refresh_token)
            headers["Authorization"] = f"Bearer {self.auth_handler.access_token}"
            response = requests.request(method, url, headers=headers, params=params, json=data)

        if response.status_code not in (200, 201):
            raise Exception(f"API request failed: {response.status_code} - {response.text}")

        return response.json()

    def post_content(self, content: str) -> Dict[str, Any]:
        endpoints = {
            "tiktok": "post/create/",
            "instagram": "me/media",
            "twitter": "tweets"
        }
        endpoint = endpoints.get(self.platform)
        if not endpoint:
            raise ValueError(f"Unsupported platform: {self.platform}")
        return self._make_request("POST", endpoint, data={"content": content})

    def fetch_trends(self, max_results: int = 10) -> List[Dict[str, Any]]:
        trends = []
        cursor = None
        while len(trends) < max_results:
            batch = self._fetch_trends_batch(cursor)
            trends.extend(batch.get("data", []))
            cursor = batch.get("next_cursor")
            if not cursor:
                break
        return trends[:max_results]

    def _fetch_trends_batch(self, cursor: Optional[str] = None) -> Dict[str, Any]:
        endpoints = {
            "tiktok": "trending/posts/",
            "twitter": "trends"
        }
        endpoint = endpoints.get(self.platform)
        if not endpoint:
            raise ValueError(f"Trends are not supported for platform: {self.platform}")
        params = {"cursor": cursor} if cursor else {}
        return self._make_request("GET", endpoint, params=params)