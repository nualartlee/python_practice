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

    sums = []
    splits = {0}
    queries = sorted(queries)

    for q in queries:
        splits.add(q[0])
        splits.add(q[1])

    for i in splits:
        sum = 0
        for q in queries:
            if q[0] <= i <= q[1]:
                sum += q[2]
        sums.append(sum)

    maximum = max(sums)
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
m = 2*10**4
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
