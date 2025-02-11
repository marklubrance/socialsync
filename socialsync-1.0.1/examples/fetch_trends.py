from socialsync.api import SocialSyncAPI
from socialsync.auth import AuthHandler
from socialsync.analytics import TrendAnalyzer

auth = AuthHandler(platform="tiktok", client_id="your_client_id", client_secret="your_client_secret")
auth.get_access_token(code="your_authorization_code")

api = SocialSyncAPI(platform="tiktok", auth_handler=auth)
trends = api.fetch_trends()

analyzer = TrendAnalyzer(data_source=api)
top_trends = analyzer.analyze_trends()
print(analyzer.generate_report(top_trends))