# EcoSim
Python implementation of the Edge Effect ecology simulation project

- Can initialize a randomly populated grid of arbitrary size and total population
- Displays ecosystem each timestep
- Individuals move randomly, but do not interact with eachother

v0.0: created the class with a simple movement rule: one individual moves right with each timestep. More complex motion and interaction to come...

v0.1: Changed class to make it more "individual-centric". Each animal is represented by a dictionary. Currently the dictionary only has keys for location and age, but it can store many other stats in the future...

### Operation

#### Dependencies
* numpy
* random

#### Usage
First, create the EcoSim object. Requires three input arguments: number of rows in the grid, number of colums in the grid, and the initial population size. For example to make a 5x3 grid with 3 animals:

```python

numRows = 5
numCols = 3
initPop = 3

myWorld = EcoSim(numRows, numCols, initPop)

```

The object steps when called and returns the current state after each step. You can use a list comprehension to iterate and save the state at each timepoint. 

```python
history = [myWorld() for _ in range(10)]

```

The function prints the grid to the terminal after each step. Each node displays the number of animals at that location. Example output:

```
Step: 0
1 - 0 - 0
|   |   |
0 - 0 - 0
|   |   |
1 - 0 - 0
|   |   |
0 - 0 - 0
|   |   |
1 - 0 - 0

Step 10
0 - 0 - 0
|   |   |
0 - 0 - 0
|   |   |
1 - 0 - 1
|   |   |
1 - 0 - 0
|   |   |
0 - 0 - 0

```


### Next steps

- Mating
- Fighting
- Aging/dieing
- Speciation
