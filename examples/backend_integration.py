from socialsync.backend_integration import BackendIntegration

backend = BackendIntegration()


backend.initialize_database()


backend.save_post_to_db("tiktok", "Hello, TikTok!")
backend.save_post_to_db("instagram", "Hello, Instagram!")


posts = backend.fetch_posts_from_db()
print("Posts from DB:", posts)


backend.cache_data("tiktok", "Cached TikTok post")
print("Cached data:", backend.get_cached_data("tiktok"))


try:
    api_response = backend.call_external_api("https://api.example.com/data", {"param": "value"})
    print("API Response:", api_response)
except Exception as e:
    print("API Error:", e)