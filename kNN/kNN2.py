#coding=utf-8
'''
Created on 2018年8月19日

@author: 89146
'''
import sys
import numpy as np
import matplotlib.pyplot as plt


#读取数据
def file2matrix(filename):
    fr = open(filename)
    returnMat = []          #样本数据矩阵
#     classlabel = []         #样本类型
    for line in fr.readlines():
        line = line.strip().split('\t')
        returnMat.append([float(line[0]),float(line[1]),float(line[2]),float(line[3])])
    return returnMat

#归一化数据
def autoNorm(data):
    #将data数据和类别拆分
    data,label = np.split(data,[3],axis=1)
    minVals = data.min(0)     #data各列的最大值
    maxVals = data.max(0)       #data各列的最小值
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(data))
    m = data.shape[0]
    #tile函数将变量内容复制成输入矩阵同样大小的矩阵
    normDataSet = data - np.tile(minVals,(m,1))        
    normDataSet = normDataSet/np.tile(ranges,(m,1))
    #拼接
    normDataSet = np.hstack((normDataSet,label))
    return normDataSet
    

#构建kdTree将特征空间划分
class kd_tree:
    """
    定义结点
    value:节点值
    left:左子树
    right:右子树
    """
    def __init__(self, value):
        self.value = value
        self.dimension = None       #记录划分的维数
        self.left = None
        self.right = None
    
    def setValue(self, value):
        self.value = value
    
    #类似Java的toString()方法
    def __str__(self):
        return str(self.value)

#将数据划分构造平衡kd树，这里函数设计可以不用给root，在函数内部构造返回即可
def creat_kdTree(dataIn, k, root, deep):
    """
    data:要划分的特征空间（即数据集）
    k:表示要选择k个近邻
    root:树的根结点
    deep:结点的深度
    """
    #选择x(l)(即为第l个特征)为坐标轴进行划分，找到x(l)的中位数进行划分
#     x_L = data[:,deep%k]        #这里选取第L个特征的所有数据组成一个列表
    #获取特征值中位数，这里是难点如果numpy没有提供的话
    
    if(dataIn.shape[0]>0):      #如果该区域还有实例数据就继续
        dataIn = dataIn[dataIn[:,int(deep%k)].argsort()]       #numpy的array按照某列进行排序
        data1 = None; data2 = None
        #拿取根据xL排序的中位数的数据作为该子树根结点的value
        if(dataIn.shape[0]%2 == 0):     #该数据集有偶数个数据
            mid = int(dataIn.shape[0]/2)
#             print("偶数"+str(dataIn.shape))
#             print(data[mid,:])
            root = kd_tree(dataIn[mid,:])
            root.dimension = deep%k
            dataIn = np.delete(dataIn,mid, axis = 0)
            data1,data2 = np.split(dataIn,[mid], axis=0) 
#             np.delete(data2, 0, axis = 0)     #mid行元素分到data2中，删除放到根结点中
        elif(dataIn.shape[0]%2 == 1):
            mid = int((dataIn.shape[0]+1)/2 - 1)        #这里出现递归溢出，当shape为(1,4)时出现，原因是np.delete时没有赋值给dataIn
#             print("奇数"+str(dataIn.shape))
            root = kd_tree(dataIn[mid,:])
            root.dimension = deep%k
            dataIn = np.delete(dataIn,mid, axis = 0)
            data1,data2 = np.split(dataIn,[mid], axis=0) 
#             np.delete(data1, mid, axis = 0)     #mid行元素分到data1中，删除放到根结点中
        #深度加一
        deep+=1
#         print(deep)
        #递归构造子树
        #这里犯了严重错误，递归调用是将root传递进去，造成程序混乱，应该给None
        root.left = creat_kdTree(data1, k, None, deep)
        root.right = creat_kdTree(data2, k, None, deep)
    return root


#前序遍历kd树
def preorder(kd_tree,i):
    print(str(kd_tree.value)+" :"+str(kd_tree.dimension)+":"+str(i))
    if kd_tree.left != None:
        preorder(kd_tree.left,i+1)
    if kd_tree.right != None:
        preorder(kd_tree.right,i+1)

  
 
#k近邻搜索
def findKNode(kdNode, closestPoints, x, k):
    """
    k近邻搜索，kdNode是要搜索的kd树
    closestPoints:是要搜索的k近邻点集合,将minDis放入closestPoints最后一列合并
    x：预测实例
    minDis：是最近距离
    k:是选择k个近邻
    """
    if kdNode == None:
        return
    #计算欧式距离
    curDis = (sum((kdNode.value[0:3]-x[0:3])**2))**0.5
    #这里相对与最近邻判断做一些改变，循环判断
#     dataIn = dataIn[dataIn[:,int(deep%k)].argsort()]
    #将closestPoints按照minDis列排序,这里存在一个问题，排序后返回一个新对象
    #不能将其直接赋值给closestPoints
    tempPoints = closestPoints[closestPoints[:,4].argsort()]
    for i in range(k):
        closestPoints[i] = tempPoints[i]
    #每次取最后一行元素操作
    if closestPoints[k-1][4] >=10000  or closestPoints[k-1][4] > curDis:
        closestPoints[k-1][4] = curDis
        #遍历修改找到的实例
#         for i in range(4):
#             closestPoints[k-1][i] = kdNode.value[i]
        closestPoints[k-1,0:4] = kdNode.value 
        
    #递归搜索叶结点
    if kdNode.value[kdNode.dimension] >= x[kdNode.dimension]:
        findKNode(kdNode.left, closestPoints, x, k)
    else:
        findKNode(kdNode.right, closestPoints, x, k)
    #计算测试点和分隔超平面的距离，如果相交进入另一个叶节点重复
    rang = abs(x[kdNode.dimension] - kdNode.value[kdNode.dimension])
    if rang > closestPoints[k-1][4]:
        return
    if kdNode.value[kdNode.dimension] >= x[kdNode.dimension]:
        findKNode(kdNode.right, closestPoints, x, k)
    else:
        findKNode(kdNode.left, closestPoints, x, k)  
    
def change(a):
    a[0][0] = 10
  
        
data = file2matrix("datingTestSet2.txt")
data = np.array(data)
# data = data[data[:,3].argsort()]
# print(data)
#归一化测试
normDataSet = autoNorm(data)
# print(normDataSet)

#树的构造测试
sys.setrecursionlimit(10000)            #设置递归深度为10000
#将数据分成测试数据和训练数据
trainSet,testSet = np.split(normDataSet,[900],axis=0)       #拆分训练集和测试集
kdTree = creat_kdTree(trainSet, 3, None, 0)
newData = testSet[1,0:3]
print("预测实例点："+str(newData))
closestPoints = np.zeros((3,5))         #初始化参数
closestPoints[:,4] = 10000.0               #给minDis列赋值
# closestPoints = list([[0,0,0,0,10000.0],
#                       [0,0,0,0,10000.0],
#                       [0,0,0,0,10000.0]])
findKNode(kdTree, closestPoints, newData, 3)
print("k近邻结果："+str(closestPoints))

# print(data.max(0))
# preorder(kdTree,1)
# print(data[500,:])

# data, label = file2matrix("datingTestSet2.txt")
# data = np.array(data);label = np.array(label)


# fig = plt.figure()          #画布
# ax = fig.add_subplot(111)           #画窗
# ax.scatter(data[:,0],data[:,1])
# ax.scatter(data[:,1], data[:,2], 1.0*label, 1.0*label)
# plt.show()
# print(data.shape[0])
# print(label)






