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
        "name": "JungfrauSquare",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [46.647655, 7.660476], [46.676139, 8.233319], [46.341512, 8.271809], [46.329850, 7.585620],[46.647655, 7.660476]
                ]
            ]
        }
    })
)

print "AOI Response:"
print json.dumps(r.json(), indent=4, separators=(',', ': '))
