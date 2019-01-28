import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA



def meanX(dataX):
    return np.mean(dataX,axis=0)#axis=0表示依照列来求均值。假设输入list,则axis=1

def pca(XMat, k):
    average = meanX(XMat) 
    m, n = np.shape(XMat)
    data_adjust = []
    avgs = np.tile(average, (m, 1))
    data_adjust = XMat - avgs
    covX = np.cov(data_adjust.T)   #计算协方差矩阵
    featValue, featVec=  np.linalg.eig(covX)  #求解协方差矩阵的特征值和特征向量
    # print(featVec.shape)
    index = np.argsort(-featValue) #依照featValue进行从大到小排序
    finalData = []
    if k > n:
        print("k must lower than feature number")
        return
    else:
        #注意特征向量时列向量。而numpy的二维矩阵(数组)a[m][n]中，a[1]表示第1行值
        selectVec = np.matrix(featVec.T[index[:k]]) # n * k
        finalData = data_adjust * selectVec.T # m * k
        print(finalData.shape, selectVec.shape)
        reconData = (finalData * selectVec) + average # k  
    print(finalData.shape)
    print(reconData.shape)
    return finalData, reconData

def loaddata(datafile):
    # return np.array(pd.read_excel("../data/cluster_entropy.xlsx"))[:, 4:]
    return np.array(pd.read_csv(datafile,sep="\t",header=-1)).astype(np.float)

def main():    
    # datafile = "data1.txt"

    # XMat = loaddata(datafile)
    # print(XMat)
    # k = 3
    # finalData, reconMat = pca(XMat, k)
    k = 3
    dataframe = pd.read_excel("../data/cluster_entropy.xlsx")
    for i in range(10):
        factors = dataframe[dataframe["cluster"].isin([i])].iloc[:, 4:]
        factors = np.array(factors)
        pca=PCA(n_components=k)
        pca.fit(factors)
        result = pca.transform(factors)
        dg = pd.DataFrame()
        for j in range(k):
            dg[j] = result[:, j]
        dg.to_excel("../data/main/" + str(i) + ".xlsx")

if __name__ == "__main__":
    main()
    # finalData, reconMat = main()
    # k = 3
    # dg = pd.DataFrame()
    # print(finalData[0])
    # for i in range(k):
    #     dg[i] = np.array(finalData)[:, i]
    # dg.to_excel("../data/2010-main.xlsx")
    # plotBestFit(finalData, reconMat)