import random
import math
import numpy as np


def simulated_annealing(initial_state):
    """Performs simulated annealing to find a solution"""
    initial_temp = 419
    final_temp = .1
    alpha = 0.01

    current_temp = initial_temp

    # Start by initializing the current state with the initial state
    current_state = initial_state
    solution = current_state

    while current_temp > final_temp:
        neighbor = get_neighbors(solution, current_temp)
        # Check if neighbor is best so far
        cost_diff = get_cost(current_state)[0] - get_cost(neighbor)[0]

        # if the new solution is better, accept it
        if cost_diff > 0:
            solution = neighbor
        # if the new solution is not better, accept it with a probability of e^(-cost/temp)
        else:
            if random.uniform(0, 1) < math.exp(-cost_diff / current_temp):
                solution = neighbor
        # decrement the temperature
        current_temp -= alpha

    return solution, get_cost(solution)


def get_cost(x):
    """Calculates cost of the argument state for your solution."""
    result = 1
    sumWoods = 0
    totalWaste = 0
    for piece in range(n):
        if sumWoods + Requests[x[piece]] > StockLength:
            result += 1
            totalWaste += StockLength - sumWoods
            sumWoods = 0
        sumWoods += Requests[x[piece]]
    return result, totalWaste


def get_neighbors(x, currTemp):
    sumWoods = 0
    sumWastes = []
    for W in range(n):
        if sumWoods + Requests[x[W]] > StockLength:
            sumWastes.append((W, StockLength - sumWoods))
            sumWoods = 0
        sumWoods += Requests[x[W]]

    WastesSorted = sorted(sumWastes, key=lambda X: X[1], reverse=True)
    stop = get_stop(len(WastesSorted) - 2, int(currTemp / 10))
    for i in range(stop):
        rand1 = WastesSorted[i][0]
        rand2 = WastesSorted[i + 2][0]
        x[rand1], x[rand2] = x[rand2], x[rand1]
    return x


def get_stop(x, y):
    if x <= y:
        return x
    else:
        return y


info = []
with open("input4.stock", "r") as filestream:
    for line in filestream:
        line = line.strip()
        line = line.replace(" ", "")
        info.append(line.split(","))

StockLength = int(info[0][0])
Requests = []

for roll in info[1]:
    Requests.append(int(roll))

n = len(Requests)

while True:
    best = list(np.random.permutation(n))
    ans = simulated_annealing(best)
    if ans[1][0] < int(info[2][0]):
        print(ans[1])
        break
    else:
        print(ans[1])
        print("not desired answer!")
