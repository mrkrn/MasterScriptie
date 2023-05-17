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

    # def purgeNodes(self, proportions):
    #     for index, i in enumerate(proportions):
    #         for j in i[1]:
    #             print(j)
    #             if j == 1:
    #                 break
    #         if j == 0:
    #             proportions.pop(index)
    #             print("Emtpy row")
    #             for part, k in enumerate(self.partitions):
    #                 if index in k:
    #                     print(self.partitions)
    #                     self.partitions[part].remove(index)
    #         print()

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
        # nodeMatrix are connectivity matrices of individual nodes
        total = 0
        for i in range(1, len(nodeMatrix)):
            total += self.sizeComplexity(nodeMatrix[i])
        total -= self.sizeComplexity(overalMatrix)

        return total
        # print(*nodeMatrix[i], sep="\n")
        # print()

    def coupComplexity(self, nodeMatrix):
        return self.genComplexity(nodeMatrix)
