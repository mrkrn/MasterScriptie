import math


class Boundary:
    def __init__(self, aggregates, exConn, inConn):
        self.aggregates = aggregates
        self.exConn = exConn  # External connections
        self.inConn = inConn  # Internal connections


class Calc(Boundary):
    def __init__(self):
        self.system = []

    def reset(self):
        for i in self.system:
            del i
        self.system = []

    def addBoundary(self, aggregates, exConn, inConn):
        temp = Boundary(aggregates, exConn, inConn)
        self.system += [temp]

    def showList(self):
        for i, item in enumerate(self.system):
            print(
                f"Autonomy boundary {i+1}: {item.aggregates} aggregates & {item.exConn} exConn & {item.inConn} inConn"
            )

    def newFormulaResult(self):
        total = 0.0
        for item in self.system:
            if item.aggregates != 0:
                total += math.pow(10, (3.1 * math.log(item.aggregates, 10)))
            if item.exConn != 0:
                total += math.pow(10, (3.1 * math.log(item.exConn, 10)))
            if item.inConn != 0:
                total += math.pow(10, (2 * math.log(item.inConn, 10)))

        # print(f'Complexity of system: {total}')
        return total

    def newFormulaResult(self):
        total = 0.0
        for item in self.system:
            if item.aggregates != 0:
                total += math.pow(10, (3.1 * math.log(item.aggregates, 10)))
            if item.exConn != 0:
                total += math.pow(10, (3.1 * math.log(item.exConn, 10)))
            if item.inConn != 0:
                total += math.pow(10, (2 * math.log(item.inConn, 10)))

        # print(f'Complexity of system: {total}')
        return total

    def clusterFormulaResult(self):
        total = 0.0
        interclusterEdges = 0
        totalNodesNum = 0
        for item in self.system:
            total += item.aggregates * item.inConn
            interclusterEdges += item.exConn
            totalNodesNum += item.aggregates

        interclusterEdges /= 2  # remove double counted edges

        total += totalNodesNum * interclusterEdges
        # print(f'Complexity of system: {total}')
        return total
