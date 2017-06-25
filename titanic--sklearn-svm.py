import csv
from sklearn.svm import SVC

train = "train.csv"
test = "test.csv"
results = "gender_submission.csv"

file = open(train)

reader = csv.reader(file)

trainData = []

for row in reader:
	rowData = []
	for item in row:
		rowData.append(item)
	trainData.append(row)
trainData.remove(trainData[0])

file.close()

#todo: combine loops to remove reiteration
for row in trainData:
	#row[0] = int(row[0])
	row[1] = int(row[1])
	row[2] = int(row[2])
	if row[4] == "male":
		row[4] = 0
	elif row[4] == 'female':
		row[4] = 1 
	else:
		print("AAAAAH")
	if len(row[5]) > 0:
		row[5] = float(row[5])
	else:
		row[5] = -1
	row[6] = int(row[6])
	row[7] = int(row[7])
	
supportVectors = []
classes = []
for row in trainData:
	temp = []
	#temp.append(row[0])
	classes.append(row[1])
	temp.append(row[2])
	temp.append(row[4])
	#temp.append(row[5])
	temp.append(row[6])
	temp.append(row[7])
	supportVectors.append(temp)

clf = SVC()
clf.fit(supportVectors, classes)

file = open(test)

reader = csv.reader(file)

testData = []

for row in reader:
	rowData = []
	for item in row:
		rowData.append(item)
	testData.append(row)
testData.remove(testData[0])

file.close()

testMatrix = []

for row in testData:
	temp = []
	#temp.append(int(row[0]))
	temp.append(int(row[1]))
	if row[3] == "male":
		temp.append(0)
	elif row[3] == "female":
		temp.append(1)
	else:
		print("FFFFFFFUUUUU")
	"""
	if len(row[4]) > 0:	
		temp.append(float(row[4]))
	else:
		temp.append(-1)
	"""
	temp.append(int(row[5]))
	temp.append(int(row[6]))
	testMatrix.append(temp)
	
predictions = clf.predict(testMatrix)

file = open(results)

reader = csv.reader(file)

realResults = []

for row in reader:
	rowData = []
	for item in row:
		rowData.append(item)
	realResults.append(rowData)
realResults.remove(realResults[0])

file.close()

correct = 0
falsePos = 0
falseNeg = 0

for i in range(len(realResults)):
	predi = int(predictions[i])
	rri = int(realResults[i][1])
	if predi == rri:
		correct += 1
	elif predi > rri:
		falsePos += 1
	elif predi < rri:
		falseNeg += 1
	else:
		print ("HUH?")

print("correct:\t", correct * 100 / len(realResults))
print("false pos:\t", falsePos * 100 / len(realResults))
print("false neg:\t", falseNeg * 100 / len(realResults))