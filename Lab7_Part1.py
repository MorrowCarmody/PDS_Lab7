# Matt Carmody
# COSC 6375
# Lab 7 Part 1

import numpy as np

arr = np.array([0,1,2,3,4,5,6,7,8,9])

for i in arr:
    if(i%2):
        arr[i]+=2

print(arr)

"""
INSTRUCTIONS:
Write a Python script in a file named Lab7_Part1.py.
Create a numpy array of integers from 0 to 9 and replace odd numbers with (num + 2), and keep even
numbers unchanged.
"""
