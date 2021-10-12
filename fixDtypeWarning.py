def getColumns(file):
    import csv
    with open(file) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            break
    return row

def makeTypeDict(keysList , valueList):
    dtypeDict = { keysList[val]: valueList[val] for val in range(len(keysList))}
    return dtypeDict
