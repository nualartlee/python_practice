#!/bin/python3

import math
import os
import random
import re
import sys
import fileinput


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for _ in range(n)]
    for query in queries:
        new_arr = arr[:query[0]]
        new_arr += map(lambda x: x + query[2], arr[query[0]:query[1]+1])
        new_arr += arr[query[1] + 1:]
        arr = new_arr
    return max(arr)


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
