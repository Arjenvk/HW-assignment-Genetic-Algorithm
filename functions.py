import numpy as np
import pandas as pd


def fitness_pop(pop, fit_matrix):
    results = []
    for i in range(len(pop)):
        path = pop[i]
        # alle 0 elementen weghalen
        path = list(filter(lambda a: a != 0, path))
        # beginpunt en eindpunt toevoegen
        path.append(10)
        path.insert(0, 0)
        # evalueren array naar fit_matrix
        fitness = 0
        for i in range(len(path) - 2):
            a = path[i]
            b = path[i + 1]
            k = fit_matrix[a][b]
            fitness = fitness + k
        results.append(fitness)
    return results

def create_child():
    child = np.int_(np.floor(np.random.uniform(0, 10, 9)))
    return child

def create_population(pop_size):
    pop = []
    for i in range(pop_size):
        pop.append(create_child())
    return pop

def order_population(population, results):
    pop_size = len(population)
    data = {'child': np.int_(np.linspace(1, pop_size, pop_size)), 'path': population, 'fitness': results}
    df = pd.DataFrame(data)
    df2 = df.sort_values(by=['fitness'])
    df2['child'] = np.int_(np.linspace(1, pop_size, pop_size))
    df3 = df2.set_index('child')
    return df3

def make_children(parent1, parent2):
    split = np.int_(np.floor(np.random.uniform(0, 9, 3)))
    children = []
    for i in range(3):
        children.append(np.concatenate((parent1[0:split[i]], parent2[split[i]:9])))
        children.append(np.concatenate((parent2[0:split[i]], parent1[split[i]:9])))
    return children


def mutate_parent(parent):
    child1 = parent
    child2 = parent
    point1 = np.int_(np.floor(np.random.uniform(0, 9)))
    point2 = np.int_(np.floor(np.random.uniform(0, 9)))
    child1[point1] = np.int_(np.floor(np.random.uniform(1, 9)))
    child2[point2] = 0
    return child1, child2

def next_generation(pop_ordered, num_survive, pop_size):
    paths = pop_ordered['path']
    pop_new = []
    num_children = num_survive * 3  # 6 kinderen per 2 ouders
    num_mutations = num_survive * 2  # 2 mutanten per ouder
    # survive as new parents
    for i in range(1, num_survive +1):
        k = paths[i]
        pop_new.append(k)

    # create children
    for i in range(1, np.int_(np.floor(num_children / 6))+1):
        parent1 = paths[i+1]
        parent2 = paths[np.int_((num_survive / 2)) + i +1]
        children = make_children(parent1, parent2)
        for i in range(len(children)):
            pop_new.append(children[i])

    # Mutate parents:
    # remove & alter path from parents
    for i in range(1, num_survive+1):
        child1, child2 = mutate_parent(paths[i])
        pop_new.append(child1)
        pop_new.append(child2)
    # fill up to pop_size with immigration
    pop_imm_size = pop_size - len(pop_new)
    pop_imm = create_population(pop_imm_size)
    for i in range(pop_imm_size):
        pop_new.append(pop_imm[i])
    return pop_new