import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/consumers/apps/me/aois'

r = requests.get(url,
    params = { 'api_key': api_key, 'api_secret': api_secret },
)

print "AOIs:"
print "------------------------------------"

for aoi in r.json()['payload']:
    print "{0} - {1}".format(aoi['name'], aoi['id'])
