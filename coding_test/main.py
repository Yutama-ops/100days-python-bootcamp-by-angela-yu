#!/bin/python3

import math
import os
import random
import re
import sys

def my_function(sentenceIn):
    a = sentenceIn.slice()
    # return sentenceIn[::-1]
    return a

mytxt = my_function("hey there, Alan")

print(mytxt)

# for i in sentenceIn:
#    ns.append(i)
#
# a = ns.reverse()
#
# print(ns)
# print(a)

# Complete the reverseAndCapitalise function below.
# def reverseAndCapitalise(sentenceIn):
#     for i in sentenceIn:
#         print(i)
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     # sentenceIn = input()
#     sentenceIn = "hey there, Alan"
#
#     res = reverseAndCapitalise(sentenceIn)
#
#     fptr.write(res + '\n')
#
#     fptr.close()
