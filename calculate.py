import calculator
      
def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return
    
    first = collection[0]
    for smaller in partition(collection[1:]):
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset]  + smaller[n+1:]
        # put `first` in its own subset 
        yield [ [ first ] ] + smaller

def main():
    possibilities = []
    calc = calculator.Calc()
    min = None
    num = []

    # partition([(1,2,3,4,5,6),(2,1,3,4,5,6),(3,1,2,4,5,6),(4,1,2,3,5,6),(5,1,2,3,4,6),(6,1,2,3,4,5)])
    # partition([(1,2,3,4),(2,1),(3,1,4,5),(4,1,3,5,7),(5,3,4,6,8),(6,5),(7,4,8),(8,5,7)])
    # partition([(1,2,3),(2,1,4),(3,1,4,6),(4,2,3),(5,6,7),(6,3,5,7,8),(7,5,6,8),(8,6,7)])
    # partition([(1,2,3),(2,1,4),(3,1,4,6),(4,2,3,8),(5,6,7),(6,3,5,7,8),(7,5,6,8),(8,4,6,7)])
    # partition([(1,2,3,5),(2,1,4),(3,1,4,5,6),(4,2,3),(5,1,3,6,7),(6,3,5,7,8),(7,5,6,8),(8,6,7)])
    # partition([(1,2,3),(2,1,3,4),(3,1,2,4),(4,2,3)])
    # partition([(1,2,5,4,7),(2,1,3),(3,2,5,6),(4,1,5,7),(5,1,3,4,7,8,9),(6,3,9),(7,1,4,5),(8,5,10),(9,5,6),(10,8)])

    for part in partition([(1,2),(2,1,3,4,5,6),(3,2,6),(4,2,5,7),(5,2,4,6),(6,2,3,5,7),(7,4,6)]):
        # print(part)
        possibilities += [part]

    for n, i in enumerate(possibilities):
        for j in i:
            # print(f'Length of subset: {len(j)}')
            connections = 0
            for node in j:
                # print(f'Subsubset: {node}')
                for tupleI in node:
                    if tupleI not in list(zip(*j))[0]:
                        connections += 1

            # print(f'Nodes in subsubset: {list(zip(*j))[0]}')
            # print(f'Connections: {connections}')

            calc.addBoundary(len(j), connections)
        if min == None or calc.Result() < min:
            min = calc.Result()
            num = [n]
        elif calc.Result() == min:
            num.append(n)
        calc.reset()        
        
    partitions = []
    for i, nums in enumerate(num):
        partitions.append([])
        for part in possibilities[nums]:
            partitions[i].append(list(zip(*part))[0])

    # print(partitions)
    print(f'Optimal partition number(s): \n\t{num}\nComplexity: \n\t{round(min,2)}\nPartition(s):\n\t', end="")
    print(*partitions, sep='\n\t')
    print(f'\nOut of {len(possibilities)} possibilities')
    

    # calc = Calc()
    # output = []

    # while True:
    #     try:
    #         output += [(int(input("\nAggregates: ")), int(input("Connections: ")))]
    #     except:
    #         break
    #     userInput = input("[Enter] to continue, [X] to remove previous: ")
    #     if userInput.lower() == "x":
    #         output.pop()

    # for item in output:
    #     calc.addBoundary(item[0], item[1])

    # calc.showList()
    # print(calc.Result())
    # calc.reset()

if __name__ == "__main__":
    main()