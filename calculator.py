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

    def newFormulaAltResult(self, output=False):
        total = 0.0
        exCons = 0
        for item in self.system:
            # total += math.pow((item.exConn), 3.1)
            exCons += item.exConn
            # total += math.pow((item.aggregates), 3.1)
            # total += math.pow(item.inConn, 2)
            # total += math.pow(item.inConn, 2)
            # total += math.pow(2, (item.inConn / 3)) - 1
            # total += (
            #     (math.pow(2, (item.exConn / 3)) - 1)
            #     + (math.pow(2, (item.inConn / 7)) - 1)
            #     + (math.pow(2, (item.aggregates / 3)) - 1)
            # )
            # if item.aggregates != 0:
            #     # total += math.pow((item.aggregates - 4), 2) + 1
            # total += math.pow((item.aggregates), 3.1)
            # total += math.pow((item.aggregates - 3), 2)
            # total += (1 / 4) * math.pow(((item.aggregates - 3)), 2)
            # if item.exConn != 0:
            #     # total += math.pow((item.exConn - 3), 2) + 1
            # total += math.pow((item.exConn - 1), 3) + 1
            #     total += math.pow((item.exConn - 1), 3) + 1
            # total += math.pow(((item.exConn)), 3.1)
            #     # total += (1 / 4) * math.pow(((item.exConn - 2)), 2)
            #     # total += math.sqrt(2 * item.exConn)

            # if item.inConn != 0:
            #     # total += math.pow(10, (2 * math.log(item.inConn, 10)))
            # total += math.pow(2, (item.inConn / 7))
            #     # total += math.sqrt(item.inConn)

            # total += math.pow((item.aggregates), 2.5)
            # total += math.pow(((item.exConn)), 2.5)
            # total += math.pow(((item.inConn)), 1.5)
            total += math.pow((item.aggregates), 2.5) + math.pow(((item.exConn)), 2.5)

            # total += (4 / (1 + math.pow(math.e, (-3.7 * (item.aggregates - 1.3))))) + (
            #     item.aggregates
            # )
            # total += (4 / (1 + math.pow(math.e, (-3.7 * (item.exConn - 1.3))))) + (
            #     item.exConn
            # )
            # total += (4 / (1 + math.pow(math.e, (-3.7 * (item.inConn - 1.3))))) + (
            #     item.inConn
            # )
        if output:
            print(f"Partitions: {len(self.system)}, exCons: {(exCons)}")
        # total += len(self.system) * (exCons / 2)

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
