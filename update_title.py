import requests
import hashlib
import base64
import urllib
import httplib
import time

#https://api.ooyala.com/v2/assets/FrbnBvbzqwLI3SYfe2gi5mOg1lQxjLxQ?api_key=lueDYyOlaYtIydG6Fr_En9pHWL1p.Y-sBm&signature=sXkiPyASSLWw0usvd%2Bs21Lmtd5ZZ5AYSTFFMOPgYcvU&expires=1408370130
#{"name": "sample_mpeg4.mp4"}
#1408372450

backlot_host = 'https://api.ooyala.com'
backlot_url = '/v2/assets/'
asset_id = 'FrbnBvbzqwLI3SYfe2gi5mOg1lQxjLxQ'
api_key = 'lueDYyOlaYtIydG6Fr_En9pHWL1p.Y-sBm'
api_secret = 'KXKXf5-EKmwg3gmuybr52fD8IRTJaXuGX0O5CrFm'

def generate_signature(secret_key, http_method, request_path, query_params, request_body=''):
	signature = secret_key + http_method.upper() + request_path
	for key, value in query_params.iteritems():
		signature += key + '=' + str(value)
	signature = base64.b64encode(hashlib.sha256(signature).digest())[0:43]
	signature = urllib.quote_plus(signature)
	return signature

time_now = int(time.time()) + (10 * 24 * 60 * 60)
query_params = {'api_key': api_key, 'expires': time_now}
signature = generate_signature(api_secret, 'get', backlot_url + asset_id, query_params)

params = urllib.urlencode({'api_key': api_key, 'expires': time_now,'signature': signature})
#conn = httplib.HTTPSConnection("api.ooyala.com")
#conn.request("GET", "/v2/assets/FrbnBvbzqwLI3SYfe2gi5mOg1lQxjLxQ")
#response = conn.getresponse()
#print response.status, response.reason
#data = response.read()
#print data

#r = requests.get('https://api.ooyala.com/v2/assets/FrbnBvbzqwLI3SYfe2gi5mOg1lQxjLxQ', params=params)
#print "url = {0}".format(r.url)
#print "response {0}".format(r.text)
#print "response {0}".format(r.content)

s = requests.Session()
r = s.get('https://api.ooyala.com/v2/assets/FrbnBvbzqwLI3SYfe2gi5mOg1lQxjLxQ', params=params)
print(r.text)

