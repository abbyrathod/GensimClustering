import os
import random
from gensim.models import KeyedVectors
import gensim.downloader as api
from nltk.corpus import stopwords
import numpy as np
stop_words = set(stopwords.words("english"))
with open("TextToString.txt","r") as f:
	data = f.readlines()
data = list(dict.fromkeys(data))
clusters = [0]*10
i = 0
while i<10 :
	RandGenerated = random.randint(1,len(data))
	if RandGenerated in clusters:
		i = i-1
	else :
		clusters[i] = RandGenerated
	i = i+1	
clusters = sorted(clusters)
print(clusters)
model = KeyedVectors.load('newmodel')
def countDistance(sentenceConst, WholeGroup):
	distance = [0]*len(WholeGroup)
	sentenceFirstString = str(sentenceConst)
	sentenceFirstString = sentenceFirstString.lower().split()
	sentenceFirstString = [w for w in sentenceFirstString if w not in stop_words]
	i = 0
	for sentence in WholeGroup:
		sentenceTwoString = str(sentence)
		sentenceTwoString = sentenceTwoString.lower().split()
		sentenceTwoString = [w for w in sentenceTwoString if w not in stop_words]
		distance[i] = model.wmdistance(sentenceFirstString, sentenceTwoString)
		i = i+1		
	return distance
FinalCluster = []
clusterOne = countDistance(data[clusters[0]],data)
clusterTwo = countDistance(data[clusters[1]],data)
clusterThree = countDistance(data[clusters[2]],data)
clusterFour = countDistance(data[clusters[3]],data)
clusterFive = countDistance(data[clusters[4]],data)
clusterSix = countDistance(data[clusters[5]],data)
clusterSeven = countDistance(data[clusters[6]],data)
clusterEight = countDistance(data[clusters[7]],data)
clusterNine = countDistance(data[clusters[8]],data)
clusterTen = countDistance(data[clusters[9]],data)
FinalCluster = [clusterOne,clusterTwo,clusterThree,clusterFour,clusterFive,clusterSix,clusterSeven,clusterEight,clusterNine,clusterTen]
#In FinalCluster, FinalCluster[clusterNumber][sentenceNumber]
SentenceDistance = [0]*len(data)
Midlevel = list(map(list,zip(*FinalCluster)))
ClusteringInfo = [0]*len(data)
output = np.argsort(Midlevel[0])
for i in range(0,len(data)):
	output = np.argsort(Midlevel[i]).tolist()
	ClusteringInfo[i] = output[0]
	output.clear()
j=0
FinalClusterIndexes = [[] for i in range(10)]
for i in range(0,len(ClusteringInfo)):
	if ClusteringInfo[i] == 0:
		FinalClusterIndexes[0].append(i)
	elif ClusteringInfo[i] == 1:
		FinalClusterIndexes[1].append(i)
	elif ClusteringInfo[i] == 2:
		FinalClusterIndexes[2].append(i)
	elif ClusteringInfo[i] == 3:
		FinalClusterIndexes[3].append(i)
	elif ClusteringInfo[i] == 4:
		FinalClusterIndexes[4].append(i)
	elif ClusteringInfo[i] == 5:
		FinalClusterIndexes[5].append(i)
	elif ClusteringInfo[i] == 6:
		FinalClusterIndexes[6].append(i)
	elif ClusteringInfo[i] == 7:
		FinalClusterIndexes[7].append(i)
	elif ClusteringInfo[i] == 8:
		FinalClusterIndexes[8].append(i)
	elif ClusteringInfo[i] == 9:
		FinalClusterIndexes[9].append(i)
	j = j+1
print(FinalCluster)
print(FinalClusterIndexes) #In FinalClusterIndexes, FinalClusterIndexes[clusterNumber][SentenceNumber]
def ClusterAverages(FinalClusterIndexes,FinalCluster):
	ClusterMean = [i for i in range(0,10)]
	for i in range(0,10):
		SumOfCluster = 0
		for j in range(0,len(FinalClusterIndexes[i])):
			SumOfCluster = SumOfCluster+FinalCluster[i][FinalClusterIndexes[i][j]]
		if len(FinalClusterIndexes[i])==0 :
			ClusterMean[i] = SumOfCluster/1
		else:
			ClusterMean[i] = SumOfCluster/len(FinalClusterIndexes[i])
	return ClusterMean
ClusterAverageReturn = ClusterAverages(FinalClusterIndexes,FinalCluster)
print(ClusterAverageReturn)	