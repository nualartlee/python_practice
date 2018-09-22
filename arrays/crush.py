#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput
import datetime


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    # Sort the queries according to span endpoints
    def sort_by_second(x):
        return x[1]

    queries.sort(key=sort_by_second)
    sums = []

    # For each of the sorted queries, test to find intersections
    i = 0
    while i < len(queries) - 1:

        # Start with the query value
        sum = queries[i][2]

        # For each subsequent query...
        j = i + 1
        while j < len(queries):

            # ...if it intersects, add the values
            if queries[i][1] >= queries[j][0]:
                sum += queries[j][2]
                j += 1

            # ...else skip to next non-tested query
            else:
                j -= 1
                break
        if j > i:
            i = j
        else:
            i += 1
        sums.append(sum)

    print(len(sums))

    # Return the maximum of the possible sums
    return max(sums)


if __name__ == '__main__':

    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #nm = input().split()

    nm = fileinput.input()
    line1 = nm[0].split()

    n = int(line1[0])

    m = int(line1[1])

    queries = []

    for i in range(m):
        queries.append(list(map(int, nm[i+1].rstrip().split())))

    result = arrayManipulation(n, queries)

    print(result)
    #fptr.write(str(result) + '\n')
    #fptr.close()

start = datetime.datetime.now()
n = 10**7
m = 2*10**5
ops = []
for i in range(m):
    op = random.sample(range(n), 2)
    op = sorted(op)
    op.append(random.randint(1, 10**9))
    ops.append(op)

print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(arrayManipulation(n, ops))
print(datetime.datetime.now() - start)
