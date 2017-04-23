#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 
The ultility functions to convert data
Created on Tue Apr 18 17:20:40 2017
@author: Martin

"""

import pandas as pd

#read in data from csv file and output a ndarray
def csvToNdarray(fileName):
    return pd.read_csv(fileName, sep=',', header=1).values

#read in data from csv file and output a list
def csvToList(fileName):
    return pd.read_csv(fileName, sep=',', header=1).values.tolist()

#read in data from txt file with a ',' delimiter and output a ndarray
def txtCommaToNdarray(fileName):
    return pd.read_csv(fileName, sep=',', header=None).as_matrix()

#read in data from txt file with a ',' delimiter and output a list
def txtCommaToList(fileName):
    return pd.read_csv(fileName, sep=',', header=None).as_matrix().tolist()

def txtSpaceToNdarray(fileName):
    return pd.read_csv(fileName, sep=' ', header=None).as_matrix()

#read in data from txt file with space delimiter and output a list
def txtSpaceToList(fileName):
   return pd.read_csv(fileName, sep=' ', header=None).as_matrix().tolist()
