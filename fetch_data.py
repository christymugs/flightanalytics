import requests

def fetch_flight_data():
    url = "https://api.aviationstack.com/v1/flights"
    params = {
        'access_key': 'YOUR_API_KEY',
        'limit': 100
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data
