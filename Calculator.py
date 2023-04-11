import math
import boundary

class Calc(boundary.Boundary):
    def __init__(self):
        self.system = []

    def reset(self):
        for i in self.system:
            del i
        self.system = []

    def addBoundary(self, aggregates, connections):
        temp = boundary.Boundary(aggregates, connections)
        self.system += [temp]
    
    def showList(self):
        for i, item in enumerate(self.system):
            print(f'Autonomy boundary {i+1}: {item.aggregates} aggregates & {item.connections} connections')
    
    def Result(self):
        total = 0.0
        for item in self.system:
            if item.aggregates != 0:
                total += math.pow(10, (3.1*math.log(item.aggregates, 10)))
            if item.connections != 0:
                total += math.pow(10, (3.1*math.log(item.connections, 10)))
        
        # print(f'Complexity of system: {total}')
        return total