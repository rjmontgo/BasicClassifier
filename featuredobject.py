class FeaturedObject:

	def __init__(self, name):
		self.vals = []
		self.name = name

	
	def addVal(self, val):
		self.vals.append(val)

	def getVal(self, index):
		return self.vals[index]

	def getName(self):
		return self.name