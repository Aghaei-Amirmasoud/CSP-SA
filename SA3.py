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
    stop = get_stop(len(WastesSorted), int(currTemp / 10))
    for i in range(stop):
        rand1 = WastesSorted[i][0]
        x[rand1], x[rand1 + 1] = x[rand1 + 1], x[rand1]
    return x


def get_stop(x, y):
    if x <= y:
        return x
    else:
        return y


StockLength = 100
Requests = [106, 187, 914, 106, 33, 18, 402, 230, 507, 495, 609, 627, 346, 295, 312, 107, 716, 88, 106, 248, 689, 115, 106, 218, 672, 618, 117, 805, 306, 753, 414, 84, 557, 266, 409, 144, 69, 116, 333, 88, 264, 967, 180, 251, 71, 788, 581, 555, 988, 292, 60, 125, 532, 405, 170, 249, 181, 686, 283, 424, 933, 23, 99, 135, 246, 337, 648, 753, 354, 518, 45, 286, 315, 370, 557, 463, 312, 284, 61, 412, 457, 118, 268, 123, 232, 788, 678, 371, 171, 557, 549, 286, 356, 92, 148, 515, 301, 632, 987, 660, 868, 92, 544, 211, 70, 75, 145, 125, 278, 441, 368, 351, 119, 662, 653, 186, 517, 43, 224, 506, 592, 501, 149, 79, 241, 53, 80, 437, 46, 78, 149, 525, 149, 126, 365, 460, 280, 266, 109, 86]

n = len(Requests)

best = list(np.random.permutation(n))
ans = simulated_annealing(best)
print(ans[1])

