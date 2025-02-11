import asyncio
from socialsync.api import SocialSyncAPI
from socialsync.auth import AuthHandler
from socialsync.sync_manager import SyncManager


auth_tiktok = AuthHandler(platform="tiktok", client_id="your_client_id", client_secret="your_client_secret")
auth_instagram = AuthHandler(platform="instagram", client_id="your_client_id", client_secret="your_client_secret")

auth_tiktok.get_access_token(code="your_authorization_code")
auth_instagram.get_access_token(code="your_authorization_code")


sync_manager = SyncManager(
    platforms=["tiktok", "instagram"],
    auth_handlers={"tiktok": auth_tiktok, "instagram": auth_instagram}
)


async def main():
    await sync_manager.sync_posts("Hello, SocialSync!")

    # Sync trends
    trends = await sync_manager.sync_trends()
    print("Trends:", trends)

asyncio.run(main())