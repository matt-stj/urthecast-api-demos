import requests
import os
import json
import datetime

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']

# Replace "iss" with other satellites.
# https://developers.urthecast.com/docs/satellite-tracker#satellites
url = 'https://api.urthecast.com/v1/satellite_tracker/satellites/iss/orbit_points'

r = requests.get(url,
    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        'limit': 1,
        'epoch_lte': datetime.datetime.now().isoformat()
    },
)

print "Current location of ISS:"
print "------------------------"
# GeoJSON spec says [longitude, latitude], which is why these may appear backwards
print "Latitude: {0}".format(r.json()['payload'][0]['geometry']['coordinates'][1])
print "Longitude: {0}".format(r.json()['payload'][0]['geometry']['coordinates'][0])

# To dump whole response:
# print json.dumps(r.json(), indent=4, separators=(',', ': '))
