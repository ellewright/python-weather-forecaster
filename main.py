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

def convert_to_cardinal(angle):
    return (
        "North" if 0 <= angle < 22.5 else
        "Northeast" if 22.5 <= angle < 67.5 else
        "East" if 67.5 <= angle < 112.5 else
        "Southeast" if 112.5 <= angle < 157.5 else
        "South" if 157.5 <= angle < 202.5 else
        "Southwest" if 202.5 <= angle < 247.5 else
        "West" if 247.5 <= angle < 292.5 else
        "Northwest" if 292.5 <= angle < 337.5 else
        "North"
    )

def main():
    requested_city = input("Type in a city to receive its weather data: ").lower()

    try:
        requested_lat, requested_lon = convert_to_coords(requested_city)
        requested_data = get_weather_data(requested_lat, requested_lon)
        city = requested_data["name"]
        temp = round(requested_data["main"]["temp"])
        feels_like = round(requested_data["main"]["feels_like"])
        humidity = requested_data["main"]["humidity"]
        wind_speed = requested_data["wind"]["speed"]
        wind_direction = convert_to_cardinal(requested_data["wind"]["deg"])
        name = requested_data["weather"][0]["main"]
        details = requested_data["weather"][0]["description"]

        print(f"{city} is currently experiencing {name} weather, specifically: {details}.")
        print(f"It is {temp} degrees Fahrenheit. It feels like {feels_like} degrees. Humidity is at {humidity}%.")
        print(f"Winds are blowing {wind_speed} miles per hour in the {wind_direction} direction.")
    except:
        print("An error occured when searching for that city! Please try again.")

main()