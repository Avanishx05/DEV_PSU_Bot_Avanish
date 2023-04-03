from Bot_Functions import places
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

    if location == "invalid":
        return "Invalid Location"
    # base_url variable to store url
    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&appid=" + api_key + "&units=" + units

    # get method of requests module
    # return response object
    response = requests.get(complete_url)
    report = response.json()
    if units == 'imperial':
        return ("temperature: "+ str(report['main']['temp']) + "°F"+ "\n" + 
            "feels like: "+ str(report['main']['feels_like']) + "°F"+ "\n" + 
            "Minimum temperature: " + str(report['main']['temp_min']) + "°F"+ "\n" +
            "Maximum temperature: " + str(report['main']['temp_max']) + "°F")
    
    #metric
    if units == 'metric':
        return ("temperature: "+ str(report['main']['temp']) + "°C"+ "\n" + 
            "feels like: "+ str(report['main']['feels_like']) + "°C"+ "\n" + 
            "Minimum temperature: " + str(report['main']['temp_min']) + "°C"+ "\n" +
            "Maximum temperature: " + str(report['main']['temp_max']) + "°C")
    #standard
    if units == 'standard':
        return ("temperature: "+ str(report['main']['temp']) + "K"+ "\n" + 
            "feels like: "+ str(report['main']['feels_like']) + "K"+ "\n" + 
            "Minimum temperature: " + str(report['main']['temp_min']) + "K"+ "\n" +
            "Maximum temperature: " + str(report['main']['temp_max']) + "K")