import numpy as np
from random import randint


class EcoSim(object):

	def __init__(self, numRows, numColumns, initPop, maxSeedPerNode = 1):

		
		# Save the ecoysystem parameters
		self._numRows = numRows
		self._numColumns = numColumns
		self._initPop = initPop
		self._maxSeedPerNode = maxSeedPerNode
		self._stepNum = 0

		# Initialize the world...
		self._worldHistory = (np.zeros((self._numRows, self._numColumns),
		 dtype=np.int),)


		# Populate the world
		remainingOrgs = self._initPop

		while(remainingOrgs):

			# Get the number of organisms to add to the node
			if ((self._maxSeedPerNode * remainingOrgs) <= 2):
				orgsToAdd = remainingOrgs

			else:
				orgsToAdd = np.random.randint(0, self._maxSeedPerNode * remainingOrgs)

			#print(orgsToAdd, remainingOrgs)

			# Add the orgs to a random node
			row = np.random.randint(0, (self._numRows - 1))
			col = np.random.randint(0, (self._numColumns - 1))

			#print(row, col)

			self._worldHistory[-1][row, col] += orgsToAdd

			remainingOrgs -= orgsToAdd


		# Display the ecosystem
		self.show()

	def step(self):
		
		self._stepNum += 1
		print("Step " + str(self._stepNum))

		# Make the matrix for the next step
		#self._worldHistory += (self._worldHistory[-1],)

		# Get the displacement matrix
		deltaN = self.getDisplacements()

		# Calculate the new population matrix
		newWorld = self._worldHistory[-1] + deltaN

		# Add the step to the history
		self._worldHistory += (newWorld,)

		self.show()

	# Method to calculate the displacements at each node...
	# Currently one individual moves one node to the right each step.
	# The grid is bounded so flux out is always zero.
	# choose something more complex later...
	def getDisplacements(self):

		displacements = np.zeros((self._numRows, self._numColumns),
		 dtype=np.int)

		# Move the individuals away from the col = 0 edge
		for row in range(0, (self._numRows - 1)):
			for col in range(0, (self._numColumns - 1)):

				if(self._worldHistory[-1][row, col] > 0):

					# Change in N at the node
					displacements[row, col] += -1

					# Flux in the positive X direction
					displacements[row, col + 1] += 1

		
		return displacements



	def __call__(self):

		self.step() 



	# Method to print the current ecosystem. Numbers at the nodes 
	# are the numer of individuals at that node
	def show(self):

		for row in range(self._numRows - 1):

			# Print a row of organisms
			for col in range(self._numColumns - 1):

				print(self._worldHistory[-1][row, col]),
				print("-"),

			print(self._worldHistory[-1][row, -1])

			# Print the vertial links
			for col in range(self._numColumns - 1):
				print("|  "),

			print("|")

		# Print the last row of organisms
		for col in range(self._numColumns - 1):

			print(self._worldHistory[-1][-1, col]),
			print("-"),

		print(self._worldHistory[-1][-1, -1])



if __name__ == '__main__':

	myWorld = EcoSim(5, 5, 20, 0.3)

	for index in range(0,10):
		myWorld()

