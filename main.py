import os
from dotenv import load_dotenv
import requests
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

load_dotenv()

def get_weather_data(lat, lon):
    api_key = os.getenv("API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=imperial"
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

# todo: make method for converting meteorological degrees into cardinal directions

def main():
    requested_city = input("Type in a city to receive its weather data: ").lower()
    requested_lat, requested_lon = convert_to_coords(requested_city)
    requested_data = get_weather_data(requested_lat, requested_lon)

    requested_name = requested_data["name"]
    requested_temp = round(requested_data["main"]["temp"])
    requested_feels_like = round(requested_data["main"]["feels_like"])
    requested_wind_speed = requested_data["wind"]["speed"]
    requested_weather_description = requested_data["weather"][0]["main"]

    print(f"{requested_name} is currently experiencing {requested_weather_description}.")
    print(f"It is {requested_temp} degrees Fahrenheit. It feels like {requested_feels_like} degrees.")
    print(f"Winds are blowing {requested_wind_speed} miles per hour.")

main()