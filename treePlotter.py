#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The functions to visualize the result of dataSet spitting by Decision Tree
Created on Fri Apr 21 15:13:35 2017
@author: Martin

"""

import matplotlib.pyplot as plt

#node pattern
decisionNode = dict(boxstyle="square", fc="0.75")
leafNode = dict(boxstyle="round", fc="w")
arrow_args = dict(arrowstyle="<|-",shrinkB=12)

#get the number of leafs in the tree(dict strut)
def getNumLeafs(tree):
    numLeafs = 0
    #base case: empty tree
    if not tree: return 0
    for key,value in tree.items():
        if isinstance(value, dict): numLeafs+=getNumLeafs(value) 
        else: numLeafs+=1
    return numLeafs

#get the depth of the tree(dict strut)
def getTreeDepth(tree):
    maxDepth = 0
    parentNode = list(tree.keys())[0]
    subTree = tree[parentNode]
    for key, value in subTree.items():
        if isinstance(value, dict): currentDepth=1 + getTreeDepth(value)
        else: currentDepth=1
        if currentDepth > maxDepth: maxDepth = currentDepth
    return maxDepth

#plot the node on the figure
def plotNode(nodeTxt, nodePt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt,
                            xy=parentPt,
                            xycoords='axes fraction',
                            xytext=nodePt,
                            textcoords='axes fraction',
                            va="center",
                            ha="center",
                            bbox=nodeType,
                            arrowprops=arrow_args)

#plot the node txt on the box
def plotMidText(nodePt, parentPt, nodeTxt):
    xMid=(parentPt[0]-nodePt[0])/2.0 + nodePt[0]
    yMid=(parentPt[1]-nodePt[1])/2.0 + nodePt[1]
    createPlot.ax1.text(xMid, yMid, nodeTxt)
    
#plot the tree on the figure
def plotTree(tree, parentPt, nodeTxt):
    numLeafs = float(getNumLeafs(tree))
    parentTxt = list(tree.keys())[0]
    nodePt = (plotTree.xOff + 0.5*(1.0 + numLeafs)/plotTree.totalW, plotTree.yOff)
    plotMidText(nodePt, parentPt, nodeTxt)
    plotNode(parentTxt, nodePt, parentPt, decisionNode)
    secondDict = tree[parentTxt]
    plotTree.yOff = plotTree.yOff - 1.0/plotTree.totalD
    for key, value in secondDict.items():
        if isinstance(value, dict):
            plotTree(value,nodePt,str(key))
        else:
            plotTree.xOff = plotTree.xOff + 1.0/plotTree.totalW
            plotMidText((plotTree.xOff, plotTree.yOff), nodePt, str(key))
            plotNode(value, (plotTree.xOff, plotTree.yOff), nodePt, leafNode)
    plotTree.yOff = plotTree.yOff + 1.0/plotTree.totalD
    
#the create function call from outside function
def createPlot(tree):
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, **axprops,frameon=False)
    plotTree.totalW = float(getNumLeafs(tree))
    plotTree.totalD = float(getTreeDepth(tree))
    plotTree.xOff = -0.5/plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(tree, (0.5,1.0), '')
    plt.show()
    