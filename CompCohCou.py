import complexity


def main():
    graph = [
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    partition = [
        [1],
        [2, 3, 4],
        [5, 6, 7, 8, 9],
        [10, 11, 12, 13],
    ]

    # [1],
    # [2, -1, 4],
    # [5, 6, 7, -1, 9],
    # [10, 11, -1, -1],

    # [1],
    # [2,3],
    # [4,5,6,7,8],
    # [9,10,11,12],

    # [1],
    # [2,3],
    # [4,5,6,7],
    # [8,9,10,11],

    # [1],
    # [2,3],
    # [4,5,6],
    # [7,8,9,10],

    # [1],
    # [2,3],
    # [4,5,6],
    # [7,8],

    GenComp = complexity.Complexity(graph, partition)
    GenComp.pL()
    # GenComp.print()

    # print(*(GenComp.returnMatrix(GenComp.interMatrix())), sep="\n", end="\n\n")
    # x, y = GenComp.purgeNodes(GenComp.interMatrix(), partition)
    # print(*(GenComp.returnMatrix(x)), y, sep="\n")

    subGraphlist = []
    for i in range(0, len(GenComp.matrix)):
        subGraphlist += [GenComp.subgraphMatrix(i)]

    for j in subGraphlist:
        GenComp.pL(j)
        # print(*j, sep="\n")
        # print()

    # print(GenComp.sizeComplexity())
    print(
        "\nGeneral Complexity = "
        + str(round(GenComp.genComplexity(subGraphlist), 1))
        + "\n"
    )

    # graph = [
    #     [1, 1, 1, 0, 0, 0],  # 1 = 1
    #     [1, 0, 0, 1, 0, 0],  # 2 = 2
    #     # [0, 0, 0, 0, 1, 1], #3
    #     [0, 0, 0, 0, 1, 0],  # 4 = 3
    #     [0, 1, 0, 0, 1, 0],  # 5 = 4
    #     [0, 0, 1, 0, 0, 0],  # 6 = 5
    #     [0, 0, 0, 0, 0, 1],  # 7 = 6
    #     # [0, 0, 0, 0, 0, 0], #8
    #     # [0, 0, 0, 0, 0, 0], #9
    #     [0, 0, 0, 0, 0, 1],  # 10 = 7
    #     [0, 0, 0, 1, 0, 0],  # 11 = 8
    #     # [0, 0, 0, 0, 0, 0], #12
    #     # [0, 0, 0, 0, 0, 0], #13
    #     # [0, 0, 0, 0, 0, 0], #14
    # ]
    # partition = [
    #     [1],
    #     [2, 3],
    #     [4, 5, 6],
    #     [7, 8],
    # ]
    # partition = [
    #     [1],
    #     [2, 4],
    #     [5, 6, 7],
    #     [10, 11],
    # ]

    # CouplinComp = complexity.Coupling(graph, partition)
    # x, y = GenComp.purgeNodes(GenComp.interMatrix(), partition)
    # x = GenComp.returnMatrix(x)
    # print(*x, y, sep="\n")

    couplinGraph, couplinPartition = GenComp.purgeNodes(
        GenComp.interMatrix(), partition
    )
    couplinGraph = GenComp.returnMatrix(couplinGraph)

    CouplinComp = complexity.Coupling(couplinGraph, couplinPartition)

    CouplinComp.pL()
    # CouplinComp.print()

    subGraphlist = []
    for i in range(0, len(CouplinComp.matrix)):
        subGraphlist += [CouplinComp.subgraphMatrix(i)]

    for j in subGraphlist:
        CouplinComp.pL(j)
        # print(*j, sep="\n")
        # print()

    print(
        "\nCoupling = " + str(round(CouplinComp.coupComplexity(subGraphlist), 1)) + "\n"
    )

    cohesionGraph, cohesionPartition = GenComp.purgeNodes(
        GenComp.intraMatrix(), partition
    )
    cohesionGraph = GenComp.returnMatrix(cohesionGraph)
    # print(*cohesionGraph, cohesionPartition, sep="\n", end="\n\n")

    CohesionComp = complexity.Cohesion(cohesionGraph, cohesionPartition)

    CohesionComp.pL()
    # CohesionComp.print()

    # print(len(GenComp.matrix))
    completeComp = complexity.Cohesion(
        CohesionComp.completeMatrix(len(GenComp.matrix)), partition
    )

    completeComp.pL()
    # completeComp.print()

    cohesionSubgraph = []
    for i in range(0, len(CohesionComp.matrix)):
        cohesionSubgraph += [CohesionComp.subgraphMatrix(i)]

    for j in cohesionSubgraph:
        CohesionComp.pL(j)

    completeSubgraph = []
    for i in range(0, len(completeComp.matrix)):
        completeSubgraph += [completeComp.subgraphMatrix(i)]

    for j in completeSubgraph:
        completeComp.pL(j)

    print(
        "\nCohesion = "
        + str(round(CohesionComp.cohComplexity(cohesionSubgraph, completeSubgraph), 2))
        + "\n"
    )

    return


if __name__ == "__main__":
    main()
