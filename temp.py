import random as rand
from datetime import datetime as dt

rand.seed(dt.now().timestamp())
totalDistance = 0
optimumDistance = 0
total = 0
truth = [1, 2, 3, 4, 5]

try:
    for j in range(0, 1000000):
        test = rand.sample(range(1, 6), 5)
        for i in range(0, 5):
            totalDistance += abs(i - test.index(truth[i]))
        optimumDistance += test.index(truth[0])
        total += 1
        print(total)
        # print(test, totalDistance, optimumDistance)
        # exit()
    raise
except:
    print(f"Out of {total} tries:")
    print(
        f"Average total distance: {round(totalDistance/total, 1)}, total distance: {totalDistance}"
    )
    print(
        f"Average optimum distance: {round(optimumDistance/total, 1)}, total optimum distance: {optimumDistance}"
    )
    exit()
