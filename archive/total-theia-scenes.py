import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/archive/scenes'

r = requests.get(url, params={
    'api_key': api_key,
    'api_secret': api_secret,
    # For list of available sensor_platforms, see:
    # https://developers.urthecast.com/docs/archive
    'sensor_platform': 'theia',
})

total = r.json()['meta']['total']

print "There are {0} Theia images available in the UC archive".format(total)
