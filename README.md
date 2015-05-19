# EcoSim
Python implementation of the Edge Effect ecology simulation project

- Can initialize a randomly populated grid of arbitrary size and total population
- Displays ecosystem each timestep
- Individuals move randomly, but do not interact with eachother

	v0.0: created the class with a simple movement rule: one individual moves right with each timestep. More complex motion and interaction to come...

	v0.1: Changed class to make it more "individual-centric". Each animal is represented by a dictionary. Currently the dictionary only has keys for location and age, but it can store many other stats in the future...

### Next steps

- Mating
- Fighting
- Aging/dieing
- Speciation
