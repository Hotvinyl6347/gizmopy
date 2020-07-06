import requests
import json

def call_api(path):
    api = "https://www.gizmo.moe"
    try:
        request = requests.get(api + path)
        if request.status_code != 200:
            raise Exception(f"Request Failed: {request.status_code}")
        else:
            return json.loads(request.text)
    except Exception as e:
        raise Exception(f"Invalid JSON response: {e}")

def get_user(username: str):
    try:
        return call_api(f'/api/user?query={username}')
    except Exception as e:
        raise Exception(f"Request failed: {e}")