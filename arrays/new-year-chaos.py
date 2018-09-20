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
    print(q)
    tarr = sorted([[q[i], q[i] - i - 1] for i in range(len(q))])
    result = 0
    print(tarr)
    for i in range(len(q)):
        if tarr[i][1] < i - 2:
            return "Too chaotic"
        result += abs(tarr[i][0] - i)
    return result // 2


def attempt2(q):
    """
    Bubble sort too slow.

    :param q:
    :return:
    """
    tarr = [[q[i], i] for i in range(len(q))]
    for i in range(len(q)):
        if tarr[i][1] > i + 2:
            print("Too chaotic")
    result = 0
    for j in range(len(q) - 1):
        for i in range(j, len(q) - 1):
            if q[i] > q[i + 1]:
                result += 1
                temp = q[i]
                q[i] = q[i+1]
                q[i + 1] = temp
            #print("{0} {1}".format(q[i], result))
    print(result)
    return


def attempt3(q):
    """
    Bubble sort counting

    :param q:
    :return:
    """
    tarr = sorted([[q[i], i] for i in range(len(q))])
    for i in range(len(q)):
        if tarr[i][1] < i - 2:
            print("Too chaotic")
            return
    result = 0
    for j in range(len(q) - 1):
        previous = result
        for i in range(len(q) - j - 1):
            if q[i] > q[i+1]:
                result += 1
                temp = q[i]
                q[i] = q[i+1]
                q[i+1] = temp
    print(result)
    return


def attempt3fast(q):
    """
    Bubble sort counting

    :param q:
    :return:
    """
    length = len(q)
    tarr = sorted([[q[i], i] for i in range(length)])
    for i in range(length):
        if tarr[i][1] < i - 2:
            print("Too chaotic")
            return
    result = 0
    for j in range(length - 1):
        for i in range(length - j - 1):
            if q[i] > q[i+1]:
                result += 1
                temp = q[i]
                q[i] = q[i+1]
                q[i+1] = temp
    print(result)
    return


def attempt21(q):

    tagged_q = [[i, 0] for i in q]
    for i in range(len(tagged_q)):
        if tagged_q[i][0] - i - 1 > 2:
            print("Too chaotic")
            return

    def merge_sort(q):

        if len(q) == 1:
            return q

        a = merge_sort(q[:len(q) // 2])
        b = merge_sort(q[len(q) // 2:])
        sorted_q = []
        while a and b:
            if a[0][0] < b[0][0]:
                sorted_q.append(a.pop(0))
            else:
                a[0][1] += 1
                sorted_q.append(b.pop(0))

        if a:
            sorted_q.extend(a)
        if b:
            sorted_q.extend(b)

        return sorted_q

    sorted_q = merge_sort(tagged_q)
    result = 0
    for i in sorted_q:
        result += i[1]
    print(result)


def rand_array(length, swaps):
    arr = [i for i in range(length)]
    #print('swap')
    swap = random.sample(range(1, length), swaps)
    #print(swap)
    for i in range(0, swaps):
        j = swap[i]
        temp = arr[j]
        arr[j] = arr[j - 1]
        arr[j - 1] = temp
    return arr


def rand_array_free(length, swaps):
    arr = [i for i in range(length)]
    for i in range(swaps):
        j = k = 0
        while j == k or abs(k - j) > 1:
            j = random.randint(0, length - 1)
            k = random.randint(0, length - 1)
        temp = arr[j]
        arr[j] = arr[k]
        arr[k] = temp
        #print("swapped {0} {1}".format(j, k))
    return arr


if __name__ == '__main__':

    start = datetime.datetime.now()

    import fileinput
    data_input = fileinput.input()
    line1 = data_input[0].split()
    tests = int(line1[0])
    test = 0
    for i in range(1, tests * 2, 2):
        test += 1
        length = int(data_input[i].split()[0])
        arr = [int(i) for i in data_input[i+1].split()]
        #print("\n\n***** Starting test {0} of {1}".format(test, tests))
        #print(datetime.datetime.now() - start)
        start = datetime.datetime.now()

        #print('\nPython sort')
        #sorted(arr.copy())
        #print(datetime.datetime.now() - start)
        #start = datetime.datetime.now()

        #print('\n')
        attempt3(arr.copy())
        #print(datetime.datetime.now() - start)
        start = datetime.datetime.now()


    print('\nGenerating array')
    length = 10000
    ra = rand_array(length, 1003)
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    attempt3(ra.copy())
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    attempt3fast(ra.copy())
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

    attempt21(ra.copy())
    print(datetime.datetime.now() - start)
    start = datetime.datetime.now()

