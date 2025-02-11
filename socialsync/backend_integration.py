import sqlite3
import requests
import asyncio
from typing import List, Dict, Any
import aiohttp

class BackendIntegration:
    def __init__(self, db_path: str = "data.db"):
        self.db_path = db_path
        self.cache = {}

    def initialize_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT,
                content TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        conn.commit()
        conn.close()

    def save_post_to_db(self, platform: str, content: str):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (platform, content) VALUES (?, ?)", (platform, content))
        conn.commit()
        conn.close()

    def fetch_posts_from_db(self) -> List[Dict[str, Any]]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM posts")
        rows = cursor.fetchall()
        conn.close()
        return [{"id": row[0], "platform": row[1], "content": row[2], "timestamp": row[3]} for row in rows]

    def cache_data(self, key: str, value: Any):
        self.cache[key] = value

    def get_cached_data(self, key: str) -> Any:
        return self.cache.get(key)

    def call_external_api(self, url: str, params: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.get(url, params=params)
        if response.status_code != 200:
            raise Exception(f"API request failed: {response.status_code} - {response.text}")
        return response.json()

    async def async_call_external_api(self, url: str, params: Dict[str, Any]) -> Dict[str, Any]:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if response.status != 200:
                    raise Exception(f"API request failed: {response.status} - {await response.text()}")
                return await response.json()

    def batch_process_data(self, data: List[Dict[str, Any]]):
        for item in data:
            self.save_post_to_db(item["platform"], item["content"])
            self.cache_data(item["platform"], item["content"])