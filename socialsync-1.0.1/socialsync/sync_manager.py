import asyncio
from typing import List, Dict, Any
from socialsync.api import SocialSyncAPI
from socialsync.auth import AuthHandler

class SyncManager:
    def __init__(self, platforms: List[str], auth_handlers: Dict[str, AuthHandler]):
        self.platforms = platforms
        self.auth_handlers = auth_handlers

    async def async_post_content(self, platform: str, content: str):
        api = SocialSyncAPI(platform, self.auth_handlers[platform])
        try:
            await api.post_content(content)
            print(f"Successfully posted on {platform}")
        except Exception as e:
            print(f"Failed to post on {platform}: {e}")

    async def sync_posts(self, content: str):
        tasks = [self.async_post_content(platform, content) for platform in self.platforms]
        await asyncio.gather(*tasks)

    async def async_fetch_trends(self, platform: str) -> List[Dict[str, Any]]:
        api = SocialSyncAPI(platform, self.auth_handlers[platform])
        try:
            trends = await api.fetch_trends()
            return trends
        except Exception as e:
            print(f"Failed to fetch trends from {platform}: {e}")
            return []

    async def sync_trends(self) -> Dict[str, List[Dict[str, Any]]]:
        tasks = [self.async_fetch_trends(platform) for platform in self.platforms]
        results = await asyncio.gather(*tasks)
        return {platform: trends for platform, trends in zip(self.platforms, results)}

    async def schedule_sync(self, content: str, interval: int = 3600):
        while True:
            await self.sync_posts(content)
            await asyncio.sleep(interval)