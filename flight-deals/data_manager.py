import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/25e51d5921145d82e04dc8bfce9c9463/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass