# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:37:40 2024

@author: A0029445
"""

import pandas

file2 = pandas.read_csv("diab_data.csv")

print (file2.info())

print(file2.describe())