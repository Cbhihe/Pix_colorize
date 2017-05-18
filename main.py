import base64           # to encode image
import Algorithmia      # module with methods to pipe request 
import os

from flask import Flask, request
app = Flask(__name__, static_url_path='')

api_key = os.environ.get('API_KEY')  # API_KEY is provided by Algorithmia on account registration
                                     # API_KEY must be set as an environment variable in the app's RTE  
if api_key is None:
   raise Exception("Environment variable API_KEY is not set.")

client = Algorithmia.client(api_key) 
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.5')   # instantiate Algorithmia class for wanted algorithm

def process_image(image_base64):
   req = {
      "image": image_base64
   }
   return algo.pipe(req).result     # returns result of http request passed on to flask

def get_image_base64(image_file):   # image encode base64
   return "data:image/jpeg;base64," + base64.b64encode(image_file.read())

@app.route('/', methods=['GET'])    # decorator
# only accessed upon loading the flask site frontend
# GET received by backend when frontend is loaded
def root():
   return app.send_static_file('index.html')

@app.route('/image', methods=['POST']) # decorator
# invoked when the static initial (black and white) file is passed to backend ...
def image():
   result = process_image(request.data);  # flask magic here ! 
   # "data" is an attribute of the "resquest" object in flask
   # "request.data" contains the input image as a large base64 encoded string 
   # passed on to main.py by the angularJS frontend.
   return get_image_base64(client.file(result['output']).getFile())   
   # Algorithmia gets processed file from loc "output" (has the form of an http location)
   # where "client." specifies the API_KEY and "getFile()" downloads the file in binary format
   # to be base64 encoded by flask frontend.
                                                

if __name__ == '__main__':
   app.run(host='0.0.0.0')    
   # not just processes in the the container but also the local host (127.0.0.1) 
   # can access the website served by flask.
