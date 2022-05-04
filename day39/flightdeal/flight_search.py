import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/"
TEQUILA_API_KEY = {
        "apikey": "REMDq4a4rqQNQRNSq1b4DRv4jGVLVq0f"
    }

class FlightSearch:
    def update_iata(self, city_name):
        param = {
            "term": city_name,
            "location_types": "city"
        }
        self.response = requests.get(url=f"{TEQUILA_ENDPOINT}locations/query", headers=TEQUILA_API_KEY, json=param)
        return  self.response.text