import os
from dotenv import load_dotenv
import requests
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

def get_weather_data(lat, lon):
    api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

def convert_to_coords(city_name):
    api_key = os.getenv("API_KEY")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        city_data = response.json()
        lat, lon = city_data[0]["lat"], city_data[0]["lon"]
        return (lat, lon)