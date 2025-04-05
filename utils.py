import requests
from dotenv import load_dotenv
import os

load_dotenv('.env', override=True)
API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')

GEOCODE_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

def geocode_address_string(address: str):
    params = {
        'address': address,
        'key': API_KEY
    }

    try:
        response = requests.get(GEOCODE_URL, params=params)
        result = response.json()

        if result['status'] == 'OK':
            data = result['results'][0]
            location = data['geometry']['location']
            lat, lng = location['lat'], location['lng']

            # Parse address components
            components = {comp['types'][0]: comp['long_name'] for comp in data['address_components']}
            city = components.get('locality') or components.get('postal_town') or ""
            state = components.get('administrative_area_level_1', "")
            country = components.get('country', "")

            # Neo4j-compatible dict
            neo4j_data = {
                'location': {
                    'latitude': lat,
                    'longitude': lng
                },
                'country': country,
                'city': city,
                'state': state
            }

            return neo4j_data

        else:
            print(f"Error: {result['status']}")
            return None

    except Exception as e:
        print(f"Exception: {e}")
        return None

if __name__ == "__main__":
    print(geocode_address_string("ROYAL BANK PLAZA, 200 BAY STREET, TORONTO, A6, M5J2J5"))