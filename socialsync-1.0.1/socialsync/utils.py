import re
from typing import List, Dict, Any
import time

def validate_response(response: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(response, dict):
        raise ValueError("Invalid response format.")
    if "error" in response:
        raise Exception(f"API error: {response['error']}")
    return response

def sanitize_content(content: str) -> str:
    if not isinstance(content, str):
        raise ValueError("Content must be a string.")
    return content.strip()

def paginate_results(fetch_function, limit: int = 100) -> List[Dict[str, Any]]:
    results = []
    cursor = None
    while True:
        batch = fetch_function(cursor=cursor)
        results.extend(batch.get("data", []))
        cursor = batch.get("next_cursor")
        if not cursor or len(results) >= limit:
            break
    return results[:limit]

def retry_on_failure(func, retries: int = 3, delay: int = 1):
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(delay * (attempt + 1))

def extract_hashtags(text: str) -> List[str]:
    return re.findall(r"#(\w+)", text)

def validate_email(email: str) -> bool:
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(regex, email) is not None

def validate_url(url: str) -> bool:
    regex = r"^(https?://)?(www\.)?[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}(/\S*)?$"
    return re.match(regex, url) is not None