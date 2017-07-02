from featuredobject import *
from math import sqrt

numberObjects = input("Number of ideal objects: ")

try:
	numberObjects = int(numberObjects)
except ValueError:
	print("Did not give an integer")
	exit(1)

if (numberObjects <= 0):
	print("Did not give a positive integer")
	exit(1)

numberFeat = input("Number of features per object: ")

try:
	numberFeat = int(numberFeat)
except ValueError:
	print("Did not give an integer")
	exit(1)

if (numberFeat <= 0):
	print("Did not give a positive integer")
	exit(1)

featNames = []
for i in range(numberFeat):
	name = input("Name of feature " + str(i + 1) + ":" )
	featNames.append(name)


objArray = []
for i in range(numberObjects):
	name = input("Name of object " + str(i + 1) + ":")
	obj = FeaturedObject(name)
	for j in range(numberFeat):
		val = input("Value for " + obj.name + ", feature " + featNames[j] + ":")
		try:
			val = float(val)
		except ValueError:
			print("Not a valid feature value, must be a real number")
			exit(1)
		obj.addVal(val)
	objArray.append(obj)


test = input("Do you want to test? (y to test, anything else to quit): ")
while (test == "y"):
	obj = FeaturedObject("test")
	for i in range(numberFeat):
		val = input("Value for testObject, feature " + featNames[i] + ": ")
		try:
			val = float(val)
		except ValueError:
			print("Not a valid feature value, must be a real number")
			exit(1)
		obj.addVal(val)

	arrayDist = []
	for i in range(numberObjects):
		dist = 0
		for j in range(numberFeat):
			dist += (obj.getVal(j) - objArray[i].getVal(j)) ** 2
		arrayDist.append(dist)

	minm = arrayDist[0]
	index = 0
	for i in range(1, numberObjects):
		if (arrayDist[i] < minm):
			minm = arrayDist[i]
			index = i

	print("It is most likely " + objArray[index].getName())
	print()
	test = input("Would you like to test again? (y to test, anything else to quit): ")
