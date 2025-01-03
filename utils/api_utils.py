# utils/api_utils.py

import requests

def get_all_users_from_api():
    """
    Assume we have an endpoint returning JSON, e.g.:
    [
      {"username": "User1", "role": "Admin", "status": "Enabled", "employeeName": "Orange Test"},
      ...
    ]
    If 'api.example.com' doesn't exist, you can skip or mock it.
    """
    url = "https://api.example.com/hrm/users"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()
    except Exception as e:
        # If the endpoint is not real, consider skipping or mocking
        print(f"API call failed: {e}")
        return []
