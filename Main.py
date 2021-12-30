import numpy as np
import functions as fnc
import pandas as pd
import math
import matplotlib.pyplot as plt

# fitness matrix
fit_matrix = [
    [1000, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [10, 1000, 0, 0, 0, 0, 0, 2, 0, 0],
    [10, 10, 1000, 0, 0, 0, 0, 0, 0, 0],
    [10, 10, 10, 1000, 0, 0, 0, 0, 0, 0],
    [10, 10, 10, 10, 1000, 0, 0, 0, 0, 0],
    [10, 10, 10, 10, 10, 1000, 0, 0, 0, 0],
    [10, 10, 10, 10, 10, 10, 1000, 0, 0, 0],
    [10, 10, 10, 10, 10, 10, 10, 1000, 0, 0],
    [10, 10, 2, 10, 10, 10, 10, 10, 1000, 0],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 1000]
]

# simulation controls:
pop_size = 150       # size of the populations - veelvoud van 10
num_survive = 20     # number of survivors of each generation - veelvoud van 10
num_iter = 100       # number of iterations in simulations


# maak een initiele populatie
pop = fnc.create_population(pop_size)

# bepaal fitness populatie
results = fnc.fitness_pop(pop, fit_matrix)
avg = [np.average(results)]
best = [np.amin(results)]

# order population by fitness
pop_ordered = fnc.order_population(pop, results)

for i in range(num_iter):
    # create next generation
    next_generation = fnc.next_generation(pop_ordered, num_survive, pop_size)

    # assess fitness new generation
    results = fnc.fitness_pop(next_generation, fit_matrix)
    avg.append(np.average(results))
    best.append(np.amin(results))

    # order population by fitness
    pop_ordered = fnc.order_population(next_generation, results)


plt.plot(avg)
plt.plot(best)
plt.show()


