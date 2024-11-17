import sys
import os

def setup():
    sys.path.append(os.path.join(os.path.dirname(__file__), 'data'))
    sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))
    # print(sys.path)
    
setup()
