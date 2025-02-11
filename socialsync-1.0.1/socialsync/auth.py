import requests
import time
import hashlib
from typing import Optional

class AuthHandler:
    def __init__(self, platform: str, client_id: str, client_secret: str, redirect_uri: Optional[str] = None):
        self.platform = platform
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = None
        self.expires_at = None
        self.refresh_token = None
        self.token_url = self._get_token_url()

    def _get_token_url(self) -> str:
        urls = {
            "tiktok": "https://open-api.tiktok.com/oauth/access_token/",
            "instagram": "https://api.instagram.com/oauth/access_token",
            "twitter": "https://api.twitter.com/2/oauth2/token"
        }
        return urls.get(self.platform)

    def get_access_token(self, code: Optional[str] = None, refresh_token: Optional[str] = None) -> str:
        if not self.token_url:
            raise ValueError(f"Unsupported platform: {self.platform}")

        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        if refresh_token:
            payload["grant_type"] = "refresh_token"
            payload["refresh_token"] = refresh_token
        elif code:
            payload["grant_type"] = "authorization_code"
            payload["code"] = code
            payload["redirect_uri"] = self.redirect_uri
        else:
            raise ValueError("Either 'code' or 'refresh_token' must be provided.")

        response = requests.post(self.token_url, data=payload)
        data = response.json()
        if response.status_code != 200:
            raise Exception(f"Failed to obtain access token: {data.get('error_description')}")

        self.access_token = data["access_token"]
        self.refresh_token = data.get("refresh_token")
        self.expires_at = time.time() + data.get("expires_in", 3600)
        return self.access_token

    def is_token_expired(self) -> bool:
        return time.time() >= self.expires_at if self.expires_at else True

    def revoke_token(self):
        if not self.access_token:
            raise ValueError("No active token to revoke.")
        revoke_url = {
            "tiktok": "https://open-api.tiktok.com/oauth/revoke/",
            "instagram": "https://graph.instagram.com/revoke_token",
            "twitter": "https://api.twitter.com/2/oauth2/revoke"
        }.get(self.platform)
        if not revoke_url:
            raise ValueError(f"Token revocation not supported for platform: {self.platform}")
        response = requests.post(revoke_url, data={"token": self.access_token})
        if response.status_code != 200:
            raise Exception(f"Failed to revoke token: {response.text}")
        self.access_token = None
        self.expires_at = None

    def validate_token(self):
        if self.is_token_expired():
            self.refresh_token()
        return self.access_token

    def hash_token(self, token: str) -> str:
        return hashlib.sha256(token.encode()).hexdigest()

    def secure_storage(self, token: str, storage_path: str):
        hashed_token = self.hash_token(token)
        with open(storage_path, "w") as f:
            f.write(hashed_token)

    def load_token(self, storage_path: str) -> str:
        with open(storage_path, "r") as f:
            hashed_token = f.read().strip()
        return hashed_token