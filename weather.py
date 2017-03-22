import forecastio
from geopy.geocoders import Nominatim

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    api_key = os.environ['API_KEY']
    forecast = forecastio.load_forecast(api_key, location.latitude, location.longitude).currently()
    return "{} and {} in {}".format(forecast.summary, forecast.temperature, location.address)
