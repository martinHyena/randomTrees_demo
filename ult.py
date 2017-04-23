#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

The ultility functions to convert data
Created on Tue Apr 18 17:20:40 2017
@author: Martin

"""

import pandas as pd

#read in data from csv file and output a ndarray data set and list of label
def csvToNdarray(fileName):
    dataSet=pd.read_csv(fileName, sep=',', header=0)
    return dataSet.values, dataSet.columns.tolist()

#read in data from csv file and output a list of data set and list of label
def csvToList(fileName):
    dataSet=pd.read_csv(fileName, sep=',', header=0)
    return dataSet.values.tolist(), dataSet.columns.tolist()
    

#read in data from txt file with a ',' delimiter and output a ndarray data set and list of label
def txtCommaToNdarray(fileName):
    dataSet=pd.read_csv(fileName, sep=',', header=0)
    return dataSet.values, dataSet.columns.tolist()

#read in data from txt file with a ',' delimiter and output a list of data set and list of label
def txtCommaToList(fileName):
    dataSet=pd.read_csv(fileName, sep=',', header=0)
    return dataSet.values.tolist(), dataSet.columns.tolist()

#read in data from txt file with a ' ' delimiter and output a ndarray data set and list of label
def txtSpaceToNdarray(fileName):
    dataSet=pd.read_csv(fileName, sep=' ', header=0)
    return dataSet.values, dataSet.columns.tolist()

#read in data from txt file with space delimiter and output a list of data set and list of label
def txtSpaceToList(fileName):
    dataSet=pd.read_csv(fileName, sep=' ', header=0)
    return dataSet.values.tolist(), dataSet.columns.tolist()
