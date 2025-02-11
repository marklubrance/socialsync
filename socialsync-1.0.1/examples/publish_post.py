from socialsync.api import SocialSyncAPI
from socialsync.auth import AuthHandler

auth = AuthHandler(client_id="your_client_id", client_secret="your_client_secret")
auth.get_access_token(code="your_authorization_code")

api = SocialSyncAPI(base_url="https://api.example.com", auth_handler=auth)
response = api.post_content("Hello, SocialSync!")
print("Post created:", response)