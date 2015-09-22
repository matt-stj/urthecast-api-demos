import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/archive/scenes'

# Please update this with an AOI ID that you own
aoiID = 'AU7m8ATfeevUx1XkebEX'

r = requests.get(url, params={
    'api_key': api_key,
    'api_secret': api_secret,
    # We only want scenes that intersect with our AOI
    'geometry_intersects': aoiID
})

total = r.json()['meta']['total']

print "Imagery of AOI {0} (total: {1})".format(aoiID, total)
print "---------------------------------------------------"

for scene in r.json()['payload']:
    print "{0} - acquired on {1} by {2} (cloud coverage: {3}%)".format(scene['id'], scene['acquired'], scene['sensor_platform'], scene['cloud_coverage'])
