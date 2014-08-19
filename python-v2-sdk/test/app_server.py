import unittest
import json
import sys
sys.path.append("..")
from api import OoyalaAPI
from flask import Flask,make_response
from flask import request
from functools import wraps

app = Flask(__name__)

class TestOoyalaAPI(object):
    def setUp(self):
        self.api = OoyalaAPI('lueDYyOlaYtIydG6Fr_En9pHWL1p.Y-sBm',
                             'KXKXf5-EKmwg3gmuybr52fD8IRTJaXuGX0O5CrFm')

    def get_all_assets(self):
        # Get all assets
        try:
          res = self.api.get('assets')
          print "all assests {0}".format(res)
        except:
          self.get_all_assets()

    def get_asset(self, asset_id):
        # Get all assets
        try:
          res = self.api.get('assets/'+asset_id)
          print "assest id {0} details {1}".format(asset_id, res)
        except:
          self.get_asset(asset_id)

    
    def update_asset(self, asset_id, asset_key, asset_value):
        try:
          res = self.api.patch('assets/'+asset_id,{asset_key: asset_value})
          print "after patch {0}".format(res)
        except:
          self.update_asset(asset_id, asset_key, asset_value)
    
        # Remove channel and video assets
        #self.assertTrue(self.api.delete('assets/%s' % video_id))

"""
if __name__ == "__main__ test":
	app = TestOoyalaAPI()
	app.setUp()
	print "----------------------------------------------------------"
	app.get_all_assets()
	print "----------------------------------------------------------"
	app.get_asset('FrbnBvbzqwLI3SYfe2gi5mOg1lQxjLxQ')
	print "----------------------------------------------------------"
	app.update_asset('FrbnBvbzqwLI3SYfe2gi5mOg1lQxjLxQ', 'name', 'govi Miramax Partners with Ooyala and Facebook')
"""

def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator

def access_ctrl(f):
    @wraps(f)
    @add_response_headers({'Access-Control-Allow-Origin': '*'})
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function



@app.route("/ooyala/update_title")
@access_ctrl
def update_title():
    try:
      asset_id = request.args.get('asset_id')
      asset_key = request.args.get('asset_key')
      asset_val = request.args.get('asset_val')
      print "asset_id: {0}, asset_key: {1}, asset_val:{2}".format(asset_id, asset_key, asset_val)
    except:
      return "invalid params"
    api_instance.update_asset(asset_id, asset_key, asset_val)
    return "success"

if __name__ == "__main__":
    api_instance = TestOoyalaAPI()
    api_instance.setUp()
    app.run('0.0.0.0', 443, debug=True)


