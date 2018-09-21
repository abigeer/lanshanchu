#coding = utf-8
'''
Created on 2018年8月11日

@author: 89146

svm的SMO算法实现
'''
import numpy as np
import matplotlib.pyplot as plt
import random

#简化版SMO
#辅助函数
def loadDataSet(filename):  #读取数据集函数
    dataMat = []        #数据矩阵
    labelMat = []       #数据对应的类别
    fr = open(filename)
    for line in fr.readlines():     #逐行读取文件
        lineArr = line.strip().split('\t')      #去掉两边空格，同时按空格拆分字符串
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

def selectJrand(i, m):       #随机选择alpha(smo算法对应的内层循环)
    """
    i:第一个alpha下标
    m：所有alpha数目
    只要函数值不等于输入值i，函数就会进行随机选择
    """
    #相当于第二个参数选择，这里进行了简化
    j = i
    while(j == i):
        j = int(random.uniform(0,m))        #random模块下的uniform函数用于随机产生一个实数
    return j

def clipAlpha(aj, H, L):         #对沿着约束方向aj的解进行剪辑
    """
    aj:SMO算法选择的第二个变量
    H:在约束方向解的上界
    L:在约束方向解的下界
    L < aj < H
    """
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj
    
#简化版SMO实现
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
     """
     dataMatIn:数据集
     classLabels:类别标签
     C:常数C
     toler:容错率
     maxIter:最大外循环次数
     """  
     #将dataMatIn转换成矩阵，将classLabels转换成列向量,数据和标签一一对应
     dataMatrix  = np.mat(dataMatIn); labelMat = np.mat(classLabels).transpose()
     #b是分离超平面函数的截距，m，n分别是数据的个数和维数
     b = 0; m,n = np.shape(dataMatrix)
     #初始化原始问题对偶问题的解向量alpha为零
     alphas = np.mat(np.zeros((m,1)))
     iter = 0 #iter用于记录一次优化中alpha没有被优化的个数，alpha都没有被优化则加1
     while(iter < maxIter):
         alphaPairsChanged = 0   #用于记录alpha值是否被优化
         for i in range(m):  #SMO中称为外循环用于选择本次优化的第一个alpha（这里做了简化）
             #g_x是分离超平面方程，gxi是svm对第i个数据的预测
             #g_x = sum(ai*yi*K(xi,x))+b,在这里不使用核函数,直接xi和x内积（xi,x）
             #multiply表示向量元素对应相乘
             gXi = float(np.multiply(alphas,labelMat).T\
                         *(dataMatrix*dataMatrix[i,:].T))+b
             #计算预测误差（gxi是对xi进行预测值）
             Ei = gXi - float(labelMat[i])
             if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or \
                ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):       #用于检验是否满足kkt条件
                 #如果在toler范围内检测违反kkt条件则选择该alpha作为第一个alpha进行优化
                 j = selectJrand(i, m)       #内层循环，使用随机方式选择第二个优化的alpha（简化）
                 gXj = float(np.multiply(alphas, labelMat).T\
                             *(dataMatrix*dataMatrix[j,:].T)) + b
                 Ej = gXj - float(labelMat[j])
                 #记录未优化的alpha的旧值，即alphaOld,使用copy()函数这样不会进行值引用
                 alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy()
                 #计算剪辑alpha的界:
                 #1.yi != yj, L = max(0,alphaJold-alphaIold),H = min(C,C+alphaJold-alphaIold)
                 #2.yi = yj, L = max(0,alphaJold+alphaIold-C), H = min(C,alphaJold-alphaIold)
                 if (labelMat[i] != labelMat[j]):
                     L = max(0,alphas[j] - alphas[i])
                     H = min(C, C+alphas[j] - alphas[i])
                 else:
                     L = max(0,alphas[j] + alphas[i] -C)
                     H = min(C, alphas[j] + alphas[i])
                 if L==H: print ("L==H"); continue
                 #开始计算剪辑优化alpha：alphaJnew_unc = alphaJold + yj(Ei-Ej)/eta
                 #eta = kii+ kjj-2kij=||theta(xi)-theta(xj)||^2
                 #计算eta的负值,eta本身一定是正数
                 eta = 2.0*dataMatrix[i,:]*dataMatrix[j,:].T\
                          - dataMatrix[i,:]*dataMatrix[i,:].T \
                          - dataMatrix[j,:]*dataMatrix[j,:].T
                 if (eta > 0 ):
                     print("eta<0"); continue
                 alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                 #对优化的alpha进行剪辑
                 alphas[j] = clipAlpha(alphas[j], H, L)
                 #设置更新条件
                 if(abs(alphas[j] - alphaJold) < 0.00001):
                     print("j not moving enough"); continue
                 #优化alphai
                 alphas[i] = alphaIold + labelMat[i]*labelMat[j]*(alphaJold - alphas[j])               #这里发生错误，按照公式出现错误应该是alphaold+
                                                                 
#                  alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])
                 b1 = b - Ei - labelMat[i]*dataMatrix[i,:]*dataMatrix[i,:].T\
                          *(alphas[i] - alphaIold) - labelMat[j]*dataMatrix[j,:]\
                          *dataMatrix[i,:].T*(alphas[j] - alphaJold)
                 b2 = b - Ej - labelMat[i]*dataMatrix[i,:]*dataMatrix[j,:].T\
                          *(alphas[i] - alphaIold) - labelMat[j]*dataMatrix[j,:]\
                          *dataMatrix[j,:].T*(alphas[j] - alphaJold)
                 if (0 < alphas[j]) and (alphas[j] < C): b = b1
                 elif (0 < alphas[i]) and (alphas[i] < C): b = b2
                 else: b = (b1+b2)/2.0
                 alphaPairsChanged += 1
                 print ("iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged))
         if(alphaPairsChanged == 0): iter +=1
         else: iter = 0
         print("iteration number: %d" % iter)
     return b, alphas
                 

# def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
#     dataMatrix = np.mat(dataMatIn); labelMat = np.mat(classLabels).transpose()
#     b = 0; m,n = np.shape(dataMatrix)
#     alphas = np.mat(np.zeros((m,1)))
#     iter = 0
#     while (iter < maxIter):
#         alphaPairsChanged = 0
#         for i in range(m):
#             fXi = float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[i,:].T)) + b
#             Ei = fXi - float(labelMat[i])#if checks if an example violates KKT conditions
#             if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
#                 j = selectJrand(i,m)
#                 fXj = float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
#                 Ej = fXj - float(labelMat[j])
#                 alphaIold = alphas[i].copy(); alphaJold = alphas[j].copy();
#                 if (labelMat[i] != labelMat[j]):
#                     L = max(0, alphas[j] - alphas[i])
#                     H = min(C, C + alphas[j] - alphas[i])
#                 else:
#                     L = max(0, alphas[j] + alphas[i] - C)
#                     H = min(C, alphas[j] + alphas[i])
#                 if L==H: print( "L==H"); continue
#                 eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - dataMatrix[i,:]*dataMatrix[i,:].T - dataMatrix[j,:]*dataMatrix[j,:].T
#                 if eta >= 0: print ("eta>=0"); continue
#                 alphas[j] -= labelMat[j]*(Ei - Ej)/eta
#                 alphas[j] = clipAlpha(alphas[j],H,L)
#                 if (abs(alphas[j] - alphaJold) < 0.00001): print( "j not moving enough"); continue
#                 alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])#update i by the same amount as j
#                                                                         #the update is in the oppostie direction
#                 b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
#                 b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
#                 if (0 < alphas[i]) and (C > alphas[i]): b = b1
#                 elif (0 < alphas[j]) and (C > alphas[j]): b = b2
#                 else: b = (b1 + b2)/2.0
#                 alphaPairsChanged += 1
#                 print ("iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged))
#         if (alphaPairsChanged == 0): iter += 1
#         else: iter = 0
#         print ("iteration number: %d" % iter)
#     return b,alphas


#可视化                     
data, label = loadDataSet("testSet.txt")   #都是tuple
#测试
b, alphas = smoSimple(data, label, 0.6, 0.001, 40)
print(b)
print(alphas[alphas>0])
print(np.shape(alphas[alphas>0]))
label3 = np.where(alphas > 0)

data = np.array(data)
label = np.array(label)
label1 = np.where(label == 1)  #返回label为1的下标
label2 = np.where(label == -1)
plt.scatter(data[label1,0],data[label1,1],marker='x', color='r',label='0', s=15)
plt.scatter(data[label2,0],data[label2,1],marker='o', color='b',label='0', s=15)
plt.scatter(data[label3,0],data[label3,1],marker='o', color='y',label='0', s=15)
# print(data[label1,0])               
plt.show()            
                
            
        
    
    
    
    


if __name__ == '__main__':
    pass
    
    
    
    
    
    