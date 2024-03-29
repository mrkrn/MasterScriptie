import numpy as np
import sys


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 formulaPerformance.py filename")
        exit()

    f = open(sys.argv[1])
    content = []
    for line in f.readlines():
        content += [list(map(int, line.split(",")))]
    perfMatrix = np.array(content)
    formulaPerf = [(0, 0, 0)]
    score = 0
    fromOptimum = 0
    fromTop3 = 0
    # print(perfMatrix)
    for i in perfMatrix[1:]:
        for index, j in enumerate(i):
            # print(abs(index - (np.where(j == perfMatrix[0])[0][0])))
            if j == perfMatrix[0][0]:
                fromOptimum = abs(index - (np.where(j == perfMatrix[0])[0][0]))
                fromTop3 += abs(index - (np.where(j == perfMatrix[0])[0][0]))
            elif j == perfMatrix[0][1] or j == perfMatrix[0][2]:
                fromTop3 += abs(index - (np.where(j == perfMatrix[0])[0][0]))
            score += abs(index - (np.where(j == perfMatrix[0])[0][0]))
        # print(index, np.where(j == perfMatrix[0])[0][0])
        formulaPerf += [(score, fromOptimum, fromTop3)]
        score = 0
        fromOptimum = 0
        fromTop3 = 0
    print(perfMatrix)
    print(formulaPerf)

    names = ["Perceived real", "New formula", "Coupling", "Cohesion", "Cluster"]

    print(
        *[
            f"{names[i]}: {j[0]}, optimum difference: {j[1]}, top 3 difference: {j[2]}"
            for i, j in enumerate(formulaPerf)
        ],
        sep="\n",
    )


if __name__ == "__main__":
    main()
