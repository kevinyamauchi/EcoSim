import numpy as np
import random


class EcoSim(object):

	def __init__(self, numRows, numColumns, initPop, maxSeedPerNode = 1):

		
		# Save the ecoysystem parameters
		self._numRows = numRows
		self._numColumns = numColumns
		self._initPop = initPop
		self._maxSeedPerNode = maxSeedPerNode
		self._stepNum = 0

		self._numParams = 3


		# Get a list of the nodes to get an animal (random draw, no replacement)
		allNodes = range(self._numRows * self._numColumns)
		nodesToSeed = random.sample(allNodes, self._initPop)

		# Initialize the world
		self._worldHistory = [[{'index': x, 'time': 0, 'age': self._initialAge(),
			'row': self._getRow(nodesToSeed[x]),
			'col': self._getCol(nodesToSeed[x])} for x in range(self._initPop)],]


		# Display the ecosystem
		self.show()

	def step(self):
		
		self._stepNum += 1
		print("Step " + str(self._stepNum))

		# Make the matrix for the next step
		self._worldHistory += (self._worldHistory[-1],)

		# Generate a list of indices in random order to make moves
		animalIndices = range(len(self._worldHistory[-1]))
		random.shuffle(animalIndices)


		# Iterate through the animals
		for ind in animalIndices:
			
			roll = random.randint(0, 3)

			if(roll == 0):
				self._moveUp(ind)

			elif(roll == 1):
				self._moveRight(ind)

			elif(roll == 2):
				self._moveDown(ind)

			elif(roll == 3):
				self._moveLeft(ind)


		self.show()


	def __call__(self):

		self.step() 



	# Method to print the current ecosystem. Numbers at the nodes 
	# are the numer of individuals at that node
	def show(self):

		currentState = np.zeros((self._numRows, self._numColumns), 
			dtype = np.int)

		for animal in self._worldHistory[-1]:

			row = animal['row']
			col = animal['col']

			currentState[row, col] = 1

		for row in range(self._numRows - 1):

			# Print a row of organisms
			for col in range(self._numColumns - 1):

				print(currentState[row, col]),
				print("-"),

			print(currentState[row, -1])

			# Print the vertial links
			for col in range(self._numColumns - 1):
				print("|  "),

			print("|")

		# Print the last row of organisms
		for col in range(self._numColumns - 1):

			print(currentState[-1, col]),
			print("-"),

		print(currentState[-1, -1])


	# Method to get the row number from an index
	def _getRow(self, index):

		return index // self._numColumns

	# Method to get the col number from an index
	def _getCol(self, index):

		return index % self._numColumns

	# Method to set intiial age of an organism. All organisms are newborn for now.
	# Can add function later.
	def _initialAge(self):

		return 0

	# Method to check if any of the animals in the current step are in 
	# the specified position (returns True if occupied)
	def _isOccupied(self, row, col):

		occupied  = False

		for animal in self._worldHistory[-1]:

			if ((animal['row'] == row) & (animal['col'] == col)):

				occupied = True

				break


		return occupied

	# Method to move up
	def _moveUp(self, animalIndex):

		newRow = self._worldHistory[-1][animalIndex]['row'] - 1

		newCol = self._worldHistory[-1][animalIndex]['col']

		# Don't move and return false if in the top row already
		if(newRow < 0):
			return False

		# Don't move and return false if the space is occupied
		elif(self._isOccupied(newRow, newCol)):
			return False

		# Move up if no reason not to
		else:

			self._worldHistory[-1][animalIndex]['row'] = newRow
			self._worldHistory[-1][animalIndex]['col'] = newCol

			return True

	# Method to move down
	def _moveDown(self, animalIndex):

		newRow = self._worldHistory[-1][animalIndex]['row'] + 1

		newCol = self._worldHistory[-1][animalIndex]['col']

		# Don't move and return false if in the bottom row already
		if(newRow > (self._numRows - 1)):
			return False

		# Don't move and return false if the space is occupied
		elif(self._isOccupied(newRow, newCol)):
			return False

		# Move up if no reason not to
		else:

			self._worldHistory[-1][animalIndex]['row'] = newRow
			self._worldHistory[-1][animalIndex]['col'] = newCol

			return True

	# Method to move right
	def _moveRight(self, animalIndex):

		newRow = self._worldHistory[-1][animalIndex]['row']

		newCol = self._worldHistory[-1][animalIndex]['col'] + 1

		# Don't move and return false if in the rightest row already
		if(newCol > (self._numColumns - 1)):
			return False

		# Don't move and return false if the space is occupied
		elif(self._isOccupied(newRow, newCol)):
			return False

		# Move up if no reason not to
		else:

			self._worldHistory[-1][animalIndex]['row'] = newRow
			self._worldHistory[-1][animalIndex]['col'] = newCol

			return True

	# Method to move Left
	def _moveLeft(self, animalIndex):

		newRow = self._worldHistory[-1][animalIndex]['row']

		newCol = self._worldHistory[-1][animalIndex]['col'] - 1

		# Don't move and return false if in the leftest
		if(newCol < 0):
			return False

		# Don't move and return false if the space is occupied
		elif(self._isOccupied(newRow, newCol)):
			return False

		# Move up if no reason not to
		else:

			self._worldHistory[-1][animalIndex]['row'] = newRow
			self._worldHistory[-1][animalIndex]['col'] = newCol

			return True




if __name__ == '__main__':

	myWorld = EcoSim(5, 5, 4)

	for index in range(0,10):
		myWorld()

