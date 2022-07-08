# This Python script is for creating trimmed data file
import os

# Create list of data files
# dataList - data files without double quotes
# datadqList - data files with double quotes
dataDir = os.path.join(os.getcwd() + "/data")
dataList = os.listdir(dataDir)
dataList.remove('with_dq')

data_dq_Dir = os.path.join(os.getcwd() + "/data/with_dq")
datadqList = os.listdir(data_dq_Dir)

# 사용년월, 노선번호, 노선명, 버스정류장ARS번호, 역명, 00시~23시승차총승객수
# metadata (e.g. 사용년월, 노선번호, 역명...) couldn't be used due to wrongly formatted raw data
# Should create trimmedData directory first!

# Trim Data (without_dq) dataList
for fileName in dataList:
    print('Open file: ' + fileName + "...")
    file = open('data/' + fileName, 'r')
    print('Create file: ' + fileName + " in trimmedData dir...")
    trimmedfile = open('trimmedData/' + fileName, 'w')

    print("Processing data...")
    newData = ""
    newRow = None
    for line in file:
        row = []
        rawRow = line.strip().split(',')
        # Trim first row
        if rawRow[0] == '사용년월':
            continue
        # metadata
        row.append(rawRow[0])
        row.append(rawRow[1])
        row.append(rawRow[2])
        row.append(rawRow[4])
        row.append(rawRow[5])
        # data
        for time in rawRow[6:-1]:
            row.append(time)
        newRow = ','.join(row) + '\n'
        newData = newData + newRow
    print("Processing data done...")
    if newData == None:
        continue
    trimmedfile.write(newData)
    file.close()
    print("Data write to new file done...")


# Trim Data (with_dq) datadqList
for fileName in datadqList:
    print('Open file: ' + fileName + "...")
    file = open('data/with_dq/' + fileName, 'r')
    print('Create file: ' + fileName + " in trimmedData dir...")
    trimmedfile = open('trimmedData/' + fileName, 'w')

    print("Processing data...")
    newData = ""
    newRow = None
    for line in file:
        row = []
        rawRow = line.strip().split('","')
        # Trim first row
        if rawRow[0] == '"사용년월':
            continue
        # metadata
        row.append(rawRow[0][1:]) # [1:] for format '"202201' -> '202201'
        row.append(rawRow[1])
        row.append(rawRow[2])
        row.append(rawRow[4])
        row.append(rawRow[5])
        # data
        for time in rawRow[6:-1]:
            row.append(time)
        newRow = ','.join(row) + '\n'
        newData = newData + newRow
    print("Processing data done...")
    if newData == None:
        continue
    trimmedfile.write(newData)
    file.close()
    trimmedfile.close()
    print("Data write to new file done...")

print('All data written successfully')


