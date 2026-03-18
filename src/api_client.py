import requests
import time

def fetch_api_data(url, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
        except Exception:
            time.sleep(2)
    raise Exception("API request failed")