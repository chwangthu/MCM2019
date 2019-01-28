# -*- coding:utf-8
import numpy as np
import pandas as pd

def entropy(dataset):
    n, k = np.shape(dataset)
    maximum = np.max(dataset, axis=0) #minimum in column
    minimum = np.min(dataset, axis=0)
    data = (dataset - minimum) * 1.0 / (maximum - minimum)
    col_sum = np.sum(data, axis=0)
    data = data / col_sum
    a = data * 1.0
    a[np.where(data==0)]=0.0001
    e = (-1.0/np.log(n))*np.sum(data*np.log(a), axis=0) # e 1*k
    w = (1 - e) / np.sum(1 - e)
    recodes = np.sum(dataset * w, axis=1)
    return recodes

if __name__ == "__main__":
    li = np.array(li)
    entropy(li)