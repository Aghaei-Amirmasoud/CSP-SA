# simulated annealing search of a one-dimensional objective function
from numpy.random import randn
import numpy as np


def random_start():
    """ Random point in the interval."""
    return np.random.permutation(reqLen)


def acceptance_probability(cost, new_cost, temperature):
    if new_cost < cost:
        return 1
    else:
        p = np.exp(- (new_cost - cost) / temperature)
        return p


def temperature(fraction):
    """ Example of temperature decreasing as the process goes on."""
    return max(0.001, min(1, 1 - fraction))


# objective function
def costFunction(state):
    rolls = waste = 0
    solution = 1
    for i in range(reqLen):
        if StockLength < Requests[state[i]] + rolls:
            waste += StockLength - rolls
            rolls = 0
            solution += 1
        rolls += Requests[state[i]]
    return solution


def neighbour(state, currTemp):
    Wastes = []
    rollSum = 0
    for roll in range(reqLen):
        if rollSum + Requests[state[roll]] > StockLength:
            Wastes.append((roll, StockLength - rollSum))
            rollSum = 0
        rollSum += Requests[state[roll]]
    sortedWastes = sorted(Wastes, key=lambda x: x[-1], reverse=True)
    stop = min(len(sortedWastes) - 2, int(currTemp / 10))
    for i in range(stop):
        chosen1 = sortedWastes[i][0]
        chosen2 = sortedWastes[i + 2][0]
        state[chosen1], state[chosen2] = state[chosen2], state[chosen1]
    return state


# simulated annealing algorithm
def simulated_annealing(n_iterations, temp):
    # generate an initial point
    best = random_start()
    # evaluate the initial point
    best_eval = costFunction(best)
    # current working solution
    curr, curr_eval = best, best_eval
    scores = list()
    # run the algorithm
    for i in range(n_iterations):
        # take a step
        candidate = neighbour(best, temp)
        # evaluate candidate point
        candidate_eval = costFunction(candidate)
        # check for new best solution
        if candidate_eval < best_eval:
            # store new best point
            curr, curr_eval = candidate, candidate_eval
            best, best_eval = candidate, candidate_eval
            # report progress
            print('>%d f(%d) = %d' % (i, i, best_eval))
        # check if we should keep the new point
        else:
            # calculate temperature for current epoch
            fraction = temp / float(i + 1)
            t = temperature(fraction)
            # calculate metropolis acceptance criterion
            metropolis = acceptance_probability(candidate_eval, curr_eval, t)
            # store the new current point
            if np.random.rand() < metropolis:
                curr, curr_eval = candidate, candidate_eval
    return [best, best_eval, scores]


info = []
with open("input4.stock", "r") as filestream:
    for line in filestream:
        line = line.strip()
        line = line.replace(" ", "")
        info.append(line.split(","))

StockLength = int(info[0][0])
Goal = int(info[2][0])
Requests = []

for roll in info[1]:
    Requests.append(int(roll))

reqLen = len(Requests)

while True:
    best = np.random.permutation(reqLen)
    best_eval = costFunction(best)
    current, current_eval = best, best_eval
    best, score, scores = simulated_annealing(n_iterations=1000, temp=200)
    if score < Goal:
        print('f(best) = %d' % score)
        print("desired answer!")
        # line plot of best scores
        break
    else:
        print('f(best) = %d' % score)
        print("not desired answer!")
