from random import random
# Convert string column to integer
def str_column_to_int(dataset, column):
	class_values = [row[column] for row in dataset]
	unique = set(class_values)
	lookup = dict()
	for i, value in enumerate(unique):
		lookup[value] = i
	for row in dataset:
		row[column] = lookup[row[column]]
	return lookup


def dataSetToArray(dataset, rowSize):
    rowLst = []
    for i in range (0, len(dataset)):
        colLst = []
        for j in range (0,rowSize):
            if j == rowSize-1 :
                colLst.append(int(dataset.iloc[i][j]))
                continue
            colLst.append(dataset.iloc[i][j])
        rowLst.append(colLst)
    return rowLst

arr = [random() for i in range(0,3)]
print (arr)