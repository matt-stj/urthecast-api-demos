import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/archive/scenes'

# This is the scene ID we want to filter by
scene_id = 'DgfsRkm1SUqoXYIZVviJoQ'

r = requests.get(url, params={
    'api_key': api_key,
    'api_secret': api_secret,

    # Restrict to a single scene ID
    'id': scene_id
})

print "Scene {0} metadata:".format(scene_id)
print json.dumps(r.json()['payload'][0], indent=4, separators=(',', ': '))
