# simulated annealing search of a one-dimensional objective function
from numpy.random import randn
import numpy as np
from matplotlib import pyplot
from numpy import exp
from numpy.random import rand


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
    sortedWastes = sorted(Wastes, key=lambda x: x[1], reverse=True)
    stop = min(len(sortedWastes), int(currTemp / 10))
    for i in range(stop):
        random1 = sortedWastes[i][0]
        random2 = sortedWastes[i + 2][0]
        state[random1], state[random2] = state[random2], state[random1]
    return state


# simulated annealing algorithm
def simulated_annealing(n_iterations, temp):
    # generate an initial point
    best = np.random.permutation(reqLen)
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
            # keep track of scores
            scores.append(best_eval)
        # check if we should keep the new point
        else:
            diff = candidate_eval - curr_eval
            # calculate temperature for current epoch
            t = temp / float(i + 1)
            # calculate metropolis acceptance criterion
            metropolis = exp(-diff / t)
            # check if we should keep the new point
            if diff < 0 or rand() < metropolis:
                # store the new current point
                curr, curr_eval = candidate, candidate_eval
    return [best, best_eval, scores]


StockLength = 1000
Requests = [106, 187, 914, 106, 33, 18, 402, 230, 507, 495, 609, 627, 346, 295, 312, 107, 716, 88, 106, 248, 689, 115, 106, 218, 672, 618, 117, 805, 306, 753, 414, 84, 557, 266, 409, 144, 69, 116, 333, 88, 264, 967, 180, 251, 71, 788, 581, 555, 988, 292, 60, 125, 532, 405, 170, 249, 181, 686, 283, 424, 933, 23, 99, 135, 246, 337, 648, 753, 354, 518, 45, 286, 315, 370, 557, 463, 312, 284, 61, 412, 457, 118, 268, 123, 232, 788, 678, 371, 171, 557, 549, 286, 356, 92, 148, 515, 301, 632, 987, 660, 868, 92, 544, 211, 70, 75, 145, 125, 278, 441, 368, 351, 119, 662, 653, 186, 517, 43, 224, 506, 592, 501, 149, 79, 241, 53, 80, 437, 46, 78, 149, 525, 149, 126, 365, 460, 280, 266, 109, 86]

reqLen = len(Requests)

best = np.random.permutation(reqLen)
best_eval = costFunction(best)
current, current_eval = best, best_eval
best, score, scores = simulated_annealing(n_iterations=1000, temp=200)
print('best answer we got = %d' % score)
# line plot of best scores
pyplot.plot(scores, '.-')
pyplot.xlabel('Improvement Number')
pyplot.ylabel('Evaluation f(x)')
pyplot.show()

