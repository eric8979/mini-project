import os
import csv

dataDir = os.path.join(os.getcwd() + "/data")
dataFileList = os.listdir(dataDir)
for i in range(len(dataFileList)):
    dataFileList[i] = os.path.join("data/" + dataFileList[i])

file = open('data/2022_04.txt', 'r')
for line in file:
    print(line)

