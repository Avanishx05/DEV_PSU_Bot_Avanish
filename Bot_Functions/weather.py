import places
from dotenv import load_dotenv
import os
import requests
import json
def find_weather(location, units):
    load_dotenv()
    api_key = os.getenv('WEATHER_TOKEN')
    location = places.get_location(location)
    lat = location[0]
    lon = location[1]
    print(location[0])
    if location == "invalid":
        return "Invalid Location"
    # base_url variable to store url
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key + "&units=" + units

    # get method of requests module
    # return response object
    response = requests.get(complete_url).json()
    print(response)
    #report = response.json()['main']

find_weather('statecollege', 'imperial')