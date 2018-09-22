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

    intersects = []

    # Check intersection in the sorted queries
    while queries:
        queries = sorted(queries)
        print(len(queries))

        # Only one operation left
        if len(queries) == 1:
            intersects.append(queries.pop(0)[2])
            break

        # First intersects with second
        if queries[0][1] >= queries[1][0]:

            # First overlaps second
            if queries[0][1] >= queries[1][1]:
                queries[0][0] = queries[1][1] + 1
                queries[1][2] += queries[0][2]
                continue

            # Second extends beyond first
            else:
                queries[0][0] = queries[1][0]
                queries[0][2] += queries[1][2]
                queries[1][0] = queries[0][1] + 1
                continue

        # First does not intersect second
        else:
            intersects.append(queries.pop(0)[2])

    maximum = max(intersects)
    return maximum


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
m = 2*10**3
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
