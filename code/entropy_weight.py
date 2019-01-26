# -*- coding:utf-8

import numpy as np
import pandas as pd

li=[[100,90,100,84,90,100,100,100,100],
    [100,100,78.6,100,90,100,100,100,100],
    [75,100,85.7,100,90,100,100,100,100],
    [100,100,78.6,100,90,100,94.4,100,100],
    [100,90,100,100,100,90,100,100,80],
    [100,100,100,100,90,100,100,85.7,100],
    [100, 100 ,78.6, 100 ,90 , 100, 55.6, 100, 100],
    [87.5,100 ,85.7 ,   100 ,100 ,100, 100 ,100 ,100],
    [100 ,100, 92.9  ,  100 ,80 , 100 ,100 ,100 ,100],
    [100,90 ,100 ,100, 100, 100, 100, 100, 100],
    [100,100 ,92.9 ,   100, 90 , 100, 100 ,100 ,100]]

def entropy(dataset):
    n, k = np.shape(dataset)
    maximum = np.max(dataset, axis=0) #minimum in column
    minimum = np.min(dataset, axis=0)
    data = (dataset - minimum) * 1.0 / (maximum - minimum)
    col_sum = np.sum(data, axis=0)
    data = data / col_sum
    # print(data)
    # print(col_sum)
    a = data * 1.0
    a[np.where(data==0)]=0.0001
    e = (-1.0/np.log(n))*np.sum(data*np.log(a), axis=0) # e 1*k
    w = (1 - e) / np.sum(1 - e)
    recodes = np.sum(dataset * w, axis=1)
    return recodes

if __name__ == "__main__":
    li = np.array(li)
    entropy(li)