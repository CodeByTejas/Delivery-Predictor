import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

def fetch_weather_data(city):
    """Fetch current weather data for a specific city"""
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        'key': WEATHER_API_KEY,
        'q': city
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return {
            'temperature': data['current']['temp_c'],
            'is_raining': data['current']['precip_mm'] > 0
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None