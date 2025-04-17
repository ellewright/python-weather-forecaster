import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

def get_weather_data(lat, lon):
    api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()