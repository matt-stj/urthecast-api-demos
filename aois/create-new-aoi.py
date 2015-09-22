import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/consumers/apps/me/aois'

r = requests.post(url,
    headers = { 'Content-Type': 'application/json' },
    params = { 'api_key': api_key, 'api_secret': api_secret },
    # Check out http://geojson.io for help with creating GeoJSON objects
    data = json.dumps({
        "name": "San Francisco",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [-122.51747131347655, 37.71261539271678],
                    [-122.51747131347655, 37.82036164330873],
                    [-122.35507965087889, 37.82036164330873],
                    [-122.35507965087889, 37.71261539271678],
                    [-122.51747131347655, 37.71261539271678]
                ]
            ]
        }
    })
)

print "AOI Response:"
print json.dumps(r.json(), indent=4, separators=(',', ': '))
