import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/archive/scenes'

r = requests.get(url, params={
    'api_key': api_key,
    'api_secret': api_secret,
})

total = r.json()['meta']['total']

print "Total number of scenes available UC archive: {0}".format(total)
