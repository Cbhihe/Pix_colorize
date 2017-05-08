import base64
import Algorithmia
import os

from flask import Flask, request
app = Flask(__name__, static_url_path='')


api_key = os.environ.get('API_KEY')
if api_key is None:
   raise Exception("Environment variable API_KEY is not set.")

client = Algorithmia.client(api_key) 
algo = client.algo('deeplearning/ColorfulImageColorization/1.1.5')

def process_image(image_base64):
   req = {
      "image": image_base64
   }
   return algo.pipe(req).result

def get_image_base64(image_file):
   return "data:image/jpeg;base64," + base64.b64encode(image_file.read())

@app.route('/', methods=['GET'])
def root():
   return app.send_static_file('index.html')

@app.route('/image', methods=['POST'])
def image():
   result = process_image(request.data);
   return get_image_base64(client.file(result['output']).getFile())

if __name__ == '__main__':
   app.run(host='0.0.0.0')   
