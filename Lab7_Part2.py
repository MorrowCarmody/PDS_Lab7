# Matt Carmody
# COSC 6375
# Lab 7 Part 2

import numpy as np

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
np_arr = np.array(arr)
n = int(len(arr)/4)
np_arr = np_arr.reshape(n,4)
print(np_arr)

"""
INSTRUCTIONS:
Write a Python script in a file named Lab7_Part2.py.
Convert below one -dimensional array into n-dimensional array of shape(n,4)
Input = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
"""
