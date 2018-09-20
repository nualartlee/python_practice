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
    for i in range(len(sorted(queries)) - 1):
        if set(range(queries[i][0], queries[i][1]+1)).intersection(set(range(queries[i+1][0], queries[i+1][1]+1))):
            queries[i+1][2] += queries[i][2]

    maximum = max([i[2] for i in queries])
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
n = 10**5
m = 10**4
ops = []
for i in range(m):
    op = random.sample(range(n), 2)
    op.append(random.randint(1, 10**9))
    ops.append(op)

print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(arrayManipulation(n, ops))
print(datetime.datetime.now() - start)
