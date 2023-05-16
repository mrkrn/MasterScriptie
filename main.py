import calculator
import sys


def partition(collection):
    if len(collection) == 1:
        yield [collection]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[first] + subset] + smaller[n + 1 :]
        # put `first` in its own subset
        yield [[first]] + smaller


def manual():
    calc = calculator.Calc()
    output = []

    while True:
        try:
            output += [
                (
                    int(input("\nAggregates: ")),
                    int(input("External connections: ")),
                    int(input("Internal connections: ")),
                )
            ]
        except:
            break
        userInput = input("[Enter] to continue, [X] to remove previous: ")
        if userInput.lower() == "x":
            output.pop()

    for item in output:
        calc.addBoundary(item[0], item[1], item[2])

    calc.showList()
    print(calc.Result())
    calc.reset()

    return


def coded(graph=None):
    possibilities = []
    calcOld = calculator.Calc()
    calcNew = calculator.Calc()
    minOld = None
    minNew = None
    numOld = []
    numNew = []

    # [(1,2,3,4,5,6),(2,1,3,4,5,6),(3,1,2,4,5,6),(4,1,2,3,5,6),(5,1,2,3,4,6),(6,1,2,3,4,5)]
    # partition([(1,2,3,4),(2,1),(3,1,4,5),(4,1,3,5,7),(5,3,4,6,8),(6,5),(7,4,8),(8,5,7)])
    # partition([(1,2,3),(2,1,4),(3,1,4,6),(4,2,3),(5,6,7),(6,3,5,7,8),(7,5,6,8),(8,6,7)])
    # partition([(1,2,3),(2,1,4),(3,1,4,6),(4,2,3,8),(5,6,7),(6,3,5,7,8),(7,5,6,8),(8,4,6,7)])
    # partition([(1,2,3,5),(2,1,4),(3,1,4,5,6),(4,2,3),(5,1,3,6,7),(6,3,5,7,8),(7,5,6,8),(8,6,7)])
    # [(1,2,3),(2,1,3,4),(3,1,2,4),(4,2,3)]
    # partition([(1,2,5,4,7),(2,1,3),(3,2,5,6),(4,1,5,7),(5,1,3,4,7,8,9),(6,3,9),(7,1,4,5),(8,5,10),(9,5,6),(10,8)])
    # partition([(1,2),(2,1,3,4,5,6),(3,2,6),(4,2,5,7),(5,2,4,6),(6,2,3,5,7),(7,4,6)])
    # [("a","c"),("b","d","e","h"),("c","a","d"),("d","b","c","f","j"),("e","b","h","j"),("f","d","j"),("g","h"),("h","b","e","g","i"),("i","h","j"),("j","d","e","f","i","k"),("k","j")]
    # [("Vehicle","Maintenance_Job"),("Notification","Maintenance_Job","Customer"),
    #    ("Maintenance_Job","Vehicle","Notification","Customer","Invoice","Product"),
    #    ("Customer","Notification","Maintenance_Job","Invoice","Sale"),
    #    ("Invoice","Maintenance_Job","Customer","Product"),
    #    ("Product","Maintenance_Job","Invoice","Sale"),
    #    ("Sale","Customer","Product")]
    # (1,2),(2,1,3,4),(3,2,5),(4,2,5,6),(5,3,4,6),(6,4,5,7,8,9,10),(7,6,8),(8,6,7),(9,6,10),(10,6,9,11),(11,10)

    if graph is None:
        graph = [
            (1, 2, 6, 8),
            (2, 1, 3, 4),
            (3, 2, 5),
            (4, 2, 5),
            (5, 3, 4, 10),
            (6, 1, 7, 10),
            (7, 6),
            (8, 1, 9),
            (9, 8, 10),
            (10, 5, 6, 9),
        ]

    # Add all possible partitions to possibilities
    for part in partition(graph):
        # print(part)
        possibilities += [part]

    # For each possible partition
    for n, i in enumerate(possibilities):
        # For each autonomy boundary in partition i
        for j in i:
            exConn = 0  # Num connections going over boundary j
            inConn = 0  # Num connections within boundary j
            edges = {}  # Dict to prevent internal connections being counted twice
            # For each node in autonomy boundary j
            for node in j:
                # For each tuple element in node except first(node id)
                for tupleI in node[1:]:
                    if tupleI not in list(zip(*j))[0]:
                        exConn += 1
                    elif (node[0], tupleI) not in edges:
                        edges[(node[0], tupleI)] = 1
                        edges[(tupleI, node[0])] = 1
                        inConn += 1
            # print(f'Boundary: {list(zip(*j))[0]}, exConn: {exConn}, inConn: {inConn}')

            # print(f'Nodes in subsubset: {list(zip(*j))[0]}')
            # print(f'Connections: {connections}')

            # Old formula => discard internal connections
            calcOld.addBoundary(len(j), exConn, 0)
            # New formula => track internal connections
            calcNew.addBoundary(len(j), exConn, inConn)
        # print("-------------------")

        if minOld == None or calcOld.Result() < minOld:
            minOld = calcOld.Result()
            numOld = [n]
        elif calcOld.Result() == minOld:
            numOld.append(n)

        if minNew == None or calcNew.Result() < minNew:
            minNew = calcNew.Result()
            numNew = [n]
        elif calcNew.Result() == minNew:
            numNew.append(n)

        calcOld.reset()
        calcNew.reset()

    partitionsOld = []
    partitionsNew = []

    for i, nums in enumerate(numOld):
        partitionsOld.append([])
        for part in possibilities[nums]:
            partitionsOld[i].append([x[0] for x in part])

    for i, nums in enumerate(numNew):
        partitionsNew.append([])
        for part in possibilities[nums]:
            partitionsNew[i].append([x[0] for x in part])

    # print(partitions)
    print("---------Old Formula---------")
    print(
        f"Optimal partition number(s): \n\t{numOld}\nComplexity: \n\t{round(minOld,2)}\nPartition(s):",
        end="",
    )
    for outcomes in range(len(partitionsOld)):
        print("\n\t", end="")
        print(*partitionsOld[outcomes], sep="\n\t", end="")
        print("\n--------", end="")
    print("-New Formula---------")
    print(
        f"Optimal partition number(s): \n\t{numNew}\nComplexity: \n\t{round(minNew,2)}\nPartition(s):",
        end="",
    )
    for outcomes in range(len(partitionsNew)):
        print("\n\t", end="")
        print(*partitionsNew[outcomes], sep="\n\t", end="")
        print("\n--------", end="")

    print(f"\nOut of {len(possibilities)} possibilities\n")

    if (
        input("Output https://csacademy.com/app/graph_editor/ code? [y/n]: ").lower()
        == "y"
    ):
        print(*list(zip(*graph))[0], sep="\n")
        print()
        for node in graph:
            for edge in node[1:]:
                print(node[0], edge)

    return


def fileInput(fileName):
    tempFile = open(fileName, "r")
    node2edge = False
    edges = {}

    for node in tempFile.readlines():
        if node == "\n":
            node2edge = True
            continue
        if not node2edge:
            edges[node.strip().split(" ")[0]] = []
        else:
            if node.strip().split(" ")[0] not in edges.keys():
                continue
            try:
                if node.strip().split(" ")[1] not in edges[node.strip().split(" ")[0]]:
                    edges[node.strip().split(" ")[0]].append(node.strip().split(" ")[1])
                    edges[node.strip().split(" ")[1]].append(node.strip().split(" ")[0])
            except Exception:
                continue
    graph = []

    for key, values in edges.items():
        graph.append(tuple([key, *values]))

    # print(graph)
    return graph


def main():
    if "--help" in sys.argv or len(sys.argv) < 2:
        print(
            """Command usage: python3 main.py [OPTION]
    --help,         Shows this screen.
    -f filename,    Use a file as input for system.
    -c,             Use a hardcoded graph representation.
    -m,             Use manual input for graph.
    """
        )
        return

    for i in range(len(sys.argv)):
        if sys.argv[i] == "-f":
            if (i + 1) < len(sys.argv) and open(sys.argv[i + 1], "r"):
                coded(fileInput(sys.argv[i + 1]))
                return
            else:
                raise NameError("No input file given")
        if sys.argv[i] == "-c":
            coded()
            return
        if sys.argv[i] == "-m":
            manual()
            return


if __name__ == "__main__":
    main()
