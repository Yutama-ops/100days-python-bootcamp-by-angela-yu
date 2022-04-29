#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getMaxUnits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER_ARRAY boxes
#  2. LONG_INTEGER_ARRAY unitsPerBox
#  3. LONG_INTEGER truckSize


def getMaxUnits(boxes, unitsPerBox, truckSize):
    # Write your code here
    # 1 < box < 10**5
    # box = units/box
    # 1< boxi < 10**7
    # 1< units per box < 10**5
    # 1< trucks size < 10**8
    # trucks size 1 contains 1 box with max units perbox
    # x = > truck
    # x = < b ,  x = >n
    units = []
    y = 0
    for i in boxes:
        for x in range(i):
            units.append(unitsPerBox[y])
        y += 1
    units.sort()
    total_unit = sum(units[-truckSize:])

    return total_unit

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     boxes_count = int(input().strip())
#
#     boxes = []
#
#     for _ in range(boxes_count):
#         boxes_item = int(input().strip())
#         boxes.append(boxes_item)
#
#     unitsPerBox_count = int(input().strip())
#
#     unitsPerBox = []
#
#     for _ in range(unitsPerBox_count):
#         unitsPerBox_item = int(input().strip())
#         unitsPerBox.append(unitsPerBox_item)
#
#     truckSize = int(input().strip())
#
#     result = getMaxUnits(boxes, unitsPerBox, truckSize)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
