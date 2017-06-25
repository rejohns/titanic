"""
titanic--sklearn-svm.py		Robert Johns	June 25, 2017
Basic implementation of sklearn's SVC (support vector classifier) to train a classifier
for Kaggle's titanic contest.

features used:
-Survived
-Pclass
-Sex
-SibSp
-Parch

features not used:
-PassengerId
-Name
-Age
-Ticket
-Fare
-Cabin
-Embarked
"""

#todo: clean up loops, do all in one go if possible
#todo: find a way to incorporate cabin data into classifier. give numbers for cabins

import csv
from sklearn.svm import SVC

train = "train.csv"
test = "test.csv"
results = "gender_submission.csv"

#get training data
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

#build train data matrix: convert to ints where appropriate
#todo: combine loops to remove reiteration
for row in trainData:
	row[1] = int(row[1])
	row[2] = int(row[2])
	if row[4] == "male":
		row[4] = 0
	elif row[4] == 'female':
		row[4] = 1 
	else:
		print("AAAAAH")
	row[6] = int(row[6])
	row[7] = int(row[7])
	
#build train data matrix: split into classes vector and feature matrix
supportVectors = []
classes = []
for row in trainData:
	temp = []
	classes.append(row[1])
	temp.append(row[2])
	temp.append(row[4])
	temp.append(row[6])
	temp.append(row[7])
	supportVectors.append(temp)

#run classifier
clf = SVC()
clf.fit(supportVectors, classes)

#get test data
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

#format test data
testMatrix = []
for row in testData:
	temp = []
	temp.append(int(row[1]))
	if row[3] == "male":
		temp.append(0)
	elif row[3] == "female":
		temp.append(1)
	else:
		print("FFFFFFFUUUUU")
	temp.append(int(row[5]))
	temp.append(int(row[6]))
	testMatrix.append(temp)

#run predictor
predictions = clf.predict(testMatrix)

#get given results
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

#calculate and percentage correct, false positive, false negative 
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
