# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:42:20 2024

@author: A0029445
"""

import pandas

file3 = pandas.read_csv("iris_data.csv")

print (file3.info())

print(file3.describe())