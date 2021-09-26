# pylint: disable=missing-docstring

import sys
import requests

BASE_URI = "https://www.metaweather.com"

def search_city(query):
    """Find a city with the search api"""
    url = f"{BASE_URI}/api/location/search/?query={query}"
    response = requests.get(url).json()
    if response == []:
        return None
    if len(response) > 1:
        print('Your input returned the following cities')
        for index, city in enumerate(response):
            print(f'{index + 1} - {city["title"]}')
        choice = input("Please type the number of the city you want:\n> ")
        city = response[int(choice) - 1]
    else:
        city = response[0]
    return city

def weather_forecast(woeid):
    """Get the 5 day forecast for that city"""
    url = f"{BASE_URI}/api/location/{woeid}"
    response = requests.get(url).json()
    return response["consolidated_weather"][:5]

def main():
    """Display weather forecast for given city"""
    query = input("City?\n> ")
    city = search_city(query)
    print(f"Here's the weather in {city['title']}")
    forecast = weather_forecast(city["woeid"])
    for row in forecast:
        temp = round(row["the_temp"], 1)
        print(f"{row['applicable_date']}: {row['weather_state_name']} {temp}°C")

if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
