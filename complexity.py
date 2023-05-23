import math
import copy


class Complexity:
    def __init__(self, graph=[], partition=[]):
        self.matrix = [[0] * len(graph[0])] + graph
        self.partitions = [[0]] + partition
        self.proportions = []
        for i in range(0, len(self.matrix)):
            self.proportions += [[i, self.matrix[i], 1]]

    def print(self):
        try:
            for num, part in enumerate(self.partitions):
                print("Environment") if num == 0 else print("Partition " + str(num))

                for i in part:
                    # print(part)
                    print(
                        str(self.proportions[i][0])
                        + ": "
                        + str(self.proportions[i][1])
                        + "; pL(n) = "
                        + str(self.proportions[i][2])
                    )
        except:
            print("Index error on index: " + str(i))
            return

    def equals(self, arr1, arr2):
        for i in range(0, len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True

    def pL(self, proportionMatrix=None):
        if proportionMatrix == None:
            proportionMatrix = self.proportions
        else:
            for elem in proportionMatrix:
                elem[2] = 1
        for i in range(0, len(proportionMatrix)):
            for j in range(i + 1, len(proportionMatrix)):
                if self.equals(proportionMatrix[i][1], proportionMatrix[j][1]):
                    proportionMatrix[i][2] += 1
                    proportionMatrix[j][2] += 1

        for k in proportionMatrix:
            k[2] /= len(proportionMatrix)

    def subgraphMatrix(self, node):
        # print("=" * 20 + "subgraphMatrix" + "=" * 20)
        subGraph = copy.deepcopy(self.proportions)
        for index, i in enumerate(subGraph[node][1]):
            # print(index, i)
            for j in subGraph:
                if j[0] == node:
                    continue
                if i == 0:
                    j[1][index] = 0
        # print(*subGraph, sep="\n")
        # print("=" * 20 + "subgraphMatrix" + "=" * 20)
        return subGraph

    def intraMatrix(self, proportionMatrix=None, partitions=None):
        if proportionMatrix == None:
            proportionMatrix = copy.deepcopy(self.proportions)
        if partitions == None:
            partitions = copy.deepcopy(self.partitions)

        for part in range(1, len(partitions)):
            # print(
            #     *(proportionMatrix[partitions[part][0] : (partitions[part][-1] + 1)]),
            #     sep="\n",
            # )
            # print()
            # if len(partitions[part]) == 1:
            #     continue
            for edgeBitindex in range(0, len(proportionMatrix[partitions[part][0]][1])):
                # print(edgeBitindex)
                total = 0
                for dist in proportionMatrix[
                    partitions[part][0] : (partitions[part][-1] + 1)
                ]:
                    if dist[1][edgeBitindex] == 1:
                        total += 1

                if total != 2:
                    for dist in proportionMatrix[
                        partitions[part][0] : (partitions[part][-1] + 1)
                    ]:
                        dist[1][edgeBitindex] = 0

            # print(
            #     *(proportionMatrix[partitions[part][0] : (partitions[part][-1] + 1)]),
            #     sep="\n",
            # )
        return proportionMatrix

    def interMatrix(self, proportionMatrix=None):
        if proportionMatrix == None:
            proportionMatrix = copy.deepcopy(self.proportions)

        intraMatrix = self.intraMatrix()

        for edgebit in range(0, len(proportionMatrix[0][1])):
            for proportion, x in enumerate(proportionMatrix):
                if intraMatrix[proportion][1][edgebit] == 1:
                    proportionMatrix[proportion][1][edgebit] = 0

        return proportionMatrix

    def returnMatrix(self, proportionMatrix=None):
        if proportionMatrix == None:
            proportionMatrix = copy.deepcopy(self.proportions)

        if proportionMatrix[0][0] == 0:
            return list(map(list, zip(*proportionMatrix)))[1][1:]

        return list(map(list, zip(*proportionMatrix)))[1]

    def purgeNodes(self, proportions, partitions):
        returnProportions = copy.deepcopy(proportions)
        returnPartitions = copy.deepcopy(partitions)

        for proportion in proportions:
            for edgebit in proportion[1]:
                if edgebit == 1:
                    break
            if edgebit == 0 and proportion[0] != 0:
                # print("Empty row", proportion)
                remove = False
                for i, part in enumerate(returnPartitions):
                    for j, node in enumerate(part):
                        if remove and node != -1:
                            returnPartitions[i][j] -= 1
                        if partitions[i][j] == proportion[0]:
                            remove = True
                            returnPartitions[i][j] = -1

        # +[-1] because env variable is always 0
        flattenPartitions = [-1] + [x for sublist in returnPartitions for x in sublist]
        for i in range(0, len(flattenPartitions)):
            if flattenPartitions[i] == -1:
                returnProportions[i][0] = -1

        for i in range(0, len(returnPartitions)):
            returnPartitions[i] = list(filter(lambda x: x != -1, returnPartitions[i]))

        returnProportions = [x for x in returnProportions if (x[0] != -1)]

        return (returnProportions, returnPartitions)

    def sizeComplexity(self, proportionMatrix=None):
        if proportionMatrix == None:
            proportionMatrix = self.proportions
        total = 0.0
        for n in proportionMatrix:
            if n[0] == 0:
                continue
            total += -math.log(n[2], 2)
        return total

    def genComplexity(self, nodeMatrix, overalMatrix=None):
        if overalMatrix == None:
            overalMatrix = self.proportions
        # nodeMatrix = array of all connectivity matrices of individual nodes
        total = 0
        for i in range(1, len(nodeMatrix)):
            total += self.sizeComplexity(nodeMatrix[i])
        total -= self.sizeComplexity(overalMatrix)

        return total
        # print(*nodeMatrix[i], sep="\n")
        # print()


class Coupling(Complexity):
    def __init__(self, graph=[], partition=[]):
        super().__init__(graph, partition)

    def coupComplexity(self, interMatrix):
        return self.genComplexity(interMatrix)


class Cohesion(Complexity):
    def __init__(self, graph=[], partition=[]):
        super().__init__(graph, partition)

    def completeMatrix(self, nodesNum):
        edgeMatrix = []
        for i in range(0, nodesNum):
            edgeMatrix += [[0] * round((nodesNum * (nodesNum - 1)) / 2)]

        startColumn = 0
        edgeCount = nodesNum - 1
        for index, row in enumerate(edgeMatrix):
            counterRow = index + 1
            for i in range(startColumn, startColumn + edgeCount):
                edgeMatrix[index][i] = 1
                edgeMatrix[counterRow][i] = 1
                counterRow += 1
            startColumn += edgeCount
            edgeCount -= 1
        # print(*edgeMatrix, sep="\n")
        # print()
        return edgeMatrix

    def cohComplexity(self, intraMatrix, completeMatrix):
        return self.genComplexity(intraMatrix) / self.genComplexity(completeMatrix)
