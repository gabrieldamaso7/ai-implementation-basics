import requests

def fetch_eod_appl_quote() -> dict:
    url = "https://api.marketstack.com/v2/eod?access_key=612436ce85ca5ea9810b59da4ec2760c&symbols=AAPL"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if not data.get("data"):
            raise ValueError("No data found in response")

        if "open" not in data["data"][0] or "close" not in data["data"][0]:
            raise ValueError("Unexpected response format")
        
        return data

    except requests.exceptions.Timeout:
        raise TimeoutError("Request timed out")
    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"An error occurred while fetching data: {e}")