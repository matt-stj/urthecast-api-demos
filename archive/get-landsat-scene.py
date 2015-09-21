import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/archive/scenes'

# When selecting scenes from the Archive, you can either use the "id" parameter
# or you can use the "owner_id" parameter. In this example, we'll use the
# owner_id parameter.
landsat_scene_id = 'LC80990232015258LGN00'

r = requests.get(url, params={
    'api_key': api_key,
    'api_secret': api_secret,

    # Restrict to a single ownder ID
    'owner_id': landsat_scene_id
})

print "Scene {0} metadata:".format(landsat_scene_id)
print json.dumps(r.json()['payload'][0], indent=4, separators=(',', ': '))
