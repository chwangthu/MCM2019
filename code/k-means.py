# This file is used to cluster nodes
from numpy import *
import time
from math import radians, cos, sin, asin, sqrt
import matplotlib.pyplot as plt
 

def calculate_dis(vec1,
                  vec2):
    """
    Calculate the distance between two places
    """
    # print(vec1)
    # print(vec2)
    lat1 = vec1[0]
    lon1 = vec1[1]
    lat2 = vec2[0]
    lon2 = vec2[1]
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
 
    # haversine
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # the radius of earth
    return c * r * 1000 # return in meters

# calculate Euclidean distance
def euclDistance(vector1, vector2):
    return sqrt(sum(power(vector2 - vector1, 2)))
 
# init centroids with random samples
def initCentroids(dataSet, k):
	numSamples, dim = dataSet.shape
	centroids = zeros((k, dim))
	for i in range(k):
		index = int(random.uniform(0, numSamples))
		centroids[i, :] = dataSet[index, :]
	return centroids
 
# k-means cluster
def kmeans(dataSet, k):
    numSamples = dataSet.shape[0]
    # first column stores which cluster this sample belongs to,
    # second column stores the error between this sample and its centroid
    clusterAssment = mat(zeros((numSamples, 2)))
    res = zeros((numSamples, 1))
    clusterChanged = True

    ## step 1: init centroids
    centroids = initCentroids(dataSet, k)

    while clusterChanged:
        clusterChanged = False
        ## for each sample
        for i in range(numSamples):
            minDist  = 100000000000.0
            minIndex = 0
            ## for each centroid
            ## step 2: find the centroid who is closest
            for j in range(k):
                distance = calculate_dis(centroids[j, :], array(dataSet[i])[0]) #convert to array
                if distance < minDist:
                    minDist  = distance
                    # print("minDist", minDist)
                    minIndex = j
                    # print("minindex", minIndex)
            
            ## step 3: update its cluster
            if clusterAssment[i, 0] != minIndex:
                clusterChanged = True
                clusterAssment[i, :] = minIndex, minDist**2
                res[i] = minIndex

		## step 4: update centroids
        for j in range(k):
            pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
            centroids[j, :] = mean(pointsInCluster, axis = 0)
 
    print('Congratulations, cluster complete!')
    print(centroids)
    return centroids, clusterAssment, res
 
# show your cluster only available with 2-D data
def showCluster(dataSet, k, centroids, clusterAssment):
	numSamples, dim = dataSet.shape
	if dim != 2:
		print("Sorry! I can not draw because the dimension of your data is not 2!")
		return 1
 
	mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
	if k > len(mark):
		print("Sorry! Your k is too large! please contact Zouxy")
		return 1
 
	# draw all samples
	for i in range(numSamples):
		markIndex = int(clusterAssment[i, 0])
		plt.plot(dataSet[i, 0], dataSet[i, 1], mark[markIndex])
 
	mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
	# draw the centroids
	for i in range(k):
		plt.plot(centroids[i, 0], centroids[i, 1], mark[i], markersize = 12)
 
	plt.show()

## step 1: load data
print("step 1: load data...")
dataSet = []
county_id = []
file = open("../data/geography")
file.readline()
for line in file.readlines():
    lineArr = line.split()
    county_id.append(int(lineArr[1]))
    dataSet.append([float(lineArr[-2]), float(lineArr[-1])])
# print(dataSet[0])
# fileIn = open('../data/testSet.txt')
# for line in fileIn.readlines():
#     lineArr = line.split()
#     # print(lineArr[0], lineArr[1])
#     dataSet.append([float(lineArr[0]), float(lineArr[1])])
 
## step 2: clustering...
print("step 2: clustering...")
dataSet = mat(dataSet)
k = 10
centroids, clusterAssment, res = kmeans(dataSet, k)

for i in range(len(res)):
    print(i, county_id[i], int(res[i][0]))

## step 3: show the result
# print("step 3: show the result...")
# showCluster(dataSet, k, centroids, clusterAssment)

import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet("cluster")
worksheet.write(0, 1, "FIPS_Combined")
worksheet.write(0, 2, "cluster")
worksheet.write(0, 3, "latitude")
worksheet.write(0, 4, "longitude")
for i in range(len(res)):
    worksheet.write(i+1, 0, i)
    worksheet.write(i+1, 1, county_id[i])
    worksheet.write(i+1, 2, int(res[i][0]))
    worksheet.write(i+1, 3, centroids[int(res[i][0])][0])
    worksheet.write(i+1, 4, centroids[int(res[i][0])][1])
workbook.save("../data/cluster.xls")