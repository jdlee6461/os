import numpy as np
import copy
import pprint

pp = pprint.PrettyPrinter(indent=4)

def banker(allocations, needs, available):
    continue


def req(process, request, allocations, needs, available):
    continue
        

if __name__ == "__main__":
    max_resources = [10, 5, 7]

    requires = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    allocations = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    needs = [list(np.subtract(requires[i], allocations[i])) for i in range(len(allocations))]

    available = copy.deepcopy(max_resources)
    for allocation in allocations:
        available = list(np.subtract(available, allocation))

    # Current sate is supposed to be safe
    if banker(allocations, needs, available):
        print("Current state is safe")
    else:
        print("Current state is unsafe")

    # Try several cases
    process = 0
    request = [0, 2, 0]

    if req(process, request, allocations, needs, available):
        print("Request (%s) from P%d is granted" % (request, process))
    else:
        print("Request (%s) from P%d is NOT granted" % (request, process))
