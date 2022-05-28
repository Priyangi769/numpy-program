# Your task is to print a reversed Numpy array with the element type float.

import numpy as np

print (np.array(map(float, raw_input().split()), float)[::-1])
