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

    GenComp = complexity.Complexity(graph, partition)
    GenComp.pL()

    GenComp.print()

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

    graph = [
        [1, 1, 1, 0, 0, 0],  # 1 = 1
        [1, 0, 0, 1, 0, 0],  # 2 = 2
        # [0, 0, 0, 0, 1, 1], #3
        [0, 0, 0, 0, 1, 0],  # 4 = 3
        [0, 1, 0, 0, 1, 0],  # 5 = 4
        [0, 0, 1, 0, 0, 0],  # 6 = 5
        [0, 0, 0, 0, 0, 1],  # 7 = 6
        # [0, 0, 0, 0, 0, 0], #8
        # [0, 0, 0, 0, 0, 0], #9
        [0, 0, 0, 0, 0, 1],  # 10 = 7
        [0, 0, 0, 1, 0, 0],  # 11 = 8
        # [0, 0, 0, 0, 0, 0], #12
        # [0, 0, 0, 0, 0, 0], #13
        # [0, 0, 0, 0, 0, 0], #14
    ]
    partition = [
        [1],
        [2, 3],
        [4, 5, 6],
        [7, 8],
    ]

    CouplinComp = complexity.Complexity(graph, partition)
    CouplinComp.pL()

    CouplinComp.print()
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
    return


if __name__ == "__main__":
    main()
