class SocialSyncError(Exception):
    pass

class AuthenticationError(SocialSyncError):
    pass

class APIRequestError(SocialSyncError):
    pass

class PlatformNotSupportedError(SocialSyncError):
    pass

class InvalidResponseError(SocialSyncError):
    pass

class TokenRevocationError(SocialSyncError):
    pass

class PostNotFoundError(SocialSyncError):
    pass

class UserNotFoundError(SocialSyncError):
    pass

class RateLimitExceededError(SocialSyncError):
    pass