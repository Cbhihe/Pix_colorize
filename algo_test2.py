"""algo module / test2: colorize a simple image"""

import Algorithmia

def colorize_this():
    """ function to blablabla  """
    input_image = {
        # Set location of your own image
        "image": "data://Cbhihe/clc2_data/elephant-savannah_bw.jpg"
    }
    client_name = Algorithmia.client("simMpO/lyo5qwbHRpplIWPyilgM1")
    # insert your own API key above or define it as env-var API_KEY below
    # client_name = Algorithmia.client("API_KEY")
    algo = client_name.algo('deeplearning/ColorfulImageColorization/1.1.5')
    print algo.pipe(input_image)

colorize_this()
