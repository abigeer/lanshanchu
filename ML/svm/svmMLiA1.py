#coding = utf-8
'''
Created on 2018年8月16日
改进版完整SMO算法
@author: 89146
'''
import numpy as np
import matplotlib.pyplot as plt
import random
from time import clock
from networkx.algorithms.bipartite.basic import color

def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

def selectJrand(i,m):
    j = i
    while(j==i):
        j = int(random.uniform(0,m))
    return j

def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    elif aj < L:
        aj = L
    return aj

class optStruct:
    def __init__(self, dataMatIn, classLabel, C, toler):  #相当于Java的构造方法，self类似与this
        self.X = dataMatIn
        self.labelMat = classLabel
        self.C = C
        self.toler = toler
        self.m = np.shape(dataMatIn)[0]       #样本的个数
        self.alphas = np.mat(np.zeros((self.m,1)))       #alpha列表初始化为0值
        self.b = 0
        self.eCatch = np.mat(np.zeros((self.m,2)))       #用于存储Ei的列表[k,v]k表示是否有效，v表示Ei值
        
def calcEk(oS, k):      #用于计算Ek
    gXk = float(np.multiply(oS.alphas, oS.labelMat).T*(oS.X*oS.X[k,:].T)) + oS.b
    Ek = gXk - float(oS.labelMat[k])
    return Ek

def selectJ(i, oS, Ei):     #内循环选择第二个alphas
    maxK = -1
    Ej = 0
    maxDeltaE = 0       #计算Ei和Ej间的最大变化|Ei - Ej|
    oS.eCatch[i] = [1,Ei]       #将Ei放入设置为有效
    validEcatch = np.nonzero(oS.eCatch[:,0])[0]     #取有效的Ei，这里eCatch[:,0]是m*1维
    if(len(validEcatch) > 1):
        for k in validEcatch:
            if k == i: continue
            Ek = calcEk(oS,k)
            deltaE = abs(Ei - Ej)
            if(deltaE > maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej = Ek
        return maxK, Ej
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
        return j, Ej

def innerL(oS, i):      #类似于smoSimple
    """
    1.在toler范围内检验KTT条件，选中第一个alpha
    2.选择第二个alpha
    3.同时计算更新alpha和b
    """
    Ei = calcEk(oS, i)
    '''这里出现了错误，两个kTT约束检验写成了and应该是or'''
    if ((oS.labelMat[i]*Ei < - oS.toler) and (oS.alphas[i] < oS.C)) or \
         ((oS.labelMat[i]*Ei > oS.toler) and (oS.alphas[i] > 0)):       #检验是否违反KKT条件
        j, Ej = selectJ(i, oS, Ei)
        alphaIold = oS.alphas[i].copy(); alphaJold = oS.alphas[j].copy()
        if(oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, alphaJold - alphaIold)
            H = min(oS.C, oS.C+alphaJold-alphaIold)
        else:
            L = max(0,alphaJold+alphaIold-oS.C)
            H = min(oS.C, alphaJold + alphaIold)
        if H == L: print("---->H==L"); return 0
        eta = oS.X[i,:]*oS.X[i,:].T + oS.X[j,:]*oS.X[j,:].T - 2.0*oS.X[i,:]*oS.X[j,:].T
        if(eta<=0): print("---->eta<=0"); return 0
        oS.alphas[j] += oS.labelMat[j]*(Ei - Ej)/eta
        oS.alphas[j] = clipAlpha(oS.alphas[j], H, L)
        if(abs(oS.alphas[j] - alphaJold) < 0.00001):
            print("---->alphaJ not move enough"); return 0
        '''这里忘记更新alphas[i]'''
        oS.alphas[i] = alphaIold + oS.labelMat[i]*oS.labelMat[j]*(alphaJold - oS.alphas[j])
        b1 = oS.b - Ei - oS.labelMat[i]*oS.X[i,:]*oS.X[i,:].T*(oS.alphas[i] - alphaIold)\
                 - oS.labelMat[j]*oS.X[j,:]*oS.X[i,:].T*(oS.alphas[j] - alphaJold)
        b2 = oS.b - Ej - oS.labelMat[i]*oS.X[i,:]*oS.X[j,:].T*(oS.alphas[i] - alphaIold)\
                 - oS.labelMat[j]*oS.X[j,:]*oS.X[j,:].T*(oS.alphas[j] - alphaJold)
        if((0 < oS.alphas[i]) and (oS.C > oS.alphas[j])): oS.b = b1
        elif((0 < oS.alphas[j]) and (oS.C > oS.alphas[j])): oS.b = b2
        else: oS.b = (b1 + b2)/2.0
        return 1
    else: return 0
        
def smoP(dataMatIn, classLabels, C, toler, maxIter,):
    oS = optStruct(np.mat(dataMatIn), np.mat(classLabels).transpose(), C, toler)
    alphaPairsChanged = 0
    iter = 0
    entirSet = True     #启发式方法，为True时表示遍历所有数据集，为False是表示遍历所有非支持向量点
    while(iter < maxIter) and ((entirSet) or (alphaPairsChanged > 0)):
        #当迭代次数超越最大迭代次数时或者迭代所有数据集alpha没有一个改变是退出
        alphaPairsChanged = 0
        if entirSet:
            for i in range(oS.m):
                alphaPairsChanged += innerL(oS, i)
                print("---->第%d轮（全数据）迭代,第%d个alpha,已经改变%d个alpha"%(iter, i, alphaPairsChanged))
            iter+=1
        else:
            nonBoundIs = np.nonzero((oS.alphas.A > 0 )*(oS.alphas.A < C))[0] #这里出错少写[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(oS, i)
                print("---->第%d轮（非边界值）迭代,第%d个alpha,已经改变%d个alpha"%(iter, i, alphaPairsChanged))
            iter += 1
        #交换迭代方法
        if entirSet : entirSet = False
        elif(alphaPairsChanged == 0): entirSet = True
        print("---->迭代轮数（iterNumber）%d"%(iter))
    return oS.b, oS.alphas

start = clock()    
data, label = loadDataSet("testSet.txt")   #都是tuple
data = np.array(data); label = np.array(label)
b, alphas = smoP(data, label, 0.6, 0.001, 40)
print(b)
print(alphas[alphas>0])
print(np.shape(alphas[alphas>0]))
#可视化
label1 = np.where(label == 1)
label2 = np.where(label == -1)
label3 = np.where(alphas > 0)       #支持向量点
plt.scatter(data[label1,0],data[label1,1],marker='x', color='r',label='0', s=15)
plt.scatter(data[label2,0],data[label2,1],marker='o', color='b',label='0', s=15)
plt.scatter(data[label3,0],data[label3,1],marker='o', color='y',label='0', s=15)
#绘制超平面
x1 = np.arange(0,10,0.5)
label = np.mat(label); data = np.mat(data)
w = np.multiply(alphas,label.T).T*data
x2 = -(w[0,0]*x1 + b[0,0])/w[0,1]
plt.plot(x1,x2,color='black')
# print(np.shape(x1),np.shape(x2))
plt.show()
finish = clock()
print("运行时间："+str(finish - start)+"s")
    
    


