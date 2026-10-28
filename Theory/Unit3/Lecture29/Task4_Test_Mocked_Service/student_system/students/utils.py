import requests


def fetch_external_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return {
            "data": response.json(),
            "error": None
        }
    except requests.Timeout:
        return {
            "data": None,
            "error": "External service timed out"
        }