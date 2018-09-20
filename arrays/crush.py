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

    queries = sorted([[i[0], i[1], i[2], i[2]] for i in queries])
    length = len(queries)

    i = 0
    while i < length - 1:
        # Check intersection in the sorted queries
        adder = 0
        j = i + 1
        while j < length:
            if queries[i][1] >= queries[j][0]:
                adder += queries[j-1][2]
                queries[j][3] += adder
            else:
                break
            j += 1
        i = j

    maximum = max([query[3] for query in queries])
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
m = 2*10**5
ops = []
for i in range(m):
    op = random.sample(range(n), 2)
    op.append(random.randint(1, 10**9))
    ops.append(op)

print(datetime.datetime.now() - start)
start = datetime.datetime.now()
print(arrayManipulation(n, ops))
print(datetime.datetime.now() - start)
