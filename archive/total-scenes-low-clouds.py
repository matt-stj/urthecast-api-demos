import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/archive/scenes'

r = requests.get(url, params={
    'api_key': api_key,
    'api_secret': api_secret,
    # Cloud coverage should be less than or equal to twenty percent
    'cloud_coverage_lte': 20
})

total = r.json()['meta']['total']

print "There are {0} low cloud scenes available in the UC archive".format(total)
