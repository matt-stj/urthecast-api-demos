import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/event_streams/events'

r = requests.get(url,
    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        'limit': 1
    },
)

print "Most recent event:"
print json.dumps(r.json()['payload'][0], indent=4, separators=(',', ': '))
