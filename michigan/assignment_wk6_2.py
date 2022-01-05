'''
Find the place_id
'''

import urllib.request
import urllib.parse
import urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'


def ssl_no_verification():
    ''' (None) -> SSLContext
    '''
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def get_input():
    ''' (None) -> str

    Ask user for an address.
    '''
    address = input('Enter location: ')
    if address == '':
        address = 'Universidad de San Carlos de Guatemala'
    return address


address = get_input()

parms = dict()
parms['address'] = address
parms['key'] = api_key
url = serviceurl + urllib.parse.urlencode(parms)
ctx = ssl_no_verification()

urlhandler = urllib.request.urlopen(url, context=ctx)
data = urlhandler.read().decode()

try:
    jsn = json.loads(data)
except:
    jsn = None
    quit()

if not jsn or 'status' not in jsn or jsn['status'] != 'OK':
    quit()

place_id = jsn['results'][0]['place_id']
print(place_id)
