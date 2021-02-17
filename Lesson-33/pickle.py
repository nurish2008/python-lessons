# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 00:24:02 2021

@author: Sony
"""

import pickle 

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)
