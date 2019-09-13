"""
Easy puzzle
Find the greatest summation of the 'hourglass' within each 3x3 kernel
in a 2d array

"""

#!/bin/python3

import math
import os
import random
import re
import sys



# Helper function to sum hourglass in array
def SumHourglass(arr):
    pos1 = arr[0][0]
    pos2 = arr[0][1]
    pos3 = arr[0][2]
    mid = arr[1][1]
    pos4 = arr[2][0]
    pos5 = arr[2][1]
    pos6 = arr[2][2]
    return pos1 + pos2 + pos3 + mid + pos4 + pos5 + pos6

def CreateKernel(arr, pos1, pos2):
    arr1 = []
    for i in range(pos2, pos2 + 3, 1):
        arr1.append(arr[i][pos1:pos1+3])
    return arr1

# Complete the hourglassSum function below.
def hourglassSum(arr):
    # given 2d array here
    highest = -sys.maxsize -1  # min size
    # create kernel n number of times
    for i in range(0, len(arr)-2, 1):
        for j in range(0, len(arr[0])-2, 1):
            # Create kernel with window size 3x3
            newKernel = CreateKernel(arr, i, j)
            kernelValue = SumHourglass(newKernel)
            if kernelValue > highest:
                highest = kernelValue
    return highest 


## Driver code
print(hourglassSum([
[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]))