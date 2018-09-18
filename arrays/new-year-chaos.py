#!/bin/python3

import datetime
import random


def attempt1(q):
    """
    Tagged array

    :param q:
    :return:
    """
    print('attempt 1')
    tarr = [[q[i], i] for i in range(len(q))]
    result = 0
    for i in range(len(q)):
        if q[i] > i + 2:
            return "Too chaotic"
        if q[i] != i:
            result += abs(q[i] - i)
    return result // 2


def attempt2(q):
    """
    Bubble sort too slow.

    :param q:
    :return:
    """
    result = 0
    for j in range(len(q) - 1):
        for i in range(j, len(q) - 1):
            if q[i] > i + 3:
                result =  "Too chaotic"
                print(result)
                return
            if q[i] > q[i + 1]:
                result += 1
                temp = q[i]
                q[i] = q[i+1]
                q[i + 1] = temp
            #print("{0} {1}".format(q[i], result))
    print(result)
    return


def rand_array(length, swaps):
    arr = [i for i in range(length)]
    print('swap')
    swap = random.sample(range(1, length), swaps)
    print(swap)
    for i in range(0, swaps):
        j = swap[i]
        k = swap[i] - 1
        temp = arr[j]
        arr[j] = arr[k]
        arr[k] = temp
    return arr


def rand_array_free(length, swaps):
    arr = [i for i in range(length)]
    for i in range(swaps):
        j = k = 0
        while j == k or abs(k - j) > 2:
            j = random.randint(0, length - 1)
            k = random.randint(0, length - 1)
        temp = arr[j]
        arr[j] = arr[k]
        arr[k] = temp
        print("swapped {0} {1}".format(j, k))
    return arr


if __name__ == '__main__':

    start = datetime.datetime.now()

    print('\nGenerating array')
    length = 100000
    ra = rand_array(length, 999)
    #print(ra)
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    print('\nPython')
    sorted(ra.copy())
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    print('\n')
    print(attempt1(ra.copy()))
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    q = [1, 2, 5, 3, 7, 8, 6, 4]
    print('\n')
    print(attempt1(q))
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()
