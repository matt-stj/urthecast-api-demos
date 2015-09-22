import requests
import os
import json
import datetime

api_key = os.environ['UC_API_KEY']
api_secret = os.environ['UC_API_SECRET']

# We are going to determine when each sensor will be flying over our AOI next.
# Please note that a forecast is not a guarantee of capture.
base_url = 'https://api.urthecast.com/v1/satellite_tracker/sensor_platforms/'
theia_url = base_url + 'theia/forecasts'
oli_tirs_url = base_url + 'oli-tirs/forecasts'

# Please update this with an AOI ID that you own
aoiID = 'AU7m8ATfeevUx1XkebEX'

r_theia = requests.get(theia_url,
    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        'limit': 1,
        # Sort by the orbit point epoch, for chrono order
        'sort': 'first_orbit_point_epoch',
        # Only want forecasts happening in the future
        'epoch_gte': datetime.datetime.now().isoformat(),
        # Must intersect with our AOI geometry
        'geometry_intersects': aoiID
    },
)

r_oli_tirs = requests.get(oli_tirs_url,
    params = {
        'api_key': api_key,
        'api_secret': api_secret,
        'limit': 1,
        # Sort by the orbit point epoch, for chrono order
        'sort': 'first_orbit_point_epoch',
        # Only want forecasts happening in the future
        'epoch_gte': datetime.datetime.now().isoformat(),
        # Must intersect with our AOI geometry
        'geometry_intersects': aoiID
    },
)

print "Next capture opportunities for AOI {0}".format(aoiID)
print "-------------------------------------------------------"
print "Theia: {0}".format(r_theia.json()['payload'][0]['first_orbit_point_epoch'])
print "Landsat-8: {0}".format(r_oli_tirs.json()['payload'][0]['first_orbit_point_epoch'])

# To see full response:
# print json.dumps(r_theia.json(), indent=4, separators=(',', ': '))
# print json.dumps(r_oli_tirs.json(), indent=4, separators=(',', ': '))
