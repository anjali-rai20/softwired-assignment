import requests
import json
import time

BASE_URL = 'https://www.nseindia.com'
API_BASE_URL = "https://www.nseindia.com/api/option-chain-indices"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,hi;q=0.8',
    'Referer': BASE_URL
}

session = requests.Session()

try:
    initial_response = session.get(BASE_URL, headers=headers)
    if initial_response.status_code != 200:
        raise Exception(f"Failed to initialize session. Status Code: {initial_response.status_code}")
except Exception as e:
    print(f"Error initializing session: {e}")
    exit(1)

time.sleep(1)

def fetch_option_chain_data(symbol):
    try:
        response = session.get(f"{API_BASE_URL}?symbol={symbol}", headers=headers)
        print(response)
        
        if response.status_code == 200:
            try:
                data = response.json()
                if data.get('records', {}).get('data', []):
                    filename = f"{symbol}_data.json"
                    with open(filename, "w") as f:
                        json.dump(data, f, indent=4)
                    print(f"{symbol} data saved in file {filename}.")
                else:
                    print(f"No data available for {symbol}. Response may be empty.")
            except json.JSONDecodeError:
                print(f"Failed to parse JSON response for {symbol}. Response might not be JSON-formatted.")
                print("Response Text:", response.text[:500])
        else:
            print(f"Failed to fetch data for {symbol}: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Request error for {symbol}: {e}")

while True:
    fetch_option_chain_data("NIFTY")
    fetch_option_chain_data("HDFCBANK")
    time.sleep(3)