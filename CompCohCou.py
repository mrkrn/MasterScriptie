import complexity


def main(part=None):
    # graph = [
    #     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0],
    #     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    #     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # ]
    # partition = [[1], [2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13]]

    # =============Arch1=============
    graph = [
        [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1],
    ]

    # partition = [[1, 2], [3, 4], [5, 6]]

    # =============Arch2=============
    # graph = [
    #     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    #     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    #     [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 1, 1, 0, 1, 1, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    # ]

    if part == None:
        partition = [[1], [2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13]]
    else:
        partition = part
    # partition = [[1, 3, 4, 5], [2], [6], [7, 8]]

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
        + str(round(GenComp.genComplexity(subGraphlist), 2))
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

    if len(partition) == 1:
        print("\nCoupling = Undefined\n")
        CouplinValue = None
    else:
        CouplinComp = complexity.Coupling(graph, partition)
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

        CouplinValue = round(CouplinComp.coupComplexity(subGraphlist), 2)
        print("\nCoupling = " + str(CouplinValue) + "\n")

    if len(partition) == partition[-1][-1]:
        print("\nCohesion = 0.0\n")
        CohesionValue = 0.0
    else:
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
            CohesionComp.completeMatrix(len(graph)), partition
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

        CohesionValue = round(
            CohesionComp.cohComplexity(cohesionSubgraph, completeSubgraph), 2
        )
        print("\nCohesion = " + str(CohesionValue) + "\n")

    return CouplinValue, CohesionValue


if __name__ == "__main__":
    LowestCoupling = None
    HighestCohesion = None

    CouplingRanking = []
    CohesionRanking = []

    partitions = [
        [[1, 2, 3, 4, 5, 6]],
        [[1, 2, 3], [4, 5, 6]],
        [[1, 2], [3, 4], [5, 6]],
        [[1], [2], [3], [4], [5], [6]],
        [[1, 2, 3], [4, 5], [6]],
    ]
    # [[1, 2, 3, 4, 5, 6, 7, 8]],
    # [[1, 2, 3], [4, 5, 6, 7, 8]],
    # [[1, 2, 3, 4], [5, 6, 7, 8]],
    # [[1, 2, 3, 4], [5, 6], [7, 8]],
    # [[1], [2], [3], [4], [5], [6], [7], [8]],
    # [[1, 3, 4, 5], [2], [6], [7, 8]],
    # partitions = [[[1, 2, 3, 4, 5, 6]], [[1], [2], [3], [4], [5], [6]]]
    for part in partitions:
        coupling, cohesion = main(part)
        partLabel = f"Partition {partitions.index(part) + 1}: " + str(part)
        if len(CouplingRanking) == 0:
            CouplingRanking = [(coupling, partLabel)]
            CohesionRanking = [(cohesion, partLabel)]
        else:
            for i in range(0, len(CouplingRanking)):
                if CouplingRanking[i][0] == None or CouplingRanking[i][0] > coupling:
                    CouplingRanking.insert(
                        i,
                        (coupling, partLabel),
                    )
                    break
                if i == len(CouplingRanking) - 1:
                    CouplingRanking += [(coupling, partLabel)]

            for j in range(0, len(CohesionRanking)):
                if CohesionRanking[j][0] < cohesion:
                    CohesionRanking.insert(
                        j,
                        (cohesion, partLabel),
                    )
                    break
                if j == len(CohesionRanking) - 1:
                    CohesionRanking += [(cohesion, partLabel)]

        if coupling != None:
            if LowestCoupling == None or coupling < LowestCoupling[0][0]:
                LowestCoupling = [(coupling, part)]
            elif coupling == LowestCoupling[0][0]:
                LowestCoupling += [(coupling, part)]
        if HighestCohesion == None or cohesion > HighestCohesion[0][0]:
            HighestCohesion = [(cohesion, part)]
        elif cohesion == HighestCohesion[0][0]:
            HighestCohesion += [(cohesion, part)]
        print("=" * 30)

    if coupling != None:
        # print(LowestCoupling)

        print(
            "Lowest Coupling value: \n\t"
            + str(LowestCoupling[0][0])
            + "\nIn partition(s): \n\t",
            end="",
        )
        print(*[x[1] for x in LowestCoupling], sep="\n\t")

    if cohesion != None:
        # print(LowestCoupling)

        print(
            "Highest Cohesion value: \n\t"
            + str(HighestCohesion[0][0])
            + "\nIn partition(s): \n\t",
            end="",
        )
        print(*[x[1] for x in HighestCohesion], sep="\n\t")

    print("\nCoupling Ranking")
    print(
        "\n".join(
            [
                f"[{i}]\tComplexity: {str(j[0]):8s}{j[1]}"
                for i, j in enumerate(CouplingRanking, start=1)
            ]
        )
    )
    print("\nCohesion Ranking")
    print(
        "\n".join(
            [
                f"[{i}]\tComplexity: {str(j[0]):7s}{j[1]}"
                for i, j in enumerate(CohesionRanking, start=1)
            ]
        )
    )
