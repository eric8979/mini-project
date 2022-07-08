import os

rfile = open('trimmedData/old_2015_all.txt', 'r')
wfile = open('trimmedData/2015_all.txt', 'w')

newFileData = "" 
for line in rfile:
    rowList = line.strip().split(',')
    rowList.pop(-1)
    newRow = ','.join(rowList) + "\n"
    newFileData = newFileData + newRow

wfile.write(newFileData)

rfile.close()
wfile.close()

