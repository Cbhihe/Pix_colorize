""" missing docstring """

import Algorithmia

def demo_hello():
    """ function to avoid having to write parameters in upppercase """
    username = "Cbhihe"
    client_name = Algorithmia.client("simMpO/lyo5qwbHRpplIWPyilgM1")
    algo = client_name.algo('demo/Hello/0.1.1')
    print algo.pipe(username)
demo_hello()
