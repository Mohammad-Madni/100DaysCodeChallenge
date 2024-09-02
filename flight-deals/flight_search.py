import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
FLIGHT_ENDPOINT = "https://test.api.amadeus.com/v2/shopping/flight-offers"
TOKEN_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token"

class FlightSearch:

    def __init__(self):
        self._api_key = os.environ["Api_key"]
        self._api_secret = os.environ["Secret_key"]
        

    def get_destination_code(self, city_name):
        code = "testing"
        return code
