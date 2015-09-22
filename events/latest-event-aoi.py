import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/event_streams/events'

# Please update this with an AOI ID that you own
aoiID = 'AU7m8ATfeevUx1XkebEX'

r = requests.get(url,
    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        'limit': 1,
        'geometry_intersects': aoiID
    },
)

print "Most recent event for AOI {0}:".format(aoiID)
print json.dumps(r.json()['payload'][0], indent=4, separators=(',', ': '))
