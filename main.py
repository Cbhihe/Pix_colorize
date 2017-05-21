""" main.py """

import os
import base64
import Algorithmia

from flask import Flask, request

APP = Flask(__name__, static_url_path='')

API_KEY = os.environ.get('API_KEY')
# API_KEY is provided by Algorithmia on account registration
# API_KEY must be set as an environment variable in the app's RTE
if API_KEY is None:
    raise Exception("Environment variable API_KEY is not set.")

# Object construction
# instantiate Algorithmia module class for wanted algorithm
CLIENT = Algorithmia.client(API_KEY)
ALGO = CLIENT.algo('deeplearning/ColorfulImageColorization/1.1.5')

def process_image(image_base64):
    """ API call """
    req = {
        "image": image_base64
    }
    # returns result of HTTP request passed on to flask
    return ALGO.pipe(req).result

def get_image_base64(image_file):
    """ image encode base64 """
    return "data:image/jpeg;base64," + base64.b64encode(image_file.read())

# Only accessed upon loading the flask site frontend
# GET received by backend when frontend is loaded
# Backend returns index.html to frontend (GUI)
@APP.route('/', methods=['GET'])
def root():
    """ ___  """
    return APP.send_static_file('index.html')

# Invoked when input file (b&w) is passed to backend ...
@APP.route('/image', methods=['POST'])
def image():
    """ ___ """
    # flask magic here !
    result = process_image(request.data)
    # "data" is an attribute of the "resquest" object in flask
    # "request.data" contains input image as large base64 encoded string
    # passed to main.py by frontend.
    return get_image_base64(CLIENT.file(result['output']).getFile())

# Algorithmia gets processed file from loc "output" (has URL form)
# where "CLIENT." specifies API_KEY and "getFile()" downloads binary file
# to be base64 encoded by frontend.

if __name__ == '__main__':
    APP.run(host='0.0.0.0')
    # not just processes in container but any host incl localhost (127.0.0.1)
    # can access the website served by flask.
