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

    # Change span endpoint to indicate the point where the operation no longer applies
    queries = [[q[0], q[1]+1, q[2]] for q in queries]

    # Create a list of sorted points indicating the start/end of an operation
    simple_q = [[q[0], q[2]] for q in queries]
    simple_q.extend([q[1], -q[2]] for q in queries)
    simple_q.sort()

    # Create the list of all possible sums rolling through the sorted list
    sums = [0]
    sum = 0
    for q in simple_q:
        sum += q[1]
        sums.append(sum)

    # Return the maximum value of the list of possible sums
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
