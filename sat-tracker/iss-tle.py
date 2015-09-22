import requests
import os
import json
import datetime

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']

# Replace "iss" with other satellites.
# https://developers.urthecast.com/docs/satellite-tracker#satellites
url = 'https://api.urthecast.com/v1/satellite_tracker/satellites/iss/tles'

r = requests.get(url,
    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        # Only want the most recent, so limit to 1
        'limit': 1,
        # The TLE must be less than this current moment
        'epoch_lte': datetime.datetime.now().isoformat(),
        # Sort the response by epoch, descending, so most recent is first
        'sort': '-epoch'
    },
)

print "Most recent TLE for ISS:"
print "------------------------"
print json.dumps(r.json()['payload'][0], indent=4, separators=(',', ': '))
