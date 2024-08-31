import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/25e51d5921145d82e04dc8bfce9c9463/flightDeals/prices"
SHEETY_USER_NAME = ""
SHEETY_PASSWORD = ""

class DataManager:
    def __init__(self):
        self._user = SHEETY_USER_NAME
        self._password = SHEETY_PASSWORD
        self._authorization = HTTPBasicAuth(self._user, self._password)
        self._destination_data = {}

    #This class is responsible for talking to the Google Sheet.

