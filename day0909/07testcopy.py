#07testcopy.py

import math
import random
import re
import os.path
import sys
import pickle

import time
import datetime

import  copy

apple = 'rain snow'
my = apple 
print(apple)
print(my)
print()

data = [ 11,22,33]
# 양쪽 적용 mydb = data
mydb = copy.deepcopy(data) 
data[0] = 789
print('원본(data)',data)
print('복사본(mydb)',mydb)


print()

'''
rain snow
rain snow

원본(data) [789, 22, 33]
복사본(mydb) [11, 22, 33]
'''