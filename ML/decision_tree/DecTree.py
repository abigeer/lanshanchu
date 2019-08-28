#coding=utf-8
'''
决策树的实现(ID3算法)
Created on 2018年9月10日

@author: 89146
'''
from math import log
import operator

#构造数据
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels


#计算经验熵
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    #为所有分类创建字典
    labelCounts = {}            #用于保存类别中出现次数
    for featVec in dataSet:
        currentLabel = featVec[-1]  #dataSet最后一列是类别
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0        #香农熵
    #使用极大似然估计计算
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob*log(prob,2)
    return shannonEnt
    
#按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
    """
    dataSet:要划分的数据集
    axis:要划分的特征所属第几个特征
    value:要划分的特征值
    """
    #创建一个新的数据用于保存划分后的数据集
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:      #如果是这个特征
            #将符合条件的数据抽取
            reducedFeatVec = featVec[:axis]
            #将抽取到的数据丢弃划分的特征
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

#选择最好的数据集划分方式（利用信息增益（互信息））
def chooseBestFeatureToSplit(dataSet):
    """
    数据dataSet是列表元素的列表，且
    元素长度相等，元素最后一列为类别标签
    返回最好划分特征的维数
    """
    #特征数
    numFeatures = len(dataSet[0]) - 1
    #计算dataSet的经验熵
    baseEntropy = calcShannonEnt(dataSet)
    #bestInfoGain是最大信息增益
    #bestFeature是最好特征的在第几列
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        #使用列表推导，创建新列表，将dataSet中所有第i个特征写入到新
        featList = [example[i] for example in dataSet]
        #使用set不重复集合使值唯一
        uniqueVals = set(featList)
        newEntropy = 0.0
        #计算条件熵
        for value in uniqueVals:
            #根据某一特征划分数据集
            #同时计算条件熵
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        #计算信息增益
        infoGain = baseEntropy - newEntropy
        if infoGain > bestInfoGain:
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

#多数表决策略
def majorityCut(classList):
    """
    使用分类名称的列表，然后创建键值为classList中
    唯一的数据字典，字典对象存储了classList中
    每个类标签出现的频率，最后利用operate操作
    对字典排序，返回出现次数最多的分类名称
    """
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    #使用operator根据值大小对字典排序
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse = True)
    return sortedClassCount[0][0]

#构建决策树
def createTree(dataSet, labels):
    """
    dataSet:数据集
    labels：类别列表,在这里只有象征意义
    """
    #创建一个新的类别标签列表
    classList = [example[-1] for example in dataSet]
    #所有类标签相同达到停止条件，返回该类标签
    if classList.count(classList[0]) ==len(classList):
        return classList[0]
    #第二个停止条件：使用完了所有特征，仍没有划分完数据集
    if len(dataSet[0]) == 1:    #dataSet只剩下类别
        return majorityCut(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    #拿取最好特征的所有特征值创建新列表
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        #创建新的subLabels对象，在构建树过程中，不改变labels
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree
        



#香农(条件)熵测试
myData, labels = createDataSet()
shannonEnt = calcShannonEnt(myData)
print(shannonEnt)
print(myData)
#测试划分数据
splitData = splitDataSet(myData, 0, 1)
print(splitData)
#测试根据最好特征划分
featureNum = chooseBestFeatureToSplit(myData)
print(featureNum)
#测试构建树
decTree = createTree(myData, labels)
print(decTree)



