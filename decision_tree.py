#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 12:32:33 2017
Author: Long Yu
Descriptions: Implementation of Decision Tree
"""

import numpy as np
from math import log
from operator import itemgetter
# create a artificial data that simulating tree building
# First We need to write the codes that computing entropy

def computeEntropy(target):
    """ 
		data: All feature variables in data -- nested list
		target: the target variables -- int list
		return : a entropy of data -- a float
    """
    countVar = {}
    entropy = 0.0
    for num in target:
        if num not in countVar:    
            countVar[num] = 0
        countVar[num] += 1
    
    # calucate entropy
    for key in countVar:
        prob = countVar[key]/len(target)
        entropy -= prob*log(prob,2)
    
    return entropy

def splitData(x, iColumn, value):
    """
    x : ndarray
    iColumn : column index
    value : split data by value
    return reduced data set
    """
    
    return np.delete(x[x[:, iColumn] == value], iColumn, 1)
    

def findFeature(dataset):
    """
    dataset : dataset which could be mult-list or mult-array
    return the index of best feature to split
    """
    infoGain = 0.0
    bestInfoGain = 0.0
    iFeature = -1
    numFeature = dataset.shape[1] - 1 # substract y column
    baseEntropy = computeEntropy(dataset[:, -1])
    for indexCol in range(numFeature):
        uniqueValue = set(dataset[:, indexCol])
        newEntropy = 0.0
        for value in uniqueValue:
            reduceData = splitData(dataset, indexCol, value)
            prob = reduceData.shape[0]/float(dataset.shape[0])
            newEntropy += prob * computeEntropy(reduceData[:,-1])
        infoGain = baseEntropy - newEntropy
        if(infoGain > bestInfoGain):
            bestInfoGain = infoGain
            iFeature = indexCol
        return iFeature
    
def majorCount(classList):
    """
    classList : target variable list
    return majority count of target variable 
    """
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), 
                              key=itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(data, labels):
    """
    
    """
    y = data[:, -1]
    uniqueSet = np.unique(y, return_counts=True)
    if  len(uniqueSet) == y.shape[0]: # check if target variables are the same
        return y[0]
    if len(dataSet[0]) == 1:
        return majorCount(y) # check if data has any features 
    bestFeat = findFeature(data) 
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = data[:, bestFeat]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        newData = splitData(data, bestFeat, value)
        myTree[bestFeatLabel][value] = createTree(newData, subLabels)
    return myTree


if __name__ == '__main__':
    dataSet = np.array([[1, 1, 'yes'],
                        [1, 1, 'yes'],
                        [1, 0, 'no'],
                        [0, 1, 'no'],
                        [0, 1, 'no']])
    labels = ['no surfacing','flippers']
    createTree(dataSet, labels)
    findFeature(dataSet)