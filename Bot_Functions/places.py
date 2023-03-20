import googlemaps
import os
from dotenv import load_dotenv

from geopy.geocoders import Nominatim
import json
from urllib.request import urlopen

def get_location(name):

    if "me" in name.lower():

        response = urlopen("http://ipinfo.io/json")
        data = json.load(response)

        lst = data['loc'].split(',')
        
        return tuple(lst)


    else:
        loc = Nominatim(user_agent="GetLoc")

        get_loc = loc.geocode("{}".format(name))

        if get_loc == None:
            return "invalid"

        return (get_loc.latitude, get_loc.longitude)

def milesToMeter(miles):
    try:
        return miles* 1_609.344
    except:
        return 0

def find_places_nearby(location, search_string, preference):

    load_dotenv()

    map_client = googlemaps.Client(os.getenv("PLACES_TOKEN"))

    loc = get_location(location)

    if loc == "invalid":
        return "invalid location"
    
    distance = milesToMeter(5)

    blist = []

    #finding places ranked by popularity(maybe distance?)
    if preference.lower() == 'popularity':
        response = map_client.places_nearby(
            location = loc,
            keyword = search_string,
            name = search_string,
            radius = distance
        )

    elif preference.lower() == 'distance':
        response = map_client.places_nearby(
            location=loc,
            keyword= search_string,
            name=search_string,
            rank_by = 'distance'
        )

    else:
        return 'invalid preference'

    return response

#create final_list to store the results systematically
    final_list = {}

    #extend the list with results and retrive desired results
    blist.extend(response.get('results'))

    if len(blist) == 0:
        return "No results found/ Invalid search-type"
    
    for i in range(5):
        final_list[blist[i]["name"]] = blist[i]["rating"]

        response = map_client.place(
            place_id=blist[i]["place_id"],
            fields=['international_phone_number']
        )
        phone_num = response.get('result')

        if len(phone_num) == 0:
            final_list[blist[i]["name"]] = ('None', blist[i]["rating"])
        else:
            final_list[blist[i]["name"]] = (phone_num['international_phone_number'], blist[i]["rating"])

    result_string = search_string + " "

    if preference == "popularity" and location != "me":
        result_string += "in"
    else:
        result_string += "near"