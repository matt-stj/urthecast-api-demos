import requests
import os
import json

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']
url = 'https://api.urthecast.com/v1/archive/scenes'

date_ranges = [
    {
        # ISO-8601 date format
        'min': '2015-01-01', 'max': '2015-01-31', 'label': 'Jan 2015',
    },
    {
        'min': '2015-02-01', 'max': '2015-02-28', 'label': 'Feb 2015',
    },
    {
        'min': '2015-03-01', 'max': '2015-03-31', 'label': 'Mar 2015',
    },
    {
        'min': '2015-04-01', 'max': '2015-04-30', 'label': 'Apr 2015',
    },
    {
        'min': '2015-05-01', 'max': '2015-05-31', 'label': 'May 2015',
    },
    {
        'min': '2015-06-01', 'max': '2015-06-30', 'label': 'Jun 2015',
    },
    {
        'min': '2015-07-01', 'max': '2015-07-31', 'label': 'Jul 2015',
    },
    {
        'min': '2015-08-01', 'max': '2015-08-31', 'label': 'Aug 2015',
    },
    {
        'min': '2015-09-01', 'max': '2015-09-30', 'label': 'Sep 2015',
    },
]

for date_range in date_ranges:
    r = requests.get(url, params={
        'api_key': api_key,
        'api_secret': api_secret,

        # Date that imagery was acquired should be greater than or equal to
        # the start of the month, and less than or equal to the end of the month.
        'acquired_gte': date_range['min'],
        'acquired_lte': date_range['max'],

        # We do not want any scene data, just the totals, so set a limit of 0
        'limit': 0,
    })

    total = r.json()['meta']['total']

    print "{0} scenes: {1}".format(date_range['label'], total)
